# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-mesa' 'lib32-libgl' 'lib32-libgles' 'lib32-libegl' 'lib32-ati-dri' 'lib32-intel-dri' 'lib32-unichrome-dri' 'lib32-mach64-dri' 'lib32-mga-dri' 'lib32-r128-dri' 'lib32-savage-dri' 
'lib32-sis-dri' 'lib32-tdfx-dri' 'lib32-nouveau-dri')

_git=true
#_git=false

if [ "${_git}" = "true" ]; then
    pkgver=7.10.99.git20110412
  else
    pkgver=7.10.2
fi

pkgrel=1
arch=(x86_64)
makedepends=('glproto>=1.4.12' 'pkgconfig' 'lib32-libdrm>=2.4.25' 'lib32-libxxf86vm>=1.1.1' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.0.1' 'lib32-libx11>=1.4.3' 'lib32-libxt>=1.1.1' 
'lib32-gcc-libs>=4.5' 'dri2proto=2.3' 'python2' 'libxml2' 'gcc-multilib' imake 'lib32-udev')
url="http://mesa3d.sourceforge.net"
license=('custom')
if [ "${_git}" = "true" ]; then
  # mesa git shot from 7.11 branch - see for state: http://cgit.freedesktop.org/mesa/mesa/commit/?id=f05751aa2af1a8ec83c2d110385aab1b7e735238
  source=('ftp://ftp.archlinux.org/other/mesa/mesa-f05751aa2af1a8ec83c2d110385aab1b7e735238.tar.bz2')
  md5sums=('56d8862d1155f7e8054f9aa7f93ebebc')
else
  source=("ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2" nouveau-fix-header.patch)
  md5sums=('f5de82852f1243f42cc004039e10b771' '67c87b77cc2236b52a3b47dad3fbb5d4')
fi

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*   
    autoreconf -vfi
  else
    cd "${srcdir}/Mesa-${pkgver}" 
  fi

  if [ "${_git}" != "true" ]; then
    patch -Np1 -i "${srcdir}/nouveau-fix-header.patch"
  fi

  if [ "${_git}" = "true" ]; then
    ./autogen.sh --prefix=/usr \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --enable-gallium-radeon \
    --enable-gallium-r600 \
    --enable-gallium-nouveau \
    --enable-gallium-swrast \
    --enable-glx-tls \
    --with-driver=dri \
    --enable-xcb \
    --with-state-trackers=dri,glx \
    --disable-glut \
    --enable-gles1 \
    --enable-gles2 \
    --enable-egl \
    --disable-gallium-egl \
    --enable-32-bit \
    --libdir=/usr/lib32
  else
    ./configure --prefix=/usr \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --enable-gallium-radeon \
    --enable-gallium-r600 \
    --enable-gallium-nouveau \
    --enable-gallium-swrast \
    --enable-glx-tls \
    --with-driver=dri \
    --enable-xcb \
    --with-state-trackers=dri,glx \
    --disable-glut \
    --enable-gles1 \
    --enable-gles2 \
    --enable-egl \
    --disable-gallium-egl \
    --enable-32-bit \
    --libdir=/usr/lib32
  fi

  make
}

package_lib32-libgl() {
  depends=('lib32-libdrm>=2.4.25' 'lib32-libxxf86vm>=1.1.1' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.0.1' 'lib32-gcc-libs>=4.5' 'libgl')
  pkgdesc="Mesa 3-D graphics library and DRI software rasterizer (32-bit)"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*   
  else
    cd "${srcdir}/Mesa-${pkgver}" 
  fi

  install -m755 -d "${pkgdir}/usr/lib32"
  install -m755 -d "${pkgdir}/usr/lib32/xorg/modules/extensions"

  bin/minstall lib32/libGL.so* "${pkgdir}/usr/lib32/"

  if [ "${_git}" = "true" ]; then
    make -C ${srcdir}/mesa-*/src/gallium/targets/dri-swrast DESTDIR="${pkgdir}" install
  else
    make -C ${srcdir}/Mesa-${pkgver}/src/gallium/targets/dri-swrast DESTDIR="${pkgdir}" install
  fi
  ln -s swrastg_dri.so "${pkgdir}/usr/lib32/xorg/modules/dri/swrast_dri.so"
  ln -s libglx.xorg "${pkgdir}/usr/lib32/xorg/modules/extensions/libglx.so"

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  install -m755 -d "${pkgdir}/usr/share/licenses/libgl"
  ln -s libgl "$pkgdir/usr/share/licenses/libgl/lib32-libgl"
}

package_lib32-libgles() {
  depends=('libgles')
  pkgdesc="Mesa GLES libraries (32-bit)"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*   
  else
    cd "${srcdir}/Mesa-${pkgver}" 
  fi

  install -m755 -d "${pkgdir}/usr/lib32"
  install -m755 -d "${pkgdir}/usr/lib32/pkgconfig"
  bin/minstall lib32/libGLESv* "${pkgdir}/usr/lib32/"
  bin/minstall src/mapi/es1api/glesv1_cm.pc "${pkgdir}/usr/lib32/pkgconfig/"
  bin/minstall src/mapi/es2api/glesv2.pc "${pkgdir}/usr/lib32/pkgconfig/"

  install -m755 -d "${pkgdir}/usr/share/licenses/libgles"
  ln -s libgles "$pkgdir/usr/share/licenses/libgles/lib32-libgles"
}

package_lib32-libegl() {
  depends=('lib32-udev' 'libegl')
  pkgdesc="Mesa libEGL libraries (32-bit)"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*   
  else
    cd "${srcdir}/Mesa-${pkgver}" 
  fi

  install -m755 -d "${pkgdir}/usr/lib32"
  install -m755 -d "${pkgdir}/usr/lib32/pkgconfig"
  bin/minstall lib32/libEGL.so* "${pkgdir}/usr/lib32/"
  if [ "${_git}" != "true" ]; then
    install -m755 -d "${pkgdir}/usr/lib32/egl"
    bin/minstall lib32/egl/* "${pkgdir}/usr/lib32/egl/"
  fi
  bin/minstall src/egl/main/egl.pc "${pkgdir}/usr/lib32/pkgconfig/"

  install -m755 -d "${pkgdir}/usr/share/licenses/libegl"
  ln -s libgles "$pkgdir/usr/share/licenses/libegl/lib32-libegl"
}

package_lib32-mesa() {
  depends=('lib32-libgl' 'lib32-libx11>=1.4.3' 'lib32-libxt>=1.1.1' 'lib32-libdrm>=2.4.25' 'lib32-gcc-libs>=4.5' 'mesa')
  pkgdesc="Mesa 3-D graphics libraries and include files (32-bit)"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*   
  else
    cd "${srcdir}/Mesa-${pkgver}" 
  fi

  make DESTDIR="${pkgdir}" install


  rm -f "${pkgdir}/usr/lib32/libGL.so"*
  rm -f "${pkgdir}/usr/lib32/libGLESv"*
  rm -f "${pkgdir}/usr/lib32/libEGL"*
  rm -rf "${pkgdir}/usr/lib32/egl"
  rm -f ${pkgdir}/usr/lib32/pkgconfig/{glesv1_cm.pc,glesv2.pc,egl.pc}
  rm -rf "$pkgdir"/{usr/include,usr/lib32/xorg}

  install -m755 -d "${pkgdir}/usr/share/licenses/mesa"
  ln -s mesa "$pkgdir/usr/share/licenses/mesa/lib32-mesa"
}

package_lib32-ati-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI + Gallium3D for r300 and later chipsets drivers for AMD/ATI Radeon (32-bit)"
  conflicts=('xf86-video-ati<6.9.0-6')

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C radeon DESTDIR="${pkgdir}" install
  make -C r200 DESTDIR="${pkgdir}" install

  # DRI drivers for r300 and r600 are removed
  # gallium3D driver for R300 and R600 r300_dri.so/r600_dri.so
  if [ "${_git}" = "true" ]; then
    make -C ${srcdir}/mesa-*/src/gallium/targets/dri-r300 DESTDIR="${pkgdir}" install
    make -C ${srcdir}/mesa-*/src/gallium/targets/dri-r600 DESTDIR="${pkgdir}" install
  else
    make -C ${srcdir}/Mesa-${pkgver}/src/gallium/targets/dri-r300 DESTDIR="${pkgdir}" install
    make -C ${srcdir}/Mesa-${pkgver}/src/gallium/targets/dri-r600 DESTDIR="${pkgdir}" install
  fi
}

package_lib32-intel-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Intel (32-bit)"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C i810 DESTDIR="${pkgdir}" install
  make -C i915 DESTDIR="${pkgdir}" install
  make -C i965 DESTDIR="${pkgdir}" install
}

package_lib32-unichrome-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Graphics/VIA Unichrome (32-bit)"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C unichrome DESTDIR="${pkgdir}" install
}

package_lib32-mach64-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Mach64 (32-bit)"
  conflicts=('xf86-video-mach64<6.8.2')

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C mach64 DESTDIR="${pkgdir}" install
}

package_lib32-mga-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Matrox (32-bit)"
  conflicts=('xf86-video-mga<1.4.11')

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C mga DESTDIR="${pkgdir}" install
}

package_lib32-r128-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Rage128 (32-bit)"
  conflicts=('xf86-video-r128<6.8.1')

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C r128 DESTDIR="${pkgdir}" install
}

package_lib32-savage-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Sraphics/VIA Savage (32-bit)"
  conflicts=('xf86-video-savage<2.3.1')

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C savage DESTDIR="${pkgdir}" install
}

package_lib32-sis-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for SiS (32-bit)"
  conflicts=('xf86-video-sis<0.10.2')

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C sis DESTDIR="${pkgdir}" install
}

package_lib32-tdfx-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for 3dfx (32-bit)"
  conflicts=('xf86-video-tdfx<1.4.3')

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  make -C tdfx DESTDIR="${pkgdir}" install
}

package_lib32-nouveau-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa classic DRI + Gallium3D drivers for Nouveau (32-bit)"

  if [ "${_git}" = "true" ]; then
    cd ${srcdir}/mesa-*/src/mesa/drivers/dri
  else
    cd "${srcdir}/Mesa-${pkgver}/src/mesa/drivers/dri"
  fi

  # classic mesa driver for nv10 , nv20 nouveau_vieux_dri.so
  make -C nouveau DESTDIR="${pkgdir}" install
  # gallium3D driver for nv30 - nv40 - nv50 nouveau_dri.so
  if [ "${_git}" = "true" ]; then
    make -C ${srcdir}/mesa-*/src/gallium/targets/dri-nouveau DESTDIR="${pkgdir}" install
  else
    make -C ${srcdir}/Mesa-${pkgver}/src/gallium/targets/dri-nouveau DESTDIR="${pkgdir}" install
  fi
}

