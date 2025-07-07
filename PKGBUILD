# Maintainer: Peter Jung ptr1337 <admin@ptr1337.dev>
# Maintainer: loathingkernel <loathingkernel _a_ gmail _d_ com>

pkgname=proton-cachyos-slr
_srctag=10.0-20250702
pkgver=${_srctag//-/.}
pkgrel=1
epoch=1

source=(
  https://github.com/CachyOS/proton-cachyos/releases/download/cachyos-${_srctag}-slr/proton-cachyos-${_srctag}-slr-x86_64.tar.xz
)
source+=(
  proton-cachyos-slr-remove-lock.patch
)

pkgdesc="A compatibility tool for Steam Play based on Wine and additional components, experimental branch with extra CachyOS flavour (Steam Linux Runtime build)"
url="https://github.com/CachyOS/proton-cachyos"
arch=(x86_64 x86_64_v3)
options=(!strip emptydirs)
license=('BSD' 'LGPL' 'zlib' 'MIT' 'MPL' 'custom')
depends=(
  bash
  coreutils
  curl
  dbus
  desktop-file-utils
  diffutils
  freetype2
  gcc-libs
  gdk-pixbuf2
  glibc
  hicolor-icon-theme
  libxcrypt
  libxcrypt-compat
  libxkbcommon-x11
  lsb-release
  lsof
  nss
  python
  ttf-font
  usbutils
  vulkan-driver
  vulkan-icd-loader
  xdg-user-dirs
  xorg-xrandr
  xz
  zenity
)
depends_x86_64=(
  lib32-alsa-plugins
  lib32-fontconfig
  lib32-gcc-libs
  lib32-glibc
  lib32-libgl
  lib32-libgpg-error
  lib32-libnm
  lib32-libva
  lib32-libx11
  lib32-libxcrypt
  lib32-libxcrypt-compat
  lib32-libxinerama
  lib32-libxss
  lib32-nss
  lib32-pipewire
  lib32-systemd
  lib32-vulkan-driver
  lib32-vulkan-icd-loader
)
optdepends=(
  steam
  umu-launcher
)
provides=('proton')
install=${pkgname}.install

build() {
  cd proton-cachyos-${_srctag}-slr-x86_64/
  sed -i -r 's|"proton-cachyos-*"|"proton-cachyos-slr"|' compatibilitytool.vdf
  patch -Np1 -i "${srcdir}"/proton-cachyos-slr-remove-lock.patch
  rm proton.orig || true
}

package() {
    local _compatdir="$pkgdir/usr/share/steam/compatibilitytools.d"
    mkdir -p "$_compatdir/${pkgname}"
    rsync --delete -arx proton-cachyos-${_srctag}-slr-x86_64/* "$_compatdir/${pkgname}"

    mkdir -p "$pkgdir/usr/share/licenses/${pkgname}"
    mv "$_compatdir/${pkgname}"/{PATENTS.AV1,LICENSE{,.OFL}} \
        "$pkgdir/usr/share/licenses/${pkgname}"
}

b2sums=('d89a2632be20ab85fd6dd5b2e2e18b9b36187b383adf4c4eefde0470e1a1e76ad1f88f51a6d2eb9e79c928b0462491aed4915d694fcc7965b4de379919889375'
        'a106655214af49105ba1aed2216a24a06f16cff624e09c9a3b31c8fa08262289493c1e3ccbb5a00dd0a59a49f1f97d518b378bd280a3e621b94e6adde594b271')
