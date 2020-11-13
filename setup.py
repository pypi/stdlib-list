import os

from setuptools import find_packages, setup

import versioneer

rootpath = os.path.dirname(os.path.abspath(__file__))


def read(*parts):
    return open(os.path.join(rootpath, *parts), "r").read()


setup(
    name="stdlib-list",
    license="MIT",
    author="Jack Maney",
    author_email="jackmaney@gmail.com",
    url="https://github.com/jackmaney/python-stdlib-list",
    version=versioneer.get_version(),
    install_requires=["functools32;python_version<'3.2'"],
    extras_require={"develop": ["sphinx"]},
    description="A list of Python Standard Libraries (2.6-7, 3.2-9).",
    long_description="{}".format(read("README.md")),
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(exclude=["tests", "tests.*"]),
    cmdclass=versioneer.get_cmdclass(),
)
