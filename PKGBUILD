# Maintainer: Laurent Carlier <lordheavym@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-vulkan-intel' 'lib32-vulkan-radeon' 'lib32-mesa-vdpau' 'lib32-mesa')
pkgver=17.0.4
pkgrel=2
arch=('x86_64')
makedepends=('python2-mako' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'glproto' 'lib32-libdrm' 'dri2proto' 'dri3proto' 'presentproto'
             'lib32-libxshmfence' 'lib32-libxxf86vm' 'lib32-libxdamage' 'gcc-multilib' 'lib32-libelf' 'lib32-llvm' 'lib32-libvdpau'
             'lib32-wayland' 'lib32-libglvnd')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(https://mesa.freedesktop.org/archive/mesa-${pkgver}.tar.xz{,.sig}
	LICENSE
        remove-libpthread-stubs.patch
        remove-libpthread-stubs.patch
        0001-EGL-Implement-the-libglvnd-interface-for-EGL-v2.patch
        0001-Fix-linkage-against-shared-glapi.patch
        0001-glapi-Link-with-glapi-when-built-shared.patch
        0002-fixup-EGL-Implement-the-libglvnd-interface-for-EGL-v.patch
        glvnd-fix-gl-dot-pc.patch)
sha256sums=('1269dc8545a193932a0779b2db5bce9be4a5f6813b98c38b93b372be8362a346'
            'SKIP'
            '7fdc119cf53c8ca65396ea73f6d10af641ba41ea1dd2bd44a824726e01c8b3f2'
            '75ab53ad44b95204c788a2988e97a5cb963bdbf6072a5466949a2afb79821c8f'
            '75ab53ad44b95204c788a2988e97a5cb963bdbf6072a5466949a2afb79821c8f'
            '1d3475dc2f4f3e450cf313130d3ce965f933f396058828fa843c0df8115feeb9'
            'c68d1522f9bce4ce31c92aa7a688da49f13043f5bb2254795b76dea8f47130b7'
            '064dcd5a3ab1b7c23383e2cafbd37859e4c353f8839671d9695c6f7c2ef3260b'
            '81d0ced62f61677ea0cf5f69a491093409fa1370f2ef045c41106ca8bf9c46f6'
            '64a77944a28026b066c1682c7258d02289d257b24b6f173a9f7580c48beed966')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D') # Emil Velikov <emil.l.velikov@gmail.com>
validpgpkeys+=('946D09B5E4C9845E63075FF1D961C596A7203456') # "Andres Gomez <tanty@igalia.com>"

prepare() {
  cd ${srcdir}/mesa-${pkgver}

  # Now mesa checks for libpthread-stubs - so remove the check
  patch -Np1 -i ../remove-libpthread-stubs.patch

  # glvnd support patches - from Fedora
  # https://patchwork.freedesktop.org/series/12354/, v3 & v4
  patch -Np1 -i ../0001-EGL-Implement-the-libglvnd-interface-for-EGL-v2.patch
  patch -Np1 -i ../0002-fixup-EGL-Implement-the-libglvnd-interface-for-EGL-v.patch
  # non-upstreamed ones
  patch -Np1 -i ../glvnd-fix-gl-dot-pc.patch
  patch -Np1 -i ../0001-Fix-linkage-against-shared-glapi.patch
  patch -Np1 -i ../0001-glapi-Link-with-glapi-when-built-shared.patch

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
    --with-gallium-drivers=r300,r600,radeonsi,nouveau,swrast,virgl,svga \
    --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
    --with-egl-platforms=x11,drm,wayland \
    --with-vulkan-drivers=intel,radeon \
    --disable-xvmc \
    --enable-gallium-llvm \
    --enable-llvm-shared-libs \
    --enable-shared-glapi \
    --enable-libglvnd \
    --enable-glx-tls \
    --enable-egl \
    --enable-glx \
    --enable-gles1 \
    --enable-gles2 \
    --enable-gbm \
    --enable-dri \
    --enable-gallium-osmesa \
    --enable-texture-float \
    --enable-nine \
    --enable-vdpau 
    #--with-sha1=libgcrypt \

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

package_lib32-mesa-vdpau() {
  pkgdesc="Mesa VDPAU drivers (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-expat' 'lib32-llvm-libs' 'lib32-libelf' 'lib32-libxshmfence')

  install -m755 -d ${pkgdir}/usr/lib32
  cp -rv ${srcdir}/fakeinstall/usr/lib32/vdpau ${pkgdir}/usr/lib32
   
  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa-vdpau"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa-vdpau/"
}

package_lib32-mesa() {
  pkgdesc="an open-source implementation of the OpenGL specification (32-bit)"
  depends=('lib32-libdrm' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-libxshmfence'
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

  cp -rv ${srcdir}/fakeinstall/usr/lib32/pkgconfig ${pkgdir}/usr/lib32/

  # libglvnd support
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libGLX_mesa.so* ${pkgdir}/usr/lib32/
  cp -rv ${srcdir}/fakeinstall/usr/lib32/libEGL_mesa.so* ${pkgdir}/usr/lib32/
  # indirect rendering
  ln -s /usr/lib32/libGLX_mesa.so.0 ${pkgdir}/usr/lib32/libGLX_indirect.so.0
 
  install -m755 -d "${pkgdir}/usr/share/licenses/lib32-mesa"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/lib32-mesa/"
}
