"""
    Contains the unittests for the type specific errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import unittest

from typing import Type

# User.
from gutilities.exceptions.etypes import WrongTypeError


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestTypeErrors(unittest.TestCase):
    """
        Tests for the etypes errors/exceptions.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_wrongtypeerror(self):
        """
            Tests the WrongTypeError exception.
        """
        # Auxiliary variables.
        current_value: int = 6
        expected_type: Type = str

        # ---------------------------------------------------------------------
        # Test 1: The error message must match the expected message.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected message is not the same as the current "
            "message."
        )

        # Expected message.
        expected: str = (
            f"The value is not of the expected type. Current type value: "
            f"\"{type(current_value).__name__}\". Expected type: "
            f"\"{expected_type.__name__}\"."
        )

        # Error class.
        error: WrongTypeError = WrongTypeError(
            None,
            current_value,
            expected_type
        )

        self.assertEqual(error.message, expected, message)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
