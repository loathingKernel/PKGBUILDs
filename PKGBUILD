# Maintainer: Jan de Groot <jgc@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-mesa' 'lib32-libgl' 'lib32-ati-dri' 'lib32-intel-dri' 'lib32-unichrome-dri' 'lib32-mach64-dri' 'lib32-mga-dri' 'lib32-r128-dri' 'lib32-savage-dri' 'lib32-sis-dri' 'lib32-tdfx-dri' 'lib32-nouveau-dri')
pkgver=7.8.2
pkgrel=2
arch=(x86_64)
makedepends=('glproto>=1.4.11' 'pkgconfig' 'lib32-libdrm>=2.4.21' 'lib32-libxxf86vm>=1.1.0' 'lib32-libxdamage>=1.1.2' 'lib32-expat>=2.0.1' 'lib32-libx11>=1.3.3' 'lib32-libxt>=1.0.8' 'gcc-libs-multilib>=4.5' 'dri2proto=2.3' 'python')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2
        nouveau_class.h)
md5sums=('6be2d343a0089bfd395ce02aaf8adb57'
         '850546127f5185959407a78b55f898d8')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cd "${srcdir}/Mesa-${pkgver}"
  cp "${srcdir}/nouveau_class.h" "src/gallium/drivers/nouveau/"
  ./configure --prefix=/usr \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --with-dri-drivers=swrast,radeon,r200,r300,r600,i810,i915,i965,unichrome,mach64,mga,r128,savage,sis,tdfx \
    --disable-egl \
    --disable-gallium-intel \
    --enable-glx-tls \
    --with-driver=dri \
    --enable-xcb \
    --with-state-trackers=dri,glx \
    --enable-gallium-nouveau \
    --disable-glut \
    --enable-32-bit \
    --libdir=/usr/lib32
  make
}

package_lib32-libgl() {
  depends=('lib32-libdrm>=2.4.21' 'lib32-libxxf86vm>=1.1.0' 'lib32-libxdamage>=1.1.2' 'lib32-expat>=2.0.1' "libgl")
  pkgdesc="Mesa 3-D graphics library and DRI software rasterizer (32-bit)"

  cd "${srcdir}/Mesa-${pkgver}"
  install -m755 -d "${pkgdir}/usr/lib32"
  install -m755 -d "${pkgdir}/usr/lib32/xorg/modules/extensions"

  bin/minstall lib32/libGL.so* "${pkgdir}/usr/lib32/"

  cd src/mesa/drivers/dri
  make -C swrast DESTDIR="${pkgdir}" install
  ln -s libglx.xorg "${pkgdir}/usr/lib32/xorg/modules/extensions/libglx.so"

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  install -m755 -d "${pkgdir}/usr/share/licenses/libgl"
  ln -s libgl "$pkgdir/usr/share/licenses/libgl/$pkgname"
}

package_lib32-mesa() {
  depends=('lib32-libgl' 'lib32-libx11>=1.3.3' 'lib32-libxt>=1.0.8' 'gcc-libs-multilib>=4.5' 'dri2proto=2.3' 'lib32-libdrm>=2.4.20' 'glproto>=1.4.11' "mesa")
  pkgdesc="Mesa 3-D graphics libraries and include files (32-bit)"

  cd "${srcdir}/Mesa-${pkgver}"
  make DESTDIR="${pkgdir}" install

  rm -f "${pkgdir}/usr/lib32/libGL.so"*
  rm -rf "${pkgdir}/usr/lib32/xorg"

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  install -m755 -d "${pkgdir}/usr/share/licenses/mesa"
  ln -s mesa "$pkgdir/usr/share/licenses/mesa/$pkgname"
}

package_lib32-ati-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for AMD/ATI Radeon (32-bit)"
  conflicts=('xf86-video-ati<6.9.0-6')

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C radeon DESTDIR="${pkgdir}" install
  make -C r200 DESTDIR="${pkgdir}" install
  make -C r300 DESTDIR="${pkgdir}" install
  make -C r600 DESTDIR="${pkgdir}" install
}

package_lib32-intel-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Intel (32-bit)"

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C i810 DESTDIR="${pkgdir}" install
  make -C i915 DESTDIR="${pkgdir}" install
  make -C i965 DESTDIR="${pkgdir}" install
}

package_lib32-unichrome-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Graphics/VIA Unichrome (32-bit)"

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C unichrome DESTDIR="${pkgdir}" install
}

package_lib32-mach64-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Mach64 (32-bit)"
  conflicts=('xf86-video-mach64<6.8.2')

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C mach64 DESTDIR="${pkgdir}" install
}

package_lib32-mga-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Matrox (32-bit)"
  conflicts=('xf86-video-mga<1.4.11')

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C mga DESTDIR="${pkgdir}" install
}

package_lib32-r128-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Rage128 (32-bit)"
  conflicts=('xf86-video-r128<6.8.1')

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C r128 DESTDIR="${pkgdir}" install
}

package_lib32-savage-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Sraphics/VIA Savage (32-bit)"
  conflicts=('xf86-video-savage<2.3.1')

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C savage DESTDIR="${pkgdir}" install
}

package_lib32-sis-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for SiS (32-bit)"
  conflicts=('xf86-video-sis<0.10.2')

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C sis DESTDIR="${pkgdir}" install
}

package_lib32-tdfx-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for 3dfx (32-bit)"
  conflicts=('xf86-video-tdfx<1.4.3')

  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  make -C tdfx DESTDIR="${pkgdir}" install
}

package_lib32-nouveau-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa Gallium3D DRI drivers for Nouveau - highly experimental/unsupported (32-bit)"

  cd "${srcdir}/Mesa-${pkgver}/src/gallium/winsys/drm/nouveau/dri"
  make DESTDIR="${pkgdir}" install
}
