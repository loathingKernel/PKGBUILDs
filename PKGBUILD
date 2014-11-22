# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-mesa-dri' 'lib32-mesa-vdpau' 'lib32-mesa' 'lib32-mesa-libgl')
pkgver=10.3.4
pkgrel=1
arch=('x86_64')
makedepends=('python2' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'glproto' 'lib32-libdrm' 'dri2proto' 'dri3proto' 'presentproto'
             'lib32-libxshmfence' 'lib32-libxxf86vm' 'lib32-libxdamage' 'gcc-multilib' 'lib32-elfutils' 'lib32-llvm' 'lib32-systemd'
             'lib32-libvdpau' 'lib32-wayland')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2{,.sig}
#source=(ftp://ftp.freedesktop.org/pub/mesa/10.3/MesaLib-${pkgver}.tar.bz2{,.sig}
	LICENSE)
sha256sums=('e6373913142338d10515daf619d659433bfd2989988198930c13b0945a15e98a'
            'SKIP'
            '7fdc119cf53c8ca65396ea73f6d10af641ba41ea1dd2bd44a824726e01c8b3f2')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  export LLVM_CONFIG="/usr/bin/llvm-config32"

  cd ${srcdir}/?esa-*

  # our automake is far too new for their build system :)
  autoreconf -vfi

  ./configure \
    --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu \
    --libdir=/usr/lib32 \
    --prefix=/usr \
    --sysconfdir=/etc \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --with-gallium-drivers=r300,r600,radeonsi,nouveau,swrast \
    --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
    --with-egl-platforms=x11,drm,wayland \
    --enable-llvm-shared-libs \
    --enable-egl \
    --disable-gallium-egl \
    --disable-gallium-gbm \
    --enable-gbm \
    --enable-gallium-llvm \
    --enable-shared-glapi \
    --enable-glx-tls \
    --enable-dri \
    --enable-glx \
    --enable-osmesa \
    --enable-gles1 \
    --enable-gles2 \
    --enable-texture-float \
    --enable-vdpau 

  make

  mkdir $srcdir/fakeinstall
  make DESTDIR=${srcdir}/fakeinstall install
}

package_lib32-mesa-dri() {
  pkgdesc="Mesa DRI drivers (32-bit)"
  depends=('lib32-expat' 'lib32-libdrm' 'lib32-llvm-libs' 'lib32-elfutils' 'lib32-libtxc_dxtn')
  conflicts=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri')
  provides=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri')
  replaces=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri')
  optdepends=('lib32-mesa-vdpau: for accelerated video playback')
  
  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  # ati-dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/{r200,r300,r600,radeon{,si}}_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri
  # nouveau-dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/nouveau{,_vieux}_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri
  # intel-dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/{i915,i965}_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri
  # swrast
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/{kms_,}swrast_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri

  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa-dri"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa-dri/"
}

package_lib32-mesa-vdpau() {
  pkgdesc="Mesa VDPAU drivers (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-expat' 'lib32-llvm-libs' 'lib32-elfutils')

  install -m755 -d ${pkgdir}/usr/lib32
  mv -v ${srcdir}/fakeinstall/usr/lib32/vdpau ${pkgdir}/usr/lib32
   
  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa-vdpau"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa-vdpau/"
}

package_lib32-mesa() {
  pkgdesc="an open-source implementation of the OpenGL specification (32-bit)"
  depends=('lib32-libdrm' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-libxshmfence' 'lib32-systemd'
           'lib32-elfutils' 'lib32-llvm-libs' 'lib32-wayland' 'lib32-mesa-dri' 'mesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages')
  provides=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')
  conflicts=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')
  replaces=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')

  install -m755 -d ${pkgdir}/usr/lib32
  mv -v ${srcdir}/fakeinstall/usr/lib32/lib{OSMesa,gbm,glapi,wayland-egl}.so* ${pkgdir}/usr/lib32/
  #mv -v ${srcdir}/fakeinstall/usr/lib32/gallium-pipe/pipe_swrast* ${pkgdir}/usr/lib32/gallium-pipe/
  # FS#41337
  #mv -v ${srcdir}/fakeinstall/usr/lib32/gbm/gbm_gallium_drm* ${pkgdir}/usr/lib32/gbm/

  mv -v ${srcdir}/fakeinstall/usr/lib32/pkgconfig ${pkgdir}/usr/lib32/

  install -m755 -d ${pkgdir}/usr/lib32/mesa
  # move libgl/EGL/glesv*.so to not conflict with blobs - may break .pc files ?
  mv -v ${srcdir}/fakeinstall/usr/lib32/libGL.so*    ${pkgdir}/usr/lib32/mesa/
  mv -v ${srcdir}/fakeinstall/usr/lib32/libEGL.so*   ${pkgdir}/usr/lib32/mesa/
  mv -v ${srcdir}/fakeinstall/usr/lib32/libGLES*.so* ${pkgdir}/usr/lib32/mesa/

  # keep symlinks until pacman 4.2 FS#42046
  #install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa"
  #install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa/"
  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s mesa "$pkgdir/usr/share/licenses/lib32-mesa"
}

package_lib32-mesa-libgl() {
  pkgdesc="Mesa 3-D graphics library (32-bit)"
  depends=('lib32-mesa')
  provides=('lib32-libgl')
  replaces=('lib32-libgl')

  install -m755 -d ${pkgdir}/usr/lib32

  ln -s /usr/lib32/mesa/libGL.so.1.2.0 ${pkgdir}/usr/lib32/libGL.so.1.2.0
  ln -s libGL.so.1.2.0	               ${pkgdir}/usr/lib32/libGL.so.1
  ln -s libGL.so.1.2.0                 ${pkgdir}/usr/lib32/libGL.so

  ln -s /usr/lib32/mesa/libEGL.so.1.0.0 ${pkgdir}/usr/lib32/libEGL.so.1.0.0
  ln -s libEGL.so.1.0.0	                ${pkgdir}/usr/lib32/libEGL.so.1
  ln -s libEGL.so.1.0.0                 ${pkgdir}/usr/lib32/libEGL.so

  ln -s /usr/lib32/mesa/libGLESv1_CM.so.1.1.0 ${pkgdir}/usr/lib32/libGLESv1_CM.so.1.1.0
  ln -s libGLESv1_CM.so.1.1.0	              ${pkgdir}/usr/lib32/libGLESv1_CM.so.1
  ln -s libGLESv1_CM.so.1.1.0                 ${pkgdir}/usr/lib32/libGLESv1_CM.so

  ln -s /usr/lib32/mesa/libGLESv2.so.2.0.0 ${pkgdir}/usr/lib32/libGLESv2.so.2.0.0
  ln -s libGLESv2.so.2.0.0                 ${pkgdir}/usr/lib32/libGLESv2.so.2
  ln -s libGLESv2.so.2.0.0                 ${pkgdir}/usr/lib32/libGLESv2.so

  # keep symlinks until pacman 4.2 FS#42046
  #install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa-libgl"
  #install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa-libgl/"
  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s lib32-mesa "${pkgdir}/usr/share/licenses/lib32-mesa-libgl"
}
