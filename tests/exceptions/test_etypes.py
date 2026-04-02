"""
    Contains the tests for the type specific errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Type

# User.
from gutilities.exceptions.etypes import WrongTypeError


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_type_errors_wrongtypeerror() -> None:
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

    assert error.message == expected, message
