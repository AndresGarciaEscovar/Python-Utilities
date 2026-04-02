"""
    Contains the unit tests for the context manager FileTemp.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import os

from pathlib import Path

# User.
from gutilities.context_managers.cfiles import FileTemp


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_cm_file_temp() -> None:
    """
        Tests the context manager FileTemp.
    """
    # Auxiliary variables.
    content: str = "Hello, World!"

    # Set the current working directory.
    wold: str = f"{Path(os.getcwd())}"
    wnew: str = f"{Path(os.getcwd()).parent}"

    os.chdir(wnew)

    with FileTemp(path=wnew, extension="txt", content=content) as file:
        # -----------------------------------------------------------------
        # Test 1: Check the file was created.
        # -----------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = "Test 1: The temporary file was not created."

        # Check the file was created.
        path: Path = Path(file)

        assert path.exists() and path.is_file(), message

        # -----------------------------------------------------------------
        # Test 2: Check the content of the file is the same as the one
        # appended.
        # -----------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 2: The content of the temporary file is wrong."

        # Check the content of the file.
        with open(file, encoding="utf-8", mode="r") as stream:
            assert stream.read() == content, message

    # ---------------------------------------------------------------------
    # Test 3: The file must have been deleted.
    # ---------------------------------------------------------------------

    # Set the message in case an error happens.
    message = "Test 3: The temporary file was not removed."

    assert not path.exists(), message

    # Restore the working directory.
    os.chdir(wold)
