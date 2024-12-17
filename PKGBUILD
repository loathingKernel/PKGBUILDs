# Maintainer: marco.rubin@protonmail.com

_name=KDDockWidgets
pkgname=kddockwidgets-qt6
pkgver=2.2.0
pkgrel=1
pkgdesc="KDAB's Dock Widget Framework for Qt 6"
arch=('x86_64')
url="https://github.com/KDAB/KDDockWidgets"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(gcc-libs glibc 'fmt>=11' nlohmann-json 'qt6-base>=6.2.0' qt6-declarative)
makedepends=('cmake>=3.15' 'qt6-tools>=6.6.2')
source=("$url/archive/v$pkgver.tar.gz")
b2sums=('deaeae8b0662119685068128748d08fefcd7158a75157064bc95dcee4a72a300c1ca65442785b0681907dc34761e4942bb6388a32b36426311ed0176c2b7e90d')

build() {
    cd $_name-$pkgver
    # -DKDDockWidgets_NO_SPDLOG=true is needed until KDDockWidgets can be built with fmt 11
    cmake -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_PREFIX=/usr \
          -DKDDockWidgets_FRONTENDS='qtwidgets;qtquick' \
          -DKDDockWidgets_NO_SPDLOG=true \
          -DKDDockWidgets_QT6=true \
          .
    cmake --build .
}

package() {
    cd $_name-$pkgver
    DESTDIR="$pkgdir" cmake --install .
}
