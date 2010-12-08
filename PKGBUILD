# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-mesa' 'lib32-libgl' 'lib32-ati-dri' 'lib32-intel-dri' 'lib32-unichrome-dri' 'lib32-mach64-dri' 'lib32-mga-dri' 'lib32-r128-dri' 'lib32-savage-dri' 'lib32-sis-dri' 'lib32-tdfx-dri' 'lib32-nouveau-dri')
pkgver=7.9.0.git20101207
pkgrel=2
arch=(x86_64)
makedepends=('glproto>=1.4.12' 'pkgconfig' 'lib32-libdrm>=2.4.22' 'lib32-libxxf86vm>=1.1.0' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.0.1' 'lib32-libx11>=1.3.5' 'lib32-libxt>=1.0.8' 
'lib32-gcc-libs>=4.5' 'dri2proto=2.3' 'lib32-talloc' 'python2' 'libxml2' 'gcc-multilib')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=( # ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2
	# mesa git shot from 7.9 branch - see for state: http://cgit.freedesktop.org/mesa/mesa/commit/?h=7.9&id=dc4956922dfbec2fb2f60539be97760022bd4613
	ftp://ftp.archlinux.org/other/mesa/mesa-dc4956922dfbec2fb2f60539be97760022bd4613.tar.bz2
        ftp://ftp.freedesktop.org/pub/mesa/demos/8.0.1/mesa-demos-8.0.1.tar.bz2)
md5sums=('c44b2d5a82f466325163cb68abe61ec7'
         '320c2a4b6edc6faba35d9cb1e2a30bf4')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

#  cd "${srcdir}/Mesa-${pkgver}"
  cd ${srcdir}/mesa-*

  # required for git build
#  autoreconf -vfi

  # python2 build fixes
  sed -i -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
         -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" $(find $srcdir -name '*.py')
  sed -i -e "s|PYTHON2 = python|PYTHON2 = python2|" configs/{default,autoconf.in}
  sed -i -e "s|python|python2|" src/gallium/auxiliary/Makefile

#  ./configure --prefix=/usr \
  ./autogen.sh --prefix=/usr \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --disable-egl \
    --enable-gallium-radeon \
    --enable-gallium-nouveau \
    --enable-glx-tls \
    --with-driver=dri \
    --enable-xcb \
    --with-state-trackers=dri,glx \
    --disable-glut \
    --enable-32-bit \
    --libdir=/usr/lib32
  make
}

package_lib32-libgl() {
  depends=('lib32-libdrm>=2.4.22' 'lib32-libxxf86vm>=1.1.0' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.0.1' "libgl")
  pkgdesc="Mesa 3-D graphics library and DRI software rasterizer (32-bit)"

#  cd "${srcdir}/Mesa-${pkgver}"
  cd ${srcdir}/mesa-*
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
  depends=('lib32-libgl' 'lib32-libx11>=1.3.5' 'lib32-libxt>=1.0.8' 'lib32-gcc-libs>=4.5' 'dri2proto=2.3' 'lib32-libdrm>=2.4.22' 'glproto>=1.4.12' "mesa")
  pkgdesc="Mesa 3-D graphics libraries and include files (32-bit)"

#  cd "${srcdir}/Mesa-${pkgver}"
  cd ${srcdir}/mesa-*
  make DESTDIR="${pkgdir}" install

  cd "${srcdir}/mesa-demos-8.0.1/src/xdemos"
  install -m755 -d "${pkgdir}/usr/bin"
  $CC glxinfo.c -I${pkgdir}/usr/include -L${pkgdir}/usr/lib32 -lX11 -lGL -o "${pkgdir}/usr/bin/glxinfo32"

  rm -f "${pkgdir}/usr/lib32/libGL.so"*
  rm -rf "${pkgdir}/usr/lib32/xorg"
  rm -rf "${pkgdir}"/usr/{include,share}

  install -m755 -d "${pkgdir}/usr/share/licenses/mesa"
  ln -s mesa "$pkgdir/usr/share/licenses/mesa/$pkgname"
}

package_lib32-ati-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI + Gallium3D r300 drivers for AMD/ATI Radeon (32-bit)"
  conflicts=('xf86-video-ati<6.9.0-6')

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C radeon DESTDIR="${pkgdir}" install
  make -C r200 DESTDIR="${pkgdir}" install
  # classic mesa driver for R300 r300_dri.so
  #make -C r300 DESTDIR="${pkgdir}" install  <------- depricated
  # gallium3D driver for R300 r300_dri.so
#  make -C ${srcdir}/Mesa-${pkgver}/src/gallium/targets/dri-r300 DESTDIR="${pkgdir}" install
  make -C ${srcdir}/mesa-*/src/gallium/targets/dri-r300 DESTDIR="${pkgdir}" install
  make -C r600 DESTDIR="${pkgdir}" install
}

package_lib32-intel-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Intel (32-bit)"

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C i810 DESTDIR="${pkgdir}" install
  make -C i915 DESTDIR="${pkgdir}" install
  make -C i965 DESTDIR="${pkgdir}" install
}

package_lib32-unichrome-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Graphics/VIA Unichrome (32-bit)"

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C unichrome DESTDIR="${pkgdir}" install
}

package_lib32-mach64-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Mach64 (32-bit)"
  conflicts=('xf86-video-mach64<6.8.2')

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C mach64 DESTDIR="${pkgdir}" install
}

package_lib32-mga-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Matrox (32-bit)"
  conflicts=('xf86-video-mga<1.4.11')

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C mga DESTDIR="${pkgdir}" install
}

package_lib32-r128-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Rage128 (32-bit)"
  conflicts=('xf86-video-r128<6.8.1')

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C r128 DESTDIR="${pkgdir}" install
}

package_lib32-savage-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Sraphics/VIA Savage (32-bit)"
  conflicts=('xf86-video-savage<2.3.1')

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C savage DESTDIR="${pkgdir}" install
}

package_lib32-sis-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for SiS (32-bit)"
  conflicts=('xf86-video-sis<0.10.2')

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C sis DESTDIR="${pkgdir}" install
}

package_lib32-tdfx-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for 3dfx (32-bit)"
  conflicts=('xf86-video-tdfx<1.4.3')

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  make -C tdfx DESTDIR="${pkgdir}" install
}

package_lib32-nouveau-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa classic DRI + Gallium3D drivers for Nouveau (32-bit)"

#  cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  # classic mesa driver for nv10 , nv20 nouveau_vieux_dri.so
  make -C nouveau DESTDIR="${pkgdir}" install
  # gallium3D driver for nv30 - nv40 - nv50 nouveau_dri.so
#  make -C ${srcdir}/Mesa-${pkgver}/src/gallium/targets/dri-nouveau DESTDIR="${pkgdir}" install
  make -C ${srcdir}/mesa-*/src/gallium/targets/dri-nouveau DESTDIR="${pkgdir}" install
}

