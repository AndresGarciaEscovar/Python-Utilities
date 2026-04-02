"""
    Contains the tests for the dictionary errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import copy as cp

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
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_dictionary_errors_wrongkeyserror():
    """
        Tests the WrongKeysError exception.
    """
    # Auxiliary variables.
    base: dict = cp.deepcopy(BASE)
    original: dict = cp.deepcopy(base)

    # -------------------------------------------------------------------------
    # Test 1: The message error when one of the keys is missing must match
    # the expected message.
    # -------------------------------------------------------------------------

    del original["zero_0"]["one_0"]

    # Set the message in case an error happens.
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
        base=base,
        original=original,
        depth=1
    )

    assert expected == error.message, message
