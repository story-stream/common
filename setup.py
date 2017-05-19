#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

packages = find_packages(exclude=['ex_setup'])

setup(
    name='common',
    version='1.2.2.1',
    author='StoryStream',
    author_email='hello@storystream.it',
    description='A set of common libraries and utilities that are used across the StoryStream infrastructure.',
    url='https://bitbucket.org/rhayesbite/common/',
    packages=packages,
    install_requires=required,
    zip_safe=False
)
