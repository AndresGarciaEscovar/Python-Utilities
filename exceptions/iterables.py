"""
    Custom exceptions for iterables.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any, Iterable

# User.
import general.strings as ustrings


# #############################################################################
# Classes - Exceptions
# #############################################################################


class WrongLengthError(Exception):
    """
        Exception raised when the iterable is not of the expected length.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT = "The iterable is not of the expected length."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def customize(self, length_iterable: int, length: int) -> None:
        """
            Customizes the exception message.

            :param length_iterable: The length of the iterable that was not of
            the expected length.

            :param length: The expected length of the iterable.
        """
        # Auxiliary variables.
        message = ""

        # Set the value.
        if length_iterable is not None:
            message = f"Current length of the iterable: {length_iterable}. "

        if length is not None:
            message = f"{message}Expected length: {length}."

        # Set the final message.
        self.message = ustrings.messages_concat(message.strip(), self.message)

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self, message: str = None, length_iterable: int = None,
        length: int = None
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param length_iterable: The length of the iterable that was not of
            the expected length.

            :param length: The expected length of the iterable.
        """
        # Set the message.
        self.message = WrongLengthError.DEFAULT if message is None else message

        # Set the attributes.
        self.customize(length_iterable, length)

        # Call the parent constructor.
        super(WrongLengthError, self).__init__(self.message)
