# $Id: PKGBUILD 246362 2015-09-15 03:51:08Z foutrelis $
# Maintainer:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: judd <jvinet@zeroflux.org>

pkgname=ncurses5-compat-libs
_pkgname=ncurses
pkgver=6.0
pkgrel=1
pkgdesc='System V Release 4.0 curses emulation library, ABI 5'
arch=('i686' 'x86_64')
url='http://invisible-island.net/ncurses/ncurses.html'
license=('MIT')
depends=('glibc' 'gcc-libs' 'sh')
source=(ftp://invisible-island.net/ncurses/ncurses-${pkgver/_/-}.tar.gz{,.asc})
md5sums=('ee13d052e1ead260d7c28071f46eefb1'
         'SKIP')
validpgpkeys=('C52048C0C0748FEE227D47A2702353E0F7E48EDB')  # Thomas Dickey

build() {
  cd $_pkgname-${pkgver/_/-}

  ./configure --prefix=/usr --mandir=/usr/share/man \
     --with-shared --with-normal --without-debug --without-ada \
     --enable-widec --enable-pc-files --with-cxx-binding --with-cxx-shared \
     --with-abi-version=5
  make
}

package() {
  cd $_pkgname-${pkgver/_/-}
  make DESTDIR="$pkgdir" install.libs
  rm -rf "$pkgdir"/usr/include/ "$pkgdir"/usr/lib/pkgconfig "$pkgdir"/usr/lib/*.so

  # fool packages looking to link to non-wide-character ncurses libraries
  for lib in ncurses ncurses++ form panel menu; do
    echo "INPUT(-l${lib}w)" > "$pkgdir"/usr/lib/lib${lib}.so.5
  done

  # install license, rip it from the readme
  install -d "$pkgdir"/usr/share/licenses/$pkgname
  grep -B 100 '$Id' README > "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
