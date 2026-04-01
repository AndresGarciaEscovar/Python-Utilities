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
    return {"files": [], "flags": [], "interactive": False}


def _get_files_all(string: bool = False) -> list:
    """
        Gets all the files from the test directory.

        :param string: A boolean variable indicating whether the files should
         be appended as Path objects or strings. True, if the paths should be
         returned as string objects; False otherwise. False, by default.

        :return: The list of all the files to be checked.
    """
    # Auxiliary variables.
    cardw: str = "test_*.py"

    return sorted(
        (
            f"{x}" if string else x for x in Path.cwd().rglob(cardw)
            if x.is_file()
        ),
        key=lambda x: f"{x}".lower()
    )


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

            results.add(files[index - 1])

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
    files: list = _get_files_all(string=True)
    string: str = base.join(
        f"{i:2d}. {x.replace(f'{PATH_TESTS}', '')[1:]}"
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
    if arguments["interactive"]:
        # Interactive, get the files interactively.
        files = _tests_interactive()

    elif len(arguments["files"]) > 0:
        # Set the files to be checked.
        files += arguments["flags"] + arguments["files"]

    else:
        # No files requested, get ALL the files.
        files += arguments["flags"] + _get_files_all()

    # Run the checks with the given arguments.
    _run_checks(files, arguments)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    # Set the working directory.
    with WorkingDirectory(PATH_TESTS):
        run()
