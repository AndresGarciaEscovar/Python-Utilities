"""
    Contains the context manager to temporarily change the working directory.
"""


# /////////////////////////////////////////////////////////////////////////////
# Imports
# /////////////////////////////////////////////////////////////////////////////


# Standard Library.
import os

from pathlib import Path
from typing import Any, Union


# /////////////////////////////////////////////////////////////////////////////
# Classes
# /////////////////////////////////////////////////////////////////////////////


class WorkingDirectory:
    """
        Temporarily changes the working directory and restores it on exit.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __enter__(self) -> str:
        """
            Sets the working directory.

            :return: The directory set as the working directory.
        """
        # Set the working directory.
        os.chdir(self.new)

        # Return the new working directory.
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

    def __init__(self, wnew: Union[Path, str]):
        """
            Initializes the context manager.

            :param wnew: The string, or Path object, with the path to the new
            working directory.
        """
        # Set the attributes.
        self.new: str = f"{wnew}"
        self.old: str = os.getcwd()
