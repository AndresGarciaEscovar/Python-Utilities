"""
    Contains the unittests for the number validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import copy as cp
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

    def test_greater_than_bound_not_real(self) -> None:
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

    def test_greater_than_exception_not_bool(self) -> None:
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

    def test_greater_than_include_not_bool(self) -> None:
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

    def test_greater_than_validate_greater_than(self) -> None:
        """
            Tests the validate_greater_than function in the module.
        """
        # Auxiliary variables.
        dictionary: dict = {
            "value": 1,
            "bound": 0,
            "include": False,
            "exception": True,
        }
        kwargs: dict = cp.deepcopy(dictionary)

        # ---------------------------------------------------------------------
        # Test 1: Value is greater than bound.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The value must be greater than the bound, and it should "
            "yield a True result; one of these conditions is not met."
        )

        self.assertTrue(validate_greater_than(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: Value is greater than or equal.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: The value must be equal to the bound, the \"include\" "
            "flag must be set to True, and it should yield a True result; one "
            "of these conditions is not met."
        )

        # Set the values.
        dictionary["include"] = True
        dictionary["value"] = 0

        self.assertTrue(validate_greater_than(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 3: Value is less than.
        # ---------------------------------------------------------------------

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["exception"] = False
        dictionary["include"] = False
        dictionary["value"] = -2

        # Set the message in case an error happens.
        message = (
            "Test 3: The value must be less than the bound and it should "
            "yield a False result; one of these conditions is not met."
        )

        self.assertFalse(validate_greater_than(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 4: Value is less than or equal.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 4: The value must be equal to the bound, the \"include\" "
            "flag must be turned off, and it should yield a False result; one "
            "of these conditions is not met."
        )

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["exception"] = False
        dictionary["value"] = 0

        self.assertFalse(validate_greater_than(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 5: Must throw an exception.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 5: An exception must be raised."

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["exception"] = True
        dictionary["value"] = 0

        with self.assertRaises(AboveBelowBoundError, msg=message):
            validate_greater_than(**dictionary)

    def test_greater_than_value_not_real(self) -> None:
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

    def test_in_range_crange_not_real_tuple(self) -> None:
        """
            Tests there is an exception if the value of the "crange"
            parameter is not a tuple of real numbers.
        """
        # Auxiliary variables.
        dictionary: dict = {
            "value": 1,
            "crange": 3,
            "include": (True, True),
            "exception": True,
        }
        kwargs: dict = cp.deepcopy(dictionary)

        # ---------------------------------------------------------------------
        # Test 1: Not a tuple.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"crange\" is a not a 2-tuple of "
            "real numbers; it must NOT be a tuple of this type to raise an "
            "exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**dictionary)

        # ---------------------------------------------------------------------
        # Test 2: 2-tuple of complex numbers
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: One, or more, of the entries in the \"crange\" tuple are "
            "NOT real numbers, this must raise an error."
        )

        # 2-tuple of complex numbers.
        dictionary = cp.deepcopy(kwargs)
        dictionary["crange"] = (0, 0 + 1j)

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**dictionary)

        # ---------------------------------------------------------------------
        # Test 3: Tuple is longer than two entries.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 3: The tuple \"crange\" has more entries than required, "
            "this must raise an error."
        )

        # Tuple longer than 2 elements.
        dictionary = cp.deepcopy(kwargs)
        dictionary["crange"] = (0, 1, 2)

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**dictionary)

        # ---------------------------------------------------------------------
        # Test 4: Numbers in wrong order.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 4: The entries of \"crange\" are in the wrong order, this "
            "must raise an error."
        )

        # Biggest number goes before smallest number.
        dictionary = cp.deepcopy(kwargs)
        dictionary["crange"] = (3, 1)

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**dictionary)

        # ---------------------------------------------------------------------
        # Test 5: Entries are properly set.
        # ---------------------------------------------------------------------

        # Entries are as required.
        dictionary = cp.deepcopy(kwargs)
        dictionary["crange"] = (1, 4)

        validate_in_range(**dictionary)

    def test_in_range_crange_tuple_ordering(self) -> None:
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

    def test_in_range_exception_not_bool(self) -> None:
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

    def test_in_range_include_not_bool_tuple(self) -> None:
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

        # ---------------------------------------------------------------------
        # Test 1: Not a tuple.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"include\" is a not a 2-tuple of "
            "boolean variables; it must NOT be a tuple of this type to raise "
            "an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: 2-tuple of none boolean variables.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: The expected type of \"include\" is a not a 2-tuple of "
            "boolean flags; it must NOT be a tuple of this type to raise "
            "an exception."
        )

        # 2-tuple where the first entry is NOT a boolean variable.
        kwargs["include"] = (0, True)

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**kwargs)

        # ---------------------------------------------------------------------
        # Test 3: 3-tuple of boolean variables.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 3: The expected type of \"include\" is a not a 2-tuple of "
            "boolean flags; it is longer than required, this must raise an "
            "error."
        )

        # Tuple longer than 2 elements.
        kwargs["include"] = (True, False, True)

        with self.assertRaises(ValueError, msg=message):
            validate_in_range(**kwargs)

        # ---------------------------------------------------------------------
        # Test 4: No error should be raised.
        # ---------------------------------------------------------------------

        # Tuple is the correct size and with the correct content.
        kwargs["include"] = (True, True)

        validate_in_range(**kwargs)

    def test_in_range_validate_in_range(self) -> None:
        """
            Tests there is an exception if the value of the "include"
            parameter is not a tuple of boolean flags.
        """
        # Auxiliary variables.
        dictionary: dict = {
            "value": 1,
            "crange": (0, 3),
            "include": (False, False),
            "exception": False,
        }
        kwargs: dict = cp.deepcopy(dictionary)

        # ---------------------------------------------------------------------
        # Test 1: Value in the middle.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The parameters are out of range; they MUST be in range."
        )

        self.assertTrue(validate_in_range(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: End values are now included.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 2-a: Extreme case to the left, it is included."

        # Set the values.
        dictionary["include"] = (True, True)

        self.assertTrue(validate_in_range(**dictionary), msg=message)

        # Set the message in case an error happens.
        message = "Test 2-b: Extreme case to the right, it is included."

        # Set the values.
        dictionary["value"] = 1

        self.assertTrue(validate_in_range(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 3: Values at the ends are out of range.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 3-a: The value at the left end is not in the range; this "
            "value MUST be out of range."
        )

        # Set the values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["crange"] = (1, 3)
        dictionary["include"] = False, False
        dictionary["value"] = 1

        self.assertFalse(validate_in_range(**dictionary), msg=message)

        # Set the message in case an error happens.
        message = (
            "Test 3-b: The value at the right end is not in the range; this "
            "value MUST be out of range."
        )

        # Set the values.
        dictionary["value"] = 3

        self.assertFalse(validate_in_range(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 4: Values at the ends are out of range, an exception must be
        # raised.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 4-a: The value at the left end is not in the range; this "
            "value MUST be out of range and an exception must be raised."
        )

        # Set the values.
        dictionary["exception"] = True
        dictionary["value"] = 1

        with self.assertRaises(NotInRangeError, msg=message):
            validate_in_range(**dictionary)

        # Set the message in case an error happens.
        message = (
            "Test 4-b: The value at the right end is not in the range; this "
            "value MUST be out of range and an exception must be raised."
        )

        # Set the values.
        dictionary["value"] = 3

        with self.assertRaises(NotInRangeError, msg=message):
            validate_in_range(**dictionary)


class TestValidateLessThan(unittest.TestCase):
    """
        Tests for the greater than numerical validation functions in the
        module.
    """
    # /////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////

    def test_less_than_bound_not_real(self) -> None:
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
        message: str = (
            "Test 1: The expected type of \"bound\" is a real number; it must "
            "NOT be a real number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_less_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be an integer.
        kwargs["bound"] = 0

        validate_less_than(**kwargs)

    def test_less_than_exception_not_bool(self) -> None:
        """
            Tests there is an exception if the value of the "exception"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": -1,
            "bound": 0,
            "include": False,
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
            validate_less_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_less_than(**kwargs)

    def test_less_than_include_not_bool(self) -> None:
        """
            Tests there is an exception if the value of the "include"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "value": -1,
            "bound": 0,
            "include": 4,
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: The expected type of "include" is the wrong type.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The expected type of \"include\" is a boolean value; it "
            "must NOT be a boolean number to raise an exception."
        )

        with self.assertRaises(ValueError, msg=message):
            validate_less_than(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["include"] = True

        validate_less_than(**kwargs)

    def test_less_than_validate_less_than(self) -> None:
        """
            Tests the validate_less_than function in the module.
        """
        # Auxiliary variables.
        dictionary: dict = {
            "value": -1,
            "bound": 0,
            "include": False,
            "exception": True,
        }
        kwargs: dict = cp.deepcopy(dictionary)

        # ---------------------------------------------------------------------
        # Test 1: Value is less than bound.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The value must be less than the bound, and it should "
            "yield a True result; one of these conditions is not met."
        )

        self.assertTrue(validate_less_than(**kwargs), msg=message)

        # ---------------------------------------------------------------------
        # Test 2: Value is less than or equal.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: The value must be equal to the bound, the \"include\" "
            "flag must be set to True, and it should yield a True result; one "
            "of these conditions is not met."
        )

        # Set the proper values.
        dictionary["include"] = True
        dictionary["value"] = 0

        self.assertTrue(validate_less_than(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 3: Value is greater than.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 3: The value must be greater than the bound and it should "
            "yield a False result; one of these conditions is not met."
        )

        # Set the proper values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["exception"] = False
        dictionary["value"] = 1

        self.assertFalse(validate_less_than(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 4: Value is less than or equal.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 4: The value must be equal to the bound, the \"include\" "
            "flag must be turned off, and it should yield a False result; one "
            "of these conditions is not met."
        )

        # Set the proper values.
        dictionary = cp.deepcopy(kwargs)
        dictionary["exception"] = False
        dictionary["value"] = 0

        self.assertFalse(validate_less_than(**dictionary), msg=message)

        # ---------------------------------------------------------------------
        # Test 5: Must throw an exception.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 5: An exception must be raised."

        # Set the proper values.
        dictionary["exception"] = True

        with self.assertRaises(AboveBelowBoundError, msg=message):
            validate_less_than(**dictionary)


def test_less_than_value_not_real() -> None:
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

    # -------------------------------------------------------------------------
    # Test 1: The expected type of "value" is the wrong type.
    # -------------------------------------------------------------------------

    # Set the message in case an error happens.
    flag: bool = False
    message: str = (
        "Test 1: The expected type of \"value\" is a real number; it must "
        "NOT be a real number to raise an exception."
    )

    # Must throw a ValueError.
    try:
        validate_less_than(**kwargs)

    except ValueError:
        flag = True

    assert flag, message

    # -------------------------------------------------------------------------
    # Test 2: Correct types are chosen.
    # -------------------------------------------------------------------------

    # Must be an integer.
    kwargs["value"] = -1

    validate_less_than(**kwargs)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
