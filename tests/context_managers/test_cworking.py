"""
    Contains the unit tests for the context manager WorkingDirectory.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import os
import unittest

from pathlib import Path

# User.
from gutilities.context_managers.cworking import WorkingDirectory


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestWorkingDirectory(unittest.TestCase):
    """
        Contains the unit tests for the context manager WorkingDirectory.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_working_directory(self):
        """
            Tests the context manager WorkingDirectory.
        """
        # Auxiliary variables.
        wold: str = os.getcwd()
        wnew: str = f"{Path(wold).parent}"

        with WorkingDirectory(working=Path(wnew)) as working:
            # -----------------------------------------------------------------
            # Test 1: Check the directory has effectively changed.
            # -----------------------------------------------------------------

            # Set the message in case an error happens.
            message: str = "Test 1: The working directory was not changed."

            self.assertEqual(os.getcwd(), wnew, message)
            self.assertEqual(working, wnew, message)

        # ---------------------------------------------------------------------
        # Test 2: Check the directory has been restored.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 2: The working directory was not restored."

        self.assertEqual(os.getcwd(), wold, message)

        # Restore the working directory.
        os.chdir(wold)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
