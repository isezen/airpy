"""
airpy
~~~~~~~~~
Air Quality Measurements Database for Turkey
"""
# pylint: disable=C0103
import os
from glob import glob
from setuptools import setup
# import fastentrypoints


def get(x):
    """ Get something """
    with open(os.path.join(os.path.dirname(__file__),
                           'airpy', '__init__.py')) as f:
        for line in f.readlines():
            if line.startswith('__' + x + '__'):
                return line.split('=')[1].strip()[1:-1]
    return None


def get_requirements():
    """ Some gode string"""
    requirements = ['pandas']
    return requirements


setup(
    name='airpy',
    version=get('version'),
    platforms=['linux', 'darwin', 'windows'],
    packages=['airpy'],
    package_dir={'airpy': 'airpy'},
    include_package_data=True,
    setup_requires=['pytest-runner'],
    install_requires=get_requirements(),
    tests_require=['pytest'],
    scripts=['airpy-create-db'],
    author=get('author'),
    author_email=get('email'),
    description='Air Quality Measurements Database for Turkey',
    long_description=__doc__,
    license=get('license'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Any",
        "License :: OSI Approved :: AGPL v3.0 License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    keywords=['data', 'environment', 'pollutant', 'turkey'],
    url='https://github.com/isezen/airpy',
)