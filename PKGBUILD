# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa' 'lib32-mesa-libgl')
pkgver=9.2.2
pkgrel=1
arch=('x86_64')
makedepends=('python2' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'glproto' 'lib32-libdrm' 'dri2proto' 'lib32-libxxf86vm' 'lib32-libxdamage'
             'gcc-multilib' 'lib32-elfutils' 'lib32-llvm' 'lib32-systemd')
url="http://mesa3d.sourceforge.net"
license=('custom')
options=('!libtool')
source=(ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/MesaLib-${pkgver}.tar.bz2)
md5sums=('20887f8020db7d1736a01ae9cd5d8c38')

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
    --with-llvm-shared-libs \
    --enable-gallium-llvm \
    --enable-egl \
    --enable-gallium-egl \
    --with-egl-platforms=x11,drm \
    --enable-shared-glapi \
    --enable-gbm \
    --enable-glx-tls \
    --enable-dri \
    --enable-glx \
    --enable-osmesa \
    --enable-gles1 \
    --enable-gles2 \
    --enable-texture-float
  make
    
  mkdir $srcdir/fakeinstall
  make DESTDIR=${srcdir}/fakeinstall install
}

package_lib32-ati-dri() {
  pkgdesc="Mesa drivers for AMD/ATI Radeon (32-bit)"
  depends=("lib32-mesa-libgl=${pkgver}" 'lib32-libtxc_dxtn' 'ati-dri')

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/{r200,r300,r600,radeon,radeonsi}_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri/

  install -m755 -d ${pkgdir}/usr/lib32/gallium-pipe
  mv -v ${srcdir}/fakeinstall/usr/lib32/gallium-pipe/pipe_{r300,r600,radeonsi}* ${pkgdir}/usr/lib32/gallium-pipe/
  
  install -m755 -d "${pkgdir}/usr/share/licenses/ati-dri"
  ln -s ati-dri "$pkgdir/usr/share/licenses/ati-dri/lib32-ati-dri"
}

package_lib32-intel-dri() {
  pkgdesc="Mesa DRI drivers for Intel (32-bit)"
  depends=("lib32-mesa-libgl=${pkgver}" 'lib32-libtxc_dxtn' 'intel-dri')

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/{i915,i965}_dri.so ${pkgdir}/usr/lib32/xorg/modules/dri/

  install -m755 -d "${pkgdir}/usr/share/licenses/intel-dri"
  ln -s intel-dri "$pkgdir/usr/share/licenses/intel-dri/lib32-intel-dri"
}

package_lib32-nouveau-dri() {
  pkgdesc="Mesa drivers for Nouveau (32-bit)"
  depends=("lib32-mesa-libgl=${pkgver}" 'lib32-libtxc_dxtn' 'nouveau-dri')

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  mv -v ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/nouveau_{dri,vieux_dri}.so ${pkgdir}/usr/lib32/xorg/modules/dri/

  install -m755 -d ${pkgdir}/usr/lib32/gallium-pipe
  mv -v ${srcdir}/fakeinstall/usr/lib32/gallium-pipe/pipe_nouveau* ${pkgdir}/usr/lib32/gallium-pipe/

  install -m755 -d "${pkgdir}/usr/share/licenses/nouveau-dri"
  ln -s nouveau-dri "$pkgdir/usr/share/licenses/nouveau-dri/lib32-nouveau-dri"
}

package_lib32-mesa() {
  pkgdesc="an open-source implementation of the OpenGL specification (32-bit)"
  depends=('lib32-libdrm' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-systemd' 'lib32-elfutils' 'lib32-llvm-libs' 'mesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages')
  provides=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')
  conflicts=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')
  replaces=('lib32-libglapi' 'lib32-osmesa' 'lib32-libgbm' 'lib32-libgles' 'lib32-libegl')

  mv -v ${srcdir}/fakeinstall/* ${pkgdir}
  mv ${pkgdir}/usr/lib32/libGL.so.1.2.0 ${pkgdir}/usr/lib32/mesa-libGL.so.1.2.0
  rm ${pkgdir}/usr/lib32/libGL.so{,.1}
  rm -r ${pkgdir}/etc
  rm -r ${pkgdir}/usr/include
  
  install -m755 -d "${pkgdir}/usr/share/licenses/mesa"
  ln -s mesa "$pkgdir/usr/share/licenses/mesa/lib32-mesa"
}

package_lib32-mesa-libgl() {
  pkgdesc="Mesa 3-D graphics library (32-bit)"
  depends=("lib32-mesa=${pkgver}")
  provides=("lib32-libgl=${pkgver}")
  replaces=('lib32-libgl')

  install -m755 -d ${pkgdir}/usr/lib32

  ln -s mesa-libGL.so.1.2.0 ${pkgdir}/usr/lib32/libGL.so
  ln -s mesa-libGL.so.1.2.0 ${pkgdir}/usr/lib32/libGL.so.1
  ln -s mesa-libGL.so.1.2.0 ${pkgdir}/usr/lib32/libGL.so.1.2.0

  install -m755 -d "${pkgdir}/usr/share/licenses/libglapi"
  ln -s libglapi "${pkgdir}/usr/share/licenses/libglapi/lib32-libglapi"
}
