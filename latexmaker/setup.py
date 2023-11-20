"""
    File that contains the setup for the latexmaker package.
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
    "pyyaml==6.0.1",
]


# ##############################################################################
# Setup
# ##############################################################################


setup(
    author="Andres Garcia Escovar",
    author_email="andrumen@hotmail.com",
    install_requires=REQUIRED,
    packages=["latexmaker"],
    package_data={"latexmaker": ["**.yaml"]},
    package_dir={"latexmaker": "src/latexmaker"},
    name="latexmaker",
    version="1.0.0",
)
