"""
    Contains the functions for string validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import copy as cp
import unittest

# User.
from gutilities.validation.vstrings import validate_string_empty


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestValidateStringEmpty(unittest.TestCase):
    """
        Contains the tests for the validate_string_empty function.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_exception_not_bool(self):
        """
            Tests there is an exception if the value of the "exception"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": "",
            "notempty": False,
            "sstrip": False,
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
            validate_string_empty(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_string_empty(**kwargs)

    def test_notempty_not_bool(self):
        """
            Tests there is an exception if the value of the "notempty"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": "",
            "notempty": 1,
            "sstrip": False,
            "exception": False,
        }

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "notempty" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"notempty\" is a boolean value; "
            "it must NOT be a boolean number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_string_empty(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["notempty"] = True

        validate_string_empty(**kwargs)

    def test_sstrip_not_bool(self):
        """
            Tests there is an exception if the value of the "sstrip"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": "",
            "notempty": False,
            "sstrip": 1,
            "exception": False,
        }

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "sstrip" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "The expected type of \"sstrip\" is a boolean value; it must "
            "NOT be a boolean number to raise an exception."
        )

        # Must raise an assertion error.
        with self.assertRaises(ValueError, msg=message):
            validate_string_empty(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["sstrip"] = True

        validate_string_empty(**kwargs)

    def test_validate_string_empty(self):
        """
            Tests the validate_string_empty function when the string is empty.
        """
        # Auxiliary variables.
        dictionary: dict = {
            "value": "",
            "notempty": False,
            "sstrip": False,
            "exception": False,
        }
        kwargs: dict = cp.deepcopy(dictionary)

        # ---------------------------------------------------------------------
        # Test 1: String should be completely empty, but it is not.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The string is not empty; it should be empty to pass the "
            "test."
        )

        self.assertTrue(validate_string_empty(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: String is made of spaces, newlines, etc., but stripped.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: Should evaluate to True with stripping; it should be "
            "empty to pass the test or have only spaces, newlines, etc."
        )

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["sstrip"] = True
        dictionary["value"] = "  \n\t  \t\n  "

        self.assertTrue(validate_string_empty(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 3: String is completely empty and stripped.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 3: Should evaluate to True with stripping; it should be "
            "empty to pass the test."
        )

        # Set the proper values.
        dictionary = cp.deepcopy(kwargs)

        self.assertTrue(validate_string_empty(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 4: String is not empty, but stripped.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 4: Should evaluate to False; it should NOT be empty to pass "
            "the test."
        )

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["value"] = "kkkkkk"
        dictionary["sstrip"] = True

        self.assertFalse(validate_string_empty(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 5: String must not be empty.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 5: Should evaluate to True; it should NOT be empty to "
            "pass the test."
        )

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["value"] = "kkkkkk"
        dictionary["notempty"] = True

        self.assertTrue(validate_string_empty(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 6: String made of spaces, tabs, etc., but must be True.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 6: Should evaluate to True; it should NOT be empty to pass "
            "the test."
        )

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["value"] = "   \n\t\t\t  "
        dictionary["notempty"] = True

        self.assertTrue(validate_string_empty(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 7: Must raise an exception.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 7: Should evaluate to True; it should NOT be empty to pass "
            "the test."
        )

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["value"] = "   \n\t\t\t  "
        dictionary["notempty"] = True
        dictionary["sstrip"] = True
        dictionary["exception"] = True

        with self.assertRaises(ValueError, msg=message):
            validate_string_empty(**dictionary)
