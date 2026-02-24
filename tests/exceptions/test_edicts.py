"""
    Contains the unittests for the dictionary errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

from utilities.context_managers.cworking import WorkingDirectory
# User.
from utilities.exceptions.edicts import WrongKeysError

# #############################################################################
# Classes
# #############################################################################


class TestDictionaryErrors(unittest.TestCase):
        """
            Tests for the dictionary errors/exceptions.
        """
        # /////////////////////////////////////////////////////////////////////
        # Test Methods
        # /////////////////////////////////////////////////////////////////////

        def test_wrongkeyserror(self):
            """
                Tests the WrongKeysError exception.
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
                "original": original,
                "depth": None,
                "message": None
            }

            # Error message.
            mmessage: str = "The error message is not the expected one."

            # Error class.
            err: WrongKeysError = WrongKeysError(**kwargs)

            # Expected message.
            mexpected = (
                "The dictionary does not have the expected keys. \nErrors:"
                "\n- Depth: 2, Key: 'zero_0'.'one_0', Error: Missing or "
                "excess keys; missing: {'two_1'}, excess: {}."
            )

            # Check the message is the expected one.
            self.assertEqual(err.message, mexpected, mmessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
