"""
    Tests for the iterable errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

# User.
from exceptions.eiterables import WrongLengthError


# #############################################################################
# Classes
# #############################################################################


class TestIterableErrors(unittest.TestCase):
        """
            Tests for the iterable errors/exceptions.
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
                f"The iterable is not of the expected length. Current length "
                f"of the iterable: {lcurrent}. Expected length: {lexpected}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
