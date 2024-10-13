# Maintainer: Stipe Kotarac <stipe@kotarac.net>

pkgname=jay
pkgver=1.6.1
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
  libinput
  libudev.so
  libvulkan.so
  libxkbcommon.so
  mesa
  pango
)
optdepends=(
  'xorg-xwayland: X11 support'
  'xdg-desktop-portal: portal support'
)
makedepends=(
  rust
  shaderc
)
options=(!lto)
source=("$pkgname-$pkgver.tar.gz::https://github.com/mahkoh/jay/archive/v$pkgver.tar.gz")
sha512sums=('40c7f6dab28f04f37e621b327c574ab5ee4eab743a8f73fbebae20c44f49ad5f75467552a316133764e09b2609b5caf09fc3026828d694a301d2feff2326d9b5')

build() {
  cd $pkgname-$pkgver/
  cargo build --release --locked
}

check() {
  cd $pkgname-$pkgver/
  cargo test --release --locked
}

package() {
  cd $pkgname-$pkgver/

  install -D -m755 -s target/release/jay $pkgdir/usr/bin/jay
  install -D -m644 etc/jay.portal $pkgdir/usr/share/xdg-desktop-portal/portals/jay.portal
  install -D -m644 etc/jay-portals.conf $pkgdir/usr/share/xdg-desktop-portal/portals/jay-portals.conf

  mkdir -p $pkgdir/usr/share/zsh/site-functions/
  target/release/jay generate-completion zsh > $pkgdir/usr/share/zsh/site-functions/_jay

  mkdir -p $pkgdir/usr/share/bash-completion/completions/
  target/release/jay generate-completion bash > $pkgdir/usr/share/bash-completion/completions/jay

  mkdir -p $pkgdir/usr/share/fish/vendor_completions.d/
  target/release/jay generate-completion fish > $pkgdir/usr/share/fish/vendor_completions.d/jay.fish
}
