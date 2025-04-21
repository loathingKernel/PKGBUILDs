# Maintainer: Luke Featherston <lukefeatherston1223 at gmail dot com>
pkgname=gearlever
pkgver=3.2.2
pkgrel=1
pkgdesc="Manage AppImages with ease"
arch=('x86_64')
url="https://mijorus.it/projects/gearlever/"
license=('GPL-3.0-or-later')
depends=('7zip' 'binutils' 'dconf' 'dwarfs-bin' 'fuse2' 'gdk-pixbuf2' 'glibc' 'glib2' 'gtk4'
	 'hicolor-icon-theme' 'libadwaita' 'squashfs-tools' 'pango' 'python' 'python-dbus' 'python-gobject'
	 'python-pyxdg' 'python-requests' 'zlib')
makedepends=('gettext' 'meson')
checkdepends=('appstream' 'desktop-file-utils')
options=('!strip' '!debug')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/mijorus/gearlever/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('2beb95231ea4afb69b4514ac59533c84fcb1c3eb16b41e8b3f02c34f646cfbd1')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	# Arch command doesn't seem to exist on arch linux so instead we can substitute it for 'uname' for now
	sed -i "s/\(\['arch'\]\)/['uname', '-m']/g" src/AppDetails.py
	
	# Arch linux uses the 7z command instead of the 7zz included in gearlever (both official 7zip)
	sed -i "s/7zz/7z/g" src/providers/AppImageProvider.py
	
	# Direct internally used script to its new location in lib
	sed -i "s/get_appimage_offset/\/usr\/lib\/get_appimage_offset/g" src/providers/AppImageProvider.py
	
	# Fix misplaced comma
	sed -i "s/get_path(, return_stderr/get_path(return_stderr/g" src/providers/AppImageProvider.py

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
	
	cd "${srcdir}/${pkgname}-${pkgver}/"
	install -Dm644 COPYING -t "${pkgdir}/usr/share/licenses/$pkgname/"
	mkdir -p "${pkgdir}/usr/lib"
	install -Dm755 "build-aux/get_appimage_offset.sh" "${pkgdir}/usr/lib/get_appimage_offset"
	
	cd "${pkgdir}"
	rm -v "usr/share/icons/hicolor/scalable/actions/meson.build"
	rm -v "usr/share/${pkgname}/${pkgname}/meson.build"
}
