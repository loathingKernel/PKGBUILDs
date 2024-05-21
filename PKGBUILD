# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Daniel M. Capella <polycitizen@gmail.com>
# Contributor: Bin Jin <bjin@ctrl-d.org>

pkgname=shaderc-non-semantic-debug
pkgver=2024.1
pkgrel=1
pkgdesc='Collection of tools, libraries and tests for shader compilation with applied patches designed for use in pcsx2 and other emulators'
url='https://github.com/google/shaderc'
arch=('x86_64')
license=('Apache-2.0')
depends=('glibc' 'gcc-libs' 'glslang' 'spirv-tools')
makedepends=('asciidoctor' 'cmake' 'ninja' 'python' 'spirv-headers')
provides=('libshaderc_shared.so' 'shaderc')
source=(
    https://github.com/google/shaderc/archive/v${pkgver}/shaderc-${pkgver}.tar.gz
shaderc-changes.patch)
conflicts=(shaderc)

prepare() {
    cd shaderc-${pkgver}
    patch -p1 < "../shaderc-changes.patch"
    # de-vendor libs and disable git versioning
    sed '/examples/d;/third_party/d' -i CMakeLists.txt
    sed '/build-version/d' -i glslc/CMakeLists.txt
  cat <<- EOF > glslc/src/build-version.inc
"${pkgver}\\n"
"$(pacman -Q spirv-tools|cut -d \  -f 2|sed 's/-.*//')\\n"
"$(pacman -Q glslang|cut -d \  -f 2|sed 's/-.*//')\\n"
EOF
}

build() {
    cd shaderc-${pkgver}
    cmake \
    -B build \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS -ffat-lto-objects" \
    -DSHADERC_SKIP_TESTS=ON \
    -DPYTHON_EXECUTABLE=python \
    -Dglslang_SOURCE_DIR=/usr/include/glslang
    ninja -C build
    
    cd glslc
    asciidoctor -b manpage README.asciidoc -o glslc.1
}

check() {
    cd shaderc-${pkgver}
    ninja -C build test
}

package() {
    cd shaderc-${pkgver}
    DESTDIR="${pkgdir}" ninja -C build install
    install -Dm 644 glslc/glslc.1 -t "${pkgdir}/usr/share/man/man1"
    
    # Remove unused shaderc_static.pc
    #rm "${pkgdir}/usr/lib/pkgconfig/shaderc_static.pc"
}
sha256sums=('eb3b5f0c16313d34f208d90c2fa1e588a23283eed63b101edd5422be6165d528'
'216575bd302a48a083a9864b21bb569be89c00921188fa8f6f2fac8c30189b75')
