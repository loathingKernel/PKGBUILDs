# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=protonplus
_app_id=com.vysp3r.ProtonPlus
pkgver=0.4.13
pkgrel=1
pkgdesc="A simple Wine and Proton-based compatiblity tools manager for GNOME"
arch=('x86_64')
url="https://github.com/Vysp3r/ProtonPlus"
license=('GPL-3.0-or-later')
depends=('json-glib' 'libadwaita' 'libarchive' 'libgee' 'libsoup3')
makedepends=('meson' 'vala')
checkdepends=('appstream-glib')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('8d3e4c24b52d653f5212c00c4c2635078fa1df0f98eaeed135bacadd94c4f592')

build() {
  arch-meson "ProtonPlus-$pkgver" build
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs || :
}

package() {
  meson install -C build --destdir "$pkgdir"

  ln -s "/usr/bin/${_app_id}" "$pkgdir/usr/bin/$pkgname"
}
