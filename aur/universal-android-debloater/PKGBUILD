# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=universal-android-debloater
pkgver=1.1.2
pkgrel=1
pkgdesc="Cross-platform GUI written in Rust using ADB to debloat non-rooted Android devices"
arch=('x86_64')
url="https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation"
license=('GPL-3.0-or-later')
depends=(
  'android-tools'
  'gcc-libs'
)
makedepends=(
  'cargo'
  'clang'
  'cmake'
  'mold'
)
source=("$pkgname-next-generation-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz"
        'uad-ng.desktop')
conflicts=('universal-android-debloater-opengl')
sha256sums=('24e2759e011bfee1130142a8a58ef3ac6e4c26e475e561552462c6171b26b5b2'
            '8d5d790fffd35101af340792d081f8f75b61b1579bc8f89acab818f03f1071ea')

prepare() {
  cd "$pkgname-next-generation-$pkgver"
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "$pkgname-next-generation-$pkgver"
  CFLAGS+=" -ffat-lto-objects"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  export CARGO_PROFILE_RELEASE_STRIP=false
  cargo build --frozen --release --no-default-features --features wgpu,no-self-update
}

package() {
  cd "$pkgname-next-generation-$pkgver"
  install -Dm755 target/release/uad-ng -t "$pkgdir/usr/bin/"
  install -Dm644 resources/assets/logo-dark.png "$pkgdir/usr/share/pixmaps/uad-ng.png"
  install -Dm644 "$srcdir/uad-ng.desktop" -t "$pkgdir/usr/share/applications/"
}
