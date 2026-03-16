# Maintainer: Damjan Georgievski <gdamjan@gmail.com>
pkgname=go2tv
pkgver=2.2.0
pkgrel=1
pkgdesc='cast your videos to UPnP/DLNA MediaRenderer'
arch=('x86_64')
url="https://github.com/alexballas/${pkgname}"
license=('MIT')
depends=('glibc' 'libx11' 'libglvnd' 'libpipewire' )
makedepends=('go' 'pkg-config' 'libxcursor' 'libxrandr' 'libxinerama' 'libxi')
optdepends=('ffmpeg: transcoding support')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")

build() {
  cd $pkgname-$pkgver

  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"

  # allow flag from `pkg-config --cflags libpipewire-0.3` - see also https://go.dev/wiki/InvalidFlag
  export CGO_CFLAGS_ALLOW="-fno-strict-overflow"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  go build -ldflags "-s -w" -o go2tv cmd/go2tv/go2tv.go
}

package() {
  install -Dm755 $pkgname-$pkgver/$pkgname   "$pkgdir"/usr/bin/$pkgname
  install -Dm644 $pkgname-$pkgver/LICENSE    "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

sha256sums=('60e8aae8d7109920ef32f1870adcd50b6d6b6ce41b0bbcf66e3de88ceecc772b')
