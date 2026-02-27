"""
    Contains the custom exceptions for numerical validation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from numbers import Real
from typing import Union

# User.
from gutilities.general.gstrings import messages_concat


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes - Exceptions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class AboveBelowBoundError(Exception):
    """
        Exception raised when a number is above or below the expected bound;
        i.e., the opposite bound to the one provided as a parameter is an
        infinite value.

        PARAMETERS:
        ___________

        - self.message: The custom message, if any.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The value is not in the expected range."

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _customize(
        self,
        value: Union[None, Real] = None,
        bound: Union[None, Real] = None,
        include: bool = False,
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
        gmessage: str = "greater than" if greater else "less than"
        imessage: str = ", or equal to," if include else ""

        # Set the message values.
        message: str = (
            f"The given value ({value}) is NOT {gmessage}{imessage} the "
            f"bound. "
        ) if value is not None else ""

        message += f"The bound is {bound}. " if bound is not None else ""

        # Set the final message.
        self.message = messages_concat(self.message, message.strip())

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self,
        message: Union[None, str] = None,
        value: Union[None, Real] = None,
        bound: Union[None, Real] = None,
        include_greater: tuple[bool, bool] = (False, True)
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param value: The value that was not above/below the type.

            :param bound: The lower bound of the value; non-inclusive by
             default.

            :param include_greater: A tuple with two boolean values. The first
             entry is a boolean flag indicating if the lower bound is
             inclusive. True, if inclusive, False, if non-inclusive; False by
             default. The second entry is a boolean flag indicating if the
             value should be greater than the bound. True, if greater, False,
             if less; False by default.
        """
        # Auxiliary variables.
        default: str = AboveBelowBoundError.DEFAULT

        # Set the message.
        self.message: str = default if message is None else message
        self._customize(value, bound, include_greater[0], include_greater[1])

        # Call the parent constructor.
        super().__init__(self.message)


class NotInRangeError(Exception):
    """
        Exception raised when a number is not in the expected range.

        PARAMETERS:
        ___________

        - self.message: The custom message, if any.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The value is not in the expected range."

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _customize(
        self,
        value: Union[None, Real] = None,
        vrange: Union[None, tuple[Real, Real]] = None,
        include: Union[None, tuple[bool, bool]] = None
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
            message += f"Current value type: {type(value).__name__}. "

        if vrange is not None:
            message += f"{message}Expected range: {tuple(vrange)}. "

        if include is not None:
            message += f"{message}Included (lower, upper)? {tuple(include)}."

        # Set the final message.
        self.message = messages_concat(self.message, message.strip())

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self,
        message: Union[None, str] = None,
        value: Union[None, Real] = None,
        vrange: Union[None, tuple[Real, Real]] = None,
        include: Union[None, tuple[bool, bool]] = None
    ):
        """
            Constructor for the exception.

            :param message: The message to be displayed.

            :param value: The value that was not of the expected type.

            :param vrange: The expected range of the value.

            :param include: Whether the range includes the limits.
        """
        # Auxiliary variables.
        default: str = NotInRangeError.DEFAULT

        # Set the message.
        self.message: str = default if message is None else message
        self._customize(value, vrange, include)

        # Call the parent constructor.
        super().__init__(self.message)
