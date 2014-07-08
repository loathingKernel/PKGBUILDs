# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa' 'lib32-mesa-libgl')
pkgver=10.2.3
pkgrel=1
arch=('x86_64')
makedepends=('python2' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'glproto' 'lib32-libdrm' 'dri2proto' 'dri3proto' 'presentproto'
             'lib32-libxshmfence' 'lib32-libxxf86vm' 'lib32-libxdamage' 'gcc-multilib' 'lib32-elfutils' 'lib32-llvm' 'lib32-systemd'
             'lib32-libvdpau' 'lib32-wayland')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2)
sha256sums=('e482a96170c98b17d6aba0d6e4dda4b9a2e61c39587bb64ac38cadfa4aba4aeb')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  export LLVM_CONFIG=/usr/bin/llvm-config32

  cd ${srcdir}/?esa-*

  # our automake is far too new for their build system :)
  autoreconf -vfi

  ./configure --enable-32-bit \
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
    --enable-gbm \
    --enable-gallium-gbm \
    --enable-gallium-llvm \
    --enable-shared-glapi \
    --enable-glx-tls \
    --enable-dri \
    --enable-glx \
    --enable-osmesa \
    --enable-gles1 \
    --enable-gles2 \
    --enable-texture-float \
    --enable-vdpau \
    --enable-dri3

  make

  mkdir $srcdir/fakeinstall
  make DESTDIR=${srcdir}/fakeinstall install
}

package_lib32-ati-dri() {
  pkgdesc="Mesa drivers for AMD/ATI Radeon (32-bit)"
  depends=('lib32-mesa-libgl' "lib32-mesa=${pkgver}" 'lib32-libtxc_dxtn' 'ati-dri')

  install -m755 -d ${pkgdir}/usr/lib32/vdpau/
  mv -v ${srcdir}/fakeinstall/usr/lib32/vdpau/libvdpau_{r600,radeonsi}.* ${pkgdir}/usr/lib32/vdpau/

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/{r200,r300,r600,radeon,radeonsi}_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri/

  install -m755 -d ${pkgdir}/usr/lib32/gallium-pipe
  mv -v ${srcdir}/fakeinstall/usr/lib32/gallium-pipe/pipe_{r300,r600,radeonsi}* ${pkgdir}/usr/lib32/gallium-pipe/

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s ati-dri "$pkgdir/usr/share/licenses/lib32-ati-dri"
}

package_lib32-intel-dri() {
  pkgdesc="Mesa DRI drivers for Intel (32-bit)"
  depends=('lib32-mesa-libgl' "lib32-mesa=${pkgver}" 'lib32-libtxc_dxtn' 'intel-dri')

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/{i915,i965}_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri/

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s intel-dri "$pkgdir/usr/share/licenses/lib32-intel-dri"
}

package_lib32-nouveau-dri() {
  pkgdesc="Mesa drivers for Nouveau (32-bit)"
  depends=('lib32-mesa-libgl' "lib32-mesa=${pkgver}" 'lib32-libtxc_dxtn' 'nouveau-dri')

  install -m755 -d ${pkgdir}/usr/lib32/vdpau/
  mv -v ${srcdir}/fakeinstall/usr/lib32/vdpau/libvdpau_nouveau.* ${pkgdir}/usr/lib32/vdpau/

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/nouveau_{dri,vieux_dri}.so ${pkgdir}/usr/lib32/xorg/modules/dri/

  install -m755 -d ${pkgdir}/usr/lib32/gallium-pipe
  mv -v ${srcdir}/fakeinstall/usr/lib32/gallium-pipe/pipe_nouveau* ${pkgdir}/usr/lib32/gallium-pipe/

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s nouveau-dri "$pkgdir/usr/share/licenses/lib32-nouveau-dri"
}

package_lib32-mesa() {
  pkgdesc="an open-source implementation of the OpenGL specification (32-bit)"
  depends=('lib32-libdrm' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-libxshmfence' 'lib32-systemd' 'lib32-elfutils' 'lib32-llvm-libs' 'lib32-libvdpau' 'lib32-wayland' 'mesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages')
  provides=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')
  conflicts=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')
  replaces=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')

  install -m755 -d ${pkgdir}/usr/lib32/{gallium-pipe,gbm}
  mv -v ${srcdir}/fakeinstall/usr/lib32/lib{OSMesa,gbm,glapi,wayland-egl}.so* ${pkgdir}/usr/lib32/
  mv -v ${srcdir}/fakeinstall/usr/lib32/gallium-pipe/pipe_swrast* ${pkgdir}/usr/lib32/gallium-pipe/
  mv -v ${srcdir}/fakeinstall/usr/lib32/gbm/gbm_gallium_drm* ${pkgdir}/usr/lib32/gbm/

  mv -v ${srcdir}/fakeinstall/usr/lib32/pkgconfig ${pkgdir}/usr/lib32/
  
  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/swrast_dri* ${pkgdir}/usr/lib32/xorg/modules/dri/

  install -m755 -d ${pkgdir}/usr/lib32/mesa
  # move libgl/EGL/glesv*.so to not conflict with blobs - may break .pc files ?
  mv -v ${srcdir}/fakeinstall/usr/lib32/libGL.so*    ${pkgdir}/usr/lib32/mesa/
  mv -v ${srcdir}/fakeinstall/usr/lib32/libEGL.so*   ${pkgdir}/usr/lib32/mesa/
  mv -v ${srcdir}/fakeinstall/usr/lib32/libGLES*.so* ${pkgdir}/usr/lib32/mesa/

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s mesa "$pkgdir/usr/share/licenses/lib32-mesa"
}

package_lib32-mesa-libgl() {
  pkgdesc="Mesa 3-D graphics library (32-bit)"
  depends=("lib32-mesa=${pkgver}")
  provides=("lib32-libgl=${pkgver}")
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

  install -m755 -d "${pkgdir}/usr/share/licenses"
  ln -s lib32-mesa "${pkgdir}/usr/share/licenses/lib32-mesa-libgl"
}
