"""
    Contains the unittests for the number validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

from typing import  Callable

# User.
import utilities.validation.vnumbers as vnumbers


# #############################################################################
# Classes
# #############################################################################


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
            emessage = (
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

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------ 2-tuple of complex numbers ----------------- #

            # 2-tuple of complex numbers.
            kwargs["crange"] = (0, 0 + 1j)

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------- 3-tuple of real numbers ------------------- #

            # Tuple longer than 2 elements.
            kwargs["crange"] = (0, 1, 2)

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # -------------------- Numbers in wrong order ------------------- #

            # Tuple longer than 2 elements.
            kwargs["crange"] = (3, 1)

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------ No error should be raised ------------------ #

            # Tuple longer than 2 elements.
            kwargs["crange"] = (1, 4)

            vnumbers.validate_in_range(**kwargs)

        def test_excpt_not_bool(self):
            """
                Tests there is an exception if the value of the "excpt"
                parameter is not a boolean.
            """
            # Messages.
            emessage = (
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

            # Messages must match.
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
            emessage = (
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

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # --------------- 2-tuple of none boolean numbers --------------- #

            # 2-tuple of complex numbers.
            kwargs["include"] = (0, True)

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------- 3-tuple of boolean flags ------------------ #

            # Tuple longer than 2 elements.
            kwargs["include"] = (True, False, True)

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vnumbers.validate_in_range(**kwargs)

            # ------------------ No error should be raised ------------------ #

            # Tuple longer than 2 elements.
            kwargs["include"] = (True, True)

            vnumbers.validate_in_range(**kwargs)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
