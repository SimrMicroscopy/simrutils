#! /usr/bin/env python
import setuptools

DESCRIPTION = "common utilities"

URL = 'https://github.com/SimrMicroscopy/simrutils'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/SimrMicroscopy/simrutils'
VERSION = '0.0.1'
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'numpy>=1.15',
    'scipy>=1.0',
    'pandas>=0.23',
    'matplotlib>=2.2',
    'nd2reader>=3.2.3',
    'tifffile>=2020.7.24',
]


if __name__ == "__main__":
    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, 6):
        raise RuntimeError("seaborn requires python >= 3.6.")

    setup(
        name='simr-utils',
        author="Chris Wood",
        author_email="cjw@stowers.org",
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=setuptools.find_packages(),
    )
