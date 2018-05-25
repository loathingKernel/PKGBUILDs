# Maintainer: Laurent Carlier <lordheavym@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=('lib32-vulkan-intel' 'lib32-vulkan-radeon' 'lib32-libva-mesa-driver' 'lib32-mesa-vdpau' 'lib32-mesa')
pkgver=18.0.4
pkgrel=2
arch=('x86_64')
makedepends=('python2-mako' 'lib32-libxml2' 'lib32-expat' 'lib32-libx11' 'glproto' 'lib32-libdrm' 'dri2proto' 'dri3proto' 'presentproto'
             'lib32-libxshmfence' 'lib32-libxxf86vm' 'lib32-libxdamage' 'gcc-multilib' 'lib32-libelf' 'lib32-llvm' 'lib32-libvdpau'
             'lib32-libva' 'lib32-wayland' 'wayland-protocols' 'lib32-libglvnd' 'lib32-lm_sensors' 'meson')
url="http://mesa3d.sourceforge.net"
license=('custom')
source=(https://mesa.freedesktop.org/archive/mesa-${pkgver}.tar.xz{,.sig}
        LICENSE
        0001-glvnd-fix-gl.pc.patch
        0002-meson-Add-library-versions-to-swr-drivers.patch
        0003-meson-Version-libMesaOpenCL-like-autotools-does.patch
        0004-loader_dri3-Variant-2-Wait-for-pending-swaps-to-comp.patch)
sha512sums=('f9a14be46c209661ceb318add1611481445d13b47e95c7a5d2a5e5ecfdd5d2c3fa9c2b16b30035bbb8d61ccc7cb65bfa6698ac8b040273e5ab045a951a67752c'
            'SKIP'
            'f9f0d0ccf166fe6cb684478b6f1e1ab1f2850431c06aa041738563eb1808a004e52cdec823c103c9e180f03ffc083e95974d291353f0220fe52ae6d4897fecc7'
            '2f40198eff47664c831c56e8a63f60a4d1b815cf697e6bdb0be39e6d9c5df043857f6264b7cd2ccf46c07626186c565144e80f4214b5f7936ef7024c47201437'
            'c3f3baf8a5f480ce64b321c031e31c0d5819732ca34647ac545d0fd7fafa40ad4dcf1e1ec8d574754e0a44bf0cdc462ed8709c8d9b58a17e01c6ba5b4c5e91c6'
            'a2062f8a5259aabed1aa20df6a8510f0f3e914cb6bba72751249b3295285596bb7615063a7a7b7870f9f4489d0e6b774f0bced2bdde49a1aa9df6a44976462d1'
            '572901a1e9cacfacfc8c4cc3cd077a626d4aeda8c8a58f6085bae827cba8a2d4d99af1dafbb5a9296b6ebf3120e2b05a084fe1c96093074befe62597319384a1')
validpgpkeys=('8703B6700E7EE06D7A39B8D6EDAE37B02CEB490D'  # Emil Velikov <emil.l.velikov@gmail.com>
              '946D09B5E4C9845E63075FF1D961C596A7203456'  # Andres Gomez <tanty@igalia.com>
              'E3E8F480C52ADD73B278EE78E1ECBE07D7D70895'  # Juan Antonio Suárez Romero (Igalia, S.L.) <jasuarez@igalia.com>"
              'A5CC9FEC93F2F837CB044912336909B6B25FADFA') # Juan A. Suarez Romero <jasuarez@igalia.com>
  
prepare() {
  cd mesa-${pkgver}

  # glvnd support patches - from Fedora
  # non-upstreamed ones
  patch -Np1 -i ../0001-glvnd-fix-gl.pc.patch

  # Upstreamed meson fixes
  patch -Np1 -i ../0002-meson-Add-library-versions-to-swr-drivers.patch
  patch -Np1 -i ../0003-meson-Version-libMesaOpenCL-like-autotools-does.patch

  # experimental patch, should fix FS#58549
  # see https://bugs.freedesktop.org/show_bug.cgi?id=106351
  # and https://patchwork.freedesktop.org/series/42687/
  patch -Np1 -i ../0004-loader_dri3-Variant-2-Wait-for-pending-swaps-to-comp.patch
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  export LLVM_CONFIG="/usr/bin/llvm-config32"
  
  arch-meson mesa-$pkgver build \
    --libdir=/usr/lib32 \
    -D b_lto=false \
    -D b_ndebug=true \
    -D platforms=x11,wayland,drm,surfaceless \
    -D dri-drivers=i915,i965,r100,r200,nouveau \
    -D gallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,swr \
    -D vulkan-drivers=amd,intel \
    -D swr-arches=avx,avx2 \
    -D dri3=true \
    -D egl=true \
    -D gallium-extra-hud=true \
    -D gallium-nine=true \
    -D gallium-omx=false \
    -D gallium-opencl=disabled \
    -D gallium-va=true \
    -D gallium-vdpau=true \
    -D gallium-xa=true \
    -D gallium-xvmc=false \
    -D gbm=true \
    -D gles1=true \
    -D gles2=true \
    -D glvnd=true \
    -D glx=dri \
    -D libunwind=false \
    -D llvm=true \
    -D lmsensors=true \
    -D osmesa=gallium \
    -D shared-glapi=true \
    -D texture-float=true \
    -D valgrind=false

  # Print config
  meson configure build

  ninja -C build

  # fake installation to be seperated into packages
  # outside of fakeroot but mesa doesn't need to chown/mod
  DESTDIR="${srcdir}/fakeinstall" ninja -C build install
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

package_lib32-vulkan-intel() {
  pkgdesc="Intel's Vulkan mesa driver (32-bit)"
  depends=('lib32-wayland' 'lib32-libx11' 'lib32-libdrm' 'lib32-libxshmfence')
  provides=('lib32-vulkan-driver')

  _install fakeinstall/usr/share/vulkan/icd.d/intel_icd*.json
  _install fakeinstall/usr/lib32/libvulkan_intel.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-vulkan-radeon() {
  pkgdesc="Radeon's Vulkan mesa driver (32-bit)"
  depends=('lib32-wayland' 'lib32-libx11' 'lib32-llvm-libs' 'lib32-libdrm' 'lib32-libelf' 'lib32-libxshmfence')
  provides=('lib32-vulkan-driver')

  _install fakeinstall/usr/share/vulkan/icd.d/radeon_icd*.json
  _install fakeinstall/usr/lib32/libvulkan_radeon.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-libva-mesa-driver() {
  pkgdesc="VA-API implementation for gallium (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-expat' 'lib32-llvm-libs' 'lib32-libelf' 'lib32-libxshmfence')

  _install fakeinstall/usr/lib32/dri/*_drv_video.so
   
  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-mesa-vdpau() {
  pkgdesc="Mesa VDPAU drivers (32-bit)"
  depends=('lib32-libdrm' 'lib32-libx11' 'lib32-expat' 'lib32-llvm-libs' 'lib32-libelf' 'lib32-libxshmfence')

  _install fakeinstall/usr/lib32/vdpau
   
  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-mesa() {
  pkgdesc="An open-source implementation of the OpenGL specification (32-bit)"
  depends=('lib32-libdrm' 'lib32-libxxf86vm' 'lib32-libxdamage' 'lib32-libxshmfence' 'lib32-lm_sensors'
           'lib32-libelf' 'lib32-llvm-libs' 'lib32-wayland' 'lib32-libglvnd' 'mesa')
  optdepends=('opengl-man-pages: for the OpenGL API man pages'
              'lib32-mesa-vdpau: for accelerated video playback')
  provides=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri' 'lib32-mesa-libgl' 'lib32-opengl-driver')
  conflicts=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri' 'lib32-mesa-libgl')
  replaces=('lib32-ati-dri' 'lib32-intel-dri' 'lib32-nouveau-dri' 'lib32-mesa-dri' 'lib32-mesa-libgl')

  # ati-dri, nouveau-dri, intel-dri, svga-dri, swrast
  _install fakeinstall/usr/lib32/dri/*_dri.so
   
  _install fakeinstall/usr/lib32/d3d
  _install fakeinstall/usr/lib32/lib{gbm,glapi}.so*
  _install fakeinstall/usr/lib32/libOSMesa.so*
  _install fakeinstall/usr/lib32/libxatracker.so*
  _install fakeinstall/usr/lib32/libswrAVX*.so*

  # in libglvnd
  rm -v fakeinstall/usr/lib32/libGLESv{1_CM,2}.so*
  
  # in wayland
  rm -v fakeinstall/usr/lib32/libwayland-egl.so*
  rm -v fakeinstall/usr/lib32/pkgconfig/wayland-egl.pc

  _install fakeinstall/usr/lib32/pkgconfig

  # libglvnd support
  _install fakeinstall/usr/lib32/libGLX_mesa.so*
  _install fakeinstall/usr/lib32/libEGL_mesa.so*

  # indirect rendering
  ln -s /usr/lib32/libGLX_mesa.so.0 "${pkgdir}/usr/lib32/libGLX_indirect.so.0"
  
  rm -rv fakeinstall/etc
  rm -rv fakeinstall/usr/include
  rm -rv fakeinstall/usr/share

  # make sure there are no files left to install
  find fakeinstall -depth -print0 | xargs -0 rmdir

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
