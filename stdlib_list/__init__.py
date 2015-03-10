from _version import __version__

import os
import csv


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


def metadata(version):

    version = get_canonical_version(version)

    lib_file = os.path.join(data_dir, "{}.csv".format(version))

    result = {}

    with open(lib_file) as f:
        reader = csv.DictReader(f)

        for row in reader:
            module = row["module"]
            result[module] = {
                x: row[x]
                for x in ["os", "description", "deprecated"]
            }

            if result[module]["deprecated"] == "":
                result[module]["deprecated"] = None
            else:
                result[module]["deprecated"] = int(
                    result[module]["deprecated"])

    return result


def stdlib_list(version, os=None, deprecated=None,
                max_module_level=None):

    module_data = metadata(version)

    if os:
        module_data = {x: y for x, y in module_data.items() if y["os"] == os}

    if deprecated is not None:
        module_data = {
            x: y for x, y in module_data.items()
            if bool(y["deprecated"]) == bool(deprecated)
        }

    if max_module_level:
        module_data = {
            x: y for x, y in module_data.items()
            if len(x.split(".")) <= max_module_level
        }

    return sorted(module_data.keys())

import scraper
