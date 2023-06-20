# stdlib-list

This package includes lists of all of the standard libraries for Python 2.6,
2.7, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, and 3.9 along with the code for
scraping the official Python docs to get said lists.

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

For more details, check out [the docs](http://python-stdlib-list.readthedocs.org/en/latest/).

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
