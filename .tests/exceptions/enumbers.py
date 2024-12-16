"""
    Contains the custom exceptions for numerical validation.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real


# #############################################################################
# Types
# #############################################################################


# Tuple types.
tbool = tuple[bool, bool]
treal = tuple[Real, Real]


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

    DEFAULT = "The value is not in the expected range."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    # def customize(self, value: Any, vtype: Any) -> None:
    #     """
    #         Customizes the exception message.
    #
    #         :param value: The value that was not of the expected type.
    #
    #         :param vtype: The expected type of the value.
    #     """
    #     # Auxiliary variables.
    #     message = ""
    #
    #     # Set the value.
    #     if value is not None:
    #         message = f"Current type value: {value}. "
    #
    #     if vtype is not None:
    #         message = f"{message}Expected type: {vtype}."
    #
    #     # Set the final message.
    #     self.message = ustrings.messages_concat(message.strip(), self.message)

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

            :param vtype: The expected type of the value.
        """
        # Set the message.
        self.message = NotInRangeError.DEFAULT if message is None else message

        # Set the attributes.
        # self.customize(value, vtype)

        # Call the parent constructor.
        super(NotInRangeError, self).__init__(self.message)
