"""
    Contains the custom exceptions for type validation.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any

# User.
import general.gstrings as ustrings


# #############################################################################
# Classes - Exceptions
# #############################################################################


class WrongTypeError(Exception):
    """
        Exception raised when the value is not of the expected type.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT = "The value is not of the expected type."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def customize(self, value: Any, vtype: Any) -> None:
        """
            Customizes the exception message.

            :param value: The value that was not of the expected type.

            :param vtype: The expected type of the value.
        """
        # Auxiliary variables.
        message = ""

        # Set the value.
        if value is not None:
            message = f"Current type value: {value}. "

        if vtype is not None:
            message = f"{message}Expected type: {vtype}."

        # Set the final message.
        self.message = ustrings.messages_concat(message.strip(), self.message)

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self, message: str = None, value: Any = None, vtype: Any = None
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param value: The value that was not of the expected type.

            :param vtype: The expected type of the value.
        """
        # Set the message.
        self.message = WrongTypeError.DEFAULT if message is None else message

        # Set the attributes.
        self.customize(value, vtype)

        # Call the parent constructor.
        super(WrongTypeError, self).__init__(self.message)
