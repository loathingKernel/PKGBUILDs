# Maintainer: devome <evinedeng@hotmail.com>

pkgname="backrest"
pkgver=1.2.0
pkgrel=1
pkgdesc="A web UI and orchestrator for restic backup."
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/garethgeorge/${pkgname}"
license=("GPL-3.0-or-later")
depends=("restic")
makedepends=("npm" "go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}@.service")
sha256sums=('d954d98d2bf260a5b8f1120fbf3adb4278f67682a32d614dbcc2eb213f888b97'
            '528bfac979b7d0615bf70df9de4e965ad9a25bf0e06a19c7ed359a7ee47de05a')

build() {
    local ldflags="-s -w -extldflags '${LDFLAGS}'"
    export BACKREST_BUILD_VERSION="${pkgver}"

    cd "${pkgname}-${pkgver}"
    go mod tidy
    npm --prefix webui install
    npm --prefix webui run build
    find webui/dist -name '*.map' -exec rm ./{} \;
    go build -trimpath -ldflags="$ldflags" -o "${pkgname}" ./cmd/"${pkgname}"
}

package() {
    install -Dm644 "${pkgname}@.service" -t "${pkgdir}/usr/lib/systemd/system"

    cd "${pkgname}-${pkgver}"
    install -Dm755 "${pkgname}"          -t "${pkgdir}/usr/bin"
    install -Dm644 LICENSE               -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}"
}
