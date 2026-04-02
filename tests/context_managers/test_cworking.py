"""
    Contains the unit tests for the context manager WorkingDirectory.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import os

from pathlib import Path

# User.
from gutilities.context_managers.cworking import WorkingDirectory


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_cm_working_directory() -> None:
    """
        Tests the context manager WorkingDirectory.
    """
    # Auxiliary variables.
    wold: str = os.getcwd()
    wnew: str = f"{Path(wold).parent}"

    with WorkingDirectory(working=Path(wnew)) as working:
        # ---------------------------------------------------------------------
        # Test 1: Check the directory has effectively changed.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = "Test 1: The working directory was not changed."

        assert os.getcwd() == wnew, message
        assert working == wnew, message

    # -------------------------------------------------------------------------
    # Test 2: Check the directory has been restored.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message = "Test 2: The working directory was not restored."

    assert os.getcwd() == wold, message

    # Restore the working directory.
    os.chdir(wold)
