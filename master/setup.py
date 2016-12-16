#!/usr/bin/env python

{{ generated_file_note }}

from setuptools import setup, find_packages

setup(
    name='{{package}}',
    version='{{version}}',
    description='{{description}}',
    author='{{author}}',
    author_email='{{email}}',
    url='{{url}}',
    packages=find_packages(exclude=["test*"]),
    install_requires=[
        ## for p in install_requires:
        '{{p}}',
        ## endfor
    ],
    extras_require={
        ## if extras_require
        ## for key, value in extras_require | dictsort
        '{{key}}': {{value}},
        ## endfor
        ## endif
    },
    entry_points={
        'console_scripts': [
            ## if console_scripts
            ## for key, value in console_scripts | dictsort
            '{{key}}={{value}}',
            ## endfor
            ## endif
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    include_package_data=True,
)
