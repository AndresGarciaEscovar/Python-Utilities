"""
    Contains the unittests for the number validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

# User.
import utilities.validation.vnumbers as vnumbers

from utilities.exceptions.enumbers import AboveBelowBoundError, NotInRangeError


# #############################################################################
# Classes
# #############################################################################


class TestValidateGreaterThan(unittest.TestCase):
    """
        Tests for the greater than numerical validation functions in the
        module.
    """
    # /////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////

    def test_bound_not_real(self):
        """
            Tests there is an exception if the value of the "bound"
            parameter is not a real number.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"bound\" is a real number; it must "
            "NOT be a real number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": 1,
            "bound": "0",
            "include": False,
            "excpt": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_greater_than(**kwargs)

        # Must be a boolean.
        kwargs["bound"] = 0

        vnumbers.validate_greater_than(**kwargs)

    def test_excpt_not_bool(self):
        """
            Tests there is an exception if the value of the "excpt"
            parameter is not a boolean.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"excpt\" is a boolean value; it must "
            "NOT be a boolean number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": 1,
            "bound": 0,
            "include": False,
            "excpt": 1,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_greater_than(**kwargs)

        # Must be a boolean.
        kwargs["excpt"] = True

        vnumbers.validate_greater_than(**kwargs)

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
            "value": 1,
            "bound": 0,
            "include": 4,
            "excpt": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_greater_than(**kwargs)

        # Must be a boolean.
        kwargs["include"] = True

        vnumbers.validate_greater_than(**kwargs)

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
            "excpt": True,
        }

        # Must be True.
        self.assertTrue(vnumbers.validate_greater_than(**kwargs), msg=emessage)

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
            "excpt": True,
        }

        # Must be True.
        self.assertTrue(vnumbers.validate_greater_than(**kwargs), msg=emessage)

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
            "excpt": False,
        }

        # Must be True.
        self.assertFalse(
            vnumbers.validate_greater_than(**kwargs), msg=emessage
        )

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
            "excpt": False,
        }

        # Must be True.
        self.assertFalse(
            vnumbers.validate_greater_than(**kwargs), msg=emessage
        )

        # --------------------- Must throw an exception --------------------- #

        # Messages.
        emessage = "An exception must be raised."

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": False,
            "excpt": True,
        }

        # Must be True.
        with self.assertRaises(AboveBelowBoundError, msg=emessage) as _:
            vnumbers.validate_greater_than(**kwargs)

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
            "excpt": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_greater_than(**kwargs)

        # Must be a boolean.
        kwargs["value"] = 1

        vnumbers.validate_greater_than(**kwargs)


class TestValidateInRange(unittest.TestCase):
        """
            Tests for the numerical validation functions in the module.
        """
        # /////////////////////////////////////////////////////////////////////
        # Test Methods
        # /////////////////////////////////////////////////////////////////////

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
                "excpt": True,
            }

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------ 2-tuple of complex numbers ----------------- #

            # 2-tuple of complex numbers.
            kwargs["crange"] = (0, 0 + 1j)

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------- 3-tuple of real numbers ------------------- #

            # Tuple longer than 2 elements.
            kwargs["crange"] = (0, 1, 2)

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # -------------------- Numbers in wrong order ------------------- #

            # Tuple longer than 2 elements.
            kwargs["crange"] = (3, 1)

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------ No error should be raised ------------------ #

            # Tuple longer than 2 elements.
            kwargs["crange"] = (1, 4)

            vnumbers.validate_in_range(**kwargs)

        def test_crange_tuple_ordering(self):
            """
                Tests there is an exception if the value of the "crange"
                parameter is not a tuple of real numbers.
            """
            # Messages.
            emessage: str = (
                "The expected type of \"crange\" is an non-organized 2-tuple "
                "of real numbers; it must NOT be organized to raise an "
                "exception."
            )

            # --------------------- Non-organized tuple --------------------- #

            # Values.
            kwargs: dict = {
                "value": 2,
                "crange": (3, 1),
                "include": (True, True),
                "excpt": True,
            }

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------ No error should be raised ------------------ #

            # Tuple longer than 2 elements.
            kwargs["crange"] = (1, 3)

            vnumbers.validate_in_range(**kwargs)

        def test_excpt_not_bool(self):
            """
                Tests there is an exception if the value of the "excpt"
                parameter is not a boolean.
            """
            # Messages.
            emessage: str = (
                "The expected type of \"excpt\" is a boolean value; it must "
                "NOT be a boolean number to raise an exception."
            )

            # Values.
            kwargs: dict = {
                "value": 1,
                "crange": (0, 3),
                "include": (True, True),
                "excpt": 1,
            }

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # Must be a boolean.
            kwargs["excpt"] = True

            vnumbers.validate_in_range(**kwargs)

        def test_include_not_bool_tuple(self):
            """
                Tests there is an exception if the value of the "include"
                parameter is not a tuple of boolean flags.
            """
            # Messages.
            emessage: str = (
                "The expected type of \"include\" is a not a 2-tuple of "
                "boolean flags; it must NOT be a tuple of this type to raise "
                "an exception."
            )

            # ------------------------- Not a tuple ------------------------- #

            # Values.
            kwargs: dict = {
                "value": 1,
                "crange": (0, 3),
                "include": 1,
                "excpt": True,
            }

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # --------------- 2-tuple of none boolean numbers --------------- #

            # 2-tuple of complex numbers.
            kwargs["include"] = (0, True)

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------- 3-tuple of boolean flags ------------------ #

            # Tuple longer than 2 elements.
            kwargs["include"] = (True, False, True)

            # Must raise an assertion error.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------ No error should be raised ------------------ #

            # Tuple longer than 2 elements.
            kwargs["include"] = (True, True)

            vnumbers.validate_in_range(**kwargs)

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
                "excpt": False,
            }

            # Must be True.
            self.assertTrue(vnumbers.validate_in_range(**kwargs), msg=emessage)

            # ----------------- End values are now included ----------------- #

            # Values.
            kwargs["include"] = (True, True)

            # Must be True.
            self.assertTrue(vnumbers.validate_in_range(**kwargs), msg=emessage)

            # The other end.
            kwargs["value"] = 1

            # Must be True.
            self.assertTrue(vnumbers.validate_in_range(**kwargs), msg=emessage)

            # ----------------------- Value at one end ---------------------- #

            emessage = (
                "The parameters are in range; they MUST be out of range."
            )

            # Values.
            kwargs["crange"] = (1, 3)
            kwargs["include"] = (False, False)

            # Must be False.
            self.assertFalse(
                vnumbers.validate_in_range(**kwargs), msg=emessage
            )

            # -------------------- Value at the other end ------------------- #

            # Values.
            kwargs["value"] = 3

            # Must be False.
            self.assertFalse(
                vnumbers.validate_in_range(**kwargs), msg=emessage
            )

            # ----------------------- Exclude the ends ---------------------- #

            # Values.
            kwargs["value"] = 1
            kwargs["excpt"] = True

            # Must raise an assertion error.
            with self.assertRaises(NotInRangeError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # The other end.
            kwargs["value"] = 3

            # Must raise an assertion error.
            with self.assertRaises(NotInRangeError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)


class TestValidateLessThan(unittest.TestCase):
    """
        Tests for the greater than numerical validation functions in the
        module.
    """
    # /////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////

    def test_bound_not_real(self):
        """
            Tests there is an exception if the value of the "bound"
            parameter is not a real number.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"bound\" is a real number; it must "
            "NOT be a real number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": -1,
            "bound": "0",
            "include": False,
            "excpt": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_less_than(**kwargs)

        # Must be a boolean.
        kwargs["bound"] = 0

        vnumbers.validate_less_than(**kwargs)

    def test_excpt_not_bool(self):
        """
            Tests there is an exception if the value of the "excpt"
            parameter is not a boolean.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"excpt\" is a boolean value; it must "
            "NOT be a boolean number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": -1,
            "bound": 0,
            "include": False,
            "excpt": 1,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_less_than(**kwargs)

        # Must be a boolean.
        kwargs["excpt"] = True

        vnumbers.validate_less_than(**kwargs)

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
            "excpt": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_less_than(**kwargs)

        # Must be a boolean.
        kwargs["include"] = True

        vnumbers.validate_less_than(**kwargs)

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
            "excpt": True,
        }

        # Must be True.
        self.assertTrue(vnumbers.validate_less_than(**kwargs), msg=emessage)

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
            "excpt": True,
        }

        # Must be True.
        self.assertTrue(vnumbers.validate_less_than(**kwargs), msg=emessage)

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
            "excpt": False,
        }

        # Must be True.
        self.assertFalse(
            vnumbers.validate_less_than(**kwargs), msg=emessage
        )

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
            "excpt": False,
        }

        # Must be True.
        self.assertFalse(
            vnumbers.validate_less_than(**kwargs), msg=emessage
        )

        # --------------------- Must throw an exception --------------------- #

        # Messages.
        emessage = "An exception must be raised."

        # Values.
        kwargs: dict = {
            "value": 0,
            "bound": 0,
            "include": False,
            "excpt": True,
        }

        # Must be True.
        with self.assertRaises(AboveBelowBoundError, msg=emessage) as _:
            vnumbers.validate_less_than(**kwargs)

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
            "excpt": True,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vnumbers.validate_less_than(**kwargs)

        # Must be a boolean.
        kwargs["value"] = -1

        vnumbers.validate_less_than(**kwargs)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
