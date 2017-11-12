# Maintainer: Laurent Carlier <lordheavym@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-vulkan-intel' 'lib32-vulkan-radeon' 'lib32-libva-mesa-driver' 'lib32-mesa-vdpau' 'lib32-mesa')
pkgver=17.2.5
pkgrel=1
arch=('x86_64')
makedepends=('python2-mako' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'glproto' 'lib32-libdrm' 'dri2proto' 'dri3proto' 'presentproto'
             'lib32-libxshmfence' 'lib32-libxxf86vm' 'lib32-libxdamage' 'gcc-multilib' 'lib32-libelf' 'lib32-llvm' 'lib32-libvdpau'
             'lib32-libva' 'lib32-wayland' 'wayland-protocols' 'lib32-libglvnd' 'lib32-lm_sensors')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(https://mesa.freedesktop.org/archive/mesa-${pkgver}.tar.xz{,.sig}
	LICENSE
        0002-glvnd-fix-gl-dot-pc.patch)
sha256sums=('7f7f914b7b9ea0b15f2d9d01a4375e311b0e90e55683b8e8a67ce8691eb1070f'
            'SKIP'
            '7fdc119cf53c8ca65396ea73f6d10af641ba41ea1dd2bd44a824726e01c8b3f2'
            '64a77944a28026b066c1682c7258d02289d257b24b6f173a9f7580c48beed966')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D') # Emil Velikov <emil.l.velikov@gmail.com>
validpgpkeys+=('946D09B5E4C9845E63075FF1D961C596A7203456') # "Andres Gomez <tanty@igalia.com>"
validpgpkeys+=('E3E8F480C52ADD73B278EE78E1ECBE07D7D70895') # Juan Antonio Suárez Romero (Igalia, S.L.) <jasuarez@igalia.com>"

prepare() {
  cd ${srcdir}/mesa-${pkgver}

  # glvnd support patches - from Fedora
  # non-upstreamed ones
  patch -Np1 -i ../0002-glvnd-fix-gl-dot-pc.patch

  autoreconf -fiv
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  export LLVM_CONFIG="/usr/bin/llvm-config32"
  
  cd ${srcdir}/mesa-${pkgver}

  ./configure \
    --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu \
    --libdir=/usr/lib32 \
    --prefix=/usr \
    --sysconfdir=/etc \
    --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
    --with-gallium-drivers=r300,r600,radeonsi,nouveau,svga,swrast,virgl,swr \
    --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
    --with-platforms=x11,drm,wayland \
    --with-vulkan-drivers=intel,radeon \
    --disable-xvmc \
    --disable-libunwind \
    --enable-libglvnd \
    --enable-llvm \
    --enable-llvm-shared-libs \
    --enable-shared-glapi \
    --enable-lmsensors \
    --enable-glx-tls \
    --enable-egl \
    --enable-glx \
    --enable-gles1 \
    --enable-gles2 \
    --enable-gbm \
    --enable-dri \
    --enable-gallium-osmesa \
    --enable-gallium-extra-hud \
    --enable-texture-float \
    --enable-nine \
    --enable-vdpau

  make

  mkdir $srcdir/fakeinstall
  make DESTDIR=${srcdir}/fakeinstall install
}

package_lib32-vulkan-intel() {
  pkgdesc="Intel's Vulkan mesa driver (32-bit)"
  depends=('lib32-wayland' 'lib32-libx11' 'lib32-gcc-libs' 'lib32-libxshmfence')
  provides=('lib32-vulkan-driver')

  install -m755 -d ${pkgdir}/usr/share/vulkan/icd.d
  cp -rv ${srcdir}/fakeinstall/usr/share/vulkan/icd.d/intel_icd*.json ${pkgdir}/usr/share/vulkan/icd.d/

  install -m755 -d ${pkgdir}/usr/lib32
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libvulkan_intel.so ${pkgdir}/usr/lib32/

  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-vulkan-intel"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-vulkan-intel/"
}

package_lib32-vulkan-radeon() {
  pkgdesc="Radeon's Vulkan mesa driver (32-bit)"
  depends=('lib32-wayland' 'lib32-libx11' 'lib32-llvm-libs' 'lib32-libdrm' 'lib32-libelf' 'lib32-libxshmfence')
  provides=('lib32-vulkan-driver')

  install -m755 -d ${pkgdir}/usr/share/vulkan/icd.d
  cp -rv ${srcdir}/fakeinstall/usr/share/vulkan/icd.d/radeon_icd*.json ${pkgdir}/usr/share/vulkan/icd.d/
  
  install -m755 -d ${pkgdir}/usr/lib32
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libvulkan_radeon.so ${pkgdir}/usr/lib32/

  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-vulkan-radeon"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-vulkan-radeon/"
}

package_lib32-libva-mesa-driver() {
  pkgdesc="VA-API implementation for gallium (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-expat' 'lib32-llvm-libs' 'lib32-libelf' 'lib32-lm_sensors'
           'lib32-libxshmfence')

  install -m755 -d ${pkgdir}/usr/lib32/dri
  cp -av ${srcdir}/fakeinstall/usr/lib32/dri/* ${pkgdir}/usr/lib32/dri
   
  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-libva-mesa-driver"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-libva-mesa-driver/"
}

package_lib32-mesa-vdpau() {
  pkgdesc="Mesa VDPAU drivers (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-expat' 'lib32-llvm-libs' 'lib32-libelf' 'lib32-lm_sensors'
           'lib32-libxshmfence')

  install -m755 -d ${pkgdir}/usr/lib32/vdpau
  cp -av ${srcdir}/fakeinstall/usr/lib32/vdpau/* ${pkgdir}/usr/lib32/vdpau
   
  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa-vdpau"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa-vdpau/"
}

package_lib32-mesa() {
  pkgdesc="an open-source implementation of the OpenGL specification (32-bit)"
  depends=('lib32-libdrm' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-libxshmfence' 'lib32-lm_sensors'
           'lib32-libelf' 'lib32-llvm-libs' 'lib32-wayland' 'lib32-libtxc_dxtn' 'lib32-libglvnd' 'mesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages'
              'lib32-mesa-vdpau: for accelerated video playback')
  provides=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri' 'lib32-mesa-libgl' 'lib32-opengl-driver')
  conflicts=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri' 'lib32-mesa-libgl')
  replaces=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri' 'lib32-mesa-libgl')

  install -m755 -d ${pkgdir}/usr/lib32/xorg/modules/dri
  # ati-dri, nouveay-dri, intel-dri, swrast
  cp -av ${srcdir}/fakeinstall/usr/lib32/xorg/modules/dri/* ${pkgdir}/usr/lib32/xorg/modules/dri

  install -m755 -d ${pkgdir}/usr/lib32
  cp -rv ${srcdir}/fakeinstall/usr/lib32/d3d  ${pkgdir}/usr/lib32
  cp -rv ${srcdir}/fakeinstall/usr/lib32/lib{gbm,glapi}.so* ${pkgdir}/usr/lib32/
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libOSMesa.so* ${pkgdir}/usr/lib32/
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libwayland*.so* ${pkgdir}/usr/lib32/
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libswrAVX*.so* ${pkgdir}/usr/lib32/

  cp -rv ${srcdir}/fakeinstall/usr/lib32/pkgconfig ${pkgdir}/usr/lib32/

  # libglvnd support
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libGLX_mesa.so* ${pkgdir}/usr/lib32/
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libEGL_mesa.so* ${pkgdir}/usr/lib32/
  # indirect rendering
  ln -s /usr/lib32/libGLX_mesa.so.0 ${pkgdir}/usr/lib32/libGLX_indirect.so.0
 
  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa/"
}
