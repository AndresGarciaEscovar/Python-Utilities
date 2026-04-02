"""
    Contains the tests for the collection errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any

# User.
from gutilities.exceptions.ecollections import (
    NotInCollectionError, WrongLengthError
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_collection_errors_notincollectionerror():
    """
        Tests the NotInCollectionError exception.
    """
    # Auxiliary variables.
    value: Any = 6
    items: tuple = (1, 2, 3, 4, 5)

    # -------------------------------------------------------------------------
    #  Test 1: The element is not in the collection; must raise an error
    #  with the proper error.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message: str = "Test 1: The error message is not the expected one."

    # Expected message.
    expected: str = (
        f"The given item is not in the collection. Object being "
        f"validated: {value}. Collection of possible objects: {items}."
    )

    # Error class.
    error: NotInCollectionError = NotInCollectionError(None, value, items)

    assert expected == error.message, message

    # -------------------------------------------------------------------------
    #  Test 2: The element is not in the collection; must raise an error
    #  with the proper error. Now it is a string.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message = "Test 2: The error message is not the expected one."

    # The values must be consistent.
    value = "6"
    expected = (
        f"The given item is not in the collection. Object being "
        f"validated: {value}. Collection of possible objects: {items}."
    )

    # Error class.
    error = NotInCollectionError(None, value, items)

    assert expected == error.message, message


def test_collection_errors_wronglengtherror():
    """
        Tests the WrongLengthError exception.
    """
    # -------------------------------------------------------------------------
    #  Test 1: The collection is not of the expected length.
    # -------------------------------------------------------------------------

    # Auxiliary variables.
    lcurrent: int = len((1, 2, 3, 4, 5))
    lexpected: int = lcurrent + 1
    expected: str = (
        f"The collection is not of the expected length. Current "
        f"length of the collection: {lcurrent}. Expected length: "
        f"{lexpected}."
    )

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The expected message is not the same as the current "
        "message."
    )

    # Error class.
    error: WrongLengthError = WrongLengthError(None, lcurrent, lexpected)

    assert expected == error.message, message
