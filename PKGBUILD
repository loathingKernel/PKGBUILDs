# Maintainer: Otreblan <otreblain@gmail.com>

# Remember to activate multilib for proton.
# It's dependencies requiere to be build in this order:
# wine -> vkd3d-valve -> wine-valve -> proton
pkgname=legendary
pkgver=0.20.15
pkgrel=1
pkgdesc="A free and open-source replacement for the Epic Games Launcher "
arch=('any')
url="https://github.com/derrod/legendary"
license=('GPL3')
groups=()
depends=("python-requests" "python-wheel" "python-setuptools")
makedepends=()
checkdepends=()
optdepends=(
	"proton: Windows binaries support"
	"python-pywebview: Login support"
	"python-cairo: Login support (gtk)"
	"python-gobject: Login support (gtk)"
	"webkit2gtk: Login support (gtk)"
)
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
noextract=()
sha256sums=('2feeaaa76e905ea4275d12cb336aaa53183bb20f997ed0dced9800869ee526f9')

build() {
	cd "$srcdir/$pkgname-$pkgver"

	python setup.py build
}

package() {
	cd "$srcdir/$pkgname-$pkgver"

	python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}
