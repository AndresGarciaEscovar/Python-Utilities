"""
    Contains the general validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any

# User.
from exceptions.types import WrongTypeError

# #############################################################################
# Functions
# #############################################################################


def validate_type(value: Any, vtype: Any, xcpt: bool = False) -> bool:
    """
        Validates if the given value is of the expected type.

        :param value: The value to be validated.

        :param vtype: The expected type of the value.

        :param xcpt: If the exception should be raised or not.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Validate the type.
    result: bool = isinstance(value, vtype)

    # Raise the exception if needed.
    if not result and xcpt:
        raise WrongTypeError(value=value, vtype=vtype)

    return result
