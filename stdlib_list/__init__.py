from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

# Import all the things that used to be in here for backwards-compatibility reasons
from .base import stdlib_list, get_canonical_version, short_versions, long_versions, base_dir, list_dir
