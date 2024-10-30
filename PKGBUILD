# Maintainer: Stipe Kotarac <stipe@kotarac.net>

pkgname=jay
pkgver=1.7.0
pkgrel=2
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
  'rust>=1.84.0'
  shaderc
)
options=(!lto)
source=("$pkgname-$pkgver.tar.gz::https://github.com/mahkoh/jay/archive/v$pkgver.tar.gz")
sha512sums=('56d708b8c0edbe66ab150668c873c0b7b662a767fb8f2fdeadd381bbce9e801e32ad8b8027bd9bc49a8e2bb2d9cc2ee3f9ebef5de6459c76a917fa6baec2cdac')

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
  install -D -m644 etc/jay-portals.conf $pkgdir/usr/share/xdg-desktop-portal/jay-portals.conf

  mkdir -p $pkgdir/usr/share/zsh/site-functions/
  target/release/jay generate-completion zsh > $pkgdir/usr/share/zsh/site-functions/_jay

  mkdir -p $pkgdir/usr/share/bash-completion/completions/
  target/release/jay generate-completion bash > $pkgdir/usr/share/bash-completion/completions/jay

  mkdir -p $pkgdir/usr/share/fish/vendor_completions.d/
  target/release/jay generate-completion fish > $pkgdir/usr/share/fish/vendor_completions.d/jay.fish
}
