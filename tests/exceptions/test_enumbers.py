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
from utilities.exceptions.enumbers import AboveBelowBoundError, NotInRangeError


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

        def test_abovebelowbounderror(self):
            """
                Tests the AboveBelowBoundError exception.
            """
            # Error message.
            mmessage: str = "The message is not the expected one."

            # ------------- Value must be greater than or equal ------------- #

            # Variables.
            kwargs = {
                "message": None,
                "value": 7.6,
                "bound": 8,
                "include": True,
                "greater": True
            }

            # Error class.
            err: AboveBelowBoundError = AboveBelowBoundError(**kwargs)

            # Expected message.
            mexpected: str = (
                f"The value is not in the expected range. The given value "
                f"({kwargs['value']}) is NOT greater than, or equal to, the "
                f"bound. The bound is {kwargs['bound']}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)

            # ------------------ Value must be greater than ----------------- #

            # Variables.
            kwargs = {
                "message": None,
                "value": 7.6,
                "bound": 8,
                "include": False,
                "greater": True
            }

            # Error class.
            err: AboveBelowBoundError = AboveBelowBoundError(**kwargs)

            # Expected message.
            mexpected: str = (
                f"The value is not in the expected range. The given value "
                f"({kwargs['value']}) is NOT greater than the bound. The "
                f"bound is {kwargs['bound']}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)

            # --------------- Value must be less than or equal -------------- #

            # Variables.
            kwargs = {
                "message": None,
                "value": 9,
                "bound": 8,
                "include": True,
                "greater": False
            }

            # Error class.
            err: AboveBelowBoundError = AboveBelowBoundError(**kwargs)

            # Expected message.
            mexpected: str = (
                f"The value is not in the expected range. The given value "
                f"({kwargs['value']}) is NOT less than, or equal to, the "
                f"bound. The bound is {kwargs['bound']}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)

            # ------------------- Value must be less than ------------------- #

            # Variables.
            kwargs = {
                "message": None,
                "value": 9,
                "bound": 8,
                "include": False,
                "greater": False
            }

            # Error class.
            err: AboveBelowBoundError = AboveBelowBoundError(**kwargs)

            # Expected message.
            mexpected: str = (
                f"The value is not in the expected range. The given value "
                f"({kwargs['value']}) is NOT less than the bound. The bound "
                f"is {kwargs['bound']}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)

        def test_notinrangeerror(self):
            """
                Tests the NotInRangeError exception.
            """
            # Error message.
            mmessage: str = (
                "The expected message is not the same as the current message."
            )

            # Auxiliary variables.
            kwargs = {
                "message": None,
                "value": 7.6,
                "vrange": (8, 12),
                "include": (False, True)
            }

            # Error class.
            err: NotInRangeError = NotInRangeError(**kwargs)

            mexpected: str = (
                f"The value is not in the expected range. Current value type: "
                f"{type(kwargs['value']).__name__}. Expected range: "
                f"{kwargs['vrange']}. Included (lower, upper)? "
                f"{kwargs['include']}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
