from ._version import __version__


import os

base_dir = os.path.dirname(os.path.realpath(__file__))
list_dir = os.path.join(base_dir, "lists")

long_versions = ["2.6.9", "2.7.9", "3.2.6", "3.3.6", "3.4.3", "3.5"]

short_versions = [".".join(x.split(".")[:2]) for x in long_versions]


def get_canonical_version(version):

    if version in long_versions:
        version = ".".join(version.split(".")[:2])
    elif version not in short_versions:
        raise ValueError("No such version: {}".format(version))

    return version


from .base import stdlib_list
