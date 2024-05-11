# Maintainer: loathingkernel
# Contributor: Torge Matthies <openglfreak at googlemail dot com>
# Contributor: Krzysztof Bogacki <krzysztof dot bogacki at leancode dot pl>

pkgbase=ntsync
pkgname=(ntsync-dkms ntsync-header ntsync-common)
pkgver=6.8.4
pkgrel=1
pkgdesc="NT synchronization primitive driver"
arch=(x86_64)
url='https://repo.or.cz/linux/zf.git/shortlog/refs/heads/ntsync5'
license=('GPL2')
_commit=f787614c40519eb2c8ebdc116b2cd09d46e5ec85
source=("ntsync.c-$_commit::https://raw.githubusercontent.com/zen-kernel/zen-kernel/$_commit/drivers/misc/ntsync.c"
        "ntsync.h-$_commit::https://raw.githubusercontent.com/zen-kernel/zen-kernel/$_commit/include/uapi/linux/ntsync.h"
        'ntsync.conf'
        '99-ntsync.rules'
        'Makefile'
        'dkms.conf')
sha256sums=('3348129a4f2f4b938f175991a807704f8b615d43e111fb4abf60f72cf5b9f39a'
            'b5081f3618c310364879183b5093abdfda654a03a7cb00dd5d4587b723b3c205'
            'c19771ae86e7df179f6b2f4a2837d3f0cbbbba7b32baef41a3c27120c760d78f'
            'ce5221146a19206ba043211db8f27143a82f9224c0aff24a0b584b7268fcb994'
            '834a7b4c9a67a44f2cf593bf259918ea12b0c0eeee7862ed4f9fd268076171cf'
            'e81694fa952711f1b74f02b6a64ac1e90c229f93c740e4f97df5692f3af99609')

prepare() {
    sed -i -e "s/@PACKAGE_VERSION@/$pkgver/g" "$srcdir/dkms.conf"
}

package_ntsync-dkms() {
    pkgdesc+=" - out-of-tree module"
    depends=(dkms ntsync-common)
    optdepends=(
        'ntsync-header: Allow wine to be compiled with ntsync support'
    )
    provides=(NTSYNC-MODULE)
    conflicts=(ntsync)

    install -Dm644 "$srcdir/Makefile" "$pkgdir/usr/src/$pkgbase-$pkgver/Makefile"
    install -Dm644 "$srcdir/ntsync.h-$_commit" "$pkgdir/usr/src/$pkgbase-$pkgver/include/uapi/linux/ntsync.h"
    install -Dm644 "$srcdir/ntsync.c-$_commit" "$pkgdir/usr/src/$pkgbase-$pkgver/drivers/misc/ntsync.c"
    install -Dm644 "$srcdir/dkms.conf" "$pkgdir/usr/src/$pkgbase-$pkgver/dkms.conf"
}

package_ntsync-header() {
    pkgdesc+=" - linux api header file"

    install -Dm644 "$srcdir/ntsync.h-$_commit" "$pkgdir/usr/include/linux/ntsync.h"
}

package_ntsync-common() {
    pkgdesc+=" - common files"
    provides=(ntsync-udev-rule)
    conflicts=(ntsync-udev-rule)
    replaces=(ntsync-udev-rule)

    install -Dm644 "$srcdir/ntsync.conf" "$pkgdir/usr/lib/modules-load.d/ntsync.conf"
    install -Dm644 "$srcdir/99-ntsync.rules" "$pkgdir/usr/lib/udev/rules.d/99-ntsync.rules"
}

