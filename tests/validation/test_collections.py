"""
    Contains the tests for the collection errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from gutilities.exceptions.ecollections import NotInCollectionError
from gutilities.validation.vcollections import validate_in

from tests.auxiliary.genutils import RaisesException


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_validate_in_collection_not_collection() -> None:
    """
        Tests there is an exception if the object to be validated is not
        in the collection.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "vobject": 9,
        "collection": 3,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The object in the "collection" placeholder is NOT a
    # collection.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The \"collection\" parameter must be a collection; a "
        "ValueError must be raised."
    )

    # Must throw a ValueError.
    with RaisesException(ValueError, message=message):
        validate_in(**kwargs)

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a collection; e.g., a tuple.
    kwargs["collection"] = (1, 2, 9)

    validate_in(**kwargs)


def test_validate_in_exception_not_bool() -> None:
    """
        Tests there is an exception if the value of the "exception"
        parameter is not a boolean.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "vobject": 9,
        "collection": (3, 9),
        "exception": 1,
    }

    # -------------------------------------------------------------------------
    # Test 1: The object in the "exception" placeholder is NOT a
    # boolean value.
    # -------------------------------------------------------------------------

    # Messages.
    message: str = (
        "Test 1: The expected type of \"exception\" is NOT a boolean "
        "value; it must be a boolean number to NOT raise an exception."
    )

    # Must throw a ValueError.
    with RaisesException(ValueError, message=message):
        validate_in(**kwargs)

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a boolean.
    kwargs["exception"] = True

    validate_in(**kwargs)


def test_validate_in_correct_values() -> None:
    """
        Tests the validate_in function.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "vobject": 7,
        "collection": (3, 9),
        "exception": False,
    }

    # -------------------------------------------------------------------------
    # Test 1: Object not in, no exception.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The object to be validated is in the collection; it must "
        "NOT be in the collection."
    )

    assert not validate_in(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 2: Object not in, with exception.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message = (
        "Test 2: The object to be validated is in the collection; it must "
        "NOT be in the collection and raise an exception."
    )

    # Set the proper values.
    kwargs["exception"] = True

    # Must throw a NotInCollectionError.
    with RaisesException(NotInCollectionError, message=message):
        validate_in(**kwargs)

    # -------------------------------------------------------------------------
    # Test 3: Object not in, with exception.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message = (
        "Test 3: The object to be validated is NOT in the collection; it "
        "must be in the collection."
    )

    # Set the proper values.
    kwargs["vobject"] = 9

    # All collection must validate to True.
    for dtype in (list, tuple, set):
        kwargs["collection"] = dtype((3, 9))

        assert validate_in(**kwargs), message
