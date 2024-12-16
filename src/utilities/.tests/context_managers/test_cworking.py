"""
    Contains the unit tests for the context manager WorkingDirectory.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import os
import unittest

from pathlib import Path

# User.
from utilities.context_managers.cworking import WorkingDirectory


# #############################################################################
# Classes
# #############################################################################


class TestWorkingDirectory(unittest.TestCase):
    """
        Contains the unit tests for the context manager WorkingDirectory.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////////

    def test_workingdirectory(self):
        """
            Tests the context manager WorkingDirectory.
        """
        # Messages.
        message_changed: str = "The working directory was not changed."
        message_restored: str = "The working directory was not restored."

        # Set different working directories.
        wold: Path = Path(os.getcwd())
        wnew: Path = Path(__file__).parent

        if f"{wold}" == f"{wnew}":
            wnew = wnew.parent

        with WorkingDirectory(wnew=wnew) as wdir:
            # Check the working directory was changed.
            self.assertEqual(os.getcwd(), f"{wnew}", message_changed)
            self.assertEqual(wdir, f"{wnew}", message_changed)

        # Check the working directory was restored.
        self.assertEqual(os.getcwd(), f"{wold}", message_restored)

        # Restore the working directory.
        os.chdir(f"{wold}")


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
