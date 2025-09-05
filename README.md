# stdlib-list

[![PyPI version](https://badge.fury.io/py/stdlib-list.svg)](https://badge.fury.io/py/stdlib-list)
[![Downloads](https://static.pepy.tech/badge/stdlib-list)](https://pepy.tech/project/stdlib-list)
[![CI](https://github.com/pypi/stdlib-list/actions/workflows/ci.yml/badge.svg)](https://github.com/pypi/stdlib-list/actions/workflows/ci.yml)

This package includes lists of all of the standard libraries for Python 2.6
through 3.14.

**IMPORTANT**: If you're on Python 3.10 or newer, you **probably don't need this library**.
See [`sys.stdlib_module_names`](https://docs.python.org/3/library/sys.html#sys.stdlib_module_names)
and [`sys.builtin_module_names`](https://docs.python.org/3/library/sys.html#sys.builtin_module_names)
for similar functionality.

## Installation

`stdlib-list` is available on PyPI:

```bash
python -m pip install stdlib-list
```

## Usage

```python
>>> from stdlib_list import stdlib_list
>>> libraries = stdlib_list("2.7")
>>> libraries[:10]
['AL', 'BaseHTTPServer', 'Bastion', 'CGIHTTPServer', 'ColorPicker', 'ConfigParser', 'Cookie', 'DEVICE', 'DocXMLRPCServer', 'EasyDialogs']
```

For more details, check out [the docs](https://pypi.github.io/stdlib-list/).

## Credits and Project History

This library was created by [@jackmaney](https://github.com/jackmaney),
and was maintained with the help of [@ocefpaf](https://github.com/ocefpaf) and
[@ericdill](https://github.com/ericdill) until
[version 0.8.0](https://github.com/pypi/stdlib-list/releases/tag/v0.8.0),
after which the primary maintainer
[archived the project](https://github.com/pypi/stdlib-list/commit/7bc9a32789221b4e23edcb6a2c1466e8234aabbb).

With the primary maintainer's approval, the project was transferred
from `jackmaney/python-stdlib-list` to `pypi/stdlib-list`, and was adopted
by new maintainers.

The README immediately prior to the maintainership transfer is
preserved at [`READMD.md.old`](./README.md.old).
