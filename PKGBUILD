# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-mesa-vdpau' 'lib32-mesa' 'lib32-mesa-libgl')
pkgver=12.0.1
pkgrel=5
arch=('x86_64')
makedepends=('python2-mako' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'glproto' 'lib32-libdrm' 'dri2proto' 'dri3proto' 'presentproto'
             'lib32-libxshmfence' 'lib32-libxxf86vm' 'lib32-libxdamage' 'gcc-multilib' 'lib32-elfutils' 'lib32-llvm' 'lib32-systemd'
             'lib32-libvdpau' 'lib32-wayland')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/mesa-${pkgver}.tar.xz{,.sig}
	LICENSE
        remove-libpthread-stubs.patch
        0001-st-mesa-fix-reference-counting-bug-in-st_vdpau.patch
        0002-vl-dri3-fix-a-memory-leak-from-front-buffer.patch
        0001-Mesa-dev-st_glsl_to_tgsi-overlord-fix.patch)
sha256sums=('bab24fb79f78c876073527f515ed871fc9c81d816f66c8a0b051d8d653896389'
            'SKIP'
            '7fdc119cf53c8ca65396ea73f6d10af641ba41ea1dd2bd44a824726e01c8b3f2'
            'd82c329e89754266eb1538df29b94d33692a66e3b6882b2cee78f4d5aab4a39c'
            'ccc8ea7f4e38f2dc26fd29150929e943aac5bc9b56bd3eddec882c6ccd1d64a5'
            'f6c17257e96182ce51b85ef75cef4f6c205b00dfbf8fc1089cd77c4a3eda6981'
            'c1b650d2b3512d5f8f463f1974a28ed6b88e7e1936c5cfe1034ab97696d1de14')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D') # Emil Velikov <emil.l.velikov@gmail.com>

prepare() {
  cd ${srcdir}/?esa-*

  # Now mesa checks for libpthread-stubs - so remove the check
  patch -Np1 -i ../remove-libpthread-stubs.patch

  # fix memory leaks - merged upstream
  patch -Np1 -i ../0001-st-mesa-fix-reference-counting-bug-in-st_vdpau.patch
  patch -Np1 -i ../0002-vl-dri3-fix-a-memory-leak-from-front-buffer.patch
  # fix rendering in overlord series games
  patch -Np1 -i ../0001-Mesa-dev-st_glsl_to_tgsi-overlord-fix.patch

  autoreconf -fiv
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  export LLVM_CONFIG="/usr/bin/llvm-config32"

  cd ${srcdir}/?esa-*

  ./configure \
    --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu \
    --libdir=/usr/lib32 \
    --prefix=/usr \
    --sysconfdir=/etc \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --with-gallium-drivers=r300,r600,radeonsi,nouveau,swrast,virgl \
    --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
    --with-egl-platforms=x11,drm,wayland \
    --enable-gallium-llvm \
    --enable-llvm-shared-libs \
    --enable-shared-glapi \
    --enable-glx-tls \
    --enable-egl \
    --enable-glx \
    --enable-gles1 \
    --enable-gles2 \
    --enable-gbm \
    --enable-dri \
    --enable-osmesa \
    --enable-texture-float \
    --enable-nine \
    --enable-vdpau 

  make

  mkdir $srcdir/fakeinstall
  make DESTDIR=${srcdir}/fakeinstall install
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
           'lib32-elfutils' 'lib32-llvm-libs' 'lib32-wayland' 'lib32-libtxc_dxtn' 'lib32-expat' 'mesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages'
              'lib32-mesa-vdpau: for accelerated video playback')
  provides=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri')
  conflicts=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri')
  replaces=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri')

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  # ati-dri, nouveay-dri, intel-dri, swrast
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/* ${pkgdir}/usr/lib32/xorg/modules/dri

  install -m755 -d ${pkgdir}/usr/lib32
  mv -v ${srcdir}/fakeinstall/usr/lib32/d3d ${pkgdir}/usr/lib32
  mv -v ${srcdir}/fakeinstall/usr/lib32/*.so* ${pkgdir}/usr/lib32/

  mv -v ${srcdir}/fakeinstall/usr/lib32/pkgconfig ${pkgdir}/usr/lib32/

  install -m755 -d ${pkgdir}/usr/lib32/mesa
  # move libgl/EGL/glesv*.so to not conflict with blobs - may break .pc files ?
  mv -v ${pkgdir}/usr/lib32/libGL.so*    ${pkgdir}/usr/lib32/mesa/
  mv -v ${pkgdir}/usr/lib32/libEGL.so*   ${pkgdir}/usr/lib32/mesa/
  mv -v ${pkgdir}/usr/lib32/libGLES*.so* ${pkgdir}/usr/lib32/mesa/

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s mesa "$pkgdir/usr/share/licenses/lib32-mesa"
}

package_lib32-mesa-libgl() {
  pkgdesc="Mesa 3-D graphics library (32-bit)"
  depends=('lib32-mesa')
  provides=('lib32-libgl' 'lib32-libegl' 'lib32-libgles')
  conflicts=('lib32-libgl' 'lib32-libegl' 'lib32-libgles')

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

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s lib32-mesa "${pkgdir}/usr/share/licenses/lib32-mesa-libgl"
}
