# Contributor: Mettacrawer <metta.crawler@gmail.com>
# Contributor: luizribeiro <luizribeiro@gmail.com>
# Maintainer:  max.bra <max dot bra dot gtalk at gmail dot com>
# Maintainer:  graysky <therealgraysky AT protonmail DOT com>

pkgname=pi-hole-ftl
_pkgname=FTL
_servicename=pihole-FTL
pkgver=6.0.2
pkgrel=2
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
pkgdesc="The Pi-hole FTL engine"
url="https://github.com/pi-hole/FTL"
license=('EUPL-1.2')
depends=('nettle' 'gmp' 'mbedtls' 'pi-hole-web')
makedepends=('cmake')
conflicts=('dnsmasq')
provides=('dnsmasq')
install=$pkgname.install
backup=('etc/pihole/pihole-FTL.conf' 'etc/pihole/dhcp.leases')
source=($pkgname-v$pkgver.tar.gz::"https://github.com/pi-hole/FTL/archive/v$pkgver.tar.gz"
        "https://raw.githubusercontent.com/max72bra/pi-hole-ftl-archlinux-customization/master/arch-ftl-$pkgver-$pkgrel.patch"
        "$pkgname.tmpfile"
        "$pkgname.sysuser"
        "$pkgname.service")
sha256sums=('ccf7adebcfc844d29dd63742eecff585084bb53bf6421ceca1c1c15b44402314'
            'bdef08329a082de6e6a8c08e14c9ddc049a10fa10473eb8af2d21ce49c877671'
            '0feb4597a4afd9054553505d305b0feb7e1f6e1705b092561648ff37d0a2893c'
            'dd1d2a341e774d4e549373ae75604031b9af0ee44debcd71a89259d9110d2a77'
            'fd54fa39539a298a6733a8732ea2f0bcce213361900ad6aa21aad30d2395abfe')

prepare() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  patch -Np1 -i "$srcdir"/arch-ftl-$pkgver-$pkgrel.patch
}

build() {
  cd "$srcdir"/"$_pkgname"-"$pkgver"
  STATIC=false ./build.sh
}

package() {
  cd "$srcdir"
  install -Dm775 "$_pkgname"-$pkgver/pihole-FTL "${pkgdir}"/usr/bin/pihole-FTL

  install -Dm644 "$pkgname.tmpfile" "$pkgdir"/usr/lib/tmpfiles.d/$pkgname.conf
  install -Dm644 "$pkgname.sysuser" "$pkgdir"/usr/lib/sysusers.d/$pkgname.conf

  install -dm755 "$pkgdir"/etc/pihole
  install -Dm664 /dev/null "$pkgdir"/etc/pihole/dhcp.leases

  install -Dm644 "$pkgname.service" "$pkgdir"/usr/lib/systemd/system/$_servicename.service
  install -dm755 "$pkgdir/usr/lib/systemd/system/multi-user.target.wants"
  ln -s ../$_servicename.service "$pkgdir/usr/lib/systemd/system/multi-user.target.wants/$_servicename.service"

  install -dm755 "$pkgdir"/usr/share/licenses/pihole
  install -Dm644 "$_pkgname"-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/pihole/Pi-hole-FTL

  # ver. 5.0+ dnamasq dropin support
  ln -s ./pihole-FTL "$pkgdir/usr/bin/dnsmasq"
}
