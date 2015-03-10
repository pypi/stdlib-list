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
    """
    Given a ``version``, returns a ``dict``

    * Whose keys are module names for all of the standard libraries for the given version of Python, and

    * Whose values are dicts with the following keys:

      * ``"description"``: A brief description of the library
      * ``"os"``: Which OS the library is aimed at (or ``None`` if not applicable).
      * ``"deprecated"``: Either ``None`` or 1 depending on whether or not the listed module is deprecated (I use ``None``/1 instead of ``True``/``False`` to save a bit of space in the CSV files that store the data).

    :param version: The version (major and minor) of Python for which you want a list of standard libraries.
    :type version: one of ``"2.6"``, ``"2.7"``, ``"3.2"``, ``"3.3"``, or ``"3.4"``
    :return: The ``dict`` described above.
    :rtype: dict
    """

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
    """
    Given a ``version``, return a ``list`` of names of the Python Standard Libraries for that version. These names have been scraped from the Python Module Index (for example, `here <https://docs.python.org/2.7/py-modindex.html#cap-n>`_ is the module index for Python 2.7).

    :param version: The version (major and minor) of Python for which you want a list of standard libraries.
    :type version: one of ``"2.6"``, ``"2.7"``, ``"3.2"``, ``"3.3"``, or ``"3.4"``

    :param os: If this is set, return only modules designated for this OS (eg ``"Mac"``, ``"Windows"``, etc).
    :type os: string or None

    :param deprecated: If this parameter is true, only deprecated libraries will be included, if it is false and not `None`, only non-deprecated libraries will be included, and if it is ``None``, deprecated and non-deprecated libraries will be included.
    :type deprecated: bool or None

    :param max_module_level: Sets the maximum level of depth for nested modules. For example, ``xml.dom.minidom`` is a Python standard library, but if ``max_module_level`` is set to 1 or 2, then ``xml.dom.minidom`` won't show up in the resulting list.
    :type max_module_level: positive int or None

    :return: A list of standard libraries from the specified version of Python with the above specified conditions applied.
    :rtype: list
    """

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
