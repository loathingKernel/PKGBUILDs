# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>
# Maintainer: Christian Heusel <gromit@archlinux.org>
# Maintainer: Justin Kromlinger <hashworks@archlinux.org>
# Contributor: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Daniel Maslowski <info@orangecms.org>

pkgname=minio
pkgver=2024.06.06
_timever=T09-36-42Z
_pkgver="${pkgver//./-}${_timever//:/-}"
pkgrel=1
pkgdesc='Object storage server compatible with Amazon S3'
arch=('x86_64')
url='https://minio.io'
license=('AGPL-3.0-or-later')
depends=('glibc')
makedepends=('go' 'git')
options=(!lto)
source=(git+https://github.com/minio/minio.git#tag=RELEASE.${_pkgver}
        minio.conf
        minio.service
        minio.sysusers)
backup=('etc/minio/minio.conf')
sha512sums=('1aeb546733d7c5360c5838b6cc744af03fc55a5993477cb3942507c042391b2e951d04b58c3071b9dfcdeda2f04be254788f5e96678e113b151bc017612df38b'
            '9fb09d19af9d7a00e4680cd92d208ddd44ce52328f6efee68d7ee47f591cbe77ee88ce139a677bcf8836de0643de18c6c7c4005d50b0056f9b861c3d595e5233'
            'f4df8e50618712b6e5f62e2674eca4430ef17ef003426bd83ea6b427da4e0fb519589cc14547b08db4b4a0de114488920071295a680b0c1cb5fd508d31576190'
            '7e4617aed266cf48a2ff9b0e80e31641d998537c78d2c56ce97b828cfc77d96dbf64728d4235dac7382d6e5b201388bef6722959302de5e2298d93f4ec1e0e63')

build() {
  cd minio

  export CGO_LDFLAGS="${LDFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
  export MINIO_RELEASE="RELEASE"
  GO_LDFLAGS="\
      -linkmode=external \
      -compressdwarf=false \
      $(go run buildscripts/gen-ldflags.go)"

  go build -ldflags "$GO_LDFLAGS" .
}

package() {
  install -dm750 -o 103 -g 103 "${pkgdir}/srv/minio"
  install -dm750 -o 103 -g 103 "${pkgdir}/var/lib/minio"

  install -Dm755 minio/minio "${pkgdir}/usr/bin/minio"
  install -Dm600 "${srcdir}/minio.conf" "${pkgdir}/etc/minio/minio.conf"
  install -Dm644 "${srcdir}/minio.service" "${pkgdir}/usr/lib/systemd/system/minio.service"
  install -Dm644 "${srcdir}/minio.sysusers" "${pkgdir}/usr/lib/sysusers.d/minio.conf"
}
