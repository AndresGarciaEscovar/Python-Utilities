"""
    Contains the functions for linting, in particular Flake8 and Pylint.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from typing import Any, Callable, Union

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
    recursive: bool,
    isflake: Any
) -> tuple:
    """
        From the given parameters, gets the adequated and converted parameters.

        :param items: The list or tuple with the objects to be linted; all
         the objects must be strings, and must represent paths.

        :param path: The path where the results of linting will be saved.

        :param recursive: A boolean flag indicating whether the files must be
         recursively checked, in the case that a directory is passed. True,
         if directories must be recursively linted; False, otherwise.

        :param isflake: A boolean flag indicating whether the linting engine is
         flake8 or Pylint. True, if the linting engine is Flake8; False, if the
         linting engine is Pylint.

        :return: A tuple with the corrected paths of the directories and files
         to be linted; in the corresponding order.
    """
    # Set the path.
    root: Path = Path.cwd()

    if isinstance(path, (Path, str)):
        root = path if isinstance(path, Path) else Path(path)

    # Auxiliary variables.
    files: set = set()
    cache: str = "__pycache__"

    for item in items:
        # Append the file.
        if Path(item).is_file():
            files.add(item)
            continue

        # Get the files.
        function: Callable = Path(item).rglob if recursive else Path(item).glob
        files = files.union(
            f"{x}" for x in function("*")
            if x.is_file() and cache not in f"{x}" and x.suffix == ".py"
        )

    # Get the proper file path.
    file: Path = root

    if root.is_dir():
        counter: int = 0
        name: str = "results_flake8.txt" if isflake else "results_pylint.txt"
        file = root / name

        while file.is_file():
            file = Path(f"{(root / name).with_suffix('')}({counter}).txt")
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

    # Validate the values.
    tpath: Union[None, Path] = Path(path) if isinstance(path, str) else path

    if not (len(objects) > 0 and all(isinstance(x, str) for x in objects)):
        message += (
            f"The \"objects\" object must be a non-empty list or tuple of "
            f"strings that represent existing paths of files and/or "
            f"directories: {objects}. "
        )

    elif not all(Path(x).is_dir() or Path(x).suffix == ".py" for x in objects):
        message += (
            f"The elements of the \"objects\" must be paths of python files "
            f"or directories: {[f'{Path(x)}' for x in objects]}"
        )

    if tpath is not None and not (tpath.is_dir() or tpath.suffix == ".txt"):
        message += (
            f"The \"path\" {path} must correspond to a text file, i.e., a "
            f"file with a .txt extension, or a directory."
        )

    # Raise an error if needed.
    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def lint_flake8(
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

    # Get the path where the results must be saved and the files to lint.
    file, files = _get_parameters(items, path, recursive, True)

    # Set the linter.
    style_guide: flake8.StyleGuide = flake8.get_style_guide(
        format="pylint",
        ignore=[],
        isolated=True,
        select=["E", "W", "F", "C"]
    )

    # Save the statistics.
    with open(file, encoding="utf-8", mode="w") as stream:
        # Check the files or ignore.
        if len(files) > 0:
            with redirect_stdout(stream):
                with redirect_stderr(stream):
                    style_guide.check_files(files)
        else:
            stream.write("NO FILES FOUND TO LINT.\n")

    # Message to the user.
    print(f"Pylint saved the linting results in the file: {file}")


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
    file, files = _get_parameters(items, path, recursive, False)

    # Run the linter.
    with open(file, encoding="utf-8", mode="w") as stream:
        # Check the files or ignore.
        if len(files) > 0:
            reporter: TextReporter = TextReporter(stream)

            Run(
                sorted(files, key=lambda x: x.lower()),
                exit=False,
                reporter=reporter
            )

        else:
            stream.write("NO FILES FOUND TO LINT.\n")

    # Message to the user.
    print(f"Pylint saved the linting results in the file: {file}")
