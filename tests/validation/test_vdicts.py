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
from gutilities.validation.vdicts import (
    validate_keys_equal,
    validate_keys_subset
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


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestValidateDictionaryKeysEqual(unittest.TestCase):
    """
        Tests that the dictionary keys of two dictionaries are the same to a
        given depth.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_base_not_dict(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "base" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"base\" is a dictionary; it must "
            "NOT be a dictionary to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a dictionary.
        kwargs["base"] = {}

        validate_keys_equal(**kwargs)

    def test_depth_not_int(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "depth" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"depth\" is an integer; it must "
            "NOT be a integer to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # Must be an integer.
        kwargs["depth"] = 0

        validate_keys_equal(**kwargs)

    def test_dictionary_not_dict(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "dictionary" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"dictionary\" is a dictionary; it "
            "must NOT be a dictionary to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a dictionary.
        kwargs["dictionary"] = {}

        validate_keys_equal(**kwargs)

    def test_exception_not_bool(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "exception" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"exception\" is a boolean value; "
            "it must NOT be a boolean number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_keys_equal(**kwargs)

    def test_validate_keys_equal_basic(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The dictionaries are different.
        # ---------------------------------------------------------------------

        # Remove the entries.
        del kwargs["dictionary"]["zero_1"]

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The dictionaries have the same keys; this should not "
            "happen."
        )

        self.assertFalse(validate_keys_equal(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: The dictionaries are different, and must raise an exception.
        # ---------------------------------------------------------------------

        # Set the values.
        kwargs["exception"] = True

        # Set the message in case an error happens.
        message = (
            "Test 2: An exception should be raised, since it has been "
            "requested."
        )

        with self.assertRaises(WrongKeysError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 3: The dictionaries are the same.
        # ---------------------------------------------------------------------

        # Set the values.
        kwargs["dictionary"] = kwargs["base"]

        # Set the message in case an error happens.
        message = "Test 3: Dictionaries should be the same in this case."

        self.assertTrue(validate_keys_equal(**kwargs), msg=message)

    def test_validate_keys_equal_level(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The dictionaries are different beyond the second level
        # (where the base level is the zeroth level).
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The dictionaries must be different; at depth 2, the "
            "dictionaries do not have the same keys."
        )

        self.assertFalse(validate_keys_equal(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: The dictionaries must be the same at the base (zeroth) and
        # first level.
        # ---------------------------------------------------------------------

        for i in range(0, 2):
            # Set the level.
            kwargs["depth"] = i

            # Set the message in case an error happens.
            message = (
                f"Test 2: No exception should be raised until depth level 2; "
                f"current depth level: {i}. Remember that the depth is "
                f"zero-based."
            )

            self.assertTrue(validate_keys_equal(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 3: Unrestricted should, of course, be False.
        # ---------------------------------------------------------------------

        # Must throw an exception.
        kwargs["depth"] = 10000
        kwargs["exception"] = True

        # Set the message in case an error happens.
        message = (
            "An exception should be raised, since the depth level is greater "
            "than the depth of the base dictionary."
        )

        with self.assertRaises(WrongKeysError, msg=message):
            validate_keys_equal(**kwargs)


class TestValidateDictionaryKeysSubset(unittest.TestCase):
    """
        Tests that the dictionary keys of a given dictionary is a subdictionary
        of another dictionary to a given depth.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_base_not_dict(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "base" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"base\" is a dictionary; it must "
            "NOT be a dictionary to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a dictionary.
        kwargs["base"] = {}

        validate_keys_equal(**kwargs)

    def test_depth_not_int(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "depth" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"depth\" is an integer; it must "
            "NOT be a integer to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # Must be an integer.
        kwargs["depth"] = 0

        validate_keys_equal(**kwargs)

    def test_dictionary_not_dict(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "dictionary" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"dictionary\" is a dictionary; it "
            "must NOT be a dictionary to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a dictionary.
        kwargs["dictionary"] = {}

        validate_keys_equal(**kwargs)

    def test_exception_not_bool(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "exception" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"exception\" is a boolean value; "
            "it must NOT be a boolean number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_keys_equal(**kwargs)

    def test_validate_keys_equal_basic(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The dictionaries are different.
        # ---------------------------------------------------------------------

        # Remove the entries.
        del kwargs["dictionary"]["zero_1"]

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The dictionaries have the same keys; this should not "
            "happen."
        )

        self.assertFalse(validate_keys_equal(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: The dictionaries are different, and must raise an exception.
        # ---------------------------------------------------------------------

        # Set the values.
        kwargs["exception"] = True

        # Set the message in case an error happens.
        message = (
            "Test 2: An exception should be raised, since it has been "
            "requested."
        )

        with self.assertRaises(WrongKeysError, msg=message):
            validate_keys_equal(**kwargs)

        # ---------------------------------------------------------------------
        # Test 3: The dictionaries are the same.
        # ---------------------------------------------------------------------

        # Set the values.
        kwargs["dictionary"] = kwargs["base"]

        # Set the message in case an error happens.
        message = "Test 3: Dictionaries should be the same in this case."

        self.assertTrue(validate_keys_equal(**kwargs), msg=message)

    def test_validate_keys_equal_level(self):
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

        # ---------------------------------------------------------------------
        # Test 1: The dictionaries are different beyond the second level
        # (where the base level is the zeroth level).
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The dictionaries must be different; at depth 2, the "
            "dictionaries do not have the same keys."
        )

        self.assertFalse(validate_keys_equal(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: The dictionaries must be the same at the base (zeroth) and
        # first level.
        # ---------------------------------------------------------------------

        for i in range(0, 2):
            # Set the level.
            kwargs["depth"] = i

            # Set the message in case an error happens.
            message = (
                f"Test 2: No exception should be raised until depth level 2; "
                f"current depth level: {i}. Remember that the depth is "
                f"zero-based."
            )

            self.assertTrue(validate_keys_equal(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 3: Unrestricted should, of course, be False.
        # ---------------------------------------------------------------------

        # Must throw an exception.
        kwargs["depth"] = 10000
        kwargs["exception"] = True

        # Set the message in case an error happens.
        message = (
            "An exception should be raised, since the depth level is greater "
            "than the depth of the base dictionary."
        )

        with self.assertRaises(WrongKeysError, msg=message):
            validate_keys_equal(**kwargs)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
