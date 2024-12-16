"""
    Contains the unittests for the general errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

from typing import  Callable

# User.
import utilities.validation.vgeneral as vgeneral

from utilities.exceptions.ecollections import WrongLengthError
from utilities.exceptions.etypes import WrongTypeError


# #############################################################################
# Classes
# #############################################################################


class TestValidateLength(unittest.TestCase):
        """
            Tests for the length validation of collections.
        """
        # /////////////////////////////////////////////////////////////////////
        # Test Methods
        # /////////////////////////////////////////////////////////////////////

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
                "value": (1, 2),
                "length": 2,
                "excpt": 1,
            }

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vgeneral.validate_length(**kwargs)

            # Must be a boolean.
            kwargs["excpt"] = True

            vgeneral.validate_length(**kwargs)

        def test_length_positive(self):
            """
                Tests there is an exception if the value of the length is not
                a positive integer, or zero.
            """
            # Messages.
            emessage = (
                "The expected type of \"length\" is a positive integer, or "
                "zero; it must be a negative integer or a non-integer number "
                "to raise an exception."
            )

            # Values.
            kwargs: dict = {
                "value": (1, 2),
                "length": -1,
                "excpt": True,
            }

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vgeneral.validate_length(**kwargs)

            # Cannot be a non-integer number.
            kwargs["length"] = 1.2

            with self.assertRaises(AssertionError, msg=emessage) as _:
                vgeneral.validate_length(**kwargs)

        def test_correct_values(self):
            """
                Tests the value is false for valid values for the validation
                function.
            """
            # Auxiliary variables.
            alias: Callable = vgeneral.validate_length
            kwargs: dict = {
                "value": (1, 2),
                "length": 2,
                "excpt": False,
            }

            # -------------------- Different collections -------------------- #

            # Messages.
            emessage = (
                f"The given collection does not have a length of "
                f"{kwargs['length']}."
            )

            for collection in (set, tuple, list, "dict"):
                # Format the values.
                if collection == "dict":
                    kwargs["value"] = dict.fromkeys(kwargs["value"]).keys()

                else:
                    kwargs["value"] = collection(kwargs["value"])

                # Must return True.
                self.assertTrue(alias(**kwargs), emessage)

        def test_incorrect_values(self):
            """
                Tests the value is false for valid values for the validation
                function.
            """
            # Auxiliary variables.
            alias: Callable = vgeneral.validate_length
            kwargs: dict = {
                "value": (1, 2),
                "length": None,
                "excpt": False,
            }

            # ------------------- Return values is False  ------------------- #

            # Messages.
            emessage =  (
                f"The given collection has a length of {kwargs['length']}; "
                f"this should not be happening."
            )

            # Must return False.
            for length in tuple(len(kwargs["value"]) + x for x in (-1, 1)):
                kwargs["length"] = length
                self.assertFalse(alias(**kwargs), emessage)

            # ------------------- Exception must be raised ------------------ #

            # Messages.
            emessage = (
                f"The \"excpt\" flag is set to {True}; this should be raising "
                f"an error/exception."
            )

            # Tests exceptions are raised when needed.
            kwargs["excpt"] = True

            for length in tuple(len(kwargs["value"]) + x for x in (-1, 1)):
                kwargs["length"] = length
                with self.assertRaises(WrongLengthError, msg=emessage) as _:
                    alias(**kwargs)

        def test_value_not_a_collection(self):
            """
                Tests there is an exception raise when the value passed for
                validation is not a collection.
            """
            # Messages.
            emessage = (
                "The expected type of \"value\" is a \"Collection\"; it must "
                "NOT be a collection to raise an exception."
            )

            # Values.
            kwargs: dict = {
                "value": 1,
                "length": -1,
                "excpt": True,
            }

            # Messages must match.
            with self.assertRaises(AssertionError, msg=emessage) as _:
                vgeneral.validate_length(**kwargs)


class TestValidateType(unittest.TestCase):
    """
        Tests for the type validation function.
    """

    # /////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////

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
            "value": "(1, 2)",
            "vtype": str,
            "excpt": 1,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vgeneral.validate_type(**kwargs)

        # Must be a boolean.
        kwargs["excpt"] = True

        vgeneral.validate_type(**kwargs)

    def test_type_wrong(self):
        """
            Tests there is an exception if the type value is of the wrong type.
        """
        # Messages.
        emessage = (
            "The expected type of \"vtype\" must be a \"Type\" or None "
            "value. Notice that Type is a \"_SpecialType\" object itself."
        )

        # Values.
        kwargs: dict = {
            "value": "(1, 2)",
            "vtype": "str",
            "excpt": True,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vgeneral.validate_type(**kwargs)

        # Must be a boolean.
        kwargs["vtype"] = str

        vgeneral.validate_type(**kwargs)

    def test_type_wrong_element(self):
        """
            Tests there is an exception if the type of the value being validated
            is of the wrong type and False is returned; or an exception is raised
            if the "excpt" flag is set to True.
        """
        # Messages.
        emessage = (
            "The expected type of \"vtype\" must be a \"Type\" or None "
            "value. Notice that Type is a \"_SpecialType\" object itself."
        )

        # ----------------- Incorrect values, with exception ---------------- #

        # Values.
        kwargs: dict = {
            "value": "(1, 2)",
            "vtype": int,
            "excpt": True,
        }

        # Messages must match.
        with self.assertRaises(WrongTypeError, msg=emessage) as _:
            vgeneral.validate_type(**kwargs)

        # ------------------ Incorrect values, no exception ----------------- #

        # Must yield false.
        kwargs["vtype"] = int
        kwargs["excpt"] = False

        self.assertFalse(vgeneral.validate_type(**kwargs))

        # -------------------------- Correct values ------------------------- #

        # Must be yield True.
        kwargs["vtype"] = str

        self.assertTrue(vgeneral.validate_type(**kwargs))


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
