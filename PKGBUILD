# Maintainer:  Ionut Biru <ibiru@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Mikko Sepp�l� <t-r-a-y@mbnet.fi>
_pkgsourcename=mesa
pkgname=lib32-$_pkgsourcename
pkgver=7.7.1
pkgrel=0.1
pkgdesc="Mesa OpenGL library"
arch=('x86_64')
url="http://mesa3d.sourceforge.net"
license=('LGPL')
groups=('lib32')
depends=('lib32-libgl' 'lib32-gcc' 'lib32-libxt')
source=(http://mir.archlinux.fr/extra/os/i686/$_pkgsourcename-$pkgver-$pkgrel-i686.pkg.tar.xz)

build() {
	cd "$srcdir"
	mkdir -p "$pkgdir/opt/lib32/usr/lib"
	cp -dp usr/lib/*.so* "$pkgdir/opt/lib32/usr/lib"
}
md5sums=('bcb3c6fef536076b71bcf18f78974099')
sha256sums=('ea26e8b4dde821a8a987e6fc49fbc294339c019cfbb11582fcd4befc6a8714f9')
