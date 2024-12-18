"""
    Custom exceptions for collections.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any, Collection

# User.
import utilities.general.gstrings as ustrings


# #############################################################################
# Classes - Exceptions
# #############################################################################


class NotInCollectionError(Exception):
    """
        Exception raised when an object is not in the given collection.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The given item is not in the collection."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def customize(self, vobject: Any, collection: Collection) -> None:
        """
            Customizes the exception message.

            :param vobject: The object that was not found in the collection.

            :param collection: The collection in which the object should be
            found.
        """
        # Auxiliary variables.
        message: str = ""

        # Set the value.
        if vobject is not None:
            message = f"Object being validated: {vobject}. "

        if collection is not None:
            message = f"{message}Collection of possible objects: {collection}."

        # Set the final message.
        self.message = ustrings.messages_concat(self.message, message.strip())

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self, message: str = None, vobject: Any = None,
        collection: Collection = None
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param vobject: The object that was not found in the collection.

            :param collection: The collection in which the object should be
            found.
        """
        # Set the message.
        self.message: str = (
            WrongLengthError.DEFAULT if message is None else message
        )

        # Set the attributes.
        self.customize(vobject, collection)

        # Call the parent constructor.
        super(NotInCollectionError, self).__init__(self.message)


class WrongLengthError(Exception):
    """
        Exception raised when the collection is not of the expected length.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The collection is not of the expected length."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def customize(self, clength: int, elength: int) -> None:
        """
            Customizes the exception message.

            :param clength: The length of the collection that was not
            of the expected length.

            :param elength: The expected length of the collection.
        """
        # Auxiliary variables.
        message: str = ""

        # Set the value.
        if clength is not None:
            message = f"Current length of the collection: {clength}. "

        if elength is not None:
            message = f"{message}Expected length: {elength}."

        # Set the final message.
        self.message = ustrings.messages_concat(self.message, message.strip())

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self, message: str = None, clength: int = None, elength: int = None
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param clength: The length of the collection that was not of
            the expected length.

            :param elength: The expected length of the collection.
        """
        # Set the message.
        self.message: str = (
            WrongLengthError.DEFAULT if message is None else message
        )

        # Set the attributes.
        self.customize(clength, elength)

        # Call the parent constructor.
        super(WrongLengthError, self).__init__(self.message)
