# Test Package
Testing package for pip install

### Resources to building a package
https://docs.python.org/3/distutils/setupscript.html

### How to install this package
```bash
pip install git+https://github.com/jhevrin2/test-package.git
```

### How to get your package to PyPI

Good link to help with building your own PyPI package:  https://packaging.python.org/tutorials/packaging-projects/

```bash
pip install --upgrade build
pip install --upgrade twine
python -m build
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ --no-deps jhevrin2_dostuff
```

### Try out the package

```python
from dostuff.communicate import create_greeting
create_greeting(name='Jeff')
```

### Link to PyPI Package
https://test.pypi.org/project/jhevrin2-dostuff/