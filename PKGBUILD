# Maintainer: Manuel Barrio Linares <mbarriolinares at gmail dot com>
# Contributor: Leonidas P. <jpegxguy at outlook dot com>

pkgname=ksmbd-tools
pkgver=3.5.4
pkgrel=1
pkgdesc="Userspace tools for the ksmbd kernel SMB server"
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/cifsd-team/ksmbd-tools"
license=('GPL2')
depends=('KSMBD-MODULE' 'libnl')
provides=('samba')
makedepends=('meson' 'ninja')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('465ac06b75b47523953d979d9d3d831acca2b3c6b8ee3e69bcded5787bc075f9')

build() {
  cd "${pkgname}-${pkgver}"
  arch-meson build --prefix=/usr --sbindir=/usr/bin --libexecdir=/usr/lib/${pkgname} --sysconfdir=/etc -Drundir=/run
  meson compile -C build
}

package() {
	DESTDIR="${pkgdir}" ninja -C "${pkgname}-${pkgver}/build" install
}
