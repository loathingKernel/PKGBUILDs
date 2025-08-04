# Maintainer: devome <evinedeng@hotmail.com>

pkgname="backrest"
pkgver=1.9.0
pkgrel=1
pkgdesc="A web UI and orchestrator for restic backup."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/garethgeorge/${pkgname}"
license=("GPL-3.0-or-later")
depends=("restic")
makedepends=("npm" "go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}.service"
        "${pkgname}@.service")
sha256sums=('c7d3c005fd26db58b488db7c5c186f340e9ffd474d04a1503796ad2c919c4cae'
            'ce8ae2ce067b354cdc20676919efc8e9a0f7793e0cfa11b013a7b3cecabde425'
            '957ffa5c171842fe0ded3705eb3755183c78a81d50124472d3f1dcda5ca5fc1d')

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
    install -Dm644 "${pkgname}.service"  -t "${pkgdir}/usr/lib/systemd/user"
    install -Dm644 "${pkgname}@.service" -t "${pkgdir}/usr/lib/systemd/system"

    cd "${pkgname}-${pkgver}"
    install -Dm755 "${pkgname}"          -t "${pkgdir}/usr/bin"
    install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}
