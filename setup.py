#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description…
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gitcal",
    version = "0.0.1",
    author = "Eric Schrijver / OSP",
    author_email = "mail@osp.constantvzw.org",
    description = ("Create an iCalendar file based on the commits in a git repository."),
    license = "AGPLv3",
    keywords = "git calendar osp visualisation visualization icalendar",
    url = "http://osp.constantvzw.org/tools/gitcal/",
    packages=['gitcal'],
    long_description=read('README.txt'),
    classifiers=[
        "Environment :: Web Environment,
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    requires = ['vobject==0.8.1c']
)

