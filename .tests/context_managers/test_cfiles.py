"""
    Contains the unit tests for the context manager FileTemp.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import os
import unittest

from pathlib import Path

# User.
from context_managers.cfiles import FileTemp


# #############################################################################
# Classes
# #############################################################################


class TestFileTemp(unittest.TestCase):
    """
        Contains the unit tests for the context manager FileTemp.
    """

    def test_filetemp(self):
        """
            Tests the context manager FileTemp.
        """
        # Auxiliary variables.
        content: str = "Hello, World!"

        # Messages.
        mssg_created: str = "The temporary file was not created."
        mssg_content: str = "The content of the temporary file is wrong."
        mssg_removed: str = "The temporary file was not removed."

        # Set the current working directory.
        wold: Path = Path(os.getcwd())
        wnew: Path = Path(__file__).parent

        os.chdir(f"{wnew}")

        with FileTemp(path=f"{wnew}", extension="txt", content=content) as fil:
            # Check the file was created.
            path = Path(fil)
            self.assertTrue(path.exists() and path.is_file(), mssg_created)

            # Check the content of the file.
            with open(fil, mode="r") as fl:
                self.assertEqual(fl.read(), content, mssg_content)

        # Check the file was removed.
        self.assertFalse(path.exists(), mssg_removed)

        # Restore the working directory.
        os.chdir(f"{wold}")


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
