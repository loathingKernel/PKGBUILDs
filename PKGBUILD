# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Mikko Sepp�l� <t-r-a-y@mbnet.fi>
# Maintainer: Biru Ionut <ionut@archlinux.ro>
_pkgsourcename=mesa
pkgname=lib32-$_pkgsourcename
pkgver=7.4.4
pkgrel=1
pkgdesc="Mesa OpenGL library"
arch=(x86_64)
url="http://mesa3d.sourceforge.net"
license=('LGPL')
groups=('lib32')
depends=('lib32-libgl' 'lib32-gcc' 'lib32-libxt')
source=(http://mir.archlinux.fr/extra/os/i686/$_pkgsourcename-$pkgver-$pkgrel-i686.pkg.tar.gz)

build() {
	cd $srcdir
	mkdir -p $pkgdir/opt/lib32/usr/lib
	cp -dp usr/lib/*.so* $pkgdir/opt/lib32/usr/lib
}
md5sums=('cae40c217366779d642975be92495bd6')
