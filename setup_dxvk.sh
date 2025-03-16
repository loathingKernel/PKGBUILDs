#!/usr/bin/env bash

################################### Setup section ###################################

# default directories
dxvk_lib32="${dxvk_lib32:-"x32"}"
dxvk_lib64="${dxvk_lib64:-"x64"}"

# figure out where we are
basedir="$(dirname "$(readlink -f "${0}")")"

# default command to copy with
file_cmd="copyFile"

# figure out which action to perform
action="install"

# process arguments
while [[ $# -gt 0 ]]; do
  case "${1}" in
  "install") ;;
  "uninstall")
    action="uninstall"
    with_dxgi="true"
    ;;
  "--without-dxgi")
    [ "${action}" != "uninstall" ] && with_dxgi="false"
    ;;
  "--symlink")
    file_cmd="linkFile"
    ;;
  *)
    echo "Unrecognized argument: ${1}"
    echo "Usage: ${0} [install|uninstall] [--without-dxgi] [--symlink]"
    echo "The default action is 'install' if unspecified."
    exit 1
    ;;
  esac
  shift
done

################################# Helper functions ##################################

copyFile() {
  if [ -z "${1:-}" ] || [ -z "${2:-}" ]; then return 1; fi
  echo -n "copying: "
  cp -v --reflink=auto "${@}"
  return $?
}

linkFile() {
  if [ -z "${1:-}" ] || [ -z "${2:-}" ]; then return 1; fi
  echo -n "symlinking: "
  ln -s -v "${@}"
  return $?
}

# create native dll override
overrideDll() {
  $wine reg add 'HKEY_CURRENT_USER\Software\Wine\DllOverrides' /v "${1}" /d native /f >/dev/null 2>&1 || {
    echo -e "Failed to add override for ${1}" >&2
    return 1
  }
  return 0
}

# remove dll override
restoreDll() {
  # nothing to override
  $wine reg query 'HKEY_CURRENT_USER\Software\Wine\DllOverrides' /v "${1}" &>/dev/null || return 0

  $wine reg delete 'HKEY_CURRENT_USER\Software\Wine\DllOverrides' /v "${1}" /f &>/dev/null || {
    echo "Failed to remove override for ${1}" >&2
    return 1
  }
  return 0
}

# copy or link dxvk dll, back up original file
installFile() {
  if [ -z "${1:-}" ] || [ -z "${2:-}" ] || [ -z "${3:-}" ]; then return 1; fi
  local dstfile="${1:-}/${3:-}.dll"
  local srcfile="${basedir}/${2:-}/${3:-}.dll"

  if [ -f "${srcfile:-}.so" ]; then
    srcfile="${srcfile:-}.so"
  fi

  if ! [ -f "${srcfile:-}" ]; then
    echo "${srcfile:-}: File not found. Skipping." >&2
    return 1
  fi

  if [ -f "${dstfile:-}" ] || [ -h "${dstfile:-}" ]; then
    if ! [ -f "${dstfile:-}.old" ]; then
      mv -v "${dstfile:-}" "${dstfile:-}.old"
    else
      rm -v "${dstfile:-}"
    fi
    $file_cmd "${srcfile:-}" "${dstfile:-}" || return 1
  else
    echo "${dstfile:-}: File not found in wine prefix. Nothing to do." >&2
    return 1
  fi
  return 0
}

# remove dxvk dll, restore original file
uninstallFile() {
  if [ -z "${1:-}" ] || [ -z "${2:-}" ] || [ -z "${3:-}" ]; then return 1; fi
  local dstfile="${1:-}/${3:-}.dll"
  local srcfile="${basedir:-}/${2:-}/${3:-}.dll"

  if [ -f "${srcfile:-}.so" ]; then
    srcfile="${srcfile:-}.so"
  fi

  if ! [ -f "${srcfile:-}" ]; then
    echo "${srcfile:-}: File not found. Skipping." >&2
    return 1
  fi

  if ! [ -f "${dstfile:-}" ] && ! [ -h "${dstfile:-}" ]; then
    echo "${dstfile:-}: File not found. Skipping." >&2
    return 1
  fi

  if [ -f "${dstfile:-}.old" ]; then
    rm -v "${dstfile:-}"
    mv -v "${dstfile:-}.old" "${dstfile:-}"
  fi

  return 0
}

install() {
  declare -i ret=0;
  [ -n "${win64_sys_path:-}" ] && installFile "${win64_sys_path}" "${dxvk_lib64}" "${1}" && ((ret++))
  [ -n "${win32_sys_path:-}" ] && installFile "${win32_sys_path}" "${dxvk_lib32}" "${1}" && ((ret++))

  ((ret)) && { overrideDll "${1}" || return 1 ; }
  return 0
}

uninstall() {
  declare -i ret=0;
  [ -n "${win64_sys_path:-}" ] && uninstallFile "${win64_sys_path}" "${dxvk_lib64}" "${1}" && ((ret++))
  [ -n "${win32_sys_path:-}" ] && uninstallFile "${win32_sys_path}" "${dxvk_lib32}" "${1}" && ((ret++))

  ((ret)) && { restoreDll "${1}" || return 1 ; }
  return 0
}

setupWine() {
  # find wine executable
  export WINEDEBUG="${WINEDEBUG:-"-all"}"
  # disable mscoree and mshtml to avoid downloading wine gecko and mono
  # and don't show "updating prefix" dialog
  export DISPLAY=
  export WAYLAND_DISPLAY=
  export WINEDLLOVERRIDES="${WINEDLLOVERRIDES:-}${WINEDLLOVERRIDES:+";"}mscoree=;mshtml=;winex11.drv=;winewayland.drv="

  # try wine/wine64 or use the WINE env var for the wine binary
  wine="$(which "${WINE:-wine}" 2>/dev/null)" || wine="$(which "${WINE:-wine}64" 2>/dev/null)"

  if [ ! -x "$wine" ]; then
    echo "Can't find a valid wine=$wine executable in \$PATH""${WINE:+" or from the env var WINE=$WINE you set"}"'.' >&2
    return 1
  fi

  # validate wine/wineprefix/registry, and ensure wine placeholder dlls are recreated if they are missing
  # but don't create a new non-default wineprefix (by checking system.reg if WINEPREFIX is passed)
  if ! { [ -n "${WINEPREFIX:-}" ] && [ ! -r "${WINEPREFIX:-}/system.reg" ] ; }; then
    if ! { $wine wineboot -u ; }; then
      echo "Error: $wine wineboot -u returned $?." >&2
      return 1
    fi

    # if it wasn't specified, get the default WINEPREFIX from wine
    if [ -z "${WINEPREFIX:-}" ]; then
      WINEPREFIX="$($wine cmd /c 'winepath.exe -u %WINECONFIGDIR%' 2>/dev/null)" || {
        echo "Couldn't determine the default wineprefix from $wine winepath.exe." >&2
        return 1
      }
    fi
  fi

  export WINEPREFIX
  local sysregfile="${WINEPREFIX}/system.reg"

  if [ ! -r "${sysregfile:-}" ]; then
    echo "The WINEPREFIX=$WINEPREFIX is broken/invalid/doesn't exist." >&2
    return 1
  fi

  # get the winearch from the regfile
  winearch="$(grep -e '#arch=win' "${sysregfile}" | head -n 1 | grep -oe "win.*")" || {
    echo "Can't determine the prefix architecture from the $sysregfile registry file. Exiting." >&2
    return 1
  }

  # resolve 32-bit and 64-bit system paths
  # system32 will be 32-bit for WINEARCH=win32 and 64-bit for WINEARCH=win64
  win64_sys_path="$($wine cmd /c '%SystemRoot%\system32\winepath.exe -u C:\windows\system32' 2>/dev/null)"
  win64_sys_path="${win64_sys_path/$'\r'/}"

  if [ "${winearch:-}" = "win32" ]; then # win32 (32-bit only) installation
    win32_sys_path="${win64_sys_path}"
    win64_sys_path=
  else # win64 installation, check for 32-bit folder as well
    win32_sys_path="$($wine cmd /c '%SystemRoot%\syswow64\winepath.exe -u C:\windows\system32' 2>/dev/null)"
    win32_sys_path="${win32_sys_path/$'\r'/}"
  fi

  if [ -z "${win32_sys_path:-}" ] && [ -z "${win64_sys_path:-}" ]; then
    echo 'Failed to resolve C:\windows\system32.' >&2
    return 1
  fi

  return 0
}

dumpWineConfig() {
  echo ""
  echo "Wine info:" >&2
  [ -n "${WINEDEBUG:-}" ] && echo "WINEDEBUG: ${WINEDEBUG}" >&2
  [ -n "${WINEDLLOVERRIDES:-}" ] && echo "WINEDLLOVERRIDES: ${WINEDLLOVERRIDES}" >&2
  [ -n "${WINEPREFIX:-}" ] && echo "WINEPREFIX: ${WINEPREFIX}" >&2
  [ -n "${winearch:-}" ] && echo "Prefix architecture: ${winearch}" >&2
  [ -x "${wine:-}" ] && {
    { winever="$($wine --version | grep wine)" && echo "Wine version: $winever" >&2 ; } || \
      echo "Invalid wine version (\$wine=$wine)." >&2
  }

  echo "win64_sys_path: ${win64_sys_path:-"N/A"}" >&2
  echo "win32_sys_path: ${win32_sys_path:-"N/A"}" >&2

  return
}

runActions() {
  declare -a actions
  actions=(d3d8 d3d9 d3d10core d3d11)
  # always uninstall dxgi
  [ "${with_dxgi:-}" != "false" ] && actions+=(dxgi)

  declare -i actionret=0
  for verb in "${actions[@]}"; do
    $action "${verb}" || {
        ((actionret++)) || true
        continue
      }
  done

  ((actionret)) && return 1
  return 0
}

#################### Actually run the install/uninstall actions #####################

# first, figure out what kind of wine installation we're dealing with
setupWine || {
  echo "Setting up wine failed." >&2
  dumpWineConfig
  exit 1
}

runActions || {
  echo "Script finished with warnings/errors." >&2
  dumpWineConfig
  exit 1
}

echo "$action""ation complete."
# exit 0
