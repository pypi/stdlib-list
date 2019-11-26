from setuptools import setup, find_packages

import versioneer


setup(
    name="stdlib-list",
    license="MIT",
    author="Jack Maney",
    author_email="jackmaney@gmail.com",
    url="https://github.com/jackmaney/python-stdlib-list",
    version=versioneer.get_version(),
    install_requires=["functools32;python_version<'3.2'"],
    extras_require={"develop": ["sphinx"]},
    description="A list of Python Standard Libraries (2.6-7, 3.2-8).",
    long_description=f'{read("README.md")}',
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(),
    cmdclass=versioneer.get_cmdclass(),
)
