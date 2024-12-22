# Maintainer: Kevin Brodsky <corax26 at gmail dot com>

_name=ncurses
pkgname=lib32-${_name}5-compat-libs
pkgver=6.5
pkgrel=1
pkgdesc="System V Release 4.0 curses emulation library (32-bit), ABI 5"
arch=(x86_64)
url=https://invisible-island.net/ncurses/ncurses.html
license=(MIT)
depends=(
  lib32-gcc-libs
  lib32-glibc
  lib32-$_name=$pkgver
)
source=(
  $_name::git+https://github.com/ThomasDickey/ncurses-snapshots.git?signed#tag=v${pkgver/./_}
  $_name-6.3-libs.patch
  $_name-6.3-pkgconfig.patch
)
sha512sums=('da9a9e6227d14deef580785b49ab366e9b1c99890c1dd428a566572d01a7fc7da1ed110c9a80047ce6dee813f4dadf37ba43f8048c43b0ab6074a10b0c4b4ef2'
            'adb02b838c40f1e58a1b31c26d5cd0f2a1c43f3b6d68e839981764c0f6c905a9eb51dd36ff018628fdeb20747cc7467727d57135408ab4848259384077a52b28'
            '2d2c0ec3c880e638ab4aa3dbff5e28e4cd233153e24816bd87e077f848aa3edd5114cd0f2a7f6e8869dd1861a2746e512886c18264ff1676927dcc320c5ef958')
b2sums=('c0c577b633d74838d109b30ea387c10fce70fb7fea548f4f965d508dc0fc1efd2ef45a81f5c5cc960a236ccee0e3aa1d4d99d0b666692c9b5bfcdd75bad604a0'
        '31bb10e82dd018a75e57252052650d9f0f5eb5e7e887118c2ea40032b11f59ec6aa4d9bae804c615cbecdf3382f3434e0c9e9e8440fdefe66a507be020b8965c'
        'fb6cf606cf3db7f6b306272696a63bce83d52cfa91e850f9a7bdb9d3d8455a26943529a9cf79731dddc7f763c27211a9afab9c4c31dbb6d12fd720eb390eb0a3')
validpgpkeys=('19882D92DDA4C400C22C0D56CC2AF4472167BE03')  # Thomas Dickey <dickey@invisible-island.net>

prepare() {
  # do not link against test libraries
  patch -Np1 -d $_name -i ../$_name-6.3-libs.patch
  # do not leak build-time LDFLAGS into the pkgconfig files:
  # https://bugs.archlinux.org/task/68523
  patch -Np1 -d $_name  -i ../$_name-6.3-pkgconfig.patch
  # NOTE: can't run autoreconf because the autotools setup is custom and ancient
}

build() {
  local configure_options=(
    --prefix=/usr
    --libdir=/usr/lib32
    --disable-db-install
    --disable-root-access
    --disable-root-environ
    --disable-setuid-environ
    --enable-widec
    --mandir=/usr/share/man
    --with-shared
    --with-versioned-syms
    --without-ada
    --without-debug
    --without-manpages
    --without-progs
    --without-tack
    --without-tests
    --with-abi-version=5
    --without-gpm
    --without-pkg-config
  )

  export CC="gcc -m32"
  export CXX="g++ -m32"

  cd $_name
  ./configure "${configure_options[@]}"
  make
}

package() {
  make DESTDIR="$pkgdir" install -C $_name

  # fool packages looking to link to non-wide-character ncurses libraries
  for lib in ncurses form panel menu; do
    ln -sv lib${lib}w.so.5 "$pkgdir/usr/lib32/lib$lib.so.5"
  done

  # tic and ticinfo functionality is built in by default
  # make sure that anything linking against it links against libncursesw.so instead
  for lib in tic tinfo; do
    ln -sv libncursesw.so.5 "$pkgdir/usr/lib32/lib$lib.so.5"
  done

  # remove all files conflicting with ncurses
  rm -frv "$pkgdir/usr/"{bin,include,share}

  # Remove .so symlinks and static libraries (conflicting with lib32-ncurses)
  rm -fv "$pkgdir/usr/"{lib32/*.so,lib32/*.a}

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_name "$pkgdir/usr/share/licenses/$pkgname"
}

# vim: set et ts=2 sw=2:
