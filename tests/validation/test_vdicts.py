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
from gutilities.exceptions.edicts import (
    WrongKeysError,
    WrongKeysAndTypeError,
    WrongKeysSubsetError,
    WrongKeysSubsetAndTypeError
)
from gutilities.validation.vdicts import (
    validate_keys_equal,
    validate_keys_equal_and_type,
    validate_keys_subset,
    validate_keys_subset_and_type
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Auxiliary dictionary for validation.
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

BASE_TYPES: dict = {
    "zero_0": {
        "one_0": {
            "two_0": int,
            "two_1": int
        },
        "one_1": {
            "two_0": int,
            "two_1": int
        }
    },
    "zero_1": {
        "one_0": {
            "two_0": int,
            "two_1": int
        },
        "one_1": {
            "two_0": int,
            "two_1": int
        },
        "one_2": {
            "two_0": int,
            "two_1": int,
            "two_2": str
        }
    }
}


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_keys_equal_base_not_dict() -> None:
    """
        Tests there is an exception if the value of the "base"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": 9,
        "dictionary": {},
        "depth": 0,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "base" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"base\" is a dictionary; it must "
        "NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["base"] = {}

    validate_keys_equal(**kwargs)


def test_keys_equal_depth_not_int() -> None:
    """
        Tests there is an exception if the value of the "depth"
        parameter is not an integer.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "depth": "1",
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "depth" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"depth\" is an integer; it must "
        "NOT be a integer to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be an integer.
    kwargs["depth"] = 0

    validate_keys_equal(**kwargs)


def test_keys_equal_dictionary_not_dict() -> None:
    """
        Tests there is an exception if the value of the "dictionary"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": 9,
        "depth": 0,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "dictionary" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"dictionary\" is a dictionary; it "
        "must NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["dictionary"] = {}

    validate_keys_equal(**kwargs)


def test_keys_equal_exception_not_bool() -> None:
    """
        Tests there is an exception if the value of the "exception"
        parameter is not a boolean.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "depth": 0,
        "exception": 1,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "exception" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"exception\" is a boolean value; "
        "it must NOT be a boolean number to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a boolean.
    kwargs["exception"] = True

    validate_keys_equal(**kwargs)


def test_keys_equal_validate_keys_equal_basic() -> None:
    """
        Tests the validate_keys_equal function for valid and invalid cases.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": cp.deepcopy(BASE),
        "dictionary": cp.deepcopy(BASE),
        "depth": -1,
        "exception": False,
    }

    # -------------------------------------------------------------------------
    # Test 1: The dictionaries are different.
    # -------------------------------------------------------------------------

    # Remove the entries.
    del kwargs["dictionary"]["zero_1"]

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The dictionaries have the same keys; this should not "
        "happen."
    )

    assert not validate_keys_equal(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 2: The dictionaries are different, and must raise an exception.
    # -------------------------------------------------------------------------

    # Set the values.
    kwargs["exception"] = True

    # Set the message in case an error happens.
    flag: bool = False
    message = (
        "Test 2: An exception should be raised, since it has been "
        "requested."
    )

    # Must throw a WrongKeysError.
    try:
        validate_keys_equal(**kwargs)

    except WrongKeysError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 3: The dictionaries are the same.
    # -------------------------------------------------------------------------

    # Set the values.
    kwargs["dictionary"] = kwargs["base"]

    # Set the message in case an error happens.
    message = "Test 3: Dictionaries should be the same in this case."

    assert validate_keys_equal(**kwargs), message


def test_keys_equal_validate_keys_equal_level() -> None:
    """
        Tests the validate_keys_equal function for valid and invalid cases.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": cp.deepcopy(BASE),
        "dictionary": cp.deepcopy(BASE),
        "depth": 2,
        "exception": False,
    }

    # Remove the deepest level.
    del kwargs["dictionary"]["zero_0"]["one_0"]["two_0"]

    # -------------------------------------------------------------------------
    # Test 1: The dictionaries are different beyond the second level
    # (where the base level is the zeroth level).
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The dictionaries must be different; at depth 2, the "
        "dictionaries do not have the same keys."
    )

    assert not validate_keys_equal(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 2: The dictionaries must be the same at the base (zeroth) and
    # first level.
    # -------------------------------------------------------------------------

    for i in range(0, 2):
        # Set the level.
        kwargs["depth"] = i

        # Set the message in case an error happens.
        message = (
            f"Test 2: No exception should be raised until depth level 2; "
            f"current depth level: {i}. Remember that the depth is "
            f"zero-based."
        )

        assert validate_keys_equal(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 3: Unrestricted should, of course, be False.
    # -------------------------------------------------------------------------

    # Must throw an exception.
    kwargs["depth"] = 10000
    kwargs["exception"] = True

    # Set the message in case an error happens.
    flag: bool = False
    message = (
        "An exception should be raised, since the depth level is greater "
        "than the depth of the base dictionary."
    )

    # Must throw a WrongKeysError.
    try:
        validate_keys_equal(**kwargs)

    except WrongKeysError:
        flag = True

    assert flag, message


def test_keys_equal_and_type_base_not_dict() -> None:
    """
        Tests there is an exception if the value of the "base"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": 9,
        "dictionary": {},
        "extract": False,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "base" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"base\" is a dictionary; it must "
        "NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["base"] = {}

    validate_keys_equal_and_type(**kwargs)


def test_keys_equal_and_type_extract_not_bool() -> None:
    """
        Tests there is an exception if the value of the "extract"
        parameter is not a boolean.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "extract": "1",
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "extract" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"extract\" is a string; it must "
        "be a boolean value to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a boolean
    kwargs["extract"] = True

    validate_keys_equal_and_type(**kwargs)


def test_keys_equal_and_type_dictionary_not_dict() -> None:
    """
        Tests there is an exception if the value of the "dictionary"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": 9,
        "extract": True,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "dictionary" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"dictionary\" is a dictionary; it "
        "must NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["dictionary"] = {}

    validate_keys_equal_and_type(**kwargs)


def test_keys_equal_and_type_exception_not_bool() -> None:
    """
        Tests there is an exception if the value of the "exception"
        parameter is not a boolean.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "extract": False,
        "exception": 1,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "exception" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"exception\" is a boolean value; "
        "it must NOT be a boolean number to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_equal_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a boolean.
    kwargs["exception"] = True

    validate_keys_equal_and_type(**kwargs)


def test_keys_equal_and_type_validate_keys_equal_basic() -> None:
    """
        Tests the validate_keys_equal function for valid and invalid cases.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": cp.deepcopy(BASE),
        "dictionary": cp.deepcopy(BASE),
        "extract": True,
        "exception": False,
    }

    # -------------------------------------------------------------------------
    # Test 1: The dictionaries are different.
    # -------------------------------------------------------------------------

    # Remove the entries.
    del kwargs["dictionary"]["zero_1"]

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The dictionaries have the same keys; this should not "
        "happen."
    )

    assert not validate_keys_equal_and_type(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 2: The dictionaries are different, and must raise an exception.
    # -------------------------------------------------------------------------

    # Set the values.
    kwargs["exception"] = True

    # Set the message in case an error happens.
    flag: bool = False
    message = (
        "Test 2: An exception should be raised, since it has been "
        "requested."
    )

    # Must throw a WrongKeysAndTypeError.
    try:
        validate_keys_equal_and_type(**kwargs)

    except WrongKeysAndTypeError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 3: The dictionaries are the same.
    # -------------------------------------------------------------------------

    # Set the values.
    kwargs["dictionary"] = kwargs["base"]

    # Set the message in case an error happens.
    message = "Test 3: Dictionaries should be the same in this case."

    assert validate_keys_equal_and_type(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 4: Must throw a ValueError since the types should not be
    # extracted.
    # -------------------------------------------------------------------------

    # Set to False to force and error.
    kwargs["extract"] = False

    # Set the message in case an error happens.
    flag = False
    message = "Test 4: Types at the leafs are not valid."

    # Must throw a ValueError.
    try:
        validate_keys_equal_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 5: One of the elements of the end brach must be an integer,
    # but it is not; this should evaluate to False!
    # -------------------------------------------------------------------------

    # Change the value to a string.
    kwargs["base"] = cp.deepcopy(BASE_TYPES)
    kwargs["dictionary"]["zero_0"]["one_0"]["two_0"] = "hello!"
    kwargs["exception"] = False

    # Set the message in case an error happens.
    message = (
        "Test 5: One of the elements of the end brach must be an integer, "
        "but it is not; this should evaluate to False!"
    )

    assert not validate_keys_equal_and_type(**kwargs), message


def test_keys_subset_base_not_dict() -> None:
    """
        Tests there is an exception if the value of the "base"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": 9,
        "dictionary": {},
        "depth": 0,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "base" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"base\" is a dictionary; it must "
        "NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["base"] = {}

    validate_keys_subset(**kwargs)


def test_keys_subset_depth_not_int() -> None:
    """
        Tests there is an exception if the value of the "depth"
        parameter is not an integer.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "depth": "1",
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "depth" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"depth\" is an integer; it must "
        "NOT be a integer to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: The expected type of "depth" is an integer type.
    # -------------------------------------------------------------------------

    # Must be an integer.
    kwargs["depth"] = 0

    validate_keys_subset(**kwargs)


def test_keys_subset_dictionary_not_dict() -> None:
    """
        Tests there is an exception if the value of the "dictionary"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": 9,
        "depth": 0,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "dictionary" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"dictionary\" is a dictionary; it "
        "must NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["dictionary"] = {}

    validate_keys_subset(**kwargs)


def test_keys_subset_exception_not_bool() -> None:
    """
        Tests there is an exception if the value of the "exception"
        parameter is not a boolean.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "depth": 0,
        "exception": 1,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "exception" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"exception\" is a boolean value; "
        "it must NOT be a boolean number to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a boolean.
    kwargs["exception"] = True

    validate_keys_subset(**kwargs)


def test_keys_subset_validate_keys_subset_basic() -> None:
    """
        Tests the validate_keys_subkeys function for valid and invalid
        cases.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": cp.deepcopy(BASE),
        "dictionary": cp.deepcopy(BASE),
        "depth": -1,
        "exception": False,
    }

    # -------------------------------------------------------------------------
    # Test 1: The dictionaries are different, but the first is a subset
    # of the second.
    # -------------------------------------------------------------------------

    # Remove the entries.
    del kwargs["dictionary"]["zero_1"]

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The dictionaries are different, but the first is a "
        "subset of the second."
    )

    assert validate_keys_subset(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 2: The dictionaries are different, and must raise an exception.
    # -------------------------------------------------------------------------

    # Set the values.
    extra_key: str = "whatever_key"
    kwargs["dictionary"][extra_key] = "Raise an error!"
    kwargs["exception"] = True

    # Set the message in case an error happens.
    flag: bool = False
    message = (
        "Test 2: An exception should be raised, since it has been "
        "requested."
    )

    # Must throw a WrongKeysSubsetError.
    try:
        validate_keys_subset(**kwargs)

    except WrongKeysSubsetError:
        flag = True

    assert flag, message

    del kwargs["dictionary"][extra_key]

    # -------------------------------------------------------------------------
    # Test 3: The dictionaries are the same.
    # -------------------------------------------------------------------------

    # Set the values.
    kwargs["dictionary"] = kwargs["base"]

    # Set the message in case an error happens.
    message = "Test 3: Dictionaries should be the same in this case."

    assert validate_keys_subset(**kwargs), message


def test_keys_subset_validate_keys_subset_level() -> None:
    """
        Tests the validate_keys_equal function for valid and invalid cases.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": cp.deepcopy(BASE),
        "dictionary": cp.deepcopy(BASE),
        "depth": 2,
        "exception": False,
    }

    # Remove the deepest level.
    del kwargs["dictionary"]["zero_0"]["one_0"]["two_0"]

    # -------------------------------------------------------------------------
    # Test 1: The dictionaries are different beyond the second level
    # (where the base level is the zeroth level).
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The dictionaries must be different; at depth 2, the "
        "dictionaries do not have the same keys."
    )

    assert not validate_keys_subset(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 2: The dictionaries must be the same at the base (zeroth) and
    # first level.
    # -------------------------------------------------------------------------

    for i in range(0, 2):
        # Set the level.
        kwargs["depth"] = i

        # Set the message in case an error happens.
        message = (
            f"Test 2: No exception should be raised until depth level 2; "
            f"current depth level: {i}. Remember that the depth is "
            f"zero-based."
        )

        assert validate_keys_subset(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 3: Unrestricted should, of course, be False.
    # -------------------------------------------------------------------------

    # Must throw an exception.
    kwargs["depth"] = 100000
    kwargs["exception"] = True

    # Set the message in case an error happens.
    flag: bool = False
    message = (
        "An exception should be raised, since the depth level is greater "
        "than the depth of the base dictionary."
    )

    # Must throw a WrongKeysSubsetError.
    try:
        validate_keys_subset(**kwargs)

    except WrongKeysSubsetError:
        flag = True

    assert flag, message


def test_keys_subset_and_typebase_not_dict() -> None:
    """
        Tests there is an exception if the value of the "base"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": 9,
        "dictionary": {},
        "extract": True,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "base" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"base\" is a dictionary; it must "
        "NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["base"] = {}

    validate_keys_subset_and_type(**kwargs)


def test_keys_subset_and_typebase_extract_not_bool() -> None:
    """
        Tests there is an exception if the value of the "extract"
        parameter is not a boolean.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "extract": "1",
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "depth" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"extract\" is a boolean; it must "
        "NOT be a boolean to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # Must be an integer.
    kwargs["extract"] = False

    validate_keys_subset_and_type(**kwargs)


def test_keys_subset_and_typebase_not_dict() -> None:
    """
        Tests there is an exception if the value of the "dictionary"
        parameter is not a dictionary.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": 9,
        "extract": False,
        "exception": True,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "dictionary" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"dictionary\" is a dictionary; it "
        "must NOT be a dictionary to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a dictionary.
    kwargs["dictionary"] = {}

    validate_keys_subset_and_type(**kwargs)


def test_keys_subset_and_typebase_exception_not_bool() -> None:
    """
        Tests there is an exception if the value of the "exception"
        parameter is not a boolean.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": {},
        "dictionary": {},
        "extract": False,
        "exception": 1,
    }

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "exception" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"exception\" is a boolean value; "
        "it must NOT be a boolean number to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be a boolean.
    kwargs["exception"] = True

    validate_keys_subset_and_type(**kwargs)


def test_keys_subset_and_typebase_validate_keys_subset_basic() -> None:
    """
        Tests the validate_keys_subkeys function for valid and invalid
        cases.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "base": cp.deepcopy(BASE),
        "dictionary": cp.deepcopy(BASE),
        "extract": True,
        "exception": False,
    }

    # -------------------------------------------------------------------------
    # Test 1: The dictionaries are different, but the first is a subset
    # of the second.
    # -------------------------------------------------------------------------

    # Remove the entries.
    del kwargs["dictionary"]["zero_1"]

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The dictionaries are different, but the first is a "
        "subset of the second."
    )

    assert validate_keys_subset_and_type(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 2: The dictionaries are different, and must raise an exception.
    # -------------------------------------------------------------------------

    # Set the values.
    extra_key: str = "whatever_key"
    flag: bool = False
    kwargs["dictionary"][extra_key] = "Raise an error!"
    kwargs["exception"] = True

    # Set the message in case an error happens.
    message = (
        "Test 2: An exception should be raised, since it has been "
        "requested."
    )

    # Must throw a WrongKeysSubsetAndTypeError.
    try:
        validate_keys_subset_and_type(**kwargs)

    except WrongKeysSubsetAndTypeError:
        flag = True

    assert flag, message

    del kwargs["dictionary"][extra_key]

    # -------------------------------------------------------------------------
    # Test 3: The dictionaries are the same.
    # -------------------------------------------------------------------------

    # Set the values.
    kwargs["dictionary"] = kwargs["base"]

    # Set the message in case an error happens.
    message = "Test 3: Dictionaries should be the same in this case."

    assert validate_keys_subset_and_type(**kwargs), message

    # -------------------------------------------------------------------------
    # Test 4: Not extracting types must raise a ValueError.
    # -------------------------------------------------------------------------

    # Set the values.
    kwargs["extract"] = False
    kwargs["base"]["zero_0"]["one_0"]["two_0"] = "Hello!"

    # Set the message in case an error happens.
    flag = False
    message = (
        "Test 4: One of the types at the end of the base dictionary has "
        "the wrong type, this should raise a ValueError."
    )

    # Must throw a ValueError.
    try:
        validate_keys_subset_and_type(**kwargs)

    except ValueError:
        flag = True

    assert flag, message
