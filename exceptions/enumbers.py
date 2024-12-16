"""
    Contains the custom exceptions for numerical validation.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real

# User.
import general.gstrings as gstrings

from general.gtypes import tbool, treal


# #############################################################################
# Classes - Exceptions
# #############################################################################


class NotInRangeError(Exception):
    """
        Exception raised when a number is not in the expected range.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The value is not in the expected range."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def customize(
        self, value: Real = None, vrange: treal = None, include: tbool = None
    ) -> None:
        """
            Customizes the exception message.

            :param value: The value that was not of the expected type.

            :param vrange: The expected range of the value.

            :param include: Whether the range includes the limits.
        """
        # Auxiliary variables.
        message: str = ""

        # Set the value.
        if value is not None:
            message = f"Current value type: {type(value).__name__}. "

        if vrange is not None:
            message = f"{message}Expected range: {tuple(vrange)}. "

        if include is not None:
            message = f"{message}Included (lower, upper)? {tuple(include)}."

        # Set the final message.
        self.message = gstrings.messages_concat(self.message, message.strip())

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self, message: str = None, value: Real = None, vrange: treal = None,
        include: tbool = None

    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param value: The value that was not of the expected type.

            :param vrange: The expected range of the value.

            :param include: Whether the range includes the limits.
        """
        # Set the message.
        self.message: str = (
            NotInRangeError.DEFAULT if message is None else message
        )

        # Set the attributes.
        self.customize(value, vrange, include)

        # Call the parent constructor.
        super(NotInRangeError, self).__init__(self.message)
