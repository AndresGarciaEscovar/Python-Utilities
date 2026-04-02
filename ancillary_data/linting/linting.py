"""
    Contains the script to lint the project.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import shutil

from pathlib import Path

# User.
from gutilities.general.glinting import lint_flake8, lint_pylint


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Paths.
PATH_ROOT: Path = Path(__file__).parent


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _lint_directory(path: Path, name: str) -> None:
    """
        Lints the requested directory and outputs the linting files in the
        current directory.

        :param path: The path of the directory/file to be linted.

        :param name: The name to append to the output files.
    """
    # Name of the files.
    base_flake8: str = f"linting_flake8_{name}.txt"
    base_pylint: str = f"linting_pylint_{name}.txt"

    # Run Flake8.
    lint_flake8(
        [f"{path}"],
        f"{PATH_ROOT}/{base_flake8}",
        recursive=True
    )

    # Run pylint.
    lint_pylint(
        [f"{path}"],
        f"{PATH_ROOT}/{base_pylint}",
        recursive=True
    )


def _remove_cache() -> None:
    """
        Removes the pycache from the project.
    """
    # Navigate to the parent directory.
    path: Path = Path(__file__).parent.parent.parent
    directories: tuple = tuple(
        x for x in path.rglob("*")
        if x.is_dir() and x.name == "__pycache__"
    )

    # Remove the pycache.
    for directory in directories:
        if directory.is_dir():
            shutil.rmtree(f"{directory}")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run() -> None:
    """
        Runs the main program.
    """
    # Removes the cache.
    _remove_cache()

    # Auxiliary variables.
    path_src: Path = PATH_ROOT.parent.parent / "src"
    path_tst: Path = PATH_ROOT.parent.parent / "tests"

    # Lint the "src" and "tests" directories.
    _lint_directory(path_src, "src")
    _lint_directory(path_tst, "tests")

    # Removes the cache.
    _remove_cache()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    run()
