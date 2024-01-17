# Maintainer: Shae VanCleave

pkgname=python-pywebview
pkgver=4.4.1
pkgrel=1
pkgdesc="Build GUI for your Python program with JavaScript, HTML, and CSS."
arch=('any')
url='https://github.com/r0x0r/pywebview'
license=('BSD')
depends=('python' 'python-proxy_tools' 'python-bottle')
makedepends=('python-build' 'python-installer' 'python-setuptools-scm' 'python' 'python-wheel')
optdepends=('python-gobject: use with GTK'
            'python-cairo: use with GTK'
            'webkit2gtk>=2.22: use with GTK'
            'qt5-webkit: use with Qt'
            'python-qtpy: use with Qt'
            'python-pyqt5-webengine: use with Qt (PyQt5)'
            'python-pyqt5: use with Qt (PyQt5)'
            'pyside2: use with Qt (PySide2)'
            'pyside6: use with Qt (PySide6)')
install="$pkgname.install"
source=("https://pypi.python.org/packages/source/p/pywebview/pywebview-$pkgver.tar.gz"
        "https://raw.githubusercontent.com/r0x0r/pywebview/master/LICENSE")
sha256sums=('ea4c517e9265fadfd77937facb67787c07425d303b00b9d5c3a401bbb4576941'
            '4a988dd3598832cd3653de20dc33cb677d0fb53ab5551c879ca31280ae653675')

build() {
    cd "${srcdir}/pywebview-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}"
    install -Dm 644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    cd "pywebview-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
