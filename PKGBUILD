# Maintainer: Luke Featherston <lukefeatherston1223 at gmail dot com>
pkgname=gearlever
pkgver=2.0.1
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
	'bd7b2d22b858e940c816fd4a94d253850f31ae51e0fb1f3e31deb9b507014279'
)

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	
	# Run commands outside of flatpak
	sed -i 's/cmd = \['\''flatpak-spawn'\'', '\''--host'\'', \*command\]/cmd = \[\*command\]/g' src/lib/terminal.py
	# Arch command doesn't seem to exist on arch linux so instead we can substitute it for 'uname' for now
	sed -i 's/\['\''arch'\''\]/\['\''uname'\'', '\''-m'\''\]/g' src/AppDetails.py
}

build() {
	arch-meson "${srcdir}/${pkgname}-${pkgver}" build
	meson compile -C build
}

check() {
	# Only run validation tests on desktop and schema files as the appstream test fails at this time.
	# https://github.com/mijorus/gearlever/issues/76
	meson test "Validate desktop file" "Validate schema file" -C build --print-errorlogs
	# Instead, we can run an alternative to appstream_util with appstreamcli --no-net for validation.
	appstreamcli validate --no-net "${srcdir}/build/data/it.mijorus.gearlever.appdata.xml"
}

package() {
	meson install -C build --destdir "${pkgdir}"
	
	cd "${srcdir}/${pkgname}-${pkgver}"
	install -Dm644 COPYING -t "${pkgdir}/usr/share/licenses/$pkgname/"
	
	cd "${pkgdir}"
	rm -v "usr/share/icons/hicolor/scalable/actions/meson.build"
	rm -v "usr/share/${pkgname}/${pkgname}/meson.build"
}
