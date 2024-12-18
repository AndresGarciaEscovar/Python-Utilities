"""
    Contains the unittests for the dictionary errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

# User.
import utilities.validation.vdicts as vdicts

from utilities.exceptions.edicts import WrongKeysError


# #############################################################################
# Classes
# #############################################################################


class TestValidateType(unittest.TestCase):
    """
        Tests for the dictionary validation function.
    """

    # /////////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////////

    def test_base_not_dict(self):
        """
            Tests there is an exception if the value of the "base"
            parameter is not a dictionary.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"base\" is a dictionary; it must "
            "NOT be a dictionary to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "base": 9,
            "dictionary": {},
            "depth": 0,
            "excpt": True,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vdicts.validate_keys_equal(**kwargs)

        # Must be a dictionary.
        kwargs["base"] = {}

        vdicts.validate_keys_equal(**kwargs)

    def test_depth_not_int(self):
        """
            Tests there is an exception if the value of the "depth"
            parameter is not an integer.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"depth\" is an integer; it must "
            "NOT be a integer to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "base": {},
            "dictionary": {},
            "depth": "1",
            "excpt": True,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vdicts.validate_keys_equal(**kwargs)

        # Must be an integer.
        kwargs["depth"] = 0

        vdicts.validate_keys_equal(**kwargs)

    def test_dictionary_not_dict(self):
        """
            Tests there is an exception if the value of the "dictionary"
            parameter is not a dictionary.
        """
        # Messages.
        emessage: str = (
            "The expected type of \"dictionary\" is a dictionary; it must "
            "NOT be a dictionary to raise an exception."
        )

        # Values.
        kwargs: dict = {
            "base": {},
            "dictionary": 9,
            "depth": 0,
            "excpt": True,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vdicts.validate_keys_equal(**kwargs)

        # Must be a dictionary.
        kwargs["dictionary"] = {}

        vdicts.validate_keys_equal(**kwargs)

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
            "base": {},
            "dictionary": {},
            "depth": 0,
            "excpt": 1,
        }

        # Messages must match.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vdicts.validate_keys_equal(**kwargs)

        # Must be a boolean.
        kwargs["excpt"] = True

        vdicts.validate_keys_equal(**kwargs)

    def test_validate_keys_equal_basic(self):
        """
            Tests the validate_keys_equal function for valid and invalid cases.
        """
        # Multi-level dictionaries.
        base: dict = {
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

        original: dict = {
            "zero_0": {
                "one_0": {
                    "two_0": 1,
                    "two_1": 2
                },
                "one_1": {
                    "two_0": 3,
                    "two_1": 4,
                    "two_2": 5
                }
            },
        }

        # Parameters.
        kwargs: dict = {
            "base": base,
            "dictionary": original,
            "depth": None,
            "excpt": False,
        }

        # -------------------- Dictionaries are different ------------------- #

        message: str = (
            "The dictionaries have the same keys; this should not happen."
        )
        result: bool = vdicts.validate_keys_equal(**kwargs)

        self.assertFalse(result, msg=message)

        # --------- Dictionaries are different and exception raised --------- #

        message = "An exception should be raised, since it has been requested."
        kwargs["excpt"] = True

        with self.assertRaises(WrongKeysError, msg=message) as _:
            vdicts.validate_keys_equal(**kwargs)

        # -------------------- Dictionaries are the same -------------------- #

        message = "Dictionaries should be the same in this case."
        kwargs["dictionary"] = kwargs["base"]

        result = vdicts.validate_keys_equal(**kwargs)

        self.assertTrue(result, msg=message)

    def test_validate_keys_equal_level(self):
        """
            Tests the validate_keys_equal function for valid and invalid cases.
        """
        # Multi-level dictionaries; only differ in one key at a deeper level.
        base: dict = {
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

        original: dict = {
            "zero_0": {
                "one_0": {
                    "two_0": 1,
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

        # Parameters.
        kwargs: dict = {
            "base": base,
            "dictionary": original,
            "depth": None,
            "excpt": False,
        }

        # ----- Validating up to the second level (i = 1) should be True ---- #

        for i in range(0, 2):
            kwargs["depth"] = i
            message = (
                f"No exception should be raised until depth level 1; current "
                f"depth level: {i}. Remember that the depth is zero-based."
            )

            result = vdicts.validate_keys_equal(**kwargs)

            self.assertTrue(result, msg=message)

        # --------- Validating up to the third level should be False -------- #

        # Must throw an exception.
        kwargs["depth"] = 2

        result = vdicts.validate_keys_equal(**kwargs)
        message = (
            "No exception should be raised, but the result should be False."
        )
        self.assertFalse(result, msg=message)

        # An exception should be raised.
        kwargs["excpt"] = True

        message = (
            "An exception should be raised, since the depth level is greater "
            "than the depth of the base dictionary."
        )

        with self.assertRaises(WrongKeysError, msg=message) as _:
            vdicts.validate_keys_equal(**kwargs)

        # ------------- Unrestricted should, of course, be False ------------ #

        # Must throw an exception.
        kwargs["depth"] = None
        kwargs["excpt"] = False

        result = vdicts.validate_keys_equal(**kwargs)
        message = (
            "No exception should be raised, but the result should be False."
        )
        self.assertFalse(result, msg=message)

        # An exception should be raised.
        kwargs["excpt"] = True

        message = (
            "An exception should be raised, since the depth level is greater "
            "than the depth of the base dictionary."
        )

        with self.assertRaises(WrongKeysError, msg=message) as _:
            vdicts.validate_keys_equal(**kwargs)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
