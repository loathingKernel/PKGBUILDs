# Maintainer: Jan de Groot <jgc@archlinux.org>
# Maintainer: Andreas Radke <andyrtr@archlinux.org>

pkgbase=mesa
pkgname=('opencl-mesa' 'vulkan-intel' 'vulkan-radeon' 'libva-mesa-driver' 'mesa-vdpau' 'mesa')
pkgver=17.3.5
pkgrel=1
arch=('x86_64')
makedepends=('python2-mako' 'libxml2' 'libx11' 'glproto' 'libdrm' 'dri2proto' 'dri3proto' 'presentproto' 
             'libxshmfence' 'libxxf86vm' 'libxdamage' 'libvdpau' 'libva' 'wayland' 'wayland-protocols'
             'elfutils' 'llvm' 'libomxil-bellagio' 'libclc' 'clang' 'libglvnd' 'libunwind' 'lm_sensors')
url="https://www.mesa3d.org/"
license=('custom')
source=(https://mesa.freedesktop.org/archive/mesa-${pkgver}.tar.xz{,.sig}
        LICENSE
        0001-glvnd-fix-gl-dot-pc.patch)
sha512sums=('39ada2480aa12c42bbff6a1b5c957f99934193d19eb5f44e102ef8302d26f777cee63af1140aa8623bbc1ebd6d69e172cecca798780b8eb594f2ebbb217afd29'
            'SKIP'
            '25da77914dded10c1f432ebcbf29941124138824ceecaf1367b3deedafaecabc082d463abcfa3d15abff59f177491472b505bcb5ba0c4a51bb6b93b4721a23c2'
            '75849eca72ca9d01c648d5ea4f6371f1b8737ca35b14be179e14c73cc51dca0739c333343cdc228a6d464135f4791bcdc21734e2debecd29d57023c8c088b028')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D') # Emil Velikov <emil.l.velikov@gmail.com>
validpgpkeys+=('946D09B5E4C9845E63075FF1D961C596A7203456') # Andres Gomez <tanty@igalia.com>
validpgpkeys+=('E3E8F480C52ADD73B278EE78E1ECBE07D7D70895') # Juan Antonio Suárez Romero (Igalia, S.L.) <jasuarez@igalia.com>"
 
prepare() {
  cd ${srcdir}/mesa-${pkgver}

  # glvnd support patches - from Fedora
  # non-upstreamed ones
  patch -Np1 -i ../0001-glvnd-fix-gl-dot-pc.patch
  
  autoreconf -fiv
}

build() {
  cd ${srcdir}/mesa-${pkgver}

  ./configure --prefix=/usr \
    --sysconfdir=/etc \
    --with-gallium-drivers=r300,r600,radeonsi,nouveau,svga,swrast,virgl,swr \
    --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
    --with-platforms=x11,drm,wayland \
    --with-vulkan-drivers=intel,radeon \
    --disable-xvmc \
    --enable-llvm \
    --enable-llvm-shared-libs \
    --enable-shared-glapi \
    --enable-libglvnd \
    --enable-libunwind \
    --enable-lmsensors \
    --enable-egl \
    --enable-glx \
    --enable-glx-tls \
    --enable-gles1 \
    --enable-gles2 \
    --enable-gbm \
    --enable-dri \
    --enable-gallium-osmesa \
    --enable-gallium-extra-hud \
    --enable-texture-float \
    --enable-xa \
    --enable-vdpau \
    --enable-omx-bellagio \
    --enable-nine \
    --enable-opencl \
    --enable-opencl-icd \
    --with-clang-libdir=/usr/lib

  make

  # fake installation
  mkdir $srcdir/fakeinstall
  make DESTDIR=${srcdir}/fakeinstall install
}

package_opencl-mesa() {
  pkgdesc="OpenCL support for AMD/ATI Radeon mesa drivers"
  depends=('expat' 'libdrm' 'libelf' 'lm_sensors' 'libunwind' 'libclc' 'clang')
  optdepends=('opencl-headers: headers necessary for OpenCL development')
  provides=('opencl-driver')

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
  depends=('wayland' 'libx11' 'libxshmfence')
  provides=('vulkan-driver')

  install -m755 -d ${pkgdir}/usr/share/vulkan/icd.d
  mv -v ${srcdir}/fakeinstall/usr/share/vulkan/icd.d/intel_icd*.json ${pkgdir}/usr/share/vulkan/icd.d/

  install -m755 -d ${pkgdir}/usr/{include/vulkan,lib}
  mv -v ${srcdir}/fakeinstall/usr/lib/libvulkan_intel.so ${pkgdir}/usr/lib/
  mv -v ${srcdir}/fakeinstall/usr/include/vulkan/vulkan_intel.h ${pkgdir}/usr/include/vulkan

  install -m755 -d "${pkgdir}/usr/share/licenses/vulkan-intel"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/vulkan-intel/"
}

package_vulkan-radeon() {
  pkgdesc="Radeon's Vulkan mesa driver"
  depends=('wayland' 'libx11' 'libxshmfence' 'libelf' 'libdrm' 'llvm-libs')
  provides=('vulkan-driver')
 
  install -m755 -d ${pkgdir}/usr/share/vulkan/icd.d
  mv -v ${srcdir}/fakeinstall/usr/share/vulkan/icd.d/radeon_icd*.json ${pkgdir}/usr/share/vulkan/icd.d/

  install -m755 -d ${pkgdir}/usr/lib
  mv -v ${srcdir}/fakeinstall/usr/lib/libvulkan_radeon.so ${pkgdir}/usr/lib/

  install -m755 -d "${pkgdir}/usr/share/licenses/vulkan-radeon"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/vulkan-radeon/"
}

package_libva-mesa-driver() {
  pkgdesc="VA-API implementation for gallium"
  depends=('libdrm' 'libx11' 'llvm-libs' 'expat' 'libelf' 'libxshmfence' 'lm_sensors' 'libunwind')

  install -m755 -d ${pkgdir}/usr/lib/dri
  cp -av ${srcdir}/fakeinstall/usr/lib/dri/*_drv_video.so ${pkgdir}/usr/lib/dri
   
  install -m755 -d "${pkgdir}/usr/share/licenses/libva-mesa-driver"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/libva-mesa-driver/"
}

package_mesa-vdpau() {
  pkgdesc="Mesa VDPAU drivers"
  depends=('libdrm' 'libx11' 'llvm-libs' 'expat' 'libelf' 'libxshmfence' 'lm_sensors' 'libunwind')

  install -m755 -d ${pkgdir}/usr/lib/vdpau
  cp -av ${srcdir}/fakeinstall/usr/lib/vdpau/* ${pkgdir}/usr/lib/vdpau
   
  install -m755 -d "${pkgdir}/usr/share/licenses/mesa-vdpau"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/mesa-vdpau/"
}

package_mesa() {
  pkgdesc="an open-source implementation of the OpenGL specification"
  depends=('libdrm' 'wayland' 'libxxf86vm' 'libxdamage' 'libxshmfence' 'libelf' 
           'libomxil-bellagio' 'libunwind' 'llvm-libs' 'lm_sensors' 'libglvnd')
  optdepends=('opengl-man-pages: for the OpenGL API man pages'
              'mesa-vdpau: for accelerated video playback'
              'libva-mesa-driver: for accelerated video playback')
  provides=('ati-dri' 'intel-dri' 'nouveau-dri' 'svga-dri' 'mesa-dri' 'mesa-libgl' 'opengl-driver')
  conflicts=('ati-dri' 'intel-dri' 'nouveau-dri' 'svga-dri' 'mesa-dri' 'mesa-libgl')
  replaces=('ati-dri' 'intel-dri' 'nouveau-dri' 'svga-dri' 'mesa-dri' 'mesa-libgl')
  backup=('etc/drirc')

  install -m755 -d ${pkgdir}/etc
  cp -rv ${srcdir}/fakeinstall/etc/drirc ${pkgdir}/etc
  
  install -m755 -d ${pkgdir}/usr/share/glvnd/egl_vendor.d
  cp -rv ${srcdir}/fakeinstall/usr/share/glvnd/egl_vendor.d/50_mesa.json ${pkgdir}/usr/share/glvnd/egl_vendor.d/

  install -m755 -d ${pkgdir}/usr/lib/dri
  # ati-dri, nouveau-dri, intel-dri, svga-dri, swrast
  cp -av ${srcdir}/fakeinstall/usr/lib/dri/*_dri.so ${pkgdir}/usr/lib/dri
   
  cp -rv ${srcdir}/fakeinstall/usr/lib/bellagio  ${pkgdir}/usr/lib
  cp -rv ${srcdir}/fakeinstall/usr/lib/d3d  ${pkgdir}/usr/lib
  cp -rv ${srcdir}/fakeinstall/usr/lib/lib{gbm,glapi}.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libOSMesa.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libwayland*.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libxatracker.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libswrAVX*.so* ${pkgdir}/usr/lib/

  cp -rv ${srcdir}/fakeinstall/usr/include ${pkgdir}/usr
  cp -rv ${srcdir}/fakeinstall/usr/lib/pkgconfig ${pkgdir}/usr/lib/
  
  # remove vulkan headers
  rm -rf ${pkgdir}/usr/include/vulkan

  # libglvnd support
  cp -rv ${srcdir}/fakeinstall/usr/lib/libGLX_mesa.so* ${pkgdir}/usr/lib/
  cp -rv ${srcdir}/fakeinstall/usr/lib/libEGL_mesa.so* ${pkgdir}/usr/lib/
  # indirect rendering
  ln -s /usr/lib/libGLX_mesa.so.0 ${pkgdir}/usr/lib/libGLX_indirect.so.0

  install -m755 -d "${pkgdir}/usr/share/licenses/mesa"
  install -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/mesa/"
}
