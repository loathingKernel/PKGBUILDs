# Maintainer: txtsd <aur.archlinux@ihavea.quest>

pkgname=dissent
_fqpn=so.libdb.${pkgname}
pkgver=0.0.30
pkgrel=2
pkgdesc='Discord client written in go and gtk4'
arch=(x86_64 aarch64)
url='https://github.com/diamondburned/dissent'
license=('GPL-3.0-only')
depends=(
  'gtk4>=4.10.3'
  'libadwaita>=1.3.2'
  cairo
  gcc-libs
  gdk-pixbuf2
  glib2
  glibc
  gobject-introspection
  graphene
  gtksourceview5
  hicolor-icon-theme
  libspelling
  pango
)
makedepends=(git 'go>=1.20.3')
source=("git+https://github.com/diamondburned/dissent#tag=v${pkgver}")
sha256sums=('3c516858af3939240ebc1d1a1828ea41f8327a1740871d6db49826e87722bef2')

prepare() {
  cd "${pkgname}"

  export GOPATH="${srcdir}"
  export GOFLAGS="-modcacherw"
  go mod download
}

build() {
  cd "${pkgname}"

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOPATH="${srcdir}"
  export GOFLAGS="\
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -trimpath \
  "
  local _ld_flags=" \
    -compressdwarf=false \
    -linkmode=external \
  "
  go build \
    -ldflags "${_ldflags}" \
    -o build
}

package() {
  cd "${pkgname}"

  install -Dm755 "build/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 "nix/${_fqpn}.desktop" "${pkgdir}/usr/share/applications/${_fqpn}.desktop"
  install -Dm644 "nix/${_fqpn}.service" "${pkgdir}/usr/share/dbus-1/services/${_fqpn}.service"
  install -Dm644 "${pkgname}/${_fqpn}.metainfo.xml" "${pkgdir}/usr/share/metainfo/${_fqpn}.metainfo.xml"

  cp -dr internal/icons/hicolor/ "${pkgir}/usr/share/icons/"
  cp -dr internal/icons/scalable/ "${pkgir}/usr/share/icons/hicolor/"
  cp -dr internal/icons/symbolic/ "${pkgdir}/usr/share/icons/hicolor/"
}
