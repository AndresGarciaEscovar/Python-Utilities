"""
    Contains the functions for linting, in particular Flake8 and Pylint.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from pathlib import Path
from typing import Any, Union

# Third party.
import flake8.api.legacy as flake8

from pylint.lint import Run


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _parameters_linting(objects: Any, path: Any, recursive: Any) -> None:
    """
        Validates the parameters for linting. This is useful for both Pylint
        and Flake8. The recursive parameter will only be considered if there
        are any directories.

        :param objects: The list or tuple with the objects to be linted; all
         the objects must be strings, and must represent paths.

        :param path: The path where the results of linting will be saved.

        :param recursive: A boolean flag indicating whether the files must be
         recursively checked, in the case that a directory is passed. True,
         if directories must be recursively linted; False, otherwise.

        :raise ValueError: If any of the parameters are NOT valid; either in
         type or in value.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the types.
    if not isinstance(objects, (list, tuple)):
        message += "The \"objects\" must be a list or a tuple. "

    if not isinstance(path, str):
        message += "The \"path\" must be a string. "

    if not isinstance(recursive, bool):
        message += "The \"recursive\" must be a boolean value. "

    # Raise an error if needed.
    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def lint_flak8(
    objects: Union[list, tuple],
    path: Union[Path, str],
    recursive: bool = False,
) -> None:
    """
        Lints the given dictory with Flake8.

        :param objects: The list or tuple with the objects to be linted; all
         the objects must be strings, and must represent paths.

        :param path: The path where the results of linting will be saved.

        :param recursive: A boolean flag indicating whether the files must be
         recursively checked, in the case that a directory is passed. True,
         if directories must be recursively linted; False, otherwise.
    """
    # Validate the parameters.
    _parameters_linting(objects, path, recursive)


def lint_pylint(
    objects: Union[list, tuple],
    path: Union[Path, str],
    recursive: bool = False,
) -> None:
    """
        Lints the given dictory with Pylint.

        :param objects: The list or tuple with the objects to be linted; all
         the objects must be strings, and must represent paths.

        :param path: The path where the results of linting will be saved.

        :param recursive: A boolean flag indicating whether the files must be
         recursively checked, in the case that a directory is passed. True,
         if directories must be recursively linted; False, otherwise.
    """
    # Validate the parameters.
    _parameters_linting(objects, path, recursive)


# import sys
# from pylint.lint import Run

# # Optional: capture output instead of printing to standard out
# class WritableObject:
#     def __init__(self):
#         self.content = []
#     def write(self, st):
#         self.content.append(st)
#     def read(self):
#         return self.content

# pylint_output = WritableObject()

# # Arguments to pass to Pylint:
# # Pass the directory path (e.g., '.') and the --recursive=y flag.
# # Note: The recursive flag might behave differently depending on the pylint version.
# # A robust method might be to list files explicitly (see Method 2).
# pylint_args = ['.', '--recursive=y']

# # Run Pylint
# # 'exit=False' prevents the program from exiting if linting errors are found.
# # The 'reporter' argument can be used to redirect the output.
# Run(pylint_args, reporter=TextReporter(pylint_output), exit=False)

# # Process the output
# for line in pylint_output.read():
#     print(line)
