# Maintainer: Jose Riha <jose1711 gmail com>

pkgname=controllermap
pkgver=2.30.6
pkgrel=2
pkgdesc="Game controller mapping generator"
arch=('i686' 'x86_64')
url="http://www.libsdl.org"
license=('MIT')
depends=('sdl2')
makedepends=('libunwind')
source=("http://www.libsdl.org/release/SDL2-${pkgver}.tar.gz")
md5sums=('ab12cc1cf58a5dd25e69c924acb93402')

build() {
  cd $srcdir/SDL2-${pkgver}/test
  sed -i '/bmp/s%"\([^"][^"]*\)"%"/usr/share/controllermap/\1"%' controllermap.c
  ./configure --prefix=/usr
  make
}

package() {
  cd $srcdir/SDL2-${pkgver}/test
  install -Dm755 $srcdir/SDL2-${pkgver}/test/controllermap $pkgdir/usr/bin/controllermap
  install -Dm644 $srcdir/SDL2-${pkgver}/test/controllermap.bmp $pkgdir/usr/share/controllermap/controllermap.bmp
  install -Dm644 $srcdir/SDL2-${pkgver}/test/controllermap_back.bmp $pkgdir/usr/share/controllermap/controllermap_back.bmp
  install -Dm644 $srcdir/SDL2-${pkgver}/test/axis.bmp $pkgdir/usr/share/controllermap/axis.bmp
  install -Dm644 $srcdir/SDL2-${pkgver}/test/button.bmp $pkgdir/usr/share/controllermap/button.bmp
}
