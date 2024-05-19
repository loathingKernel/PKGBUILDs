# Maintainer: Luke Featherston <lukefeatherston1223 at gmail dot com>
pkgname=gearlever
pkgver=1.5.4
pkgrel=1
pkgdesc="Manage AppImages with ease"
arch=('x86_64')
url="https://mijorus.it/projects/gearlever/"
license=('GPL-3.0-or-later')
depends=( 'dbus-python' 'dconf' 'fuse2' 'gdk-pixbuf2' 'glibc' 'glib2' 'gtk4' 'hicolor-icon-theme' 'libadwaita' 'p7zip' 'pango' 'python' 'python-gobject' 'python-pyxdg' 'zlib' )
makedepends=( 'meson' 'gettext' )
checkdepends=( 'desktop-file-utils' 'appstream' )
options=( '!strip' '!debug' )
source=(
	"${pkgname}-${pkgver}.tar.gz"::"https://github.com/mijorus/gearlever/archive/refs/tags/${pkgver}.tar.gz"
	"correct-icon-names.patch"
)
sha256sums=(
	'79aaedc79f9e43e6cd5e056d01993815bdbd6ae83f0c225c2d8006cc799c043b'
	'8d9bf423855188001e4f28e7cdb367878deaf552e49b3a2ff037dba7fccd44b7'
)
_unneededicons=(
	"earth-symbolic.svg"
	"globe-symbolic.svg"
	"software-update-available-symbolic.svg"
	"web-browser-symbolic.svg"
	"window-pop-out-symbolic.svg"
	"document-edit-symbolic.svg"
	"drag-drop-symbolic.svg"
	"file-manager-symbolic.svg"
)

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	# Remove unneeded icons for improved compatibility.
	for icon in "${_unneededicons[@]}"; do
		rm -v "data/icons/hicolor/scalable/actions/$icon"
	done
	
	# Rename icons to fit a unique gearlever naming scheme.
	for icon in "data/icons/hicolor/scalable/actions"/*; do
		iconname=$(basename "$icon")
		# Skip renaming meson's build file and those beginning with gl- or gearlever-.
		if [[ ! "$iconname" =~ ^(gl-|gearlever-) ]] && [ ! "$iconname" = "meson.build" ]; then
			mv -v "$icon" "data/icons/hicolor/scalable/actions/gl-$iconname"
		fi
	done
	
	# Make sure to fix their names in any scripts that call on them, change flatpak-spawn to instead execute the command natively and rename a file-manager to use the gl-file-manager instead.
	patch -Np1 -i ../correct-icon-names.patch
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
