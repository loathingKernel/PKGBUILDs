# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-mesa' 'lib32-libgl' 'lib32-libglapi' 'lib32-libgles' 'lib32-libegl' 'lib32-ati-dri' 'lib32-intel-dri' 'lib32-unichrome-dri'
  'lib32-mach64-dri' 'lib32-mga-dri' 'lib32-r128-dri' 'lib32-savage-dri' 'lib32-sis-dri' 'lib32-tdfx-dri' 'lib32-nouveau-dri')
# prepare 7.12/8.0
# pkgname=('lib32-mesa' 'lib32-libgl' 'lib32-libglapi' 'lib32-libgles' 'lib32-libegl' 'lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri')

#_git=true
_gitdate=20111031
_git=false

if [ "${_git}" = "true" ]; then
    #pkgver=7.10.99.git20110709
    pkgver=7.11
  else
    pkgver=7.11.1
fi

pkgrel=1
arch=(x86_64)
makedepends=('glproto>=1.4.14' 'lib32-libdrm>=2.4.26' 'lib32-libxxf86vm>=1.1.1' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.0.1' 'lib32-libx11>=1.4.3'
  'lib32-libxt>=1.1.1' 'lib32-gcc-libs>=4.6.1' 'dri2proto>=2.6' 'python2' 'libxml2' 'gcc-multilib' imake 'lib32-udev' 'lib32-llvm' 'namcap')
url="http://mesa3d.sourceforge.net"
license=('custom')
if [ "${_git}" = "true" ]; then
  # mesa git shot from 7.11 branch - see for state: http://cgit.freedesktop.org/mesa/mesa/commit/?h=7.11&id=1ae00c5960af83bea9545a18a1754bad83d5cbd0
  #source=('ftp://ftp.archlinux.org/other/mesa/mesa-1ae00c5960af83bea9545a18a1754bad83d5cbd0.tar.bz2')
  source=("MesaLib-git${_gitdate}.zip"::"http://cgit.freedesktop.org/mesa/mesa/snapshot/mesa-ef9f16f6322a89fb699fbe3da868b10f9acaef98.tar.bz2")
  md5sums=('817a63bb60b81f4f817ffc9ed0a3dddd')
else
  source=("ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2")
  #source=(${source[@]} "MesaLib-git${_gitdate}.zip"::"http://cgit.freedesktop.org/mesa/mesa/snapshot/mesa-4464ee1a9aa3745109cee23531e3fb2323234d07.tar.bz2")
  md5sums=('a77307102cee844ff6544ffa8fafeac1')
fi

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  # for our llvm-config for 32 bit
  export LLVM_CONFIG=/usr/lib32/llvm/llvm-config

  cd ${srcdir}/?esa-*   
  autoreconf -vfi

  if [ "${_git}" = "true" ]; then
     ./autogen.sh --prefix=/usr \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --with-gallium-drivers=r300,r600,nouveau,swrast \
    --enable-gallium-llvm \
    --enable-gallium-egl --enable-shared-glapi \
    --enable-glx-tls \
    --with-driver=dri \
    --enable-xcb \
    --disable-glut \
    --enable-gles1 \
    --enable-gles2 \
    --enable-egl \
    --enable-texture-float \
    --enable-shared-dricore \
    --enable-32-bit \
    --libdir=/usr/lib32
    #  --enable-gallium-svga \
  else
    ./configure --prefix=/usr \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --with-gallium-drivers=r300,r600,nouveau,swrast \
    --enable-gallium-llvm \
    --enable-gallium-egl --enable-shared-glapi \
    --enable-glx-tls \
    --with-driver=dri \
    --enable-xcb \
    --disable-glut \
    --enable-gles1 \
    --enable-gles2 \
    --enable-egl \
    --enable-texture-float \
    --enable-shared-dricore \
    --enable-32-bit \
    --libdir=/usr/lib32
  fi

  make
}

package_lib32-libgl() {
  depends=('lib32-libdrm>=2.4.26' 'lib32-libxxf86vm>=1.1.1' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.0.1' 'lib32-libglapi' 'libgl')
  pkgdesc="Mesa 3-D graphics library and DRI software rasterizer (32-bit)"

  cd ${srcdir}/?esa-*
  install -m755 -d "${pkgdir}/usr/lib32"
  install -m755 -d "${pkgdir}/usr/lib32/xorg/modules/extensions"

  bin/minstall lib32/libGL.so* "${pkgdir}/usr/lib32/"
  bin/minstall lib32/libdricore.so* "${pkgdir}/usr/lib32/"
  bin/minstall lib32/libglsl.so* "${pkgdir}/usr/lib32/"

  make -C ${srcdir}/?esa-*/src/gallium/targets/dri-swrast DESTDIR="${pkgdir}" install
  ln -s swrastg_dri.so "${pkgdir}/usr/lib32/xorg/modules/dri/swrast_dri.so"
  ln -s libglx.xorg "${pkgdir}/usr/lib32/xorg/modules/extensions/libglx.so"

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  install -m755 -d "${pkgdir}/usr/share/licenses/libgl"
  ln -s libgl "$pkgdir/usr/share/licenses/libgl/lib32-libgl"
}

package_lib32-libglapi() {
  depends=('lib32-glibc' 'libglapi')
  pkgdesc="free implementation of the GL API -- shared library. The Mesa GL API module is responsible for dispatching all the gl* functions (32-bits)"

  cd ${srcdir}/?esa-*   
  install -m755 -d "${pkgdir}/usr/lib32"
  bin/minstall lib32/libglapi.so* "${pkgdir}/usr/lib32/"

  install -m755 -d "${pkgdir}/usr/share/licenses/libglapi"
  ln -s libglapi "${pkgdir}/usr/share/licenses/libglapi/lib32-libglapi"
}

package_lib32-libgles() {
  depends=('lib32-libglapi' 'libgles')
  pkgdesc="Mesa GLES libraries (32-bit)"

  cd ${srcdir}/?esa-*
  install -m755 -d "${pkgdir}/usr/lib32"
  install -m755 -d "${pkgdir}/usr/lib32/pkgconfig"
  bin/minstall lib32/libGLESv* "${pkgdir}/usr/lib32/"
  bin/minstall src/mapi/es1api/glesv1_cm.pc "${pkgdir}/usr/lib32/pkgconfig/"
  bin/minstall src/mapi/es2api/glesv2.pc "${pkgdir}/usr/lib32/pkgconfig/"

  install -m755 -d "${pkgdir}/usr/share/licenses/libgles"
  ln -s libgles "$pkgdir/usr/share/licenses/libgles/lib32-libgles"
}

package_lib32-libegl() {
  depends=('lib32-libglapi' 'lib32-libdrm' 'lib32-udev' 'lib32-libxfixes' 'lib32-libxext' 'libegl')
  pkgdesc="Mesa libEGL libraries (32-bit)"

  cd ${srcdir}/?esa-*
  make -C src/gallium/targets/egl-static DESTDIR="${pkgdir}" install

  install -m755 -d "${pkgdir}/usr/lib32"
  install -m755 -d "${pkgdir}/usr/lib32/pkgconfig"
  install -m755 -d "${pkgdir}/usr/lib32/egl"
  bin/minstall lib32/libEGL.so* "${pkgdir}/usr/lib32/"
  bin/minstall lib32/egl/* "${pkgdir}/usr/lib32/egl/"
  bin/minstall src/egl/main/egl.pc "${pkgdir}/usr/lib32/pkgconfig/"

  install -m755 -d "${pkgdir}/usr/share/licenses/libegl"
  ln -s libgles "$pkgdir/usr/share/licenses/libegl/lib32-libegl"
}

package_lib32-mesa() {
  depends=('lib32-libgl' 'lib32-libx11>=1.4.3' 'lib32-libxt>=1.1.1' 'lib32-gcc-libs>=4.6.1' 'mesa')
  pkgdesc="Mesa 3-D graphics libraries and include files (32-bit)"

  cd ${srcdir}/?esa-*
  make DESTDIR="${pkgdir}" install

  rm -f "${pkgdir}/usr/lib32/libGL.so"*
  rm -f "${pkgdir}/usr/lib32/libglapi.so"*
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
  pkgdesc="Mesa DRI radeon/r200 + Gallium3D for r300 and later chipsets drivers for AMD/ATI Radeon (32-bit)"
  conflicts=('xf86-video-ati<6.9.0-6')

  cd ${srcdir}/?esa-*/src/mesa/drivers/dri
  # classic mesa drivers for radeon,r200
  make -C radeon DESTDIR="${pkgdir}" install
  make -C r200 DESTDIR="${pkgdir}" install
  # gallium3D driver for R300 and R600 r300_dri.so/r600_dri.so
  make -C ${srcdir}/?esa-*/src/gallium/targets/dri-r300 DESTDIR="${pkgdir}" install
  make -C ${srcdir}/?esa-*/src/gallium/targets/dri-r600 DESTDIR="${pkgdir}" install
}

package_lib32-intel-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Intel (32-bit)"

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/i810 DESTDIR="${pkgdir}" install # dead in 7.12
  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/i915 DESTDIR="${pkgdir}" install
  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/i965 DESTDIR="${pkgdir}" install
}

package_lib32-unichrome-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Graphics/VIA Unichrome (32-bit)"

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/unichrome DESTDIR="${pkgdir}" install
}

package_lib32-mach64-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Mach64 (32-bit)"
  conflicts=('xf86-video-mach64<6.8.2')

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/mach64 DESTDIR="${pkgdir}" install
}

package_lib32-mga-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for Matrox (32-bit)"
  conflicts=('xf86-video-mga<1.4.11')

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/mga DESTDIR="${pkgdir}" install
}

package_lib32-r128-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for ATI Rage128 (32-bit)"
  conflicts=('xf86-video-r128<6.8.1')

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/r128 DESTDIR="${pkgdir}" install
}

package_lib32-savage-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for S3 Sraphics/VIA Savage (32-bit)"
  conflicts=('xf86-video-savage<2.3.1')

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/savage DESTDIR="${pkgdir}" install
}

package_lib32-sis-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for SiS (32-bit)"
  conflicts=('xf86-video-sis<0.10.2')

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/sis DESTDIR="${pkgdir}" install
}

package_lib32-tdfx-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa DRI drivers for 3dfx (32-bit)"
  conflicts=('xf86-video-tdfx<1.4.3')

  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/tdfx DESTDIR="${pkgdir}" install
}

package_lib32-nouveau-dri() {
  depends=("lib32-libgl=${pkgver}")
  pkgdesc="Mesa classic DRI + Gallium3D drivers for Nouveau (32-bit)"

  # classic mesa driver for nv10 , nv20 nouveau_vieux_dri.so
  make -C ${srcdir}/?esa-*/src/mesa/drivers/dri/nouveau DESTDIR="${pkgdir}" install
  # gallium3D driver for nv30 - nv40 - nv50 nouveau_dri.so
  make -C ${srcdir}/?esa-*/src/gallium/targets/dri-nouveau DESTDIR="${pkgdir}" install
}

