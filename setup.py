import setuptools 


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
    name='python-stdlib-list',
    license='MIT',
    author='Jack Maney',
    author_email='jackmaney@gmail.com',
    url='https://github.com/jackmaney/python-stdlib-list',
    version='0.0.0',
    install_requires=requirements,
    description='Scraping the Python Docs for the names of all the standard libraries.',
    long_description=long_description
)
