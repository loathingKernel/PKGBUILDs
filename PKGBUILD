# Maintainer: Luke Featherston <lukefeatherston1223 at gmail dot com>
pkgname=gearlever
pkgver=3.0.2
pkgrel=1
pkgdesc="Manage AppImages with ease"
arch=('x86_64')
url="https://mijorus.it/projects/gearlever/"
license=('GPL-3.0-or-later')
depends=('7zip' 'binutils' 'dconf' 'fuse2' 'gdk-pixbuf2' 'glibc' 'glib2' 'gtk4' 'hicolor-icon-theme'
	 'libadwaita' 'pango' 'python' 'python-dbus' 'python-gobject' 'python-pyxdg' 'python-requests'
	 'zlib')
makedepends=('gettext' 'meson')
checkdepends=('appstream' 'desktop-file-utils')
options=('!strip' '!debug')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/mijorus/gearlever/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c2c8f90ca5feec1a3b9404d7d7647955105087993fd0238f2dd5c6dcfaf364d4')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	# Arch command doesn't seem to exist on arch linux so instead we can substitute it for 'uname' for now
	sed -i "s/\(\['arch'\]\)/['uname', '-m']/g" src/AppDetails.py
	# Fix an uncritical error that occurs exiting the program prematurely due to a difference in packages
	# (https://github.com/mijorus/gearlever/pull/225#issue-2844151525)
	sed -i "/cwd=dest_path/s/)/, return_stderr=True)/" src/providers/AppImageProvider.py
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
