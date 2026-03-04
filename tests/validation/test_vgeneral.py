"""
    Contains the unittests for the general errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import unittest

from typing import Callable

# User.
from gutilities.exceptions.ecollections import WrongLengthError
from gutilities.exceptions.etypes import WrongTypeError
from gutilities.validation.vgeneral import validate_length, validate_type


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestValidateLength(unittest.TestCase):
    """
        Tests for the length validation of collections.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_correct_values(self):
        """
            Tests the value is false for valid values for the validation
            function.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": (1, 2),
            "length": 2,
            "exception": False,
        }
        length: int = kwargs["length"]

        # ---------------------------------------------------------------------
        # Test 1: The collections have a specific length..
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            f"Test 1: The given collection does not have a length of "
            f"{length}."
        )

        for collection in (set, tuple, list, "dict"):
            # Format properly.
            if collection == "dict":
                kwargs["value"] = dict.fromkeys(kwargs["value"]).keys()

            else:
                kwargs["value"] = collection(kwargs["value"])

            self.assertTrue(validate_length(**kwargs), message)

    def test_exception_not_bool(self):
        """
            Tests there is an exception if the value of the "exception"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": (1, 2),
            "length": 2,
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
            validate_length(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_length(**kwargs)

    def test_incorrect_values(self):
        """
            Tests the value is false for valid values for the validation
            function.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": (1, 2),
            "length": None,
            "exception": False,
        }
        length_expected: int = len(kwargs["value"])

        # ---------------------------------------------------------------------
        # Test 1: The length is greater than or less than the expected length.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str =  (
            f"Test 1: The given collection has a length of {length_expected}; "
            f"this should not be happening."
        )

        # Must return False.
        for length in tuple(length_expected + x for x in (-1, 1)):
            kwargs["length"] = length
            self.assertFalse(validate_length(**kwargs), message)

        # ---------------------------------------------------------------------
        # Test 2: The length is greater than or less than the expected length;
        # must raise an exception, since it is required.
        # ---------------------------------------------------------------------

        # Tests exceptions are raised when needed.
        kwargs["exception"] = True

        # Set the message in case an error happens.
        message = (
            f"Test 2: The \"exception\" flag is set to {True}, this should be "
            f"raising an error/exception, since the given collection has a "
            f"length of {length_expected}."
        )

        for length in tuple(length_expected + x for x in (-1, 1)):
            kwargs["length"] = length

            with self.assertRaises(WrongLengthError, msg=message):
                validate_length(**kwargs)

    @unittest.skip("Skip until validated.")
    def test_length_positive(self):
        """
            Tests there is an exception if the value of the length is not
            a positive integer, or zero.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": (1, 2),
            "length": -1,
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "length" is a positive integer number.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"length\" is a positive integer, "
            "or zero; it must be a negative integer or a non-integer number "
            "to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_length(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: The expected type of "length" must be an integer.
        # ---------------------------------------------------------------------

        message = (
            "Test 2: The expected type of \"length\" is a positive integer, "
            "or zero; it must be a negative integer or a non-integer number "
            "to raise an exception."
        )

        # Cannot be a non-integer number.
        kwargs["length"] = 1.2

        with self.assertRaises(ValueError, msg=message):
            validate_length(**kwargs)

    @unittest.skip("Skip until validated.")
    def test_value_not_a_collection(self):
        """
            Tests there is an exception raise when the value passed for
            validation is not a collection.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"value\" is a \"Collection\"; it must "
            "NOT be a collection to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": 1,
            "length": -1,
            "exception": True,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_length(**kwargs)


class TestValidateType(unittest.TestCase):
    """
        Tests for the type validation function.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    @unittest.skip("Skip until validated.")
    def test_exception_not_bool(self):
        """
            Tests there is an exception if the value of the "exception"
            parameter is not a boolean.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"exception\" is a boolean value; it must "
            "NOT be a boolean number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": "(1, 2)",
            "vtype": str,
            "exception": 1,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_type(**kwargs)

        # Must be a boolean.
        kwargs["exception"] = True

        validate_type(**kwargs)

    @unittest.skip("Skip until validated.")
    def test_type_wrong(self):
        """
            Tests there is an exception if the type value is of the wrong type.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"vtype\" must be a \"Type\" or None "
            "value. Notice that Type is a \"_SpecialType\" object itself."
        )

        # Values.
        kwargs: dict = {
            "value": "(1, 2)",
            "vtype": "str",
            "exception": True,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_type(**kwargs)

        # Must be a boolean.
        kwargs["vtype"] = str

        validate_type(**kwargs)

    @unittest.skip("Skip until validated.")
    def test_type_wrong_element(self):
        """
            Tests there is an exception if the type of the value being validated
            is of the wrong type and False is returned; or an exception is raised
            if the "exception" flag is set to True.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"vtype\" must be a \"Type\" or None "
            "value. Notice that Type is a \"_SpecialType\" object itself."
        )

        # ----------------- Incorrect values, with exception ---------------- #

        # Values.
        kwargs: dict = {
            "value": "(1, 2)",
            "vtype": int,
            "exception": True,
        }

        # Messages must match.
        with self.assertRaises(WrongTypeError, msg=emessage):
            validate_type(**kwargs)

        # ------------------ Incorrect values, no exception ----------------- #

        # Must yield false.
        kwargs["vtype"] = int
        kwargs["exception"] = False

        self.assertFalse(validate_type(**kwargs))

        # -------------------------- Correct values ------------------------- #

        # Must be yield True.
        kwargs["vtype"] = str

        self.assertTrue(validate_type(**kwargs))


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
