# Maintainer: Jimmy <your-email@example.com>
pkgname=somewm-git
pkgver=0.5.0.r87.gf1d2187
pkgrel=1
pkgdesc="AwesomeWM ported to Wayland - 100% Lua API compatible"
arch=('x86_64')
url="https://github.com/trip-zip/somewm"
license=('GPL-3.0-or-later')
depends=(
    'cairo'
    'dbus'
    'gdk-pixbuf2'
    'glib2'
    'libdrm'
    'libinput'
    'libxkbcommon'
    'lua51-lgi'
    'luajit'
    'pango'
    'pixman'
    'wayland'
)
makedepends=(
    'git'
    'hwdata'
    'libdisplay-info'
    'libliftoff'
    'libseat'
    'libxcb'
    'meson'
    'ninja'
    'wayland-protocols'
    'xcb-util-wm'
    'xorg-xwayland'
)
optdepends=(
    'xorg-xwayland: X11 application support'
)
provides=('somewm')
conflicts=('somewm')
source=("${pkgname}::git+https://github.com/trip-zip/somewm.git")
sha256sums=('SKIP')

pkgver() {
    cd "$pkgname"
    git describe --long --tags --abbrev=7 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "$pkgname"
    arch-meson build \
        -Db_sanitize=none \
        -Dwerror=false
    meson compile -C build
}

package() {
    cd "$pkgname"
    meson install -C build --destdir "$pkgdir"
}
