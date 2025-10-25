# Submiter: ZekeSulastin <zekesulastin@gmail.com>
# Maintainer: AdrianoML <adriano.lols@gmail.com>
# Maintainer: Cazzoo <caz.san@gmail.com>

pkgname=jstest-gtk-git
pkgver=0.1.0.r127.g92bdf8e
pkgrel=1
pkgdesc="A simple GTK2-based joystick tester and calibrator"
arch=('i686' 'x86_64')
url="https://github.com/Grumbel/jstest-gtk"
source=("git+$url.git"
		'jstest-gtk.desktop'
		'fix_datadir.patch')
license=('GPL3')
depends=('gtkmm3')
makedepends=('git' 'cmake')
_gitname="jstest-gtk"

sha256sums=('SKIP'
			'8063bdd1426bd772396929bc044de933db40a9888663bc72556ffc62a255c0fc'
			'2aa59e55543db649bc0d1288ed22ec9b0702c824edd9f84913b8eadd029cac77')

pkgver() {
  cd "$_gitname"
  git describe --long --tags | sed -r 's/^v//;s/([^-]*-g)/r\1/;s/-/./g'
}

build() {
  cd "$_gitname"

  msg "Patching..."
  patch -p1 < "../fix_datadir.patch"

  if [[ ! -e 'build' ]]; then
      mkdir build
  fi
  cd build
  cmake ..
  make
}

package() {
  cd "$_gitname"

  install -D -m755 build/jstest-gtk "${pkgdir}/usr/bin/jstest-gtk"
  install -D -m644 "./data/generic.png" "${pkgdir}/usr/share/icons/jstest-gtk.png"
  install -D -m644 "../jstest-gtk.desktop" "${pkgdir}/usr/share/applications/jstest-gtk.desktop"
  mkdir -p "${pkgdir}/usr/share/jstest-gtk"
  cp -r "../jstest-gtk/data" "${pkgdir}/usr/share/jstest-gtk/"
}
