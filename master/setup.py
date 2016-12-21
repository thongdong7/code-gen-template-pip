#!/usr/bin/env python

{{ generated_file_note }}

from setuptools import setup, find_packages

setup(
    name='{{package}}',
    version='{{version}}{{version_dev|default('')}}',
    description='{{description}}',
    author='{{author}}',
    author_email='{{email}}',
    url='{{url}}',
    packages=find_packages(exclude=["test*"]),
    install_requires=[
        ## for p in install_requires
        '{{p}}',
        ## endfor
    ],
    extras_require={
        ## for key in extras_require:
        '{{key}}': {{extras_require[key]}},
        ## endfor
    },
    entry_points={
        'console_scripts': [
            ## for key in console_scripts:
            '{{key}}={{console_scripts[key]}}',
            ## endfor
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
