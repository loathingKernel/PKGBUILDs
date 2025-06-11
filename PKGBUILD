# Contributor: NexAdn <git@nexadn.de>
# Maintainer: javsanpar <javsanpar@riseup.net>
pkgname=abaddon
pkgver=0.2.2
pkgrel=1
pkgdesc='An alternative Discord client made with C++/gtkmm'
url='https://github.com/uowuo/abaddon'
source=("git+https://github.com/uowuo/abaddon#tag=v$pkgver"
        $pkgname.desktop)
arch=('x86_64')
license=('GPL3')
makedepends=('git' 'cmake' 'nlohmann-json')
depends=('gtkmm3' 'libhandy' 'spdlog' 'opus' 'libsodium' 'rnnoise')
conflicts=('abaddon')
provides=('abaddon')
sha256sums=('SKIP'
            '7840732362b8f2202cf79b7d7c2eb0e2cbd5a83dc45c5fca4609ec15b8bea6df')

prepare () {
  cd "$pkgname"

  git submodule update --init --filter=tree:0 subprojects/{ixwebsocket,keychain,miniaudio,qrcodegen}
}

build () {
  cmake -B build -D CMAKE_INSTALL_PREFIX=/usr -S "$pkgname"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm755 abaddon.desktop \
    "$pkgdir"/usr/share/applications/abaddon.desktop
}
