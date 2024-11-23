# Maintainer: Eli Schwartz <eschwartz@archlinux.org>

# All my PKGBUILDs are managed at https://github.com/eli-schwartz/pkgbuilds

pkgname=pacman-static
pkgver=7.0.0.r3.g7736133
_cares_ver=1.34.2
_nghttp2_ver=1.64.0
_curlver=8.11.0
_sslver=3.4.0
_zlibver=1.3.1
_xzver=5.6.3
_bzipver=1.0.8
_zstdver=1.5.6
_libarchive_ver=3.7.7
_gpgerrorver=1.51
_libassuanver=3.0.0
_gpgmever=1.24.0
pkgrel=9
# use annotated tag and patch level commit from release branch (can be empty for no patches)
_git_tag=7.0.0
_git_patch_level_commit=77361331ae3864c6ea880e715c5864d59336f275
pkgdesc="Statically-compiled pacman (to fix or install systems without libc)"
arch=('i486' 'i686' 'pentium4' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://www.archlinux.org/pacman/"
license=('GPL-2.0-or-later')
depends=('pacman')
makedepends=('meson' 'musl' 'kernel-headers-musl' 'git')
options=('!emptydirs' '!lto')

# pacman
source=("git+https://gitlab.archlinux.org/pacman/pacman.git#tag=v${_git_tag}?signed"
        pacman-revertme-makepkg-remove-libdepends-and-libprovides.patch::https://gitlab.archlinux.org/pacman/pacman/-/commit/354a300cd26bb1c7e6551473596be5ecced921de.patch)

validpgpkeys=('6645B0A8C7005E78DB1D7864F99FFE0FEAE999BD'  # Allan McRae <allan@archlinux.org>
              'B8151B117037781095514CA7BBDFFC92306B1121') # Andrew Gregory (pacman) <andrew@archlinux.org>
# nghttp2
source+=("https://github.com/nghttp2/nghttp2/releases/download/v$_nghttp2_ver/nghttp2-$_nghttp2_ver.tar.xz")
# c-ares
source+=("https://github.com/c-ares/c-ares/releases/download/v${_cares_ver}/c-ares-${_cares_ver}.tar.gz"{,.asc})
validpgpkeys+=('27EDEAF22F3ABCEB50DB9A125CC908FDB71E12C2'  # Daniel Stenberg <daniel@haxx.se>
               'DA7D64E4C82C6294CB73A20E22E3D13B5411B7CA') # Brad House <brad@brad-house.com>
# curl
source+=("https://curl.haxx.se/download/curl-${_curlver}.tar.gz"{,.asc})
validpgpkeys+=('27EDEAF22F3ABCEB50DB9A125CC908FDB71E12C2') # Daniel Stenberg
# openssl
source+=("https://github.com/openssl/openssl/releases/download/openssl-${_sslver}/openssl-${_sslver}.tar.gz"{,.asc}
         "ca-dir.patch"
         "openssl-3.0.7-no-atomic.patch")
validpgpkeys+=('8657ABB260F056B1E5190839D9C4D26D0E604491'
              '7953AC1FBC3DC8B3B292393ED5E9E43F7DF9EE8C'
              'A21FAB74B0088AA361152586B8EF1A6BA9DA2D5C'
              'EFC0A467D613CB83C7ED6D30D894E2CE8B3D79F5'
              'BA5473A2B0587B07FB27CF2D216094DFD0CB81EF')

validpgpkeys+=('8657ABB260F056B1E5190839D9C4D26D0E604491'  # Matt Caswell <matt@openssl.org>
              '7953AC1FBC3DC8B3B292393ED5E9E43F7DF9EE8C'   # Matt Caswell <matt@openssl.org>
              'A21FAB74B0088AA361152586B8EF1A6BA9DA2D5C'   # Tom�? Mr�z <tm@t8m.info>
              'EFC0A467D613CB83C7ED6D30D894E2CE8B3D79F5')  # OpenSSL security team key
# zlib
source+=("https://zlib.net/zlib-${_zlibver}.tar.gz"{,.asc})
validpgpkeys+=('5ED46A6721D365587791E2AA783FCD8E58BCAFBA') # Mark Adler <madler@alumni.caltech.edu>
# xz
source+=("git+https://github.com/tukaani-project/xz#tag=v${_xzver}")
validpgpkeys+=('3690C240CE51B4670D30AD1C38EE757D69184620')  # Lasse Collin <lasse.collin@tukaani.org>
# bzip2
source+=("https://sourceware.org/pub/bzip2/bzip2-${_bzipver}.tar.gz"{,.sig})
validpgpkeys+=('EC3CFE88F6CA0788774F5C1D1AA44BE649DE760A') # Mark Wielaard <mark@klomp.org>
# zstd
source+=("https://github.com/facebook/zstd/releases/download/v${_zstdver}/zstd-${_zstdver}.tar.zst"{,.sig})
validpgpkeys+=('4EF4AC63455FC9F4545D9B7DEF8FE99528B52FFD') # Zstandard Release Signing Key <signing@zstd.net>
# libgpg-error
source+=("https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-${_gpgerrorver}.tar.bz2"{,.sig})
validpgpkeys+=('D8692123C4065DEA5E0F3AB5249B39D24F25E3B6'  # Werner Koch
               '031EC2536E580D8EA286A9F22071B08A33BD3F06'  # NIIBE Yutaka (GnuPG Release Key) <gniibe@fsij.org>
               '6DAA6E64A76D2840571B4902528897B826403ADA') # "Werner Koch (dist signing 2020)"
# libassuan
source+=("https://gnupg.org/ftp/gcrypt/libassuan/libassuan-${_libassuanver}.tar.bz2"{,.sig})
# gpgme
source+=("https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-${_gpgmever}.tar.bz2"{,.sig})
validpgpkeys+=('AC8E115BF73E2D8D47FA9908E98E9B2D19C6C8BD') #  Niibe Yutaka (GnuPG Release Key)
# libarchive
source+=("https://github.com/libarchive/libarchive/releases/download/v${_libarchive_ver}/libarchive-${_libarchive_ver}.tar.xz"{,.asc})
validpgpkeys+=('A5A45B12AD92D964B89EEE2DEC560C81CEC2276E'  # Martin Matuska <mm@FreeBSD.org>
              'DB2C7CF1B4C265FAEF56E3FC5848A18B8F14184B') # Martin Matuska <martin@matuska.org>

sha512sums=('44e00c2bc259fe6a85de71f7fd8a43fcfd1b8fb7d920d2267bd5b347e02f1dab736b3d96e31faf7b535480398e2348f7c0b9914e51ca7e12bab2d5b8003926b4'
            '1a108c4384b6104e627652488659de0b1ac3330640fc3250f0a283af7c5884daab187c1efc024b2545262da1911d2b0b7b0d5e4e5b68bb98db25a760c9f1fb1a'
            'b544196c3b7a55faacd11700d11e2fe4f16a7418282c9abb24a668544a15293580fd1a2cc5f93367c8a17c7ee45335c6d2f5c68a72dd176d516fd033f203eeec'
            'ddcda2f4c82ece7d670d0beb11485253a0f0db1f01131164e7253a20405c081844d2c69e366300c76ca0419a025e0fed516ee54314443afc39d55ce292354ad9'
            'SKIP'
            'b1dc36cfb40188d3a0f58d41968f69134e53803075b250e3e31579b8f680d9a083f3ad8f10c886a94fcd1b9b92873530ba6f73ca6ea41bbe07cb59d00918b066'
            'SKIP'
            '0784096f00c7907e477919d5ddeadb14b61bcb569a938fa739c1c714949214a7daf63574149d718dae372ed0c91c300042f4e3ba5e8633607e8034a3bda75a26'
            'SKIP'
            'b1873dbb7a49460b007255689102062756972de5cc2d38b12cc9f389b6be412da6797579b1acd3717a8cd2ee118fd9801b94e55f063d4328f050f0876a5eb53c'
            'b5887ea77417fae49b6cb1e9fa782d3021f268d5219701d87a092235964f73fa72a31428b630445517f56f2bb69dcbbb24119ef9dbf8b4e40a753369a9f9a16f'
            '580677aad97093829090d4b605ac81c50327e74a6c2de0b85dd2e8525553f3ddde17556ea46f8f007f89e435493c9a20bc997d1ef1c1c2c23274528e3c46b94f'
            'SKIP'
            '5dab9545bc63249c7716d40464f77b603a4255a91d65743d4fa8163e9819768c8a26b31dc783c1fb65904c954a6d5fd4a974420e4d599c7079828bdd3c78b593'
            '083f5e675d73f3233c7930ebe20425a533feedeaaa9d8cc86831312a6581cefbe6ed0d08d2fa89be81082f2a5abdabca8b3c080bf97218a1bd59dc118a30b9f3'
            'SKIP'
            '21f9da445afd76acaf3acb22d216c2b584d95e8c68e00f5cb3f6673f2d556dd14a7593344adf8ffd194bba3314387ee0e486d6248f6c935abca2edd8a4cf95ed'
            'SKIP'
            '4489f615c6a0389577a7d1fd7d3917517bb2fe032abd9a6d87dfdbd165dabcf53f8780645934020bf27517b67a064297475888d5b368176cf06bc22f1e735e2b'
            'SKIP'
            '7c5c95c1b85bef2d4890c068a5a8ea8a1fe0d8def6ab09e5f34fc2746d8808bbb0fc168e3bd66d52ee5ed799dcf9f258f4125cda98c8384f6411bcad8d8b3139'
            'SKIP'
            'f9d3786f27eaf88b6544a453e4b0f800cf2259d5321bf387bd1978c5ba5824b3746d28af4ec5491502cd4d5c776361805b75cb02d9bbbae26cf2a8fcfd86b871'
            'SKIP'
            '2524f71f4c2ebc254a1927279be3394e820d0a0c6dec7ef835a862aa08c35756edaa4208bcdc710dd092872b59c200b555b78670372e2830822e278ff1ec4e4a'
            'SKIP')

export LDFLAGS="$LDFLAGS -static"
export CC=musl-gcc
export CXX=musl-gcc

# https://www.openwall.com/lists/musl/2014/11/05/3
# fstack-protector and musl do not get along but only on i686
if [[ $CARCH = i686 || $CARCH = pentium4 || $CARCH = i486 ]]; then
    # silly build systems have configure checks or buildtime programs that don't CFLAGS but do do CC
    export CC="musl-gcc -fno-stack-protector"
    export CXX="musl-gcc -fno-stack-protector"
    export CFLAGS="${CFLAGS/-fstack-protector-strong/}"
    export CXXFLAGS="${CXXFLAGS/-fstack-protector-strong/}"
fi

# to enable func64 interface in musl for 64-bit file system functions
export CFLAGS+=' -D_LARGEFILE64_SOURCE'
export CXXFLAGS+=' -D_LARGEFILE64_SOURCE'

# keep using xz-compressed packages, because one use of the package is to
# recover on systems with broken zstd support in libarchive
[[ $PKGEXT = .pkg.tar.zst ]] && PKGEXT=.pkg.tar.xz

prepare() {
    cd "${srcdir}/pacman"

    # apply patch level commits on top of annotated tag for pacman
    if [[ -n ${_git_patch_level_commit} ]]; then
        if [[ v${_git_tag} != $(git describe --tags --abbrev=0 "${_git_patch_level_commit}") ]] then
            error "patch level commit ${_git_patch_level_commit} is not a descendant of v${_git_tag}"
            exit 1
        fi
        git rebase "${_git_patch_level_commit}"
    fi

    # handle local pacman patches
    local -a patches
    patches=($(printf '%s\n' "${source[@]}" | grep 'pacman-.*.patch'))
    patches=("${patches[@]%%::*}")
    patches=("${patches[@]##*/}")

    if (( ${#patches[@]} != 0 )); then
        for patch in "${patches[@]}"; do
            if [[ $patch =~ revertme-* ]]; then
                msg2 "Reverting patch $patch..."
                patch -RNp1 < "../$patch"
            else
                msg2 "Applying patch $patch..."
                patch -Np1 < "../$patch"
            fi
        done
    fi

    # openssl
    cd "${srcdir}"/openssl-${_sslver}
    patch -Np1 -i "${srcdir}/ca-dir.patch"
    case ${CARCH} in
        arm|armv6h|armv7h)
            # special patch to omit -latomic when installing pkgconfig files
            msg2 "Applying openssl patch openssl-3.0.7-no-atomic.patch..."
            patch -Np1 -i "${srcdir}/openssl-3.0.7-no-atomic.patch"
    esac
}

build() {
    export PKG_CONFIG_PATH="${srcdir}"/temp/usr/lib/pkgconfig
    export PATH="${srcdir}/temp/usr/bin:${PATH}"

    # openssl
    cd "${srcdir}"/openssl-${_sslver}
    case ${CARCH} in
        x86_64)
            openssltarget='linux-x86_64'
            optflags='enable-ec_nistp_64_gcc_128'
            ;;
        pentium4)
            openssltarget='linux-elf'
            optflags=''
            ;;
        i686)
            openssltarget='linux-elf'
            optflags='no-sse2'
            ;;
        i486)
            openssltarget='linux-elf'
            optflags='386 no-threads'
            ;;
        arm|armv6h|armv7h)
            openssltarget='linux-armv4'
            optflags=''
            ;;
        aarch64)
            openssltarget='linux-aarch64'
            optflags='no-afalgeng'
            ;;
    esac
    # mark stack as non-executable: http://bugs.archlinux.org/task/12434
    ./Configure --prefix="${srcdir}"/temp/usr \
                --openssldir=/etc/ssl \
                --libdir=lib \
                -static \
                no-ssl3-method \
                ${optflags} \
                "${openssltarget}" \
                "-Wa,--noexecstack ${CPPFLAGS} ${CFLAGS} ${LDFLAGS}"
    make build_libs
    make install_dev

    # xz
    cd "${srcdir}"/xz
    ./autogen.sh --no-po4a --no-doxygen
    ./configure --prefix="${srcdir}"/temp/usr \
                --disable-shared
    cd src/liblzma
    make
    make install

    # bzip2
    cd "${srcdir}"/bzip2-${_bzipver}
    sed -i "s|-O2|${CFLAGS}|g;s|CC=gcc|CC=${CC}|g" Makefile
    make libbz2.a
    install -Dvm644 bzlib.h "${srcdir}"/temp/usr/include/
    install -Dvm644 libbz2.a "${srcdir}"/temp/usr/lib/

    cd "${srcdir}"/zstd-${_zstdver}/lib
    make libzstd.a
    make PREFIX="${srcdir}"/temp/usr install-pc install-static install-includes

    # zlib
    cd "${srcdir}/"zlib-${_zlibver}
    ./configure --prefix="${srcdir}"/temp/usr \
                --static
    make libz.a
    make install

    # libarchive
    cd "${srcdir}"/libarchive-${_libarchive_ver}
    CPPFLAGS="-I${srcdir}/temp/usr/include" CFLAGS="-L${srcdir}/temp/usr/lib" \
        ./configure --prefix="${srcdir}"/temp/usr \
                    --without-xml2 \
                    --without-nettle \
                    --disable-{bsdtar,bsdcat,bsdcpio,bsdunzip} \
                    --without-expat \
                    --disable-shared
    make
    make install-{includeHEADERS,libLTLIBRARIES,pkgconfigDATA,includeHEADERS}

    # nghttp2
    cd "${srcdir}"/nghttp2-${_nghttp2_ver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared \
        --disable-examples \
        --disable-python-bindings
    make -C lib
    make -C lib install

    # c-ares
    # needed for curl, which does not use it in the repos
    # but seems to be needed for static builds
    cd "${srcdir}"/c-ares-${_cares_ver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared
    make -C src/lib
    make install-pkgconfigDATA
    make -C src/lib install
    make -C include install

    # curl
    cd "${srcdir}"/curl-${_curlver}
    # c-ares is not detected via pkg-config :(
    ./configure --prefix="${srcdir}"/temp/usr \
                --disable-shared \
                --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
                --disable-{dict,gopher,imap,ldap,ldaps,manual,pop3,rtsp,smb,smtp,telnet,tftp} \
                --without-{brotli,libidn2,librtmp,libssh2,libpsl} \
                --disable-libcurl-option \
                --with-openssl \
                --enable-ares="${srcdir}"/temp/usr
    make -C lib
    make install-pkgconfigDATA
    make -C lib install
    make -C include install

    # libgpg-error
    cd "${srcdir}"/libgpg-error-${_gpgerrorver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared
    make -C src
    make -C src install-{binSCRIPTS,libLTLIBRARIES,nodist_includeHEADERS,pkgconfigDATA}

    # libassuan
    cd "${srcdir}"/libassuan-${_libassuanver}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-shared
    make -C src
    make -C src install-{binSCRIPTS,libLTLIBRARIES,nodist_includeHEADERS,pkgconfigDATA}

    # gpgme
    cd "${srcdir}"/gpgme-${_gpgmever}
    ./configure --prefix="${srcdir}"/temp/usr \
        --disable-fd-passing \
        --disable-shared \
        --disable-languages
    make -C src
    make -C src install-{binSCRIPTS,libLTLIBRARIES,nodist_includeHEADERS,pkgconfigDATA}

    # ew libtool
    rm "${srcdir}"/temp/usr/lib/lib*.la

    # Finally, it's a pacman!
    mkdir -p "${srcdir}"/pacman
    cd "${srcdir}"/pacman
    meson --prefix=/usr \
        --includedir=lib/pacman/include \
        --libdir=lib/pacman/lib \
        --buildtype=plain \
        -Dbuildstatic=true \
        -Ddefault_library=static \
        -Ddoc=disabled \
        -Ddoxygen=disabled \
        -Dldconfig=/usr/bin/ldconfig \
        -Dscriptlet-shell=/usr/bin/bash \
        build
    meson compile -C build
}

package() {
    cd "${srcdir}"/pacman
    DESTDIR="${pkgdir}" meson install -C build

    rm -rf "${pkgdir}"/usr/share "${pkgdir}"/etc
    for exe in "${pkgdir}"/usr/bin/*; do
        if [[ -f ${exe} && $(head -c4 "${exe}") = $'\x7fELF' ]]; then
            mv "${exe}" "${exe}"-static
        else
            rm "${exe}"
        fi
    done

    cp -a "${srcdir}"/temp/usr/{bin,include,lib} "${pkgdir}"/usr/lib/pacman/
    sed -i "s@${srcdir}/temp/usr@/usr/lib/pacman@g" \
        "${pkgdir}"/usr/lib/pacman/lib/pkgconfig/*.pc \
        "${pkgdir}"/usr/lib/pacman/bin/*
}
