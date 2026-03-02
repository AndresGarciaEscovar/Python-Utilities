"""
    Contains the unittests for the dictionary errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import copy as cp
import unittest

# User.
from gutilities.exceptions.edicts import WrongKeysError


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


BASE: dict = {
    "zero_0": {
        "one_0": {
            "two_0": 1,
            "two_1": 2
        },
        "one_1": {
            "two_0": 3,
            "two_1": 4
        }
    },
    "zero_1": {
        "one_0": {
            "two_0": 5,
            "two_1": 6
        },
        "one_1": {
            "two_0": 7,
            "two_1": 8
        },
        "one_2": {
            "two_0": 9,
            "two_1": 10,
            "two_2": 11
        }
    }
}


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestDictionaryErrors(unittest.TestCase):
    """
        Tests for the dictionary errors/exceptions.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_wrongkeyserror(self):
        """
            Tests the WrongKeysError exception.
        """
        # Auxiliary variables.
        original: dict = cp.deepcopy(BASE)
        del original["zero_0"]["one_0"]

        # Error message.
        message: str = "Test 1: The error message is not the expected one."

        # Expected message.
        expected: str = (
            "The dictionary does not have the expected keys. \n"
            "Errors:\n"
            "- Depth: 1, Key: 'root'.'zero_0', Error: Missing or excess keys; "
            "missing: {'one_0'}, excess: {}."
        )

        # Error class.
        error: WrongKeysError = WrongKeysError(
            base=BASE,
            original=original,
            depth=1
        )

        # Check the message is the expected one.
        self.assertEqual(expected, error.message, message)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
