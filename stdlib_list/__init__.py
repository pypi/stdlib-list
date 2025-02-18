__version__ = "0.11.1"

# Import all the things that used to be in here for backwards-compatibility reasons
from .base import (
    get_canonical_version,
    in_stdlib,
    long_versions,
    short_versions,
    stdlib_list,
)

__all__ = [
    "stdlib_list",
    "in_stdlib",
    "get_canonical_version",
    "short_versions",
    "long_versions",
]
