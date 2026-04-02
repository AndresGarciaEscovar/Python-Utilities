"""
    Runs the tests from the package.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import shutil

from argparse import ArgumentParser, Namespace
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Any

# Third party.
import pytest

# User.
from gutilities.context_managers.cworking import WorkingDirectory


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Messages.
MSG_EPILOG: str = """
To use interactive mode, **do not** provide any files.

If no directory/file is provided to save the output, the output will not
be saved. To save the output, provide a valid directory path or a file
whose parent exists.
""".strip()
MSG_PROGRAM: str = "Program to check the files with pytest."
MSG_USAGE: str = """
    python3 run_tests.py [-f <file1>,...,<fileN>] [-l <flag1>,...,<flagN>,] \
[-s <save file or directory>][-i]
""".strip()

# Paths.
PATH_CURRENT: Path = Path(__file__).parent
PATH_ROOT: Path = PATH_CURRENT.parent.parent
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
    # Create the argument parser.
    parser: ArgumentParser = ArgumentParser(
        epilog=MSG_EPILOG,
        prog=MSG_PROGRAM,
        usage=MSG_USAGE,
    )

    # --------------------- Add the arguments: Optional --------------------- #

    parser.add_argument(
        "-f",
        "--files",
        default=[],
        nargs="*",
        help=(
            "The list of files to be checked; if provided, ALL files must "
            "exist."
        )
    )

    parser.add_argument(
        "-l",
        "--flags",
        default=[],
        nargs="*",
        help= (
            "The list of flags relevant to pytest; they will NOT be checked, "
            "so make sure to pass the correct pytests flags."
        )
    )

    parser.add_argument(
        "-s",
        "--save",
        default="",
        nargs="?",
        type=str,
        help=(
            "The path to the directory where the output file will be saved; "
            "if any."
        )
    )

    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help=(
            "The path to the directory where the output file will be saved; "
            "if any."
        )
    )

    # -------------------------- Read the arguments ------------------------- #

    # Get the arguments.
    arguments: Namespace = parser.parse_args()

    dictionary: dict = {
        "files": arguments.files,
        "flags": arguments.flags,
        "interactive": arguments.interactive,
        "save": arguments.save
    }

    # Validate the arguments.
    _validate_arguments(dictionary)

    return dictionary


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


def _get_unique(file: Path) -> Path:
    """
        Returns the unique path to the file; i.e., if a file exists, numbers
        the file so that it does not overwrite existing files.

        :param file: The path to the requested file.

        :return: The path to a non-existing file.
    """
    # Auxiliary variables.
    counter: int = 0
    suffix: str = file.suffix
    suffixless: Path = file.with_suffix("")

    # Fix the name.
    while file.is_file():
        file = Path(f"{suffixless}({counter})").with_suffix(suffix)
        counter += 1

    return file


def _remove_cache() -> None:
    """
        Removes the __pycache__ files.
    """
    # Auxiliary variables.
    files: list = [
        x for x in Path.cwd().rglob("*")
        if x.name == "__pycache__" and x.is_dir()
    ]

    for file in files:
        if file.exists() and file.is_dir():
            shutil.rmtree(f"{file}")


def _run_checks(files: list, arguments: dict) -> None:
    """
        Runs the checks of the given files, with the given parameters.

        :param files: The list of files to be checked; if the list is empty,
         all the files will be checked.

        :param arguments: The dictionary with the additional arguments.
    """
    # Run the tests.
    if arguments["save"] == "":
        pytest.main(files)

    else:
        # Fix the path.
        path: Path = Path(arguments["save"])
        path = path / 'pytest_results.txt' if path.is_dir() else path
        path = _get_unique(path)

        # Redirect the output and error to the file.
        with open(f"{path}", encoding="utf-8", mode="w") as stream:
            with redirect_stdout(stream):
                with redirect_stderr(stream):
                    pytest.main(files)

        # Message to the user.
        print(f"Results were saved in: {path}")


def _tests_interactive() -> tuple:
    """
        Runs the tests in an interactive way.
    """
    # Auxiliary variables.
    base: str = "\n    "
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


def _validate_arguments(params: dict) -> None:
    """
        Validates that the parameters are the proper types and contain proper
        values.

        :param params: The dictionary with the extracted parameters.
    """
    # Auxiliary variables.
    dictionary: dict = {
        "files": _validate_arguments_files,
        "flags": _validate_arguments_flags,
        "save": _validate_arguments_save_directory
    }

    # Check the basic ones.
    for name, function in dictionary.items():
        function(params[name])

    # Check the interactive flag.
    _validate_arguments_interactive(params["files"], params["interactive"])


def _validate_arguments_files(files: Any) -> None:
    """
        Validates that the files are the proper types and contain proper
        values.

        :param files: The list of files to be checked.

        :raise ValueError: If any of the types are wrong. If any of the files
         do not exist.
    """
    # No need to check.
    if isinstance(files, list) and len(files) == 0:
        return

    # Auxiliary variables.
    base: str = "\n    -"
    message: str = ""
    name: str = repr("files")

    # Check the properties.
    if not isinstance(files, list):
        # Must be a list.
        message += (
            f"The {name} parameter is not a list, it must be a list; "
            f"current type: {type(files).__name__}."
        )

    elif not all(isinstance(x, str) for x in files):
        # All entries must be strings.
        message += (
            f"There are files in the list that are not strings; current "
            f"types {', '.join(type(x).__name__ for x in files)}."
        )

    elif not all(Path(x).is_file() for x in files):
        # All entries must be existing files.
        message += (
            f"There are files in the list that are not files; current "
            f"status:{base}"
            f"{base.join(f'{x} is file: {Path(x).is_file()}' for x in files)}."
        )

    # Raise an error if needed.
    if message != "":
        raise ValueError(message.strip())


def _validate_arguments_flags(flags: Any) -> None:
    """
        Validates that the flags is a list of strings; nothing else can be
        checked.

        :param flags: The object that contains the flags.

        :raise ValueError: If the flags is not a list of strings.
    """
    # No need to check.
    if isinstance(flags, list) and len(flags) == 0:
        return

    # Auxiliary variables.
    message: str = ""
    name: str = repr("flags")

    # Check the properties.
    if not isinstance(flags, list):
        # Must be a list.
        message += (
            f"The {name} parameter is not a list, it must be a list; "
            f"current type: {type(flags).__name__}."
        )

    elif not all(isinstance(x, str) for x in flags):
        # All entries must be strings.
        message += (
            f"There are flags in the list that are not strings; current "
            f"types {', '.join(type(x).__name__ for x in flags)}."
        )

    # Raise an error if needed.
    if message != "":
        raise ValueError(message.strip())


def _validate_arguments_interactive(files: Any, interactive: Any) -> None:
    """
        Validates that the "interactive" flag is a boolean value, and it
        is consistent with the list of files.

        :param files: The already validated list of files to be checked.

        :param interactive: The parameter that must be validated to be a
         boolean flag.

        :raise ValueError: If the "interactive" object is not a boolean value.
         If there are files while using the "interactive" mode.
    """
    # Auxiliary variables.
    message: str = ""

    # Check the properties.
    if not isinstance(interactive, bool):
        # Must be a boolean value.
        message += (
            f"The \"interactive\" flag must be a boolean value; current type: "
            f"{type(interactive).__name__}."
        )

    elif interactive and len(files) > 0:
        # Flag cannot be used along with files.
        message += "The interactive flag cannot be True with files passed."

    # Raise an error if needed.
    if message != "":
        raise ValueError(message)


def _validate_arguments_save_directory(directory: Any) -> None:
    """
        Validates that the requested save directory is a valid string.

        :param arguments: The dictionary with the extracted arguments.
    """
    # Auxiliary variables.
    message: str = ""

    # Check the properties.
    if not isinstance(directory, str):
        # Must be a string.
        message += (
            f"The \"directory\" paremeter is not a string; current type: "
            f"{type(directory).__name__}."
        )

    elif Path(directory).suffix == "" and not Path(directory).is_dir():
        # Path has no suffix, i.e., a directory, but it does not exist.
        message += (
            f"The \"directory\" paremeter is a string representing a path "
            f"that has no suffix, i.e., a directory, but it does not exist: "
            f"{directory}."
        )

    elif Path(directory).suffix != "" and not Path(directory).parent.is_dir():
        # Path has a suffix, i.e., a file, but its parent does not exist.
        message += (
            f"The \"directory\" paremeter is a string representing a path "
            f"that has a suffix, i.e., a file, but its parent does not exist; "
            f"file: {directory}, parent: {Path(directory).parent}."
        )

    # Raise an error if needed.
    if message != "":
        raise ValueError(message)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run() -> None:
    """
        Run the tests.
    """
    # Remove the cache.
    _remove_cache()

    # Auxiliary variables.
    files: list = list()
    arguments: dict = _get_arguments()

    # Get the files to be checked.
    if arguments["interactive"]:
        # Interactive, get the files interactively.
        files += _tests_interactive()

    elif len(arguments["files"]) > 0:
        # Set the files to be checked.
        files = sorted(set(arguments["files"]), key=lambda x: x.lower())

    else:
        # No files requested, get ALL the files.
        files = _get_files_all()

    # Add the flags, if any.
    files = arguments["flags"] + files

    # Run the checks with the given arguments.
    _run_checks(files, arguments)

    # Remove the cache.
    _remove_cache()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    # Set the working directory.
    with WorkingDirectory(PATH_TESTS):
        run()
