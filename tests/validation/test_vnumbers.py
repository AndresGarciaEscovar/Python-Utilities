"""
    Contains the unittests for the number validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import unittest

# User.
from gutilities.exceptions.enumbers import (
    AboveBelowBoundError, NotInRangeError
)
from gutilities.validation.vnumbers import (
    validate_greater_than,
    validate_in_range,
    validate_less_than
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestValidateGreaterThan(unittest.TestCase):
    """
        Tests for the greater than numerical validation functions in the
        module.
    """
    # /////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////

    def test_bound_not_real(self):
        """
            Tests there is an exception if the value of the "bound"
            parameter is not a real number.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": 1,
            "bound": "0",
            "include": False,
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: The "bound" parameter is not the correct type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"bound\" is a real number; it must "
            "NOT be a real number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_greater_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["bound"] = 0

        validate_greater_than(**kwargs)

    def test_exception_not_bool(self):
        """
            Tests there is an exception if the value of the "exception"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": 1,
            "bound": 0,
            "include": False,
            "exception": 1,
        }

        # ---------------------------------------------------------------------
        # Test 1: The "exception" parameter is not the correct type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"exception\" is a boolean value; "
            "it must NOT be a boolean number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_greater_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_greater_than(**kwargs)

    def test_include_not_bool(self):
        """
            Tests there is an exception if the value of the "include"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": 1,
            "bound": 0,
            "include": 4,
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: The "include" parameter is not the correct type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"include\" is a boolean value; it "
            "must NOT be a boolean number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_greater_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["include"] = True

        validate_greater_than(**kwargs)

    @unittest.skip("Skipped until refactored.")
    def test_validate_greater_than(self):
        """
            Tests the validate_greater_than function in the module.
        """
        # ------------------- Value is greater than bound ------------------- #

        # Messages.
        emessage: str = (
            "The value must be greater than the bound, and it should yield a "
            "True result; one of these conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": 1,
            "bound": 0,
            "include": False,
            "exception": True,
        }

        # Must be True.
        self.assertTrue(validate_greater_than(**kwargs), msg=emessage)

        # ------------------ Value is greater than or equal ----------------- #

        # Messages.
        emessage = (
            "The value must be equal to the bound, the \"include\" flag must "
            "be set to True, and it should yield a True result; one of these "
            "conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": True,
            "exception": True,
        }

        # Must be True.
        self.assertTrue(validate_greater_than(**kwargs), msg=emessage)

        # ------------------------ Value is less than ----------------------- #

        # Messages.
        emessage = (
            "The value must be less than the bound and it should yield a "
            "False result; one of these conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": -2,
            "bound": 0,
            "include": False,
            "exception": False,
        }

        # Must be True.
        self.assertFalse(validate_greater_than(**kwargs), msg=emessage)

        # ------------------- Value is less than or equal ------------------- #

        # Messages.
        emessage = (
            "The value must be equal to the bound, the \"include\" flag must "
            "be turned off, and it should yield a False result; one of these "
            "conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": False,
            "exception": False,
        }

        # Must be True.
        self.assertFalse(validate_greater_than(**kwargs), msg=emessage)

        # --------------------- Must throw an exception --------------------- #

        # Messages.
        emessage = "An exception must be raised."

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": False,
            "exception": True,
        }

        # Must be True.
        with self.assertRaises(AboveBelowBoundError, msg=emessage):
            validate_greater_than(**kwargs)

    def test_value_not_real(self):
        """
            Tests there is an exception if the value of the "value"
            parameter is not a real number.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": "1",
            "bound": 0,
            "include": False,
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: The "value" parameter is not the correct type.
        # ---------------------------------------------------------------------

        # Messages.
        emessage: str = (
            "Test 1: The expected type of \"value\" is a real number; it must "
            "NOT be a real number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=emessage):
            validate_greater_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["value"] = 1

        validate_greater_than(**kwargs)


class TestValidateInRange(unittest.TestCase):
    """
        Tests for the numerical validation functions in the module.
    """
    # /////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////

    @unittest.skip("Skipped until refactored.")
    def test_crange_not_real_tuple(self):
        """
            Tests there is an exception if the value of the "crange"
            parameter is not a tuple of real numbers.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"crange\" is a not a 2-tuple of real "
            "numbers; it must NOT be a tuple of this type to raise an "
            "exception."
        )

        # ------------------------- Not a tuple ------------------------- #

        # Values.
        kwargs: dict = {
            "value": 1,
            "crange": 3,
            "include": (True, True),
            "exception": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_in_range(**kwargs)

        # ------------------ 2-tuple of complex numbers ----------------- #

        # 2-tuple of complex numbers.
        kwargs["crange"] = (0, 0 + 1j)

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_in_range(**kwargs)

        # ------------------- 3-tuple of real numbers ------------------- #

        # Tuple longer than 2 elements.
        kwargs["crange"] = (0, 1, 2)

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_in_range(**kwargs)

        # -------------------- Numbers in wrong order ------------------- #

        # Tuple longer than 2 elements.
        kwargs["crange"] = (3, 1)

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_in_range(**kwargs)

        # ------------------ No error should be raised ------------------ #

        # Tuple longer than 2 elements.
        kwargs["crange"] = (1, 4)

        validate_in_range(**kwargs)

    def test_crange_tuple_ordering(self):
        """
            Tests there is an exception if the value of the "crange"
            parameter is not a tuple of real numbers.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": 2,
            "crange": (3, 1),
            "include": (True, True),
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: Non-organized tuple is passed.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"crange\" is an non-organized "
            "2-tuple of real numbers; it must NOT be organized to raise an "
            "exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Organized tuple is passed; no error should be raised.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: The expected type of \"crange\" IS an organized "
            "2-tuple of real numbers."
        )

        # Tuple is properly organized.
        kwargs["crange"] = (1, 3)

        validate_in_range(**kwargs)

    def test_exception_not_bool(self):
        """
            Tests there is an exception if the value of the "exception"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": 1,
            "crange": (0, 3),
            "include": (True, True),
            "exception": 1,
        }

        # ---------------------------------------------------------------------
        # Test 1: The "exception" parameter has the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"exception\" is a boolean value; "
            "it must NOT be a boolean number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_in_range(**kwargs)

    @unittest.skip("Skipped until refactored.")
    def test_include_not_bool_tuple(self):
        """
            Tests there is an exception if the value of the "include"
            parameter is not a tuple of boolean flags.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": 1,
            "crange": (0, 3),
            "include": 1,
            "exception": True,
        }

        # ------------------------- Not a tuple ------------------------- #

        # Set the message in case an error happens.
        emessage: str = (
            "The expected type of \"include\" is a not a 2-tuple of "
            "boolean flags; it must NOT be a tuple of this type to raise "
            "an exception."
        )


        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_in_range(**kwargs)

        # --------------- 2-tuple of none boolean numbers --------------- #

        # 2-tuple of complex numbers.
        kwargs["include"] = (0, True)

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_in_range(**kwargs)

        # ------------------- 3-tuple of boolean flags ------------------ #

        # Tuple longer than 2 elements.
        kwargs["include"] = (True, False, True)

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_in_range(**kwargs)

        # ------------------ No error should be raised ------------------ #

        # Tuple longer than 2 elements.
        kwargs["include"] = (True, True)

        validate_in_range(**kwargs)

    @unittest.skip("Skipped until refactored.")
    def test_validate_in_range(self):
        """
            Tests there is an exception if the value of the "include"
            parameter is not a tuple of boolean flags.
        """
        # Messages.
        emessage: str = (
            "The parameters are out of range; they MUST be in range."
        )

        # --------------------- Value in the middle --------------------- #

        # Values.
        kwargs: dict = {
            "value": 1,
            "crange": (0, 3),
            "include": (False, False),
            "exception": False,
        }

        # Must be True.
        self.assertTrue(validate_in_range(**kwargs), msg=emessage)

        # ----------------- End values are now included ----------------- #

        # Values.
        kwargs["include"] = (True, True)

        # Must be True.
        self.assertTrue(validate_in_range(**kwargs), msg=emessage)

        # The other end.
        kwargs["value"] = 1

        # Must be True.
        self.assertTrue(validate_in_range(**kwargs), msg=emessage)

        # ----------------------- Value at one end ---------------------- #

        emessage = (
            "The parameters are in range; they MUST be out of range."
        )

        # Values.
        kwargs["crange"] = (1, 3)
        kwargs["include"] = (False, False)

        # Must be False.
        self.assertFalse(validate_in_range(**kwargs), msg=emessage)

        # -------------------- Value at the other end ------------------- #

        # Values.
        kwargs["value"] = 3

        # Must be False.
        self.assertFalse(validate_in_range(**kwargs), msg=emessage)

        # ----------------------- Exclude the ends ---------------------- #

        # Values.
        kwargs["value"] = 1
        kwargs["exception"] = True

        # Must raise an assertion error.
        with self.assertRaises(NotInRangeError, msg=emessage):
            validate_in_range(**kwargs)

        # The other end.
        kwargs["value"] = 3

        # Must raise an assertion error.
        with self.assertRaises(NotInRangeError, msg=emessage):
            validate_in_range(**kwargs)


class TestValidateLessThan(unittest.TestCase):
    """
        Tests for the greater than numerical validation functions in the
        module.
    """
    # /////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////

    def test_bound_not_real(self):
        """
            Tests there is an exception if the value of the "bound"
            parameter is not a real number.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": -1,
            "bound": "0",
            "include": False,
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "bound" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        emessage: str = (
            "The expected type of \"bound\" is a real number; it must "
            "NOT be a real number to raise an exception."
        )

        # Must raise an assertion error.
        with self.assertRaises(ValueError, msg=emessage):
            validate_less_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be an integer.
        kwargs["bound"] = 0

        validate_less_than(**kwargs)

    @unittest.skip("Skipped until refactored.")
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
            "value": -1,
            "bound": 0,
            "include": False,
            "exception": 1,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_less_than(**kwargs)

        # Must be a boolean.
        kwargs["exception"] = True

        validate_less_than(**kwargs)

    @unittest.skip("Skipped until refactored.")
    def test_include_not_bool(self):
        """
            Tests there is an exception if the value of the "include"
            parameter is not a boolean.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"include\" is a boolean value; it must "
            "NOT be a boolean number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": -1,
            "bound": 0,
            "include": 4,
            "exception": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_less_than(**kwargs)

        # Must be a boolean.
        kwargs["include"] = True

        validate_less_than(**kwargs)

    @unittest.skip("Skipped until refactored.")
    def test_validate_less_than(self):
        """
            Tests the validate_less_than function in the module.
        """
        # --------------------- Value is less than bound -------------------- #

        # Messages.
        emessage: str = (
            "The value must be less than the bound, and it should yield a "
            "True result; one of these conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": -1,
            "bound": 0,
            "include": False,
            "exception": True,
        }

        # Must be True.
        self.assertTrue(validate_less_than(**kwargs), msg=emessage)

        # ------------------- Value is less than or equal ------------------- #

        # Messages.
        emessage = (
            "The value must be equal to the bound, the \"include\" flag must "
            "be set to True, and it should yield a True result; one of these "
            "conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": True,
            "exception": True,
        }

        # Must be True.
        self.assertTrue(validate_less_than(**kwargs), msg=emessage)

        # ---------------------- Value is greater than ---------------------- #

        # Messages.
        emessage = (
            "The value must be greater than the bound and it should yield a "
            "False result; one of these conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": 1,
            "bound": 0,
            "include": False,
            "exception": False,
        }

        # Must be True.
        self.assertFalse(validate_less_than(**kwargs), msg=emessage)

        # ------------------- Value is less than or equal ------------------- #

        # Messages.
        emessage = (
            "The value must be equal to the bound, the \"include\" flag must "
            "be turned off, and it should yield a False result; one of these "
            "conditions is not met."
        )

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": False,
            "exception": False,
        }

        # Must be True.
        self.assertFalse(validate_less_than(**kwargs), msg=emessage)

        # --------------------- Must throw an exception --------------------- #

        # Messages.
        emessage = "An exception must be raised."

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": False,
            "exception": True,
        }

        # Must be True.
        with self.assertRaises(AboveBelowBoundError, msg=emessage):
            validate_less_than(**kwargs)

    @unittest.skip("Skipped until refactored.")
    def test_value_not_real(self):
        """
            Tests there is an exception if the value of the "value"
            parameter is not a real number.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"value\" is a real number; it must "
            "NOT be a real number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": "1",
            "bound": 0,
            "include": False,
            "exception": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage):
            validate_less_than(**kwargs)

        # Must be a boolean.
        kwargs["value"] = -1

        validate_less_than(**kwargs)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
