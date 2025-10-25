# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Kritoke <typeolinux@yahoo.com>
# Maintainer: kj_sh604 <406hs_jk@proton.me>

pkgname=libglademm
pkgver=2.6.7
pkgrel=7
pkgdesc="A C++ wrapper for libglade."
arch=('x86_64')
url="http://gtkmm.sourceforge.net/"
license=('LGPL')
depends=('libglade' 'gtkmm' 'libxml2-legacy')
makedepends=('pkgconfig')
source=(https://download.gnome.org/sources/${pkgname}/2.6/${pkgname}-${pkgver}.tar.bz2)
sha256sums=('38543c15acf727434341cc08c2b003d24f36abc22380937707fc2c5c687a2bc3')

build() {
  cd ${pkgname}-${pkgver}
  CXXFLAGS+=' -std=c++11'
  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var

  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

  make
}

package() {
  cd ${pkgname}-${pkgver}
  make DESTDIR="${pkgdir}" install
}
