from _version import __version__

import os


long_versions = ["2.6.9", "2.7.9", "3.2.6", "3.3.6", "3.4.3"]

short_versions = [".".join(x.split(".")[:2]) for x in long_versions]

base_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(base_dir, "lists")


def get_canonical_version(version):

    if version in long_versions:
        version = ".".join(version.split(".")[:2])
    elif version not in short_versions:
        raise ValueError("No such version: {}".format(version))

    return version


def stdlib_list(version):

    version = get_canonical_version(version)

    lib_file = os.path.join(data_dir, "{}.txt".format(version))

    with open(lib_file) as f:
        result = [x.strip() for x in f.readlines()]

    return result

import scraper
