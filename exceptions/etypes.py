"""
    Contains the custom exceptions for type validation.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any, Type

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

    DEFAULT: str = "The value is not of the expected type."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def customize(self, value: Any, vtype: Type) -> None:
        """
            Customizes the exception message.

            :param value: The value that was not of the expected type.

            :param vtype: The expected type of the value.
        """
        # Auxiliary variables.
        message: str = ""

        # Set the value.
        if value is not None:
            message = f"Current type value: \"{type(value).__name__}\". "

        if vtype is not None:
            message = f"{message}Expected type: \"{vtype.__name__}\"."

        # Set the final message.
        self.message = ustrings.messages_concat(self.message, message.strip())

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
        self.message: str = (
            WrongTypeError.DEFAULT if message is None else message
        )

        # Set the attributes.
        self.customize(value, vtype)

        # Call the parent constructor.
        super(WrongTypeError, self).__init__(self.message)
