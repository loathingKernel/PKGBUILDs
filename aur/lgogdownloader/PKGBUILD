# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: C. Dominik Bódi <dominikdotbodiatgmxdotde>
# Contributor: Joe Davison <joe@warhaggis.com>

pkgname=lgogdownloader
pkgver=3.16
pkgrel=1
pkgdesc="Open source downloader for GOG.com games, uses the GOG.com API"
url="https://sites.google.com/site/gogdownloader/"
arch=(x86_64 i686 pentium4)
license=(WTFPL)
depends=(boost-libs jsoncpp tinyxml2 rhash tidy glibc gcc-libs curl)
depends+=(libboost_filesystem.so)
makedepends=(help2man cmake boost)
source=("https://github.com/Sude-/lgogdownloader/releases/download/v${pkgver}/lgogdownloader-${pkgver}.tar.gz")
sha256sums=('24b005bf3caf00ebc8c603251f5689d66098f66dd37bdf399836289064cb0c9f')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  [[ -d build ]] || mkdir build
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_QT_GUI=OFF

  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make DESTDIR=$pkgdir install
  install -Dm644 ../COPYING ${pkgdir}/usr/share/licenses/${pkgname}/COPYING
}
