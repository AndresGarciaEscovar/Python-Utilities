"""
 Contains the functions for string validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

# User.
import utilities.validation.vstrings as vstrings


# #############################################################################
# Classes
# #############################################################################


class TestValidateStringEmpty(unittest.TestCase):
    """
        Contains the tests for the validate_string_empty function.
    """

    # #########################################################################
    # Tests
    # #########################################################################

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
            "value": "",
            "notempty": False,
            "sstrip": False,
            "excpt": 1,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vstrings.validate_string_empty(**kwargs)

        # Must be a boolean.
        kwargs["excpt"] = True

        vstrings.validate_string_empty(**kwargs)

    def test_notempty_not_bool(self):
        """
            Tests there is an exception if the value of the "notempty"
            parameter is not a boolean.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"notempty\" is a boolean value; it must "
            "NOT be a boolean number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": "",
            "notempty": 1,
            "sstrip": False,
            "excpt": False,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vstrings.validate_string_empty(**kwargs)

        # Must be a boolean.
        kwargs["notempty"] = True

        vstrings.validate_string_empty(**kwargs)

    def test_sstrip_not_bool(self):
        """
            Tests there is an exception if the value of the "sstrip"
            parameter is not a boolean.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"sstrip\" is a boolean value; it must "
            "NOT be a boolean number to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "value": "",
            "notempty": False,
            "sstrip": 1,
            "excpt": False,
        }

        # Must raise an assertion error.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vstrings.validate_string_empty(**kwargs)

        # Must be a boolean.
        kwargs["sstrip"] = True

        vstrings.validate_string_empty(**kwargs)

    def test_validate_string_empty(self):
        """
            Tests the validate_string_empty function when the string is empty.
        """
        # --------- String should be completely empty, but it is not -------- #

        # Messages.
        emessage: str = (
            "The string is not empty; it should be empty to pass the test."
        )

        # Values.
        kwargs: dict = {
            "value": "",
            "notempty": False,
            "sstrip": False,
            "excpt": False,
        }

        # Must be True.
        self.assertTrue(vstrings.validate_string_empty(**kwargs), msg=emessage)

        # ------ String is made of spaces, newlines, etc., but stripped ----- #

        # Messages.
        emessage = (
            "Should evaluate to True with stripping; it should be empty to "
            "pass the test or have only spaces, newlines, etc."
        )

        # Values.
        kwargs: dict = {
            "value": "  \n\t  \t\n  ",
            "notempty": False,
            "sstrip": True,
            "excpt": False,
        }

        # Must be True.
        self.assertTrue(vstrings.validate_string_empty(**kwargs), msg=emessage)

        # ------------- String is completely empty and stripped ------------- #

        # Messages.
        emessage = (
            "Should evaluate to True with stripping; it should be empty to "
            "pass the test."
        )

        # Values.
        kwargs: dict = {
            "value": "",
            "notempty": False,
            "sstrip": False,
            "excpt": False,
        }

        # Must be True.
        self.assertTrue(vstrings.validate_string_empty(**kwargs), msg=emessage)

        # ---------------- String is not empty, but stripped ---------------- #

        # Messages.
        emessage = (
            "Should evaluate to False; it should NOT be empty to pass the "
            "test."
        )

        # Values.
        kwargs: dict = {
            "value": "kkkkkk",
            "notempty": False,
            "sstrip": True,
            "excpt": False,
        }

        # Must be False.
        self.assertFalse(
            vstrings.validate_string_empty(**kwargs), msg=emessage
        )

        # --------------------- String must not be empty -------------------- #

        # Messages.
        emessage = (
            "Should evaluate to True; it should NOT be empty to pass the "
            "test."
        )

        # Values.
        kwargs: dict = {
            "value": "kkkkkk",
            "notempty": True,
            "sstrip": False,
            "excpt": False,
        }

        # Must be True.
        self.assertTrue(
            vstrings.validate_string_empty(**kwargs), msg=emessage
        )

        # ------- String made of spaces, tabs, etc., but must be True ------- #

        # Messages.
        emessage = (
            "Should evaluate to True; it should NOT be empty to pass the "
            "test."
        )

        # Values.
        kwargs: dict = {
            "value": "   \n\t\t\t  ",
            "notempty": True,
            "sstrip": False,
            "excpt": False,
        }

        # Must be True.
        self.assertTrue(
            vstrings.validate_string_empty(**kwargs), msg=emessage
        )

        # --------------------- Must raise an exception --------------------- #

        # Messages.
        emessage = (
            "Should evaluate to True; it should NOT be empty to pass the "
            "test."
        )

        # Values.
        kwargs: dict = {
            "value": "   \n\t\t\t  ",
            "notempty": True,
            "sstrip": True,
            "excpt": True,
        }

        # Must be True.
        with self.assertRaises(ValueError, msg=emessage) as _:
            vstrings.validate_string_empty(**kwargs)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
