# Maintainer: Stipe Kotarac <stipe@kotarac.net>

pkgname=jay
pkgver=1.12.0
pkgrel=1
pkgdesc='A Wayland Compositor'
arch=('x86_64')
license=(GPL-3.0-only)
url='https://github.com/mahkoh/jay'
provides=(
  wayland-compositor
)
depends=(
  cairo
  gcc-libs
  glib2
  glibc
  libinput
  libudev.so=1
  libvulkan.so=1
  mesa
  pango
)
optdepends=(
  'xorg-xwayland: X11 support'
  'xdg-desktop-portal: portal support'
)
makedepends=(
  cargo
  cmake
)
options=(!lto)
source=("$pkgname-$pkgver.tar.gz::https://github.com/mahkoh/jay/archive/v$pkgver.tar.gz")
install=jay.install
sha512sums=('08bac6f1d660c6db2778473b71e919b3174d3483be9138af5695d05af7efc6f3cb873ae548a753b2604740e6f9c86fdea448b7fc4905441472b02f1c7d06c207')

prepare() {
  cd $pkgname-$pkgver/
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd $pkgname-$pkgver/
  export RUSTUP_TOOLCHAIN=stable
  cargo build --frozen --release
}

check() {
  cd $pkgname-$pkgver/
  export RUSTUP_TOOLCHAIN=stable
  cargo test --frozen --release
}

package() {
  cd $pkgname-$pkgver/

  install -D -m755 -s target/release/jay $pkgdir/usr/bin/jay
  install -D -m644 etc/jay.portal $pkgdir/usr/share/xdg-desktop-portal/portals/jay.portal
  install -D -m644 etc/jay-portals.conf $pkgdir/usr/share/xdg-desktop-portal/jay-portals.conf

  mkdir -p $pkgdir/usr/share/zsh/site-functions/
  target/release/jay generate-completion zsh > $pkgdir/usr/share/zsh/site-functions/_jay

  mkdir -p $pkgdir/usr/share/bash-completion/completions/
  target/release/jay generate-completion bash > $pkgdir/usr/share/bash-completion/completions/jay

  mkdir -p $pkgdir/usr/share/fish/vendor_completions.d/
  target/release/jay generate-completion fish > $pkgdir/usr/share/fish/vendor_completions.d/jay.fish
}
