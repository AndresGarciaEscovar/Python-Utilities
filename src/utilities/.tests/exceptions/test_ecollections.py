"""
    Tests for the collection errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

# User.
from src.utilities.exceptions.ecollections import WrongLengthError


# #############################################################################
# Classes
# #############################################################################


class TestCollectionErrors(unittest.TestCase):
        """
            Tests for the collection errors/exceptions.
        """
        # /////////////////////////////////////////////////////////////////////
        # Test Methods
        # /////////////////////////////////////////////////////////////////////

        def test_wronglengtherror(self):
            """
                Tests the WrongLengthError exception.
            """
            # Error class.
            mmessage: str = (
                "The expected message is not the same as the current message."
            )

            # Auxiliary variables.
            lexpected: int = 6
            lcurrent: int = len((1, 2, 3, 4, 5))

            # Error class.
            err: WrongLengthError = WrongLengthError(None, lcurrent, lexpected)
            mexpected: str = (
                f"The collection is not of the expected length. Current "
                f"length of the collection: {lcurrent}. Expected length: "
                f"{lexpected}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
