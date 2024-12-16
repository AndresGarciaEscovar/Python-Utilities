"""
    Custom exceptions for iterables.
"""


# #############################################################################
# Imports
# #############################################################################


# User.
import general.gstrings as ustrings


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

    DEFAULT: str = "The iterable is not of the expected length."

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
            message = f"Current length of the iterable: {clength}. "

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

            :param clength: The length of the iterable that was not of
            the expected length.

            :param elength: The expected length of the iterable.
        """
        # Set the message.
        self.message: str = (
            WrongLengthError.DEFAULT if message is None else message
        )

        # Set the attributes.
        self.customize(clength, elength)

        # Call the parent constructor.
        super(WrongLengthError, self).__init__(self.message)
