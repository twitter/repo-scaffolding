#!/usr/bin/env python
"""
Copyright 2018 Twitter, Inc.
SPDX-License-Identifier: Apache-2.0
"""

from setuptools import setup

setup(
    name="add_license_headers",
    version="0.1",
    description="Add license headers to all the source files",
    author="TwitterOSS",
    author_email="opensource@twitter.com",
    url="https://github.com/twitter/repo-scaffolding",
    py_modules=['add_license_headers'],
    entry_points = {
        'console_scripts': [
            'add_license_headers = add_license_headers:entry'
        ],
    },
    )
