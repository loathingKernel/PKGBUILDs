# shellcheck shell=bash

# Maintainer: William Horvath <william at horvath dot blog>

pkgname=llvm-mingw
pkgver=19.1.7+20250114
pkgrel=1

# This controls the version we will pull.
_tag="20250114"

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
  "git+${url}#tag=${_tag}"
  "git+https://github.com/llvm/llvm-project.git#tag=llvmorg-${pkgver#"$_tag"'+'}"
)
sha256sums=('f3de01627afe67ba5427681ed33d7258fda90fc5b9b87728e21e58f0daca1deb'
            'f6c754bd1b8d7da76f357a539ff8175f214b7dc1b52391a0fe75cfb9a57f28dd')

pkgver() {
  # This looks to be where the maintainer (Martin Storsjö) does version bumps
  llvmver="$(grep -e "LLVM_VERSION:=" "${srcdir}/${pkgname}"/build-llvm.sh | sed 's/.*-\([0-9.]*\).*/\1/')"
  printf '%s+%s' "${llvmver}" "${_tag}"
}

prepare() {
  cd "${srcdir}/${pkgname}"

  chmod +x build-all.sh
  chmod +x build-llvm.sh

  rm -rf "${srcdir}/llvm-mingw/llvm-project"
  ln -srf "${srcdir}/llvm-project" "${srcdir}/llvm-mingw/"
}

build() {
  cd "${srcdir}/${pkgname}"

  # Never pop Wine prefix dialog during mingw configure
  export DISPLAY=

  # Configure to build only i686 and x86_64 targets (default builds i686, x86_64, armv7, aarch64)
  export TOOLCHAIN_ARCHS="i686 x86_64"

  # Flags from GH Actions workflow
  export LLVM_CMAKEFLAGS="-DLLVM_ENABLE_LIBXML2=OFF -DLLVM_ENABLE_TERMINFO=OFF -DLLDB_ENABLE_PYTHON=OFF"

  ./build-all.sh "${srcdir}/install/llvm-mingw"
}

package() {
  cd "${srcdir}"

  install -d "${pkgdir}/opt"
  cp -r install/llvm-mingw "${pkgdir}/opt/"

  install -d "${pkgdir}/etc/profile.d"
  echo 'export PATH="${PATH}:/opt/llvm-mingw/bin"' >"${pkgdir}/etc/profile.d/llvm-mingw.sh"

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
  find "${pkgdir}/opt/llvm-mingw" -name '*.exe.manifest' -delete
  find "${pkgdir}/opt/llvm-mingw" -name '*.la' -delete
  find "${pkgdir}/opt/llvm-mingw" -type f '(' -name '*COPYING*' -o -name '*LICENSE*' ')' -delete

  ## To strip or not to strip, that is the question 
}
