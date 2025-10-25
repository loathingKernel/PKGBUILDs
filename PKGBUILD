# Maintainer: gee
# contributors: yochananmarqos, bpierre, PedroHLC, rodrigo21, FabioLolix
pkgname='vkbasalt'
pkgver=0.3.2.10
pkgrel=1
pkgdesc='A Vulkan post-processing layer. Some of the effects are CAS, FXAA, SMAA, deband.'
arch=('x86_64')
url='https://github.com/DadSchoorse/vkBasalt'
license=('zlib')
depends=('gcc-libs' 'glslang' 'libx11')
makedepends=('git' 'meson' 'ninja' 'spirv-headers' 'vulkan-headers')
source=("git+https://github.com/DadSchoorse/vkBasalt.git#tag=v${pkgver}")
sha256sums=('9ff099c515e29d2acfbd5d328c5abedf56fd53d50b9b1380d41b41e3be8504fc')
install=vkbasalt.install

prepare() {
  cd ${srcdir}/vkBasalt
  sed -i 's|/path/to/reshade-shaders/Textures|/opt/reshade/textures|g' \
    "config/vkBasalt.conf"
  sed -i 's|/path/to/reshade-shaders/Shaders|/opt/reshade/shaders|g' \
    "config/vkBasalt.conf"
}

build() {
  cd ${srcdir}/vkBasalt

  arch-meson \
    --buildtype=release \
    -Dwith_json=true \
    build
  ninja -C build
}

package() {
  optdepends=('reshade-shaders-git')
  cd ${srcdir}/vkBasalt

  DESTDIR="${pkgdir}" ninja -C build install
  mv "${pkgdir}/usr/share/vulkan/implicit_layer.d/vkBasalt.json" "${pkgdir}/usr/share/vulkan/implicit_layer.d/vkBasalt.x86_64.json"
  install -Dm 644 config/vkBasalt.conf "${pkgdir}/usr/share/doc/${pkgname}/vkBasalt.conf.example"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
