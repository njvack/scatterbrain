#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


PACKAGE_NAME='scatterbrain'

with open("README.md", "r") as f:
    long_description = f.read()

def get_locals(filename):
    l = {}
    with open(filename, 'r') as f:
        code = compile(f.read(), filename, 'exec')
        exec(code, {}, l)
    return l


metadata = get_locals(os.path.join('src', PACKAGE_NAME, '_metadata.py'))


requirements = [
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name=PACKAGE_NAME,
    version=metadata['version'],
    description='Tools for organizing the variables of interest in a study',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Nate Vack',
    author_email='njvack@wisc.edu',
    url=f'https://github.com/njvack/{PACKAGE_NAME}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='neuroscience statisics fishing demo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)