from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='fabric-digitalocean',
    version='0.1',
    description='A collection of fabric tools for working with DigitalOcean',
    long_description=long_description,
    url='https://github.com/andrewsomething/fabric-digitalocean',
    download_url='https://github.com/andrewsomething/fabric-digitalocean/releases',
    license='BSD-2-Clause',

    author='Andrew Starr-Bochicchio',
    author_email='a.starr.b@gmail.com',

    packages=find_packages(),
    install_requires=['fabric', 'python-digitalocean', 'retry'],
    extras_require={
        'test': ['nose', 'coverage', 'responses']
    },
)
