# Maintainer: Luke Featherston <lukefeatherston1223 at gmail dot com>
pkgname=gearlever
pkgver=3.3.4
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
optdepends=('libxml2-legacy: required for LibreOffice appimage')
options=('!strip' '!debug')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/mijorus/gearlever/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('543d27d87ee77ec0f03559e4e8fe37e2d0689b4d09e5466da75bd9ebc501d6a8')

prepare() {
   cd "${srcdir}/${pkgname}-${pkgver}"
   # Arch command doesn't seem to exist on arch linux so instead we can substitute it for 'uname' for now
   sed -i "s/\(\['arch'\]\)/['uname', '-m']/g" src/AppDetails.py src/models/UpdateManager.py

   # Arch linux uses the 7z command instead of the 7zz included in gearlever (both official 7zip)
   sed -i "s/7zz/7z/g" src/providers/AppImageProvider.py

   # Direct internally used script to its new location in lib
   sed -i "s/get_appimage_offset/\/usr\/lib\/gearlever\/get_appimage_offset/g" src/providers/AppImageProvider.py
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
   mkdir -p "${pkgdir}/usr/lib/gearlever"
   install -Dm755 "build-aux/get_appimage_offset.sh" "${pkgdir}/usr/lib/gearlever/get_appimage_offset"

   cd "${pkgdir}"
   rm -v "usr/share/icons/hicolor/scalable/actions/meson.build"
   rm -v "usr/share/${pkgname}/${pkgname}/meson.build"
}
