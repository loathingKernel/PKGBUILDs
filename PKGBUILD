# Maintainer: Daniel M. Capella <polyzen@archlinux.org>

_name=aiohttp_cors
pkgname=python-aiohttp-cors
pkgver=0.8.1
pkgrel=1
pkgdesc='CORS support for aiohttp'
depends=('python-aiohttp')
makedepends=('python-setuptools')
arch=('any')
url=https://github.com/aio-libs/aiohttp-cors
license=('Apache')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('ccacf9cb84b64939ea15f859a146af1f662a6b1d68175754a07315e305fb1403')

build() {
  cd $_name-$pkgver
  python setup.py build
}

package() {
  cd $_name-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
