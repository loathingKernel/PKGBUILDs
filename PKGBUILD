# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-libglapi' 'lib32-libgl' 'lib32-mesa' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl'
         'lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri')
#_git=true
#_gitdate=20121005
_git=false

if [ "${_git}" = "true" ]; then
    pkgver=8.99.git_$_gitdate
  else
    pkgver=9.0.2
fi

pkgrel=4
arch=('x86_64')
makedepends=('glproto>=1.4.16' 'lib32-libdrm>=2.4.39' 'lib32-libxxf86vm>=1.1.2' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.1.0'
             'lib32-libx11>=1.5.0' 'lib32-libxt>=1.1.3' 'lib32-gcc-libs>=4.7.1-6' 'dri2proto>=2.8' 'python2' 'libxml2'
             'gcc-multilib' 'imake' 'lib32-llvm-amdgpu-snapshot' 'lib32-systemd')
url="http://mesa3d.sourceforge.net"
license=('custom')
options=('!libtool')
source=(llvm32.patch)
if [ "${_git}" = "true" ]; then
  # mesa git shot from 9.0 branch - see for state: http://cgit.freedesktop.org/mesa/mesa/log/?h=9.0
  #source=(${source[@]} 'ftp://ftp.archlinux.org/other/mesa/mesa-41d14eaf193c6b1eb87fe1998808a887f1c6c698.tar.gz')
  source=(${source[@]} "MesaLib-git${_gitdate}.zip"::"http://cgit.freedesktop.org/mesa/mesa/snapshot/mesa-542f6feda9bf18267dbd337943a5e871400d425a.tar.gz")
else
  source=(${source[@]} "ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2")
fi
md5sums=('5fe9ad0c5beed19bc98d8c34aaad4ade'
         'dc45d1192203e418163e0017640e1cfc')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  # for our llvm-config for 32 bit
  export LLVM_CONFIG=/usr/bin/llvm-config32

  cd ${srcdir}/?esa-*

  patch -Np1 -i ${srcdir}/llvm32.patch

  COMMONOPTS="--prefix=/usr \
    --sysconfdir=/etc \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --with-gallium-drivers=r300,r600,radeonsi,nouveau,swrast \
    --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
    --enable-gallium-llvm \
    --enable-egl \
    --enable-gallium-egl
    --with-egl-platforms=x11,drm \
    --enable-shared-glapi \
    --enable-glx-tls \
    --enable-dri \
    --enable-gles1 \
    --enable-gles2 \
    --enable-texture-float \
    --enable-osmesa \
    --enable-32-bit \
    --libdir=/usr/lib32 "

  if [ "${_git}" = "true" ]; then
    ./autogen.sh \
      $COMMONOPTS
  else
    autoreconf -vfi
    ./configure \
      $COMMONOPTS
  fi

  # fix a build break with new llvm
  sed -i "s:-Werror=implicit-function-declaration::" src/gallium/drivers/r600/Makefile

  make
}

package_lib32-libglapi() {
  depends=('lib32-glibc' 'libglapi')
  pkgdesc="free implementation of the GL API -- shared library. The Mesa GL API module is responsible for dispatching all the gl* functions (32-bits)"

  cd ${srcdir}/?esa-*   

  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" install

  install -m755 -d "${pkgdir}/usr/share/licenses/libglapi"
  ln -s libglapi "${pkgdir}/usr/share/licenses/libglapi/lib32-libglapi"
}

package_lib32-libgl() {
  depends=('lib32-libdrm>=2.4.39' 'lib32-libxxf86vm>=1.1.2' 'lib32-libxdamage>=1.1.3' 'lib32-expat>=2.1.0' 'lib32-libglapi'
           'libgl')
  pkgdesc="Mesa 3-D graphics library and DRI software rasterizer (32-bit)"

  cd ${srcdir}/?esa-*

  # fix linking because of splitted package
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" install

  # libGL & libdricore
  make -C src/glx DESTDIR="${pkgdir}" install
  make -C src/mesa/libdricore DESTDIR="${pkgdir}" install
  
  # fix linking because of splitted package - cleanup
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" uninstall
  
  # --with-gallium-drivers=swrast
  make -C src/gallium/targets/dri-swrast DESTDIR="${pkgdir}" install

  install -m755 -d "${pkgdir}/usr/share/licenses/libgl"
  ln -s libgl "${pkgdir}/usr/share/licenses/libgl/lib32-libgl"
}

package_lib32-mesa() {
  # check also gl.pc
  depends=('lib32-libgl' 'lib32-libx11>=1.5.0' 'lib32-libxext>=1.3.1' 'lib32-libxdamage' 'lib32-libxfixes' 'lib32-libxcb'
           'lib32-libxxf86vm' 'mesa')
  pkgdesc="Mesa 3-D graphics libraries and include files (32-bit)"

  cd ${srcdir}/?esa-*

  # .pc files
  make -C src/mesa DESTDIR="${pkgdir}" install-pkgconfigDATA
  make -C src/mesa/drivers/dri DESTDIR="${pkgdir}" install-pkgconfigDATA

  install -m755 -d "${pkgdir}/usr/share/licenses/mesa"
  ln -s mesa "$pkgdir/usr/share/licenses/mesa/lib32-mesa"
}

package_lib32-osmesa() {
  depends=('lib32-libglapi' 'lib32-gcc-libs' 'osmesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages')
  pkgdesc="Mesa 3D off-screen rendering library (32-bits)"

  cd ${srcdir}/?esa-*

  # fix linking because of splitted package
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" install

  make -C src/mesa/drivers/osmesa DESTDIR="${pkgdir}" install
  
  # fix linking because of splitted package - cleanup
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" uninstall
}

package_lib32-libgbm() {
  depends=('lib32-systemd' 'lib32-libglapi' 'lib32-libdrm' 'libgbm')
  pkgdesc="Mesa gbm library (32-bit)"

  cd ${srcdir}/?esa-*

  # fix linking because of splitted package
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" install

  make -C src/gbm DESTDIR="${pkgdir}" install

  # fix linking because of splitted package - cleanup
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" uninstall

  rm -r "${pkgdir}"/usr/include

  install -m755 -d "${pkgdir}/usr/share/licenses/libgbm"
  ln -s libgbm "$pkgdir/usr/share/licenses/libgbm/lib32-libgbm"
}

package_lib32-libgles() {
  depends=('lib32-libglapi' 'lib32-libdrm' 'lib32-libgbm' 'libgles')
  pkgdesc="Mesa GLES libraries (32-bit)"

  cd ${srcdir}/?esa-*

  # fix linking because of splitted package
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" install

  # --enable-gles1 --enable-gles2
  make -C src/mapi/es1api DESTDIR="${pkgdir}" install
  make -C src/mapi/es2api DESTDIR="${pkgdir}" install

  # fix linking because of splitted package - cleanup
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" uninstall
  
  rm -r "${pkgdir}"/usr/include
  
  install -m755 -d "${pkgdir}/usr/share/licenses/libgles"
  ln -s libgles "$pkgdir/usr/share/licenses/libgles/lib32-libgles"
}

package_lib32-libegl() {
  # check also egl.pc
  depends=('lib32-libx11' 'lib32-libxext' 'lib32-libxdamage' 'lib32-libxfixes' 'lib32-libxxf86vm' 'lib32-libxcb' 'lib32-libgbm' 'khrplatform-devel' 'libegl')
  pkgdesc="Mesa EGL libraries and headers"

  cd ${srcdir}/?esa-*

  make -C src/gallium/targets/egl-static DESTDIR="${pkgdir}" install

  # fix linking because of splitted package
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" install
  make -C src/gbm DESTDIR="${pkgdir}" install

  make -C src/egl DESTDIR="${pkgdir}" install

  # fix linking because of splitted package - cleanup
  make -C src/gbm DESTDIR="${pkgdir}" uninstall
  make -C src/mapi/shared-glapi DESTDIR="${pkgdir}" uninstall

  rm -r "${pkgdir}"/usr/include

  install -m755 -d "${pkgdir}/usr/share/licenses/libegl"
  ln -s libegl "$pkgdir/usr/share/licenses/libegl/lib32-libegl"

  # fix file conflicts
  rm -rf ${pkgdir}/usr/include/KHR
}

package_lib32-ati-dri() {
  depends=("lib32-libgl=${pkgver}" 'ati-dri')
  pkgdesc="Mesa DRI radeon/r200 + Gallium3D for r300 and later chipsets drivers for AMD/ATI Radeon (32-bit)"
  conflicts=('xf86-video-ati<6.9.0-6')

  cd ${srcdir}/?esa-*
  
  # fix linking because of splitted package
  make -C src/mesa/libdricore DESTDIR="${pkgdir}" install

  # classic mesa drivers for radeon,r200
  make -C src/mesa/drivers/dri/radeon DESTDIR="${pkgdir}" install
  make -C src/mesa/drivers/dri/r200 DESTDIR="${pkgdir}" install
  # gallium3D driver for r300,r600
  make -C src/gallium/targets/dri-r300 DESTDIR="${pkgdir}" install
  make -C src/gallium/targets/dri-r600 DESTDIR="${pkgdir}" install
  make -C src/gallium/targets/dri-radeonsi DESTDIR="${pkgdir}" install
  
  # fix linking because of splitted package - cleanup
  make -C src/mesa/libdricore DESTDIR="${pkgdir}" uninstall
  
  install -m755 -d "${pkgdir}/usr/share/licenses/ati-dri"
  ln -s ati-dri "$pkgdir/usr/share/licenses/ati-dri/lib32-ati-dri"
}

package_lib32-intel-dri() {
  depends=("lib32-libgl=${pkgver}" 'intel-dri')
  pkgdesc="Mesa DRI drivers for Intel (32-bit)"

  cd ${srcdir}/?esa-*
  
  # fix linking because of splitted package
  make -C src/mesa/libdricore DESTDIR="${pkgdir}" install

  make -C src/mesa/drivers/dri/i915 DESTDIR="${pkgdir}" install
  make -C src/mesa/drivers/dri/i965 DESTDIR="${pkgdir}" install
  
  # fix linking because of splitted package - cleanup
  make -C src/mesa/libdricore DESTDIR="${pkgdir}" uninstall
  
  install -m755 -d "${pkgdir}/usr/share/licenses/intel-dri"
  ln -s intel-dri "$pkgdir/usr/share/licenses/intel-dri/lib32-intel-dri"
}

package_lib32-nouveau-dri() {
  depends=("lib32-libgl=${pkgver}" 'nouveau-dri')
  pkgdesc="Mesa classic DRI + Gallium3D drivers for Nouveau (32-bit)"

  cd ${srcdir}/?esa-*
  
  # fix linking because of splitted package
  make -C src/mesa/libdricore DESTDIR="${pkgdir}" install

  # classic mesa driver for nv10 , nv20 nouveau_vieux_dri.so
  make -C src/mesa/drivers/dri/nouveau DESTDIR="${pkgdir}" install
  # gallium3D driver for nv30 - nv40 - nv50 nouveau_dri.so
  make -C src/gallium/targets/dri-nouveau DESTDIR="${pkgdir}" install
  
  # fix linking because of splitted package - cleanup
  make -C src/mesa/libdricore DESTDIR="${pkgdir}" uninstall
  
  install -m755 -d "${pkgdir}/usr/share/licenses/nouveau-dri"
  ln -s nouveau-dri "$pkgdir/usr/share/licenses/nouveau-dri/lib32-nouveau-dri"
}

