"""
    Custom exceptions for collections.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any, Collection, Union

# User.
import utilities.general.gstrings as ustrings


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes - Exceptions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class NotInCollectionError(Exception):
    """
        Exception raised when an object is not in the given collection.

        PARAMETERS:
        ___________

        - self.message: The custom message, if any.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The given item is not in the collection."

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _customize(
        self,
        vobject: Any,
        collection: Union[Collection, None]
    ) -> None:
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
        self,
        message: Union[None, str] = None,
        vobject: Any = None,
        collection: Union[Collection, None] = None
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param vobject: The object that was not found in the collection.

            :param collection: The collection in which the object was not
             found.
        """
        # Auxiliary variables.
        default: str = NotInCollectionError.DEFAULT

        # Initialize the variables.
        self.message: str = default if message is None else message
        self._customize(vobject, collection)

        # Call the parent constructor.
        super().__init__(self.message)


class WrongLengthError(Exception):
    """
        Exception raised when the collection is not of the expected length.

        PARAMETERS:
        ___________

        - self.message: The custom message, if any.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The collection is not of the expected length."

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _customize(
        self,
        clength: Union[int, None],
        elength: Union[int, None]
    ) -> None:
        """
            Customizes the exception message.

            :param clength: The length of the collection that was not
             of the expected length.

            :param elength: The expected length of the collection.
        """
        # Auxiliary variables.
        message: str = ""

        # Set the values.
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
        self,
        message: Union[None, str] = None,
        clength: Union[int, None] = None,
        elength: Union[int, None] = None
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param clength: The length of the collection that was not of
             the expected length.

            :param elength: The expected length of the collection.
        """
        # Auxiliary variables.
        default: str = WrongLengthError.DEFAULT

        # Initialize the variables.
        self.message: str = default if message is None else message
        self._customize(clength, elength)

        # Call the parent constructor.
        super().__init__(self.message)
