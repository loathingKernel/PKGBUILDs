# Maintainer: Laurent Carlier <lordheavym@gmail.com>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>

pkgbase=lib32-mesa
pkgname=(
  'lib32-vulkan-mesa-layers'
  'lib32-opencl-clover-mesa'
  'lib32-opencl-rusticl-mesa'
  'lib32-vulkan-intel'
  'lib32-vulkan-radeon'
  'lib32-vulkan-swrast'
  'lib32-vulkan-virtio'
  'lib32-libva-mesa-driver'
  'lib32-mesa-vdpau'
  'lib32-mesa'
)
pkgver=23.1.6
pkgrel=2
epoch=1
pkgdesc="An open-source implementation of the OpenGL specification (32-bit)"
url="https://www.mesa3d.org/"
arch=('x86_64')
license=('custom')
makedepends=(
  'lib32-clang'
  'lib32-expat'
  'lib32-libdrm'
  'lib32-libelf'
  'lib32-libglvnd'
  'lib32-libunwind'
  'lib32-libva'
  'lib32-libvdpau'
  'lib32-libx11'
  'lib32-libxdamage'
  'lib32-libxml2'
  'lib32-libxrandr'
  'lib32-libxshmfence'
  'lib32-libxxf86vm'
  'lib32-llvm'
  'lib32-lm_sensors'
  'lib32-rust-libs'
  'lib32-spirv-llvm-translator'
  'lib32-spirv-tools'
  'lib32-systemd'
  'lib32-vulkan-icd-loader'
  'lib32-wayland'
  'lib32-zstd'

  # shared between mesa and lib32-mesa
  'clang'
  'cmake'
  'elfutils'
  'glslang'
  'libclc'
  'meson'
  'python-mako'
  'python-ply'
  'rust-bindgen'
  'wayland-protocols'
  'xorgproto'
)
source=(
  https://mesa.freedesktop.org/archive/mesa-${pkgver}.tar.xz{,.sig}
  LICENSE
)
sha256sums=('f4c7fd8e7b472a88da7d83e9a48f6f3bd17d4ea2cc4386f7231b796f3964157a'
            'SKIP'
            '7052ba73bb07ea78873a2431ee4e828f4e72bda7d176d07f770fa48373dec537')
b2sums=('78b71ede0655e538a71d22ecbfb0bed7497c258a16ce5f7d9b627a4c9372f26292a50aec848a4923524e4862b00a6d5d3d2521b05033d9cf39d31f037bdb9254'
        'SKIP'
        '1ecf007b82260710a7bf5048f47dd5d600c168824c02c595af654632326536a6527fbe0738670ee7b921dd85a70425108e0f471ba85a8e1ca47d294ad74b4adb')
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
  local meson_options=(
    --cross-file lib32
    -D android-libbacktrace=disabled
    -D b_ndebug=true
    -D dri3=enabled
    -D egl=enabled
    -D gallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,i915,iris,crocus,zink
    -D gallium-extra-hud=true
    -D gallium-nine=true
    -D gallium-omx=disabled
    -D gallium-opencl=icd
    -D gallium-rusticl=true
    -D gallium-va=enabled
    -D gallium-vdpau=enabled
    -D gallium-xa=enabled
    -D gbm=enabled
    -D gles1=disabled
    -D gles2=enabled
    -D glvnd=true
    -D glx=dri
    -D intel-clc=enabled
    -D libunwind=enabled
    -D llvm=enabled
    -D lmsensors=enabled
    -D microsoft-clc=disabled
    -D osmesa=true
    -D platforms=x11,wayland
    -D rust_std=2021
    -D shared-glapi=enabled
    -D valgrind=disabled
    -D video-codecs=vc1dec,h264dec,h264enc,h265dec,h265enc
    -D vulkan-drivers=amd,intel,intel_hasvk,swrast,virtio-experimental
    -D vulkan-layers=device-select,intel-nullhw,overlay
  )

  # Build only minimal debug info to reduce size
  CFLAGS+=' -g1'
  CXXFLAGS+=' -g1'

  export BINDGEN_EXTRA_CLANG_ARGS="-m32"

  arch-meson mesa-$pkgver build "${meson_options[@]}"
  meson configure build # Print config

  # Evil: Hack build to make proc-macro crate native
  sed -e '/^rule rust_COMPILER$/irule rust_HACK\n command = rustc -C linker=gcc $ARGS $in\n deps = gcc\n depfile = $targetdep\n description = Compiling native Rust source $in\n' \
      -e '/^build src\/gallium\/frontends\/rusticl\/librusticl_proc_macros\.so:/s/rust_COMPILER/rust_HACK/' \
      -e '/^ LINK_ARGS =/s/ src\/gallium\/frontends\/rusticl\/librusticl_proc_macros\.so//' \
      -i build/build.ninja

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

_libdir=usr/lib32

package_lib32-vulkan-mesa-layers() {
  pkgdesc="Mesa's Vulkan layers (32-bit)"
  depends=(
    'lib32-libdrm'
    'lib32-libxcb'
    'lib32-wayland'

    'vulkan-mesa-layers'
  )
  conflicts=('lib32-vulkan-mesa-layer')
  replaces=('lib32-vulkan-mesa-layer')

  rm -rv fakeinstall/usr/share/vulkan/explicit_layer.d
  rm -rv fakeinstall/usr/share/vulkan/implicit_layer.d
  _install fakeinstall/$_libdir/libVkLayer_*.so
  rm -v fakeinstall/usr/bin/mesa-overlay-control.py

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-opencl-clover-mesa() {
  pkgdesc="OpenCL support with clover for mesa drivers (32-bit)"
  depends=(
    'lib32-clang'
    'lib32-expat'
    'lib32-libdrm'
    'lib32-libelf'
    'lib32-spirv-llvm-translator'
    'lib32-zstd'

    'libclc'
    'opencl-clover-mesa'
  )
  optdepends=('opencl-headers: headers necessary for OpenCL development')
  provides=('lib32-opencl-driver')
  replaces=("lib32-opencl-mesa<=23.1.4-1")
  conflicts=('lib32-opencl-mesa')

  rm -v fakeinstall/etc/OpenCL/vendors/mesa.icd
  _install fakeinstall/$_libdir/libMesaOpenCL*
  _install fakeinstall/$_libdir/gallium-pipe

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-opencl-rusticl-mesa() {
  pkgdesc="OpenCL support with rusticl for mesa drivers (32-bit)"
  depends=(
    'lib32-clang'
    'lib32-expat'
    'lib32-libdrm'
    'lib32-libelf'
    'lib32-lm_sensors'
    'lib32-spirv-llvm-translator'
    'lib32-zstd'

    'libclc'
    'opencl-rusticl-mesa'
  )
  optdepends=('opencl-headers: headers necessary for OpenCL development')
  provides=('lib32-opencl-driver')
  replaces=("lib32-opencl-mesa<=23.1.4-1")
  conflicts=('lib32-opencl-mesa')

  rm -v fakeinstall/etc/OpenCL/vendors/rusticl.icd
  _install fakeinstall/$_libdir/libRusticlOpenCL*

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-vulkan-intel() {
  pkgdesc="Intel's Vulkan mesa driver (32-bit)"
  depends=(
    'lib32-libdrm'
    'lib32-libx11'
    'lib32-libxshmfence'
    'lib32-systemd'
    'lib32-wayland'
    'lib32-zstd'
  )
  optdepends=('lib32-vulkan-mesa-layers: additional vulkan layers')
  provides=('lib32-vulkan-driver')

  _install fakeinstall/usr/share/vulkan/icd.d/intel_*.json
  _install fakeinstall/$_libdir/libvulkan_intel*.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-vulkan-radeon() {
  pkgdesc="Radeon's Vulkan mesa driver (32-bit)"
  depends=(
    'lib32-libdrm'
    'lib32-libelf'
    'lib32-libx11'
    'lib32-libxshmfence'
    'lib32-llvm-libs'
    'lib32-systemd'
    'lib32-wayland'
    'lib32-zstd'

    'vulkan-radeon'
  )
  optdepends=('lib32-vulkan-mesa-layers: additional vulkan layers')
  provides=('lib32-vulkan-driver')

  rm -v fakeinstall/usr/share/drirc.d/00-radv-defaults.conf
  _install fakeinstall/usr/share/vulkan/icd.d/radeon_icd*.json
  _install fakeinstall/$_libdir/libvulkan_radeon.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-vulkan-swrast() {
  pkgdesc="Vulkan software rasteriser driver (32-bit)"
  depends=(
    'lib32-libdrm'
    'lib32-libunwind'
    'lib32-libx11'
    'lib32-libxshmfence'
    'lib32-llvm-libs'
    'lib32-systemd'
    'lib32-wayland'
    'lib32-zstd'
  )
  optdepends=('lib32-vulkan-mesa-layers: additional vulkan layers')
  conflicts=('lib32-vulkan-mesa')
  replaces=('lib32-vulkan-mesa')
  provides=('lib32-vulkan-driver')

  _install fakeinstall/usr/share/vulkan/icd.d/lvp_icd*.json
  _install fakeinstall/$_libdir/libvulkan_lvp.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-vulkan-virtio() {
  pkgdesc="Venus Vulkan mesa driver for Virtual Machines (32-bit)"
  depends=(
    'lib32-libdrm'
    'lib32-libx11'
    'lib32-libxshmfence'
    'lib32-systemd'
    'lib32-wayland'
    'lib32-zstd'
  )
  optdepends=('lib32-vulkan-mesa-layers: additional vulkan layers')
  provides=('lib32-vulkan-driver')

  _install fakeinstall/usr/share/vulkan/icd.d/virtio_icd*.json
  _install fakeinstall/$_libdir/libvulkan_virtio.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-libva-mesa-driver() {
  pkgdesc="VA-API drivers (32-bit)"
  depends=(
    'lib32-expat'
    'lib32-libdrm'
    'lib32-libelf'
    'lib32-libx11'
    'lib32-libxshmfence'
    'lib32-llvm-libs'
    'lib32-zstd'
  )
  provides=('lib32-libva-driver')

  _install fakeinstall/$_libdir/dri/*_drv_video.so

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-mesa-vdpau() {
  pkgdesc="VDPAU drivers (32-bit)"
  depends=(
    'lib32-expat'
    'lib32-libdrm'
    'lib32-libelf'
    'lib32-libx11'
    'lib32-libxshmfence'
    'lib32-llvm-libs'
    'lib32-zstd'
  )
  provides=('lib32-vdpau-driver')

  _install fakeinstall/$_libdir/vdpau

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}

package_lib32-mesa() {
  depends=(
    'lib32-libdrm'
    'lib32-libelf'
    'lib32-libglvnd'
    'lib32-libunwind'
    'lib32-libxdamage'
    'lib32-libxshmfence'
    'lib32-libxxf86vm'
    'lib32-llvm-libs'
    'lib32-lm_sensors'
    'lib32-vulkan-icd-loader'
    'lib32-wayland'
    'lib32-zstd'

    'mesa'
  )
  optdepends=(
    'lib32-libva-mesa-driver: for accelerated video playback'
    'lib32-mesa-vdpau: for accelerated video playback'
    'opengl-man-pages: for the OpenGL API man pages'
  )
  provides=(
    'lib32-mesa-libgl'
    'lib32-opengl-driver'
  )
  conflicts=('lib32-mesa-libgl')
  replaces=('lib32-mesa-libgl')

  rm -v fakeinstall/usr/share/drirc.d/00-mesa-defaults.conf
  rm -v fakeinstall/usr/share/glvnd/egl_vendor.d/50_mesa.json

  # ati-dri, nouveau-dri, intel-dri, svga-dri, swrast, swr
  _install fakeinstall/$_libdir/dri/*_dri.so

  _install fakeinstall/$_libdir/d3d
  _install fakeinstall/$_libdir/lib{gbm,glapi}.so*
  _install fakeinstall/$_libdir/libOSMesa.so*
  _install fakeinstall/$_libdir/libxatracker.so*

  rm -rv fakeinstall/usr/include
  _install fakeinstall/$_libdir/pkgconfig

  # libglvnd support
  _install fakeinstall/$_libdir/libGLX_mesa.so*
  _install fakeinstall/$_libdir/libEGL_mesa.so*

  # indirect rendering
  ln -sr "$pkgdir"/$_libdir/libGLX_{mesa,indirect}.so.0

  # make sure there are no files left to install
  find fakeinstall -depth -print0 | xargs -0 rmdir

  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
