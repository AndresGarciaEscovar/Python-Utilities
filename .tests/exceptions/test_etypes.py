"""
    Tests for the types errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

from typing import Type

# User.
from exceptions.etypes import WrongTypeError


# #############################################################################
# Classes
# #############################################################################


class TestTypeErrors(unittest.TestCase):
        """
            Tests for the etypes errors/exceptions.
        """
        # /////////////////////////////////////////////////////////////////////
        # Test Methods
        # /////////////////////////////////////////////////////////////////////

        def test_wrongtypeerror(self):
            """
                Tests the WrongTypeError exception.
            """
            # Error class.
            mmessage: str = (
                "The expected message is not the same as the current message."
            )

            # Auxiliary variables.
            vcurrent: int = 6
            texpected: Type = str

            # Error class.
            err: WrongTypeError = WrongTypeError(None, vcurrent, texpected)
            mexpected: str = (
                f"The value is not of the expected type. Current type value: "
                f"\"{type(vcurrent).__name__}\". Expected type: "
                f"\"{texpected.__name__}\"."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
