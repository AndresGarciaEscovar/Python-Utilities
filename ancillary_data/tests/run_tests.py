"""
    Runs the tests from the package.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from argparse import ArgumentParser, Namespace
from pathlib import Path

# Third party.
import pytest

# User.
from gutilities.context_managers.cworking import WorkingDirectory


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Paths.
PATH_ROOT: Path = Path(__file__).parent.parent.parent
PATH_TESTS: Path = PATH_ROOT / "tests"


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_arguments() -> dict:
    """
        Gets the arguments from the command line arguments.

        :return: The dictionary with the options chosen from the command
         line arguments.
    """
    return {}


def _get_files_tests_interactive(options: list, files: list) -> list:
    """
        Validates that the list of entries is valid; i.e., that every entry
        contains an integer number in the proper range.

        :param options: The list with the numbers associated with the files to
         be validated. The numbers do not need to be unique, since they will be
         filtered out.

        :param files: The list with the available test files.

        :return: The list of files to be checked.

        :raise ValueError: If there are invalid indexes requested by the user.
    """
    # Auxiliary variables.
    message: str = ""
    results: set = set()

    # Check all the numbers.
    for i, option in enumerate(options):
        # Get the files to be validated.
        try:
            index: int = int(option.strip())

            if not (1 <= index <= len(files)):
                raise ValueError()

            results.add(f"{files[index - 1]}")

        except (IndexError, ValueError):
            message += (
                f"The {i}th entry ({repr(option)}) could not be converted "
                f"into an integer, or is out of range; valid range: [1, "
                f"{len(files)}], both ends included. "
            )

    # Raise the error if needed.
    if message != "":
        raise ValueError(message.strip())

    return sorted(results, key=lambda x: x.lower())


def _run_checks(files: list, arguments: dict) -> None:
    """
        Runs the checks of the given files, with the given parameters.

        :param files: The list of files to be checked; if the list is empty,
         all the files will be checked.

        :param arguments: The dictionary with the additional arguments.
    """
    # Run the tests.
    pytest.main(files)


def _tests_interactive() -> tuple:
    """
        Runs the tests in an interactive way.
    """
    # Auxiliary variables.
    base: str = "\n    "
    cardw: str = "test_*.py"
    files: list = sorted(
        (x for x in Path.cwd().rglob(cardw) if x.is_file()),
        key=lambda x: f"{x}".lower()
    )
    string: str = base.join(
        f"{i:2d}. {f'{x}'.replace(f'{PATH_TESTS}', '')[1:]}"
        for i, x in enumerate(files, start=1)
    )

    # Get the files to be examined.
    options: list = input(
        f"Select the files desired to be checked:{base}{string}\nFor multiple "
        f"files, use the numbers separated by commas: "
    ).split(",")

    # Validate the inputs.
    return _get_files_tests_interactive(options, files)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run() -> None:
    """
        Run the tests.
    """
    # Auxiliary variables.
    files: list = list()
    arguments: dict = _get_arguments()

    # Get the dictionary of arguments.
    files = _tests_interactive()

    # Run the checks with the given arguments.
    _run_checks(files, arguments)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    # Set the working directory.
    with WorkingDirectory(PATH_TESTS):
        run()
