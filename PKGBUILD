# Maintainer: loathingkernel <loathingkernel _a_ gmail _d_ com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Eduardo Romero <eduardo@archlinux.org>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>

pkgname=wine-cachyos
_srctag=9.0-20241031
pkgver=${_srctag//-/.}
pkgrel=1
epoch=2

_pkgbasever=${pkgver/rc/-rc}
_winever=$_pkgbasever
#_winever=${_pkgbasever%.*}

source=(wine-cachyos::git+https://github.com/CachyOS/wine-cachyos.git#tag=cachyos-${_srctag}-wine
        30-win32-aliases.conf
        wine-binfmt.conf)
source+=(
        wine-optical-flow.patch
)
validpgpkeys=(5AC1A08B03BD7A313E0A955AF5E6E9EEB9461DD7
              DA23579A74D4AD9AF9D3F945CEFAC8EAAF17519D)

pkgdesc="A compatibility layer for running Windows programs, with extra CachyOS flavor"
url="https://github.com/CachyOS/wine-cachyos"
arch=(x86_64 x86_64_v3)
options=(!staticlibs !lto !debug)
license=(LGPL-2.1-or-later)

depends=(
  attr             lib32-attr
  fontconfig       lib32-fontconfig
  libxcursor       lib32-libxcursor
  libxrandr        lib32-libxrandr
  libxi            lib32-libxi
  gettext          lib32-gettext
  freetype2        lib32-freetype2
  gcc-libs         lib32-gcc-libs
  libpcap          lib32-libpcap
  desktop-file-utils
)
depends+=(
  libxkbcommon     lib32-libxkbcommon
  wayland          lib32-wayland
)

makedepends=(autoconf bison perl flex mingw-w64-gcc
  python
  giflib                lib32-giflib
  gnutls                lib32-gnutls
  libxinerama           lib32-libxinerama
  libxcomposite         lib32-libxcomposite
  libxxf86vm            lib32-libxxf86vm
  v4l-utils             lib32-v4l-utils
  alsa-lib              lib32-alsa-lib
  libxcomposite         lib32-libxcomposite
  mesa                  lib32-mesa
  mesa-libgl            lib32-mesa-libgl
  opencl-icd-loader     lib32-opencl-icd-loader
  libpulse              lib32-libpulse
  libva                 lib32-libva
  gtk3                  lib32-gtk3
  gst-plugins-base-libs lib32-gst-plugins-base-libs
  gst-plugins-good      lib32-gst-plugins-good
  vulkan-icd-loader     lib32-vulkan-icd-loader
  sdl2                  lib32-sdl2
  libcups               lib32-libcups
  sane
  libgphoto2
  ffmpeg
  samba
  opencl-headers
  git
)

optdepends=(
  giflib                lib32-giflib
  gnutls                lib32-gnutls
  v4l-utils             lib32-v4l-utils
  libpulse              lib32-libpulse
  alsa-plugins          lib32-alsa-plugins
  alsa-lib              lib32-alsa-lib
  libxcomposite         lib32-libxcomposite
  libxinerama           lib32-libxinerama
  opencl-icd-loader     lib32-opencl-icd-loader
  libva                 lib32-libva
  gtk3                  lib32-gtk3
  gst-plugins-base-libs lib32-gst-plugins-base-libs
  gst-plugins-good      lib32-gst-plugins-good
  vulkan-icd-loader     lib32-vulkan-icd-loader
  sdl2                  lib32-sdl2
  sane
  libgphoto2
  ffmpeg
  cups
  samba           dosbox
)

provides=("wine=9.0")
conflicts=('wine')
install=wine.install

prepare() {
  # Get rid of old build dirs
  rm -rf $pkgname-{32,64}-build
  mkdir $pkgname-{32,64}-build

  pushd $pkgname
      git config user.email "wine@cachyos.org"
      git config user.name "wine cachyos"
      git tag wine-9.0 --annotate -m "$pkgver" --force
      patch -Np1 -i "$srcdir"/wine-optical-flow.patch
      ./dlls/winevulkan/make_vulkan -x vk.xml
      ./tools/make_specfiles
      ./tools/make_requests
      autoreconf -fiv
  popd
}

build() {
  # Doesn't compile without remove these flags as of 4.10
  export CFLAGS="$CFLAGS -ffat-lto-objects"

  local -a split=($CFLAGS)
  local -A flags
  for opt in "${split[@]}"; do flags["${opt%%=*}"]="${opt##*=}"; done
  local march="${flags["-march"]:-nocona}"
  local mtune="generic" #"${flags["-mtune"]:-core-avx2}"

  # From Proton
  OPTIMIZE_FLAGS="-O3 -march=$march -mtune=$mtune -mfpmath=sse -pipe -fno-semantic-interposition"
  SANITY_FLAGS="-fwrapv -fno-strict-aliasing"
  WARNING_FLAGS="-Wno-incompatible-pointer-types"
  COMMON_FLAGS="$OPTIMIZE_FLAGS $SANITY_FLAGS $WARNING_FLAGS -s"

  COMMON_LDFLAGS="-Wl,-O1,--sort-common,--as-needed"
  LTO_FLAGS="-fuse-linker-plugin -fdevirtualize-at-ltrans -flto-partition=one -flto -Wl,-flto"

  export LDFLAGS="$COMMON_LDFLAGS $LTO_FLAGS"
  export CROSSLDFLAGS="$COMMON_LDFLAGS -Wl,--file-alignment,4096"

  cd "$srcdir"

  msg2 "Building Wine-64..."

  export CFLAGS="$COMMON_FLAGS -mcmodel=small $LTO_FLAGS"
  export CXXFLAGS="$COMMON_FLAGS -mcmodel=small -std=c++17 $LTO_FLAGS"
  export CROSSCFLAGS="$COMMON_FLAGS -mcmodel=small"
  export CROSSCXXFLAGS="$COMMON_FLAGS -mcmodel=small -std=c++17"
  export PKG_CONFIG_PATH="/usr/lib/pkgconfig:/usr/share/pkgconfig"
  cd "$srcdir/$pkgname-64-build"
  ../$pkgname/configure \
    --prefix=/usr \
    --libdir=/usr/lib \
    --with-x \
    --with-wayland \
    --with-gstreamer \
    --with-mingw \
    --with-alsa \
    --without-oss \
    --disable-winemenubuilder \
    --disable-tests \
    --enable-win64 \
    --with-xattr

  make

  msg2 "Building Wine-32..."

  # Disable AVX instead of using 02, for 32bit
  export CFLAGS="$COMMON_FLAGS -mstackrealign -mno-avx $LTO_FLAGS"
  export CXXFLAGS="$COMMON_FLAGS -mstackrealign -mno-avx -std=c++17 $LTO_FLAGS"
  export CROSSCFLAGS="$COMMON_FLAGS -mstackrealign -mno-avx"
  export CROSSCXXFLAGS="$COMMON_FLAGS -mstackrealign -mno-avx -std=c++17"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
  cd "$srcdir/$pkgname-32-build"
  ../$pkgname/configure \
    --prefix=/usr \
    --with-x \
    --with-wayland \
    --with-gstreamer \
    --with-mingw \
    --with-alsa \
    --without-oss \
    --disable-winemenubuilder \
    --disable-tests \
    --with-xattr \
    --libdir=/usr/lib32 \
    --with-wine64="$srcdir/$pkgname-64-build"

  make
}

package() {
  msg2 "Packaging Wine-32..."
  cd "$srcdir/$pkgname-32-build"

  make prefix="$pkgdir/usr" \
    libdir="$pkgdir/usr/lib32" \
    dlldir="$pkgdir/usr/lib32/wine" install

  msg2 "Packaging Wine-64..."
  cd "$srcdir/$pkgname-64-build"
  make prefix="$pkgdir/usr" \
    libdir="$pkgdir/usr/lib" \
    dlldir="$pkgdir/usr/lib/wine" install

  # Font aliasing settings for Win32 applications
  install -d "$pkgdir"/usr/share/fontconfig/conf.{avail,default}
  install -m644 "$srcdir/30-win32-aliases.conf" "$pkgdir/usr/share/fontconfig/conf.avail"
  ln -s ../conf.avail/30-win32-aliases.conf "$pkgdir/usr/share/fontconfig/conf.default/30-win32-aliases.conf"
  install -Dm 644 "$srcdir/wine-binfmt.conf" "$pkgdir/usr/lib/binfmt.d/wine.conf"

  i686-w64-mingw32-strip --strip-unneeded "$pkgdir"/usr/lib32/wine/i386-windows/*.{dll,exe}
  x86_64-w64-mingw32-strip --strip-unneeded "$pkgdir"/usr/lib/wine/x86_64-windows/*.{dll,exe}

  find "$pkgdir"/usr/lib{,32}/wine -iname "*.a" -delete
  find "$pkgdir"/usr/lib{,32}/wine -iname "*.def" -delete
}

# vim:set ts=8 sts=2 sw=2 et:
b2sums=('07db0f26144e00738fbbdeff3a96c303a62c706fa56d346d8c4b5a4956697fb9a05f7a91ae1235bdb922a8ec89ebf85479e7fdc5a99a19a02ea7bde4f5416d66'
        '45db34fb35a679dc191b4119603eba37b8008326bd4f7d6bd422fbbb2a74b675bdbc9f0cc6995ed0c564cf088b7ecd9fbe2d06d42ff8a4464828f3c4f188075b'
        'e9de76a32493c601ab32bde28a2c8f8aded12978057159dd9bf35eefbf82f2389a4d5e30170218956101331cf3e7452ae82ad0db6aad623651b0cc2174a61588'
        '3c4516dd44c8bbec45fc30e75c45e3a87ca6d0275f22e1ba8a9b9a423768ea789166140519cceae3c8e24476d1d9acab5439075b073c3422c4fead4fa7a18b88')
