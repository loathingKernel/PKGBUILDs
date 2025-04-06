# Maintainer: loathingkernel <loathingkernel @at gmail .dot com>

pkgname=dxvk-nvapi-vkreflex-layer
pkgver=0.9.0
pkgrel=1
pkgdesc='Alternative NVAPI implementation on top of DXVK, Vulkan Reflex layer'
arch=('x86_64')
url="https://github.com/jp7677/dxvk-nvapi"
license=('MIT')
makedepends=('ninja' 'meson>=0.43' 'glslang' 'git')
source=(
    "git+https://github.com/jp7677/dxvk-nvapi.git#tag=v${pkgver}"
)

prepare() {
    cd dxvk-nvapi

    # Explicitly set origin URL for submodules using relative paths
    git remote set-url origin https://github.com/jp7677/dxvk-nvapi.git
    git submodule update --init --filter=tree:0 --recursive external/{Vulkan-Headers,vkroots}
}

build() {
    arch-meson dxvk-nvapi/layer build \
        --buildtype "release" \
        --strip \
        -Dabsolute_library_path=false

    ninja -C build -v
}

package() {
    depends=('vulkan-icd-loader')

    DESTDIR="$pkgdir" ninja -C build install
}

sha256sums=('47a45365a288eedbe27ce4033f6fdc07e8386225dc7670f939a2b919f82962bb')
