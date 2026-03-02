"""
    Contains the string validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any

# User.
import gutilities.validation.vgeneral as vgeneral



# ##############################################################################
# Parameter Validation
# ##############################################################################


def _parameters_validate_string_empty(
    notempty: Any,
    sstrip: Any,
    exception: Any
) -> None:
    """
        Validates the parameters for the validate_string_empty function are of
        the correct type.

        :param notempty: A boolean flag indicating if the string should not be
         empty. If True, the string must not be empty. If False, the string
         must be empty. Default is False.

        :param sstrip: A boolean flag indicating if the string should be
         stripped before validation. True, if the string should be stripped;
         False, otherwise. Default is False.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raise ValueError: If any of the types or values of the variables are
         not the expected ones.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the quantities.
    if not isinstance(notempty, bool):
        message += "The expected type of \"notempty\" must be a boolean. "

    if not isinstance(sstrip, bool):
        message += "The expected type of \"sstrip\" must be a boolean. "

    if not isinstance(exception, bool):
        message += "The expected type of \"exception\" must be a boolean. "

    #  Raise an error if needed.
    if message != "":
        raise ValueError(message.strip())


# ##############################################################################
# Functions
# ##############################################################################


def validate_string_empty(
    value: str,
    notempty: bool = False,
    sstrip: bool = False,
    exception: bool = False
) -> bool:
    """
        Validates the string is empty.

        :param value: The string to be validated.

        :param notempty: A boolean flag indicating if the string should not be
         empty. If True, the string must not be empty. If False, the string
         must be empty. Default is False.

        :param sstrip: A boolean flag indicating if the string should be
         stripped before validation. Default is False.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises ValueError: If the validation fails and the exception flag is
         True.
    """
    # Validate the parameters.
    _parameters_validate_string_empty(notempty, sstrip, exception)

    # Check that the object to validate is a string.
    vgeneral.validate_type(value, str, False)

    # Get the validation.
    tvalue: str = value.strip() if sstrip else value
    result: bool = tvalue != "" if notempty else tvalue == ""

    # Raise the exception if necessary.
    if not result and exception:
        # Exception message.
        message: str = (
            f"The string is{' ' if notempty else ' not '}empty; it must be"
            f"{' not ' if notempty else ' '}empty."
        )

        # Raise the exception.
        raise ValueError(message)

    return result
