# Maintainer: devome <evinedeng@hotmail.com>

pkgname="backrest"
pkgver=1.6.1
pkgrel=1
pkgdesc="A web UI and orchestrator for restic backup."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/garethgeorge/${pkgname}"
license=("GPL-3.0-or-later")
depends=("restic")
makedepends=("npm" "go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}@.service")
sha256sums=('a727ccee7c80db011693dfbd66b8c4ee3775cdad511b0c4c8363a53220270f2c'
            '54d7ceddc2d3abb1c00a3f45ff7dd43b5fdc05c6be1019ead7f7cbf4a40ab926')

build() {
    export BACKREST_BUILD_VERSION="${pkgver}"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"

    cd "${pkgname}-${pkgver}"
    go mod tidy
    npm --prefix webui install
    npm --prefix webui run build
    find webui/dist -type f -name '*.map' -exec rm {} \;
    go build -trimpath -ldflags="-s -w -extldflags '${LDFLAGS}'" -o "${pkgname}" ./cmd/"${pkgname}"
}

package() {
    install -Dm644 "${pkgname}@.service" -t "${pkgdir}/usr/lib/systemd/system"

    cd "${pkgname}-${pkgver}"
    install -Dm755 "${pkgname}"          -t "${pkgdir}/usr/bin"
    install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}
