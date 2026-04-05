# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Maximilian Stein <theoddbird@posteo.org>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

pkgbase=lib32-libsoup
pkgname=(
  lib32-libsoup
)
pkgver=2.74.3
pkgrel=4
pkgdesc="HTTP client/server library for GNOME (32-bit)"
url="https://wiki.gnome.org/Projects/libsoup"
arch=(x86_64)
license=(LGPL-2.0-or-later)
depends=(
  lib32-brotli
  lib32-glib-networking
  lib32-glib2
  lib32-glibc
  lib32-krb5
  lib32-libpsl
  lib32-libxml2
  lib32-sqlite
  lib32-zlib
  libsoup
)
makedepends=(
  git
  glib2-devel
  meson
  samba
)
checkdepends=(
  apache
  php-apache
)
source=(
  "git+https://gitlab.gnome.org/GNOME/libsoup.git#tag=$pkgver"
  0001-Disable-flaky-test.patch
)
b2sums=('9f2a278482af7ab851aa08b69f59bdd9de8187cac8cb2ac0d904ff087155afaadab253842d7c48fd8e162b3cba742565226e3ec390e671dc7921075fc089949d'
        'b468451f6e411c3a4e0b03b593ea8498f74d73bca6ee679baa6c81c45de0773ddc5d627000dcc3738c9ae4ba59cad36c63ca074c6f4bfb7c3574cda3452a670e')

prepare() {
  cd libsoup

  # Update to branch HEAD for CVE fixes
  # https://gitlab.archlinux.org/archlinux/packaging/packages/libsoup/-/issues/1
  git cherry-pick -n 2.74.3..5739a090529209c2afc13f482256573bcd9ce940

  # https://gitlab.gnome.org/GNOME/libsoup/-/issues/120
  git apply -3 ../0001-Disable-flaky-test.patch
}

build() {
  local meson_options=(
    --cross-file lib32
    -D introspection=disabled
    -D krb5_config=krb5-config
    -D sysprof=disabled
    -D vapi=disabled
  )

  arch-meson libsoup build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

package_lib32-libsoup() {
  depends+=(
    libbrotlidec.so
    libgssapi_krb5.so
    libg{lib,object,io}-2.0.so
    libpsl.so
  )
  optdepends=('samba: Windows Domain SSO')
  provides+=(libsoup{,-gnome}-2.4.so)

  meson install -C build --destdir "$pkgdir"

  rm -r "$pkgdir"/usr/{include,share}
}

# vim:set sw=2 sts=-1 et:
