"""
    Contains the custom exceptions for numerical validation.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real

# User.
import utilities.general.gstrings as gstrings

from utilities.general.gtypes import tbool, treal


# #############################################################################
# Classes - Exceptions
# #############################################################################


class AboveBelowBoundError(Exception):
    """
        Exception raised when a number is above or below the expected bound;
        i.e., the opposite bound to the one provided as a parameter is an
        infinite value.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The value is not in the expected range."

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def customize(
        self, value: Real = None, bound: Real = None, include: bool = False,
        greater: bool = True
    ) -> None:
        """
            Customizes the exception message.

            :param value: The value that was not above/below the type.

            :param bound: The lower bound of the value; non-inclusive by
            default.

            :param include: A boolean flag indicating if the lower bound is
            inclusive. True, if inclusive; False, if non-inclusive. False by
            default.

            :param greater: A boolean flag indicating if the value should be
            greater than the bound. True, if greater; False, if less.
            True by default.
        """
        # Auxiliary variables.

        message: str = ""
        gmessage: str = "greater than" if greater else "less than"
        imessage: str = ", or equal to," if include else ""

        # Set the value.
        if value is not None:
            message = (
                f"The given value ({value}) is NOT {gmessage}{imessage} the "
                f"bound. "
            )

        if bound is not None:
            message += f"The bound is {bound}. "

        # Set the final message.
        self.message = gstrings.messages_concat(self.message, message.strip())

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self, message: str = None, value: Real = None, bound: Real = None,
        include: bool = False, greater: bool = True
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param value: The value that was not above/below the type.

            :param bound: The lower bound of the value; non-inclusive by
            default.

            :param include: A boolean flag indicating if the lower bound is
            inclusive. True, if inclusive; False, if non-inclusive. False by
            default.

            :param greater: A boolean flag indicating if the value should be
            greater than the bound. True, if greater; False, if less.
            True by default.
        """
        # Set the message.
        self.message: str = (
            AboveBelowBoundError.DEFAULT if message is None else message
        )

        # Set the attributes.
        self.customize(value, bound, include, greater)

        # Call the parent constructor.
        super(AboveBelowBoundError, self).__init__(self.message)


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
