# Maintainer: loathingkernel <loathingkernel @at gmail .dot com>
# Contributor: gbr <gbr@protonmail.com>
# Contributor: Lubosz Sarnecki <lubosz0@gmail.com>
# Original Package: Martin Wimpress <code@flexion.org>

_pkgbase=nvidia-settings
pkgname=lib32-libxnvctrl
pkgver=550.90.07
pkgrel=1
pkgdesc='NVIDIA NV-CONTROL X extension (32-bit)'
url='https://github.com/NVIDIA/nvidia-settings'
arch=('x86_64')
license=('GPL2')
depends=('lib32-gcc-libs' 'lib32-jansson' 'lib32-libxext')
optdepends=('libxnvctrl: XNVCtrl development headers')
options=('staticlibs')
source=(${_pkgbase}-${pkgver}.tar.gz::https://github.com/NVIDIA/nvidia-settings/archive/${pkgver}.tar.gz
        nvidia-settings-libxnvctrl_so.patch)
sha512sums=('926470be416b9e692891aeea8748f2e529caf4914495048d864b123aaf12ade4dad84abb5ab9aa6837121fd41acc3cd697b567f70486ef49870e7841145bde2d'
            '0303fe615d6ef4e14112998c531a17613b94776f9a6a027ddb81e400fddd5f2ff15583da8b8631c2306aca854edf2f54a8007eb36f1732b4c064c857aaf268ae')

prepare() {
  export PREFIX=/usr
  export NV_USE_BUNDLED_LIBJANSSON=0
  export OUTPUTDIR=out

  cd ${_pkgbase}-${pkgver}
  patch -Np1 -i "${srcdir}"/nvidia-settings-libxnvctrl_so.patch
}

build() {
  cd ${_pkgbase}-${pkgver}
  export CFLAGS+=" -ffat-lto-objects"
  make CC='gcc -m32' PREFIX=/usr OUTPUTDIR=out NV_USE_BUNDLED_LIBJANSSON=0 -C src/libXNVCtrl
}

package() {
  cd ${_pkgbase}-${pkgver}
  install -d "${pkgdir}/usr/lib32"
  cp -Pr src/libXNVCtrl/out/libXNVCtrl.* -t "$pkgdir/usr/lib32"
}
