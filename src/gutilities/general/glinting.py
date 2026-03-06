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
from pylint.reporters.text import TextReporter


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_parameters(
    items: Union[list, tuple],
    path: Union[None, Path, str],
    recursive: bool
) -> tuple:
    """
        From the given parameters, gets the adequated and converted parameters.

        :param items: The list or tuple with the objects to be linted; all
         the objects must be strings, and must represent paths.

        :param path: The path where the results of linting will be saved.

        :param recursive: A boolean flag indicating whether the files must be
         recursively checked, in the case that a directory is passed. True,
         if directories must be recursively linted; False, otherwise.

        :return: A tuple with the corrected paths of the directories and files
         to be linted, the path
    """
    # Set the path.
    root: Path = Path.cwd()

    if isinstance(path, (Path, str)):
        root = path if isinstance(path, Path) else Path(path)

    # Auxiliary variables.
    files: set = set()

    for item in items:
        # Append the file.
        if Path(item).is_file():
            files.add(item)
            continue

        # Get the files.
        function: callable = Path(item).rglob if recursive else Path(item).glob
        files = files.union(f"{x}" for x in function("*") if x.suffix == ".py")

    # Get the proper file path.
    file: Path = root

    if root.is_dir():
        counter: int = 0
        file = root / "results_pylint.txt"

        while file.is_file():
            file = root / f"results_pylint({counter}).txt"
            counter += 1

    return f"{file}", sorted(files, key=lambda x: x.lower())


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

    if not (path is None or isinstance(path, (Path, str))):
        message += "The \"path\" must be None, a Path, or a string. "

    if not isinstance(recursive, bool):
        message += "The \"recursive\" must be a boolean value. "

    # Raise an error if needed.
    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def lint_flak8(
    items: Union[list, tuple],
    path: Union[None, Path, str] = None,
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
    _parameters_linting(items, path, recursive)

    # Set the path.
    root: Path = Path.cwd()

    if isinstance(path, (Path, str)):
        root = path if isinstance(path, Path) else Path(path)


def lint_pylint(
    items: Union[list, tuple],
    path: Union[None, Path, str] = None,
    recursive: bool = False,
) -> None:
    """
        Lints the given dictory with Pylint.

        :param items: The list or tuple with the objects to be linted; all
         the objects must be strings, and must represent paths.

        :param path: The path where the results of linting will be saved.

        :param recursive: A boolean flag indicating whether the files must be
         recursively checked, in the case that a directory is passed. True,
         if directories must be recursively linted; False, otherwise.
    """
    # Validate the parameters.
    _parameters_linting(items, path, recursive)

    # Get the path where the results must be saved and the files to lint.
    file, files = _get_parameters(items, path, recursive)

    # Run the linter.
    with open(file, encoding="utf-8", mode="w") as stream:
        reporter: TextReporter = TextReporter(stream)

        Run(
            sorted(files, key=lambda x: x.lower()),
            exit=False,
            reporter=reporter
        )

    # Message to the user.
    print(f"Pylint saved the linting results in the file: {file}")


# #############################################################################
# TO DELETE!
# #############################################################################

def run() -> None:
    """
        Runs the main program.
    """
    # Set the directory to the source directory.
    directory: Path = Path(__file__).parent.parent.parent
    files: list = []

    lint_pylint([f"{directory}"], recursive=True)

if __name__ == "__main__":
    run()
