"""
    Contains the unittests for the collection errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import unittest

# User.
from gutilities.exceptions.ecollections import NotInCollectionError
from gutilities.validation.vcollections import validate_in


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestValidateIn(unittest.TestCase):
    """
        Tests for the existence in collection validation function.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_collection_not_collection(self):
        """
            Tests there is an exception if the object to be validated is not
            in the collection.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "vobject": 9,
            "collection": 3,
            "exception": True,
        }

        # ---------------------------------------------------------------------
        # Test 1: The object in the "collection" placeholder is NOT a
        # collection.
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The \"collection\" parameter must be a collection; a "
            "ValueError must be raised."
        )

        # Must validate to False and raise an exception.
        with self.assertRaises(ValueError, msg=message):
            validate_in(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a collection; e.g., a tuple.
        kwargs["collection"] = (1, 2, 9)

        validate_in(**kwargs)

    def test_exception_not_bool(self):
        """
            Tests there is an exception if the value of the "exception"
            parameter is not a boolean.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "vobject": 9,
            "collection": (3, 9),
            "exception": 1,
        }

        # ---------------------------------------------------------------------
        # Test 1: The object in the "exception" placeholder is NOT a
        # boolean value.
        # ---------------------------------------------------------------------

        # Messages.
        message: str = (
            "Test 1: The expected type of \"exception\" is NOT a boolean "
            "value; it must be a boolean number to NOT raise an exception."
        )

        # Must raise an exception.
        with self.assertRaises(ValueError, msg=message):
            validate_in(**kwargs)

        # ---------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # ---------------------------------------------------------------------

        # Must be a boolean.
        kwargs["exception"] = True

        validate_in(**kwargs)

    def test_validate_in(self):
        """
            Tests the validate_in function.
        """
        # Auxiliary variables.
        kwargs: dict = {
            "vobject": 7,
            "collection": (3, 9),
            "exception": False,
        }

        # ---------------------------------------------------------------------
        # Test 1: Object not in, no exception
        # ---------------------------------------------------------------------

        # Set the message in case an error happens.
        emessage: str = (
            "Test 1: The object to be validated is in the collection; it must "
            "NOT be in the collection."
        )

        # Messages validate to False.
        self.assertFalse(validate_in(**kwargs), msg=emessage)

        # ------------------ Object not in, with exception ------------------ #

        # Messages.
        message = (
            "Test 2: The object to be validated is in the collection; it must "
            "NOT be in the collection and raise an exception."
        )

        # Values.
        kwargs["exception"] = True

        # Must validate to False and raise an exception.
        with self.assertRaises(NotInCollectionError, msg=message):
            validate_in(**kwargs)

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
            self.assertTrue(validate_in(**kwargs), msg=emessage)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
