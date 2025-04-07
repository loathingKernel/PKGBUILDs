# shellcheck shell=bash

# Maintainer: William Horvath <william at horvath dot blog>

pkgname=llvm-mingw
pkgver=20.1.2+20250402
pkgrel=1

# This controls the version we will pull.
_tag="20250402"

# When updating, needs to be manually changed to the mingw_commit echoed during prepare().
mingw_commit="d0c80252d68bfad98d1f4cc9cdb31e851e26b63a"

pkgdesc="A self-contained LLVM/Clang/LLD based mingw-w64 toolchain for i686 and x86_64 targets"
arch=('x86_64')
url="https://github.com/mstorsjo/${pkgname}"
license=(
  'LicenseRef-custom'
  'ZPL-2.1'
  'GPL-3.0'
  'GPL-3.0-with-GCC-exception'
  'GFDL-1.3-or-later'
  'Apache-2.0 WITH LLVM-exception'
  'custom:ISC'
)
depends=(
  'gcc-libs'
  'glibc'
  'zlib'
  'libffi'
  'libedit'
  'ncurses'
  'libxml2'
  'bash'
)
makedepends=(
  'cmake>=3.20.0'
  'ninja'
  'python'
  'git'
  'libxml2'
  'zlib'
  'xz'
  'swig'
  'lua53'
  'doxygen'
  'perl'
)
optdepends=('wine: for running Windows executables')
groups=('mingw-w64-toolchain' 'mingw-w64') # not sure...
provides=( # what to do here?
  'mingw-w64-gcc'
  'mingw-w64-clang'
  'mingw-w64-binutils'
  'mingw-w64-tools'
  'mingw-w64-crt'
  'mingw-w64-headers'
  'mingw-w64-winpthreads'
  'mingw-w64-winstorecompat'
  'llvm-mingw-w64-toolchain'
)
options=('staticlibs' '!buildflags' '!emptydirs')
source=(
  "llvm-mingw-${_tag}.tar.gz::https://github.com/mstorsjo/llvm-mingw/archive/refs/tags/${_tag}.tar.gz"
  "llvm-project-${pkgver%'+'"$_tag"}.tar.gz::https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-${pkgver%'+'"$_tag"}.tar.gz"
  "mingw-w64-g${mingw_commit:0:6}.tar.gz::https://github.com/mingw-w64/mingw-w64/archive/${mingw_commit}.tar.gz"
)
sha256sums=('9e2a1f6d2808356bfb053a7ad2a82dd45158cb776795a2466b8225e33a10358d'
            '9ee597456405ddf4809bcf66a4765137a68a85361347ca2a4bb13d9176e932ab'
            'e5e52c89a5ac47ff81d6eea83ddc63b6258d365df053cba0e2f8c8d30dc0b211')

pkgver() {
  # This looks to be where the maintainer (Martin Storsjö) does version bumps
  llvmver="$(grep -e "LLVM_VERSION:=" "${srcdir}/${pkgname}"/build-llvm.sh | sed 's/.*-\([0-9.]*\).*/\1/')"
  printf '%s+%s' "${llvmver}" "${_tag}"
}

prepare() {
  cd "${srcdir}"

  find "./" -maxdepth 1 -type d -name llvm-mingw-\* -exec mv '{''}' "./${pkgname}" ';'

  chmod +x "${pkgname}/build-all.sh"
  chmod +x "${pkgname}/build-llvm.sh"

  unlink "${srcdir}/${pkgname}/llvm-project" &>/dev/null || rm -rf "${srcdir}/${pkgname}/llvm-project"
  find "./" -maxdepth 1 -type d -name llvm-project-\* -exec ln -srf '{''}' "./${pkgname}/llvm-project" ';'

  unlink "${srcdir}/${pkgname}/mingw-w64" &>/dev/null || rm -rf "${srcdir}/${pkgname}/mingw-w64"
  find "./" -maxdepth 1 -type d -name mingw-w64-\* -exec ln -srf '{''}' "./${pkgname}/mingw-w64" ';'

  _mingw_commit="$(grep -e "MINGW_W64_VERSION:=" "${srcdir}/${pkgname}"/build-mingw-w64.sh | cut -f2 -d'=' | tr -d '}')"
  echo "mingw_commit=${_mingw_commit}"
}

build() {
  cd "${srcdir}/${pkgname}"

  # Never pop Wine prefix dialog during mingw configure
  export DISPLAY=
  export WAYLAND_DISPLAY=

  # Configure to build only i686 and x86_64 targets (default builds i686, x86_64, armv7, aarch64)
  export TOOLCHAIN_ARCHS="i686 x86_64"

  # Flags from GH Actions workflow
  export LLVM_CMAKEFLAGS="-DLLVM_ENABLE_LIBXML2=OFF -DLLVM_ENABLE_TERMINFO=OFF -DLLDB_ENABLE_PYTHON=OFF"

  ./build-all.sh "${srcdir}/${pkgname}/install/llvm-mingw"
}

package() {
  cd "${srcdir}"

  install -d "${pkgdir}/opt"
  cp -r "${srcdir}/${pkgname}/install/llvm-mingw" "${pkgdir}/opt/"

  install -d "${pkgdir}/etc/profile.d"
  echo 'export PATH="${PATH}:/opt/llvm-mingw/bin"' >"${pkgdir}/etc/profile.d/${pkgname}.sh"

  ## llvm-mingw license
  install -Dm644 "${srcdir}/${pkgname}/LICENSE.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.llvm-mingw.txt" # ISC

  ## llvm/llvm-libs license
  install -Dm644 "${srcdir}/${pkgname}/llvm-project/LICENSE.TXT" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.llvm.txt" # Apache-2.0 WITH LLVM-exception

  ## MinGW licenses
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.MinGW-w64-meta.txt" # ZPL
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/COPYING.MinGW-w64/COPYING.MinGW-w64.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.MinGW-w64.txt" # ?
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/COPYING.MinGW-w64-runtime/COPYING.MinGW-w64-runtime.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.MinGW-w64-runtime.txt" # ?
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-crt/profile/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.profile.txt"
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-libraries/libmangle/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.libmangle.txt"
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-libraries/pseh/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.pseh.txt"
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-libraries/winpthreads/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.winpthreads.txt"
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-libraries/winstorecompat/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.winstorecompat.txt"
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-tools/gendef/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.gendef.txt"
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-tools/genidl/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.genidl.txt"
  install -Dm644 "${srcdir}/${pkgname}/mingw-w64/mingw-w64-tools/genpeimg/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.genpeimg.txt"

  ## cleanup
  find "${pkgdir}/opt/${pkgname}" -name '*.exe.manifest' -delete
  find "${pkgdir}/opt/${pkgname}" -name '*.la' -delete
  find "${pkgdir}/opt/${pkgname}" -type f '(' -name '*COPYING*' -o -name '*LICENSE*' ')' -delete

  ## To strip or not to strip, that is the question 
}
