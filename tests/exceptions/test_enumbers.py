"""
    Contains the unittests for the numerical validation errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import unittest

# User.
from gutilities.exceptions.enumbers import (
    AboveBelowBoundError, NotInRangeError
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestNumberErrors(unittest.TestCase):
    """
        Tests for the number validation errors.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_abovebelowbounderror(self):
        """
            Tests the AboveBelowBoundError exception.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "message": None,
            "value": 7.6,
            "bound": 8,
            "include_greater": (True, True),
        }

        # ---------------------------------------------------------------------
        # Test 1: The error message must match the expected message.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The message is not the expected one; value is greater "
            "than or equal."
        )

        # Expected message.
        expected: str = (
            f"The value is not in the expected range. The given value "
            f"({kwargs['value']}) is NOT greater than, or equal to, the "
            f"bound. The bound is {kwargs['bound']}."
        )

        # Set the message in case an error happens.
        error: AboveBelowBoundError = AboveBelowBoundError(**kwargs)

        # Check the message is the expected one.
        self.assertEqual(error.message, expected, message)

        # ---------------------------------------------------------------------
        # Test 2: The error message must match the expected message.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: The message is not the expected one; value is greater "
            "than."
        )

        # Change the parameters as needed.
        kwargs["include_greater"] = (False, True)

        # Expected message.
        expected = (
            f"The value is not in the expected range. The given value "
            f"({kwargs['value']}) is NOT greater than the bound. The "
            f"bound is {kwargs['bound']}."
        )

        # Set the message in case an error happens.
        error = AboveBelowBoundError(**kwargs)

        # Check the message is the expected one.
        self.assertEqual(error.message, expected, message)

        # ---------------------------------------------------------------------
        # Test 3: The error message must match the expected message.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 3: The message is not the expected one; value is less than "
            "or equal."
        )

        # Change the parameters as needed.
        kwargs["value"] = 9
        kwargs["include_greater"] = (True, False)

        # Error class.
        error = AboveBelowBoundError(**kwargs)

        # Expected message.
        expected = (
            f"The value is not in the expected range. The given value "
            f"({kwargs['value']}) is NOT less than, or equal to, the "
            f"bound. The bound is {kwargs['bound']}."
        )

        # Check the message is the expected one.
        self.assertEqual(error.message, expected, message)

        # ---------------------------------------------------------------------
        # Test 4: The error message must match the expected message.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 4: The message is not the expected one; value is less than."
        )

        # Change the parameters as needed.
        kwargs["include_greater"] = (False, False)

        # Error class.
        error = AboveBelowBoundError(**kwargs)

        # Expected message.
        expected = (
            f"The value is not in the expected range. The given value "
            f"({kwargs['value']}) is NOT less than the bound. The bound "
            f"is {kwargs['bound']}."
        )

        # Check the message is the expected one.
        self.assertEqual(error.message, expected, message)

    @unittest.skip("Temporary skip the test.")
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


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
