# Maintainer: devome <evinedeng@hotmail.com>

pkgname="backrest"
pkgver=1.12.1
pkgrel=2
pkgdesc="A web UI and orchestrator for restic backup."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/garethgeorge/${pkgname}"
license=("GPL-3.0-or-later")
depends=("restic")
makedepends=("npm" "go" "unzip")
source=("${pkgname}-${pkgver}.zip::${url}/archive/refs/tags/v${pkgver}.zip"
        "${pkgname}.service"
        "${pkgname}@.service")
sha256sums=('c119f322472c34eceba8f8f9d806584a6d8b9b809b5cbce5bab0367b6645fa94'
            'ce8ae2ce067b354cdc20676919efc8e9a0f7793e0cfa11b013a7b3cecabde425'
            '957ffa5c171842fe0ded3705eb3755183c78a81d50124472d3f1dcda5ca5fc1d')

prepare() {
    export BACKREST_BUILD_VERSION="${pkgver}"

    cd "${pkgname}-${pkgver}"
    go mod tidy
    npm --prefix webui install
    go generate ./...
}

build() {
    export BACKREST_BUILD_VERSION="${pkgver}"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"

    local _commit=$(unzip -qz "${pkgname}-${pkgver}.zip")

    cd "${pkgname}-${pkgver}"
    go build \
        -trimpath \
        -ldflags="-s -w -X main.version=${pkgver} -X main.commit=${_commit} -extldflags '${LDFLAGS}'" \
        -o "${pkgname}" \
        ./cmd/"${pkgname}"
}

package() {
    install -Dm644 "${pkgname}.service"  -t "${pkgdir}/usr/lib/systemd/user"
    install -Dm644 "${pkgname}@.service" -t "${pkgdir}/usr/lib/systemd/system"

    cd "${pkgname}-${pkgver}"
    install -Dm755 "${pkgname}"          -t "${pkgdir}/usr/bin"
    install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}
