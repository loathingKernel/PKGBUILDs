# Maintainer: Jan de Groot <jgc@archlinux.org>
# Maintainer: Andreas Radke <andyrtr@archlinux.org>

pkgbase=mesa
pkgname=('opencl-mesa' 'vulkan-intel' 'libva-mesa-driver' 'mesa-vdpau' 'mesa' 'mesa-libgl')
pkgver=12.0.3
pkgrel=3
arch=('i686' 'x86_64')
makedepends=('python2-mako' 'libxml2' 'libx11' 'glproto' 'libdrm' 'dri2proto' 'dri3proto' 'presentproto' 
             'libxshmfence' 'libxxf86vm' 'libxdamage' 'libvdpau' 'libva' 'wayland' 'elfutils' 'llvm'
             'systemd' 'libomxil-bellagio' 'libgcrypt' 'libclc' 'clang')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(ftp://ftp.freedesktop.org/pub/mesa/${pkgver}/mesa-${pkgver}.tar.xz{,.sig}
        LICENSE
        remove-libpthread-stubs.patch
        0001-loader-dri3-add-get_dri_screen-to-the-vtable.patch
        0002-loader-dri3-import-prime-buffers-in-the-currently-bo.patch)
sha256sums=('1dc86dd9b51272eee1fad3df65e18cda2e556ef1bc0b6e07cd750b9757f493b1'
            'SKIP'
            '7fdc119cf53c8ca65396ea73f6d10af641ba41ea1dd2bd44a824726e01c8b3f2'
            'd82c329e89754266eb1538df29b94d33692a66e3b6882b2cee78f4d5aab4a39c'
            '52eb98eb6c9c644383d9743692aea302d84c4f89cfaa7a276b9276befc2d9780'
            '96ad07e241d16802b14b14ca3d6965fa7f4f4b8c678d62ba375291910dce3b4a')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D') # Emil Velikov <emil.l.velikov@gmail.com>

prepare() {
  cd ${srcdir}/?esa-*

  # Now mesa checks for libpthread-stubs - so remove the check
  patch -Np1 -i ../remove-libpthread-stubs.patch
  
  # fix FS#50240 - https://bugs.freedesktop.org/show_bug.cgi?id=71759
  # merged upstream
  patch -Np1 -i ../0001-loader-dri3-add-get_dri_screen-to-the-vtable.patch
  patch -Np1 -i ../0002-loader-dri3-import-prime-buffers-in-the-currently-bo.patch

  autoreconf -fiv
}

build() {
  cd ${srcdir}/?esa-*

  ./configure --prefix=/usr \
    --sysconfdir=/etc \
    --with-dri-driverdir=/usr/lib/xorg/modules/dri \
    --with-gallium-drivers=r300,r600,radeonsi,nouveau,svga,swrast,virgl \
    --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
    --with-egl-platforms=x11,drm,wayland \
    --with-vulkan-drivers=intel \
    --with-sha1=libgcrypt \
    --disable-xvmc \
    --enable-gallium-llvm \
    --enable-llvm-shared-libs \
    --enable-shared-glapi \
    --enable-egl \
    --enable-glx \
    --enable-glx-tls \
    --enable-gles1 \
    --enable-gles2 \
    --enable-gbm \
    --enable-dri \
    --enable-osmesa \
    --enable-texture-float \
    --enable-xa \
    --enable-vdpau \
    --enable-omx \
    --enable-nine \
    --enable-opencl --enable-opencl-icd \
    --with-clang-libdir=/usr/lib

  make

  # fake installation
  mkdir $srcdir/fakeinstall
  make DESTDIR=${srcdir}/fakeinstall install
}

package_opencl-mesa() {
  pkgdesc="OpenCL support for AMD/ATI Radeon mesa drivers"
  depends=('expat' 'libdrm' 'elfutils' 'libxfixes' 'libxext' 'opencl-icd-loader' 'libclc' 'clang')
  optdepends=('opencl-headers: headers necessary for OpenCL development')
  
  install -m755 -d ${pkgdir}/etc
  cp -rv ${srcdir}/fakeinstall/etc/OpenCL ${pkgdir}/etc/
  
  install -m755 -d ${pkgdir}/usr/lib/gallium-pipe
  cp -rv ${srcdir}/fakeinstall/usr/lib/lib*OpenCL* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/gallium-pipe/pipe_{r600,radeonsi}.so ${pkgdir}/usr/lib/gallium-pipe/

  install -m755 -d "${pkgdir}/usr/share/licenses/opencl-mesa"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/opencl-mesa/"
}

package_vulkan-intel() {
  pkgdesc="Intel's Vulkan mesa driver"
  depends=('vulkan-icd-loader' 'libgcrypt' 'wayland' 'libxcb')
  
  install -m755 -d ${pkgdir}/usr/share
  mv -v ${srcdir}/fakeinstall/usr/share/vulkan ${pkgdir}/usr/share/

  install -m755 -d ${pkgdir}/usr/{include/vulkan,lib}
  mv -v ${srcdir}/fakeinstall/usr/lib/libvulkan_intel.so ${pkgdir}/usr/lib/
  mv -v ${srcdir}/fakeinstall/usr/include/vulkan/vulkan_intel.h ${pkgdir}/usr/include/vulkan

  install -m755 -d "${pkgdir}/usr/share/licenses/vulkan-intel"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/vulkan-intel/"
}

package_libva-mesa-driver() {
  pkgdesc="VA-API implementation for gallium"
  depends=('libdrm' 'libx11' 'llvm-libs' 'expat' 'elfutils')

  install -m755 -d ${pkgdir}/usr/lib
  cp -rv ${srcdir}/fakeinstall/usr/lib/dri ${pkgdir}/usr/lib
   
  install -m755 -d "${pkgdir}/usr/share/licenses/libva-mesa-driver"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/libva-mesa-driver/"
}

package_mesa-vdpau() {
  pkgdesc="Mesa VDPAU drivers"
  depends=('libdrm' 'libx11' 'llvm-libs' 'expat' 'elfutils')

  install -m755 -d ${pkgdir}/usr/lib
  cp -rv ${srcdir}/fakeinstall/usr/lib/vdpau ${pkgdir}/usr/lib
   
  install -m755 -d "${pkgdir}/usr/share/licenses/mesa-vdpau"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/mesa-vdpau/"
}

package_mesa() {
  pkgdesc="an open-source implementation of the OpenGL specification"
  depends=('libdrm' 'wayland' 'libxxf86vm' 'libxdamage' 'libxshmfence' 'systemd' 'elfutils' 
           'libomxil-bellagio' 'expat' 'libgcrypt' 'libtxc_dxtn' 'llvm-libs')
  optdepends=('opengl-man-pages: for the OpenGL API man pages'
              'mesa-vdpau: for accelerated video playback'
              'libva-mesa-driver: for accelerated video playback')
  provides=('ati-dri' 'intel-dri' 'nouveau-dri' 'svga-dri' 'mesa-dri')
  conflicts=('ati-dri' 'intel-dri' 'nouveau-dri' 'svga-dri' 'mesa-dri')
  replaces=('ati-dri' 'intel-dri' 'nouveau-dri' 'svga-dri' 'mesa-dri')

  install -m755 -d ${pkgdir}/etc
  cp -rv ${srcdir}/fakeinstall/etc/drirc ${pkgdir}/etc
  
  install -m755 -d ${pkgdir}/usr/lib/xorg/modules/dri
  # ati-dri, nouveau-dri, intel-dri, svga-dri, swrast
  cp -av ${srcdir}/fakeinstall/usr/lib/xorg/modules/dri/* ${pkgdir}/usr/lib/xorg/modules/dri
   
  cp -rv ${srcdir}/fakeinstall/usr/lib/bellagio  ${pkgdir}/usr/lib
  cp -rv ${srcdir}/fakeinstall/usr/lib/d3d  ${pkgdir}/usr/lib
  cp -rv ${srcdir}/fakeinstall/usr/lib/lib{gbm,glapi}.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libOSMesa.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libwayland*.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libxatracker.so* ${pkgdir}/usr/lib/

  cp -rv ${srcdir}/fakeinstall/usr/include ${pkgdir}/usr
  cp -rv ${srcdir}/fakeinstall/usr/lib/pkgconfig ${pkgdir}/usr/lib/
  
  # remove vulkan headers
  rm -rf ${pkgdir}/usr/include/vulkan

  install -m755 -d ${pkgdir}/usr/lib/mesa
  # move libgl/EGL/glesv*.so to not conflict with blobs - may break .pc files ?
  cp -rv ${srcdir}/fakeinstall/usr/lib/libGL.so* 	${pkgdir}/usr/lib/mesa/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libEGL.so* 	${pkgdir}/usr/lib/mesa/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libGLES*.so*	${pkgdir}/usr/lib/mesa/

  install -m755 -d "${pkgdir}/usr/share/licenses/mesa"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/mesa/"
}

package_mesa-libgl() {
  pkgdesc="Mesa 3-D graphics library"
  depends=('mesa')
  provides=('libgl' 'libgles' 'libegl')
  conflicts=('libgl' 'libgles' 'libegl')
 
  # See FS#26284
  install -m755 -d "${pkgdir}/usr/lib/xorg/modules/extensions"
  ln -s libglx.xorg "${pkgdir}/usr/lib/xorg/modules/extensions/libglx.so"

  ln -s /usr/lib/mesa/libGL.so.1.2.0 ${pkgdir}/usr/lib/libGL.so.1.2.0
  ln -s libGL.so.1.2.0	             ${pkgdir}/usr/lib/libGL.so.1
  ln -s libGL.so.1.2.0               ${pkgdir}/usr/lib/libGL.so

  ln -s /usr/lib/mesa/libEGL.so.1.0.0 ${pkgdir}/usr/lib/libEGL.so.1.0.0
  ln -s libEGL.so.1.0.0	              ${pkgdir}/usr/lib/libEGL.so.1
  ln -s libEGL.so.1.0.0               ${pkgdir}/usr/lib/libEGL.so

  ln -s /usr/lib/mesa/libGLESv1_CM.so.1.1.0 ${pkgdir}/usr/lib/libGLESv1_CM.so.1.1.0
  ln -s libGLESv1_CM.so.1.1.0	            ${pkgdir}/usr/lib/libGLESv1_CM.so.1
  ln -s libGLESv1_CM.so.1.1.0               ${pkgdir}/usr/lib/libGLESv1_CM.so

  ln -s /usr/lib/mesa/libGLESv2.so.2.0.0 ${pkgdir}/usr/lib/libGLESv2.so.2.0.0
  ln -s libGLESv2.so.2.0.0               ${pkgdir}/usr/lib/libGLESv2.so.2
  ln -s libGLESv2.so.2.0.0               ${pkgdir}/usr/lib/libGLESv2.so

  install -m755 -d "${pkgdir}/usr/share/licenses/mesa-libgl"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/mesa-libgl/"
}
