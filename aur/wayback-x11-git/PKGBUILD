# Maintainer: Coraline Shuryn <coraline.shuryn@gmail.com>
pkgname=wayback-x11-git
_pkgname=wayback
pkgver=0.2.r10.cfb2e83
pkgrel=1
pkgdesc="An experimental X compatibility layer for Wayland."
arch=('x86_64')
url="https://wayback.freedesktop.org/"
license=('MIT')
depends=('wayland' 'libxkbcommon' 'wlroots0.19' 'glibc' 'xorg-xwayland' 'scdoc')
makedepends=('git' 'meson' 'wayland-protocols')
source=("git+https://gitlab.freedesktop.org/wayback/wayback.git")
sha256sums=('SKIP')

pkgver() {
  cd "$_pkgname"
  git describe --long --tags | sed 's/-/.r/; s/-g/./'
}

build() {
  cd "$_pkgname"
  meson setup _build -Dprefix=/usr -Dlibexecdir="lib/$_pkgname"
  cd _build
  meson compile
}

package() {
  cd "$_pkgname/_build"
  meson install --destdir "$pkgdir"
  install -Dm644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
