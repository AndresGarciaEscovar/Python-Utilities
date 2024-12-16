"""
    Contains the unittests for the numerical validation errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

from numbers import Real

# User.
from utilities.exceptions.enumbers import NotInRangeError
from utilities.general.gtypes import tbool, treal


# #############################################################################
# Classes
# #############################################################################


class TestNumberErrors(unittest.TestCase):
        """
            Tests for the number validation errors.
        """
        # /////////////////////////////////////////////////////////////////////
        # Test Methods
        # /////////////////////////////////////////////////////////////////////

        def test_notinrangeerror(self):
            """
                Tests the NotInRangeError exception.
            """
            # Error class.
            mmessage: str = (
                "The expected message is not the same as the current message."
            )

            # Auxiliary variables.
            vvalue: Real = 7.6
            vrange: treal = (8, 12)
            vinclude: tbool = (False, True)

            # Error class.
            err: NotInRangeError = NotInRangeError(
                None, vvalue, vrange, vinclude
            )

            mexpected: str = (
                f"The value is not in the expected range. Current value type: "
                f"{type(vvalue).__name__}. Expected range: {vrange}. Included "
                f"(lower, upper)? {vinclude}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
