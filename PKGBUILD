# shellcheck shell=bash
# shellcheck disable=SC1091,SC2164

# Maintainer: William Horvath <william at horvath dot blog>
# Contributor: Adrià Cereto i Massagué <ssorgatem at gmail.com>

# shellcheck disable=SC2034
pkgname=('dxvk-msvc-git')
pkgver=2.5.3.r86.gcf946eb98
pkgrel=1
pkgdesc="A Vulkan-based compatibility layer for Direct3D 9/10/11 which allows running 3D applications on Linux using Wine (Clang+MSVC headers Windows DLL version)"
arch=('x86_64')
url="https://github.com/doitsujin/dxvk"
license=('zlib/libpng')
depends=('vulkan-icd-loader' 'lib32-vulkan-icd-loader')
provides=("dxvk" "d9vk" "dxvk=$pkgver")
makedepends=('wine' 'clang' 'libunwind' 'cmake' 'ninja' 'meson>=0.43' 'glslang' 'git' 'python')
optdepends=('msvc-wine-git: A very convenient package for having the msvc headers available globally. This is the preferred method instead of letting this PKGBUILD manage it.')
conflicts=('d9vk'  "dxvk" 'dxvk-mingw-git')
options=('!strip' '!staticlibs' 'lto')
source=(
    "git+https://github.com/doitsujin/dxvk.git"
    "git+https://github.com/Joshua-Ashton/mingw-directx-headers.git"
    "git+https://github.com/KhronosGroup/Vulkan-Headers.git"
    "git+https://github.com/KhronosGroup/SPIRV-Headers.git"
    "git+https://gitlab.freedesktop.org/JoshuaAshton/libdisplay-info.git#commit=275e645"
    "https://raw.githubusercontent.com/NovaRain/DXSDK_Collection/61827822ad945fac5acb3123ab00c378654bfcd7/DXSDK_Aug2007/Include/d3d8caps.h"
    "https://raw.githubusercontent.com/NovaRain/DXSDK_Collection/61827822ad945fac5acb3123ab00c378654bfcd7/DXSDK_Aug2007/Include/d3d8types.h"
    "https://raw.githubusercontent.com/NovaRain/DXSDK_Collection/61827822ad945fac5acb3123ab00c378654bfcd7/DXSDK_Aug2007/Include/d3d8.h"
    "git+https://github.com/mstorsjo/msvc-wine.git#commit=49ae4b6"
    "setup_dxvk.sh"
    "clang.patch" # contains the clang-msvc build changes
)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'e341e1f897220f586c95e1843059031633d780ea08800eea023ce3282730dfe7'
            'b4966d702022996aa435acba24b98e125c4f5d6f4d9089c3bc62cede876ad9f6'
            '6c03f80228539ad1a78390186ae9ebeae40d5c02559a39b58ed8ec4738a7b957'
            'd06d0375a6976ccbf452bba2feb7d7e5db43c6631bd4d59ad563315e9c973ccb'
            'bf7883203d9c8fe729131f1f9d82da799f33a1c3c3ebb22d2070ac77e337de8c'
            '0f688815530ab5e8cc89b9b45d9b1d66cd8cd5a7770fb8249339af555a30dfe7'
            '5b059c4084940d31460a34ec579026fe9526f7cb9bdcc0b6d928271ab52f89db')

pkgver() {
    # shellcheck disable=SC2154
    cd "${srcdir}/dxvk"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/v//g'
}

_regpath="${PATH}"
_topdir="${startdir:-$(pwd)}"
_tempprefix="${_topdir}/.winepfx"

if [ -x "${_topdir}/msvc/bin/x64/cl" ] && [ -f "${_topdir}/msvc/.done-msvc" ]; then
    _msvcpath="${_topdir}/msvc/bin"
else
    _msvcpath="/opt/msvc/bin"
fi

_prepare_msvc() {
    if [ -x "${_msvcpath}/x64/cl" ]; then
        return
    elif [ -x "${_topdir}/msvc/bin/x64/cl" ] && [ -f "${_topdir}/msvc/.done-msvc" ]; then
        _msvcpath="${_topdir}/msvc/bin"
        return
    fi

    echo "!!! WARNING !!!"
    echo "Downloading MSVC toolchain+headers to the PKGBUILD folder! This requires about ~8GB of space when uncompressed."
    echo "If you want to use a globally shared installation, please install the 'msvc-wine-git' AUR package."
    echo "The script will continue in 3 seconds, CTRL+C now if you want to install the separate package instead (recommended)."
    echo "!!! WARNING !!!"
    echo "3..." && sleep 1 && echo "2..." && sleep 1 && echo "1..." && sleep 1

    cd "${srcdir}/msvc-wine"

    if [ ! -d "${_topdir}/msvc" ]; then mkdir "${_topdir}/msvc"; fi

    python vsdownload.py --accept-license --dest "${_topdir}/msvc" --architecture x86 --architecture x64

    ./install.sh "${_topdir}/msvc"

    touch "${_topdir}/msvc/.done-msvc"
    _msvcpath="${_topdir}/msvc/bin"
}

_strip=
_debug=
_lto=

prepare() {
    if [ ! -d "${_tempprefix}" ]; then mkdir "${_tempprefix}"; fi
    export WINEPREFIX="${_tempprefix}"
    export DISPLAY=

    _prepare_msvc # will prefer global install
    echo "Using MSVC headers from ${_msvcpath}"

    cd "${srcdir}/dxvk"

    git submodule init include/{native/directx,vulkan,spirv} subprojects/libdisplay-info
    git config submodule.include/native/directx.url "${srcdir}/mingw-directx-headers"
    git config submodule.include/vulkan.url "${srcdir}/Vulkan-Headers"
    git config submodule.include/spirv.url "${srcdir}/SPIRV-Headers"
    git config submodule.subprojects/libdisplay-info.url "${srcdir}/libdisplay-info"
    git -c protocol.file.allow=always submodule update include/{native/directx,vulkan,spirv} subprojects/libdisplay-info

    git -C subprojects/libdisplay-info reset --hard

    cp -r --update "${srcdir}/d3d8"{,types,caps}.h "${srcdir}/dxvk/include/"

    # patch the build system a bit
    mapfile -t patchlist < <(find "${srcdir}" '(' -type f -o -type l ')' -regex ".*\.patch" | LC_ALL=C sort -f)

    for patch in "${patchlist[@]}"; do
        patch -Np1 <"${patch}"
    done

    # debug, strip, lto handling (requires editing sources because meson)
    for opt in "${options[@]}"; do
        if [ "${opt}" = "debug" ]; then
            # this is schizo because meson sucks
            sed -i "s|_DEPRECATION_WARNINGS'|\0, '-ggdb', '-gdwarf-4', '-gz=zstd'|g" \
                "${srcdir}/dxvk/meson.build"
            sed -i 's|OPT:ICF|\0,/DEBUG:DWARF|g' "${srcdir}/dxvk/meson.build"
            # don't strip + debug because it (meson) just doesn't integrate well with makepkg yet
            _strip=
            _debug=1
        elif [ "${opt}" = "strip" ] && [ -z "${_debug}" ]; then
            _strip=--strip
        elif [ "${opt}" = "lto" ]; then
            sed -i "s|_DEPRECATION_WARNINGS'|\0, '-flto=thin'|g" "${srcdir}/dxvk/meson.build"
        fi
    done

    if [ -z "${_debug}" ]; then
        echo "!!! This package won't have debug symbols. Consider adding 'debug' to your PKGBUILD options to allow for better support from the developers."
    else
        echo "!!! This package will have debug symbols, which substantially increases the size, but allows for better support from the developers."
    fi

    # -march= flag handling
    _march=
    if [ -n "${CFLAGS}" ]; then
        _march="$(echo "$CFLAGS" | grep -o '\-march=[^ ]*')"
    elif [ -n "${CXXFLAGS}" ]; then
        _march="$(echo "$CXXFLAGS" | grep -o '\-march=[^ ]*')"
    fi

    if [[ "${_march}" =~ .*march.* ]]; then
        sed -i "s|_DEPRECATION_WARNINGS'|\0, '${_march}'|g" "${srcdir}/dxvk/meson.build"
    fi

    # ccache handling
    if [ -n "${BUILDENV}" ]; then for _env in "${BUILDENV[@]}"; do
        if [ "${_env}" = "ccache" ]; then
            for arch in win32 win64; do
                sed -i "s|'clang|'ccache', \0|g" \
                    "${srcdir}/dxvk/build-${arch}.txt"
            done
        fi
    done; fi
}

build() {
    export WINEPREFIX="${_tempprefix}"
    export DISPLAY=

    export PATH="${_msvcpath}/x64:${_regpath}" && BIN="${_msvcpath}/x64" . "${srcdir}/msvc-wine/msvcenv-native.sh"

    export PKG_CONFIG="pkg-config"
    export PKG_CONFIG_PATH="/usr/lib/pkgconfig:/usr/share/pkgconfig"

    cd "${srcdir}"
    # shellcheck disable=SC2086
    meson dxvk "build/x64" \
        --cross-file dxvk/build-win64.txt \
        --prefix "/usr/share/dxvk/x64" \
        --bindir "" --libdir "" \
        --buildtype "release" ${_strip}
    ninja -C "build/x64"

    export PATH="${_msvcpath}/x86:${_regpath}" && BIN="${_msvcpath}/x86" . "${srcdir}/msvc-wine/msvcenv-native.sh"
    export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"

    # shellcheck disable=SC2086
    meson dxvk "build/x32" \
        --cross-file dxvk/build-win32.txt \
        --prefix "/usr/share/dxvk/x32" \
        --bindir "" --libdir "" \
        --buildtype "release" ${_strip}
    ninja -C "build/x32"

    export PATH="${_regpath}"
}

package() {
    export WINEPREFIX="${_tempprefix}"
    export DISPLAY=

    export PATH="${_msvcpath}/x86:${_regpath}" && BIN="${_msvcpath}/x86" . "${srcdir}/msvc-wine/msvcenv-native.sh"
    # shellcheck disable=SC2154
    DESTDIR="${pkgdir}" ninja -C "build/x32" install

    export PATH="${_msvcpath}/x64:${_regpath}" && BIN="${_msvcpath}/x64" . "${srcdir}/msvc-wine/msvcenv-native.sh"
    DESTDIR="${pkgdir}" ninja -C "build/x64" install

    install -Dm 644 setup_dxvk.sh "${pkgdir}/usr/share/dxvk/setup_dxvk.sh"
    mkdir -p "${pkgdir}/usr/bin"
    ln -s /usr/share/dxvk/setup_dxvk.sh "${pkgdir}/usr/bin/setup_dxvk"
    chmod +x "${pkgdir}/usr/share/dxvk/setup_dxvk.sh"
}
