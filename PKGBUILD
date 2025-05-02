# Maintainer: Alexander Courtis <alex@courtis.org>
# Contributor: Aaron van Geffen <aaron@aaronweb.net>
# Contributor: Sven-Hendrik Haase <svenstaro@gmail.com>
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Markus Martin <markus@archwyrm.net>

# Uses master until upstream has been tagged: https://github.com/jbeder/yaml-cpp/issues/1356

_pkgbase=yaml-cpp
pkgname=lib32-yaml-cpp
pkgver=master
pkgrel=1
pkgdesc="YAML parser and emitter in C++, written around the YAML 1.2 spec (32-bits)"
url="https://github.com/jbeder/yaml-cpp"
arch=('x86_64')
license=('MIT')
depends=('lib32-gcc-libs' 'lib32-glibc')
makedepends=('cmake' 'gcc-multilib' 'ninja')
source=("https://github.com/jbeder/yaml-cpp/archive/refs/heads/master.tar.gz")
sha512sums=('2551c3b228781460bbfede810bcd35e3cc34730f723cdf215ac8cd59304e8290d3e5230b114c352c6cc3636da28b940e12fed534260ab05dd0c30f3eb83b346c')

build() {
  cd "${_pkgbase}-${pkgver}"

  export CFLAGS="-m32 ${CFLAGS}"
  export CXXFLAGS="-m32 ${CXXFLAGS}"
  export LDFLAGS="-m32 ${LDFLAGS}"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cmake -GNinja \
        -Bbuild \
        -DCMAKE_POLICY_VERSION_MINIMUM=4.0 \
        -DYAML_CPP_BUILD_TESTS=OFF \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib32 \
        -DBUILD_SHARED_LIBS=ON \
        -DYAML_BUILD_SHARED_LIBS=ON \
        -DCMAKE_BUILD_TYPE=Release
  ninja -C build
}

package() {
  cd "${_pkgbase}-${pkgver}"
  DESTDIR="$pkgdir" ninja -C build install
  rm -rf "${pkgdir}"/usr/{include,share}
  rm -rf "${pkgdir}"/usr/{lib32,lib32/pkgconfig}/*{gtest,gmock}*
  rm -rf "${pkgdir}"/usr/lib32/cmake/GTest
}
