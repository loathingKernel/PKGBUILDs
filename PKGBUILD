# Maintainer: devome <evinedeng@hotmail.com>

pkgname="backrest"
pkgver=0.17.0
pkgrel=2
pkgdesc="A web UI and orchestrator for restic backup."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/garethgeorge/${pkgname}"
license=("GPL-3.0-or-later")
depends=("restic")
makedepends=("npm" "go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}@.service")
sha256sums=('9a7b8ae835d9535ca39fff516c407e3e4facf50f37c19401716484ff80e9cfe2'
            '54d7ceddc2d3abb1c00a3f45ff7dd43b5fdc05c6be1019ead7f7cbf4a40ab926')

build() {
    local ldflags="-s -w -extldflags '${LDFLAGS}'"
    export BACKREST_BUILD_VERSION="${pkgver}"

    cd "${pkgname}-${pkgver}"
    go mod tidy
    npm --prefix webui install
    npm --prefix webui run build
    find webui/dist -name '*.map' -exec rm ./{} \;
    go build -trimpath -ldflags="$ldflags" -o "${pkgname}" .
}

package() {
    install -Dm644 "${pkgname}@.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}@.service"

    cd "${pkgname}-${pkgver}"
    install -Dm755 "${pkgname}"          "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 LICENSE               "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 README.md             "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}
