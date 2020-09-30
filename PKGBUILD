# Maintainer: Laurent Carlier <lordheavym@gmail.com>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-vulkan-mesa-layers' 'lib32-opencl-mesa' 'lib32-vulkan-intel' 'lib32-vulkan-radeon' 'lib32-libva-mesa-driver' 'lib32-mesa-vdpau' 'lib32-mesa')
pkgdesc="An open-source implementation of the OpenGL specification (32-bit)"
pkgver=20.2.0
pkgrel=2
arch=('x86_64')
makedepends=('python-mako' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'xorgproto' 'lib32-libdrm'
             'lib32-libxshmfence' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-libvdpau'
             'lib32-libva' 'lib32-wayland' 'wayland-protocols' 'lib32-zstd' 'lib32-libelf'
             'lib32-llvm' 'libclc' 'clang' 'lib32-clang' 'lib32-libglvnd' 'lib32-libunwind'
             'lib32-lm_sensors' 'lib32-libxrandr' 'glslang' 'meson')
url="https://www.mesa3d.org/"
license=('custom')
source=(https://mesa.freedesktop.org/archive/mesa-${pkgver}.tar.xz{,.sig}
        LICENSE)
sha512sums=('3dd7def04ba4f196be8fd59999285febb10366e89d6e649c518b436b732c62d3f1bd235fc470de7fda4b4cc09a1baaadca4222dcdc2449225d789b151cea69d7'
            'SKIP'
            'f9f0d0ccf166fe6cb684478b6f1e1ab1f2850431c06aa041738563eb1808a004e52cdec823c103c9e180f03ffc083e95974d291353f0220fe52ae6d4897fecc7')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D'  # Emil Velikov <emil.l.velikov@gmail.com>
              '946D09B5E4C9845E63075FF1D961C596A7203456'  # Andres Gomez <tanty@igalia.com>
              'E3E8F480C52ADD73B278EE78E1ECBE07D7D70895'  # Juan Antonio Suárez Romero (Igalia, S.L.) <jasuarez@igalia.com>
              'A5CC9FEC93F2F837CB044912336909B6B25FADFA'  # Juan A. Suarez Romero <jasuarez@igalia.com>
              '71C4B75620BC75708B4BDB254C95FAAB3EB073EC'  # Dylan Baker <dylan@pnwbakers.com>
              '57551DE15B968F6341C248F68D8E31AFC32428A6') # Eric Engestrom <eric@engestrom.ch>

prepare() {
  cd mesa-$pkgver
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG="i686-pc-linux-gnu-pkg-config"
  cat >crossfile.ini <<END
[binaries]
llvm-config = '/usr/bin/llvm-config32'
END

  # swr driver is broken with some cpu see FS#66972

  arch-meson mesa-$pkgver build \
    --native-file crossfile.ini \
    --libdir=/usr/lib32 \
    -D b_lto=true \
    -D b_ndebug=true \
    -D platforms=x11,wayland \
    -D dri-drivers=i915,i965,r100,r200,nouveau \
    -D gallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,iris \
    -D vulkan-drivers=amd,intel \
    -D vulkan-overlay-layer=true \
    -D vulkan-device-select-layer=true \
    -D swr-arches=avx,avx2 \
    -D dri3=enabled \
    -D egl=enabled \
    -D gallium-extra-hud=true \
    -D gallium-nine=true \
    -D gallium-omx=disabled \
    -D gallium-opencl=icd \
    -D gallium-va=enabled \
    -D gallium-vdpau=enabled \
    -D gallium-xa=enabled \
    -D gallium-xvmc=disabled \
    -D gbm=enabled \
    -D gles1=disabled \
    -D gles2=enabled \
    -D glvnd=true \
    -D glx=dri \
    -D libunwind=enabled \
    -D llvm=enabled \
    -D lmsensors=enabled \
    -D osmesa=gallium \
    -D shared-glapi=enabled \
    -D valgrind=disabled

  # Print config
  meson configure build

  ninja -C build
  meson compile -C build

  # fake installation to be seperated into packages
  # outside of fakeroot but mesa doesn't need to chown/mod
  DESTDIR="${srcdir}/fakeinstall" meson install -C build
}

_install() {
  local src f dir
  for src; do
    f="${src#fakeinstall/}"
    dir="${pkgdir}/${f%/*}"
    install -m755 -d "${dir}"
    mv -v "${src}" "${dir}/"
  done
}

package_lib32-vulkan-mesa-layers() {
  pkgdesc="Mesa's Vulkan layers (32-bit)"
  depends=('lib32-libdrm' 'lib32-libxcb' 'lib32-wayland' 'vulkan-mesa-layers')
  conflicts=('lib32-vulkan-mesa-layer')
  replaces=('lib32-vulkan-mesa-layer')

  rm -rv fakeinstall/usr/share/vulkan/explicit_layer.d
  _install fakeinstall/usr/lib32/libVkLayer_MESA_overlay.so
  rm -rv fakeinstall/usr/bin/mesa-overlay-control.py

  rm -rv fakeinstall/usr/share/vulkan/implicit_layer.d
  _install fakeinstall/usr/lib32/libVkLayer_MESA_device_select.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-opencl-mesa() {
  pkgdesc="OpenCL support for AMD/ATI Radeon mesa drivers (32-bit)"
  depends=('lib32-expat' 'lib32-libdrm' 'lib32-libelf' 'lib32-clang' 'lib32-zstd' 'opencl-mesa')
  optdepends=('opencl-headers: headers necessary for OpenCL development')
  provides=('lib32-opencl-driver')

  rm -rv fakeinstall/etc/OpenCL
  _install fakeinstall/usr/lib32/lib*OpenCL*
  _install fakeinstall/usr/lib32/gallium-pipe

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-vulkan-intel() {
  pkgdesc="Intel's Vulkan mesa driver (32-bit)"
  depends=('lib32-wayland' 'lib32-libx11' 'lib32-libxshmfence' 'lib32-libdrm' 'lib32-zstd')
  optdepends=('lib32-vulkan-mesa-layers: additional vulkan layers')
  provides=('lib32-vulkan-driver')

  _install fakeinstall/usr/share/vulkan/icd.d/intel_icd*.json
  _install fakeinstall/usr/lib32/libvulkan_intel.so
  rm -rv fakeinstall/usr/include/vulkan/vulkan_intel.h

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-vulkan-radeon() {
  pkgdesc="Radeon's Vulkan mesa driver (32-bit)"
  depends=('lib32-wayland' 'lib32-libx11' 'lib32-libxshmfence' 'lib32-libelf' 'lib32-libdrm'
           'lib32-zstd' 'lib32-llvm-libs')
  optdepends=('lib32-vulkan-mesa-layers: additional vulkan layers')
  provides=('lib32-vulkan-driver')

  _install fakeinstall/usr/share/vulkan/icd.d/radeon_icd*.json
  _install fakeinstall/usr/lib32/libvulkan_radeon.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-libva-mesa-driver() {
  pkgdesc="VA-API implementation for gallium (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-llvm-libs' 'lib32-expat' 'lib32-libelf'
           'lib32-libxshmfence' 'lib32-zstd')

  _install fakeinstall/usr/lib32/dri/*_drv_video.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-mesa-vdpau() {
  pkgdesc="Mesa VDPAU drivers (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-llvm-libs' 'lib32-expat' 'lib32-libelf'
           'lib32-libxshmfence' 'lib32-zstd')

  _install fakeinstall/usr/lib32/vdpau

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-mesa() {
  depends=('lib32-libdrm' 'lib32-wayland' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-libxshmfence'
           'lib32-libelf' 'lib32-libunwind' 'lib32-llvm-libs' 'lib32-lm_sensors' 'lib32-libglvnd'
           'lib32-zstd' 'mesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages'
              'lib32-mesa-vdpau: for accelerated video playback'
              'lib32-libva-mesa-driver: for accelerated video playback')
  provides=('lib32-mesa-libgl' 'lib32-opengl-driver')
  conflicts=('lib32-mesa-libgl')
  replaces=('lib32-mesa-libgl')

  rm -rv fakeinstall/usr/share/drirc.d/00-mesa-defaults.conf
  rm -rv fakeinstall/usr/share/glvnd/egl_vendor.d/50_mesa.json

  # ati-dri, nouveau-dri, intel-dri, svga-dri, swrast, swr
  _install fakeinstall/usr/lib32/dri/*_dri.so

  #_install fakeinstall/usr/lib32/bellagio
  _install fakeinstall/usr/lib32/d3d
  _install fakeinstall/usr/lib32/lib{gbm,glapi}.so*
  _install fakeinstall/usr/lib32/libOSMesa.so*
  _install fakeinstall/usr/lib32/libxatracker.so*
  #_install fakeinstall/usr/lib32/libswrAVX*.so*

  # in vulkan-headers
  rm -rv fakeinstall/usr/include/vulkan

  rm -rv fakeinstall/usr/include
  _install fakeinstall/usr/lib32/pkgconfig

  # libglvnd support
  _install fakeinstall/usr/lib32/libGLX_mesa.so*
  _install fakeinstall/usr/lib32/libEGL_mesa.so*

  # indirect rendering
  ln -s /usr/lib32/libGLX_mesa.so.0 "${pkgdir}/usr/lib32/libGLX_indirect.so.0"

  # make sure there are no files left to install
  find fakeinstall -depth -print0 | xargs -0 rmdir

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
