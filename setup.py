# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='timologio_eu',
    version=version,
    description='Timologio Theme',
    author='GAM LTD',
    author_email='info@gam.gr',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
