"""
    Contains the context manager to temporarily change the working directory.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import os

from pathlib import Path
from typing import Any, Union


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class WorkingDirectory:
    """
        Temporarily changes the working directory and restores it on exit.

        PARAMETERS:
        ___________

        - self.new: The path to the new working directory.

        - self.old: The path to current/old working directory.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __enter__(self) -> str:
        """
            Sets the working directory.

            :return: The directory set as the working directory.
        """
        # Set the working directory.
        self.old: str = os.getcwd()
        os.chdir(self.new)

        return self.new

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """
            Restores the working directory.

            :param exc_type: The object with the exception types.

            :param exc_value: The object with the exception values.

            :param traceback: The object with the exception tracebacks.
        """
        # Restore the working directory.
        os.chdir(self.old)

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, working: Union[Path, str]) -> None:
        """
            Initializes the context manager.

            :param working: The string, or Path object, with the path to the
             new working directory.
        """
        # Set the attributes.
        self.new: str = f"{working}"
        self.old: str = ""
