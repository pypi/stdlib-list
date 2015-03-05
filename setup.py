import setuptools
from stdlib_list import __version__


try:
    with open('README.rst') as f:
        long_description = f.read()
except IOError:
    long_description = ""
try:
    with open("'requirements.txt'") as f:
        requirements = [x for x in [y.strip() for y in f.readlines()] if x]
except IOError:
    requirements = []


setuptools.setup(
    name='stdlib-list',
    license='MIT',
    author='Jack Maney',
    author_email='jackmaney@gmail.com',
    url='https://github.com/jackmaney/python-stdlib-list',
    version=__version__,
    install_requires=requirements,
    description='A list of Python Standard Libraries (2.6-7, 3.2-4).',
    long_description=long_description,
    include_package_data=True,
    packages=setuptools.find_packages()
)
