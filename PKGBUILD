# Maintainer: KokaKiwi <kokakiwi+aur@kokakiwi.net>

pkgname=dwarfs
pkgver=0.9.8
pkgrel=1
pkgdesc="A fast high compression read-only file system"
url='https://github.com/mhx/dwarfs'
arch=('x86_64' 'aarch64')
license=('GPL-3.0-only')
depends=(
  'fuse3' 'openssl' 'boost-libs' 'jemalloc' 'xxhash' 'fmt'
  'lz4' 'xz' 'zstd' 'brotli' 'libarchive' 'flac'
  'libunwind' 'google-glog' 'fmt' 'gflags' 'double-conversion'
)
makedepends=(
  'cmake' 'ruby-ronn'
  'python' 'python-mistletoe'
  'boost' 'libevent' 'libdwarf' 'chrono-date'
  'utf8cpp' 'range-v3'
  'gtest'
)
source=("$pkgname-$pkgver.tar.xz::https://github.com/mhx/dwarfs/releases/download/v$pkgver/dwarfs-$pkgver.tar.xz"
0001-makepkg-Disable-faulty-test.patch)
sha256sums=('df5529f50a679f1db89936ea8ea082555863076ffa6899fe37b65120790e1075'
            '9b16db168518a4130f6f3e05475daee2195df40e10a0f56e8aa0b5062f0a529d')
b2sums=('18ab6366e9a9bf8fe2d1e469f2c83b6a014e1c9e9ee2f43e0cd788c524f3b5af3c8067c6397ffc614e4d540825d6e33a87bef54da89fcc9fa2eeda5c39c0399a'
        '81115c6d69d201095d5207b7d878619a6f43f9f03933824e28e7cd85a164786bef1388d6a5369052c8be25db47da588a22249152ac58c78baea2cf60fcfec4a7')

prepare() {
  cd "$pkgname-$pkgver"

  patch -Np1 -i "$srcdir/0001-makepkg-Disable-faulty-test.patch"
}

build() {
  # Setting up release flags manually here so we get to use `CMAKE_BUILD_TYPE=None`
  # and keep makepkg-defined flags for build
  # cf. https://wiki.archlinux.org/title/CMake_package_guidelines#Fixing_the_automatic_optimization_flag_override
  export CFLAGS="$CFLAGS -DNDEBUG"
  export CXXFLAGS="$CXXFLAGS -DNDEBUG"

  cmake -B build -S "$pkgname-$pkgver" \
    -W no-dev \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D CMAKE_BUILD_TYPE=None \
    -D WITH_TESTS=ON \
    -D PREFER_SYSTEM_ZSTD=ON \
    -D PREFER_SYSTEM_XXHASH=ON \
    -D PREFER_SYSTEM_LIBFMT=ON \
    -D PREFER_SYSTEM_GTEST=ON

  cmake --build build
}

check() {
  #TODO: Find a way to either load the `fuse` module for the tests or disable the tests only when `fuse` module is not
  #      loaded
  #      Also wtf with perfmon test??
  cmake --build build --target test -- ARGS="-E '(dwarfs/tools_test\..*|dwarfsextract_test\.perfmon)'"
}

package() {
  cmake --install build --prefix "$pkgdir/usr"

  mv "$pkgdir/usr/sbin"/* "$pkgdir/usr/bin"
  rm -rf "$pkgdir/usr/sbin"

  install -Dm0644 "$pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
