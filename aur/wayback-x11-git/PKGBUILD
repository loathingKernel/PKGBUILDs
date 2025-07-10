# Maintainer: Coraline Shuryn <coraline.shuryn@gmail.com>
pkgname=wayback-x11-git
_pkgname=wayback
pkgver=r14.8be8101
pkgrel=1
pkgdesc="An experimental X compatibility layer for Wayland."
arch=('x86_64')
url="https://github.com/kaniini/wayback"
license=('MIT')
depends=('wayland' 'libxkbcommon' 'wlroots0.19' 'glibc')
makedepends=('git' 'meson' 'wayland-protocols')
source=("git+https://github.com/kaniini/wayback.git")
sha256sums=('SKIP')

pkgver() {
  cd "$_pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

build() {
  cd "$_pkgname"
  meson setup _build -Dprefix=/usr
  cd _build
  meson compile
}

package() {
  cd "$_pkgname/_build"
  meson install --destdir "$pkgdir"
  install -Dm644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
