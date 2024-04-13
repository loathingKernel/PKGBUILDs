# Maintainer: devome <evinedeng@hotmail.com>

pkgname="backrest"
pkgver=0.17.1
pkgrel=1
pkgdesc="A web UI and orchestrator for restic backup."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/garethgeorge/${pkgname}"
license=("GPL-3.0-or-later")
depends=("restic")
makedepends=("npm" "go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}@.service")
sha256sums=('2c0c80eca3800607bcba2b1a44e450bc132cd04e27e93abec9732d533e8f4871'
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
    install -Dm644 "${pkgname}@.service" -t "${pkgdir}/usr/lib/systemd/system"

    cd "${pkgname}-${pkgver}"
    install -Dm755 "${pkgname}"          -t "${pkgdir}/usr/bin"
    install -Dm644 LICENSE               -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}
