# Maintainer: Luke Featherston <lukefeatherston1223 at gmail dot com>
pkgname=gearlever
pkgver=2.0.7
pkgrel=1
pkgdesc="Manage AppImages with ease"
arch=('x86_64')
url="https://mijorus.it/projects/gearlever/"
license=('GPL-3.0-or-later')
depends=( 'binutils' 'dconf' 'fuse2' 'gdk-pixbuf2' 'glibc' 'glib2' 'gtk4' 'hicolor-icon-theme' 'libadwaita' 'p7zip' 'pango' 'python' 'python-dbus' 'python-gobject' 'python-pyxdg' 'python-requests' 'zlib' )
makedepends=( 'gettext' 'meson' )
checkdepends=( 'appstream' 'desktop-file-utils' )
options=( '!strip' '!debug' )
source=(
	"${pkgname}-${pkgver}.tar.gz"::"https://github.com/mijorus/gearlever/archive/refs/tags/${pkgver}.tar.gz"
)
sha256sums=(
	'772721843b6c323f7f4e74e4da3d72879f2b194d3d4ad981a8b783235fe270a1'
)

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	
	# Arch command doesn't seem to exist on arch linux so instead we can substitute it for 'uname' for now
	sed -i 's/\['\''arch'\''\]/\['\''uname'\'', '\''-m'\''\]/g' src/AppDetails.py
}

build() {
	arch-meson "${srcdir}/${pkgname}-${pkgver}" build
	meson compile -C build
}

check() {
	meson test -C build --print-errorlogs
}

package() {
	meson install -C build --destdir "${pkgdir}"
	
	cd "${srcdir}/${pkgname}-${pkgver}"
	install -Dm644 COPYING -t "${pkgdir}/usr/share/licenses/$pkgname/"
	
	cd "${pkgdir}"
	rm -v "usr/share/icons/hicolor/scalable/actions/meson.build"
	rm -v "usr/share/${pkgname}/${pkgname}/meson.build"
}
