"""
    File that contains the setup for the latex_maker package.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General.
from setuptools import setup


# ##############################################################################
# Global Variables
# ##############################################################################


REQUIRED: list = [
    "pyyaml==6.0",
]


# ##############################################################################
# Setup
# ##############################################################################


setup(
    author="Andres Garcia Escovar",
    author_email="andrumen@hotmail.com",
    install_requires=REQUIRED,
    package_data={"": ["**.yaml"]},
    package_dir={"": "src"},
    name="latex_maker",
    version="0.0.1",
)