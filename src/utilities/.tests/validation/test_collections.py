"""
    Contains the unittests for the collection errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

# User.
import utilities.validation.vcollections as vcollections

from utilities.exceptions.ecollections import NotInCollectionError


# #############################################################################
# Classes
# #############################################################################


class TestValidateIn(unittest.TestCase):
    """
        Tests for the existence in collection validation function.
    """

    # /////////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////////

    def test_collection_not_collection(self):
        """
            Tests there is an exception if the object to be validated is not
            in the collection.
        """
        # Messages.
        emessage: str = (
            "The collection must be a collection; it must NOT be a collection "
        )

        # Values.
        kwargs: dict = {
            "vobject": 9,
            "collection": 3,
            "excpt": True,
        }

        # Must validate to False and raise an exception.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vcollections.validate_in(**kwargs)

        # Must be a collection; e.g., a tuple.
        kwargs["collection"] = (1, 2, 9)

        vcollections.validate_in(**kwargs)

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
            "vobject": 9,
            "collection": (3, 9),
            "excpt": 1,
        }

        # Must raise an exception.
        with self.assertRaises(AssertionError, msg=emessage) as _:
            vcollections.validate_in(**kwargs)

        # Must be a boolean.
        kwargs["excpt"] = True

        vcollections.validate_in(**kwargs)

    def test_validate_in(self):
        """
            Tests the validate_in function.
        """
        # ------------------- Object not in, no exception ------------------- #

        # Messages.
        emessage: str = (
            "The object to be validated is in the collection; it must NOT "
            "be in the collection."
        )

        # Values.
        kwargs: dict = {
            "vobject": 7,
            "collection": (3, 9),
            "excpt": False,
        }

        # Messages validate to False.
        self.assertFalse(vcollections.validate_in(**kwargs), msg=emessage)

        # ------------------ Object not in, with exception ------------------ #

        # Messages.
        emessage = (
            "The object to be validated is in the collection; it must NOT "
            "be in the collection."
        )

        # Values.
        kwargs["excpt"] = True

        # Must validate to False and raise an exception.
        with self.assertRaises(NotInCollectionError, msg=emessage) as _:
            vcollections.validate_in(**kwargs)

        # ------------------ Object not in, with exception ------------------ #

        # Messages.
        emessage = (
            "The object to be validated is NOT in the collection; it must be "
            "in the collection."
        )

        # Values.
        kwargs["vobject"] = 9

        for dtype in (list, tuple, set):
            kwargs["collection"] = dtype((3, 9))

            # Must validate to True.
            self.assertTrue(vcollections.validate_in(**kwargs), msg=emessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
