"""
    Contains the general validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any, Iterable

# User.
from src.utilities.exceptions.ecollections import WrongLengthError
from src.utilities.exceptions.etypes import WrongTypeError


# #############################################################################
# Functions
# #############################################################################


def validate_type(value: Any, vtype: Any, excpt: bool = False) -> bool:
    """
        Validates if the given value is of the expected type.

        :param value: The value to be validated.

        :param vtype: The expected type of the value.

        :param excpt: If the exception should be raised or not.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Validate the type.
    result: bool = isinstance(value, vtype)

    # Raise the exception if needed.
    if not result and excpt:
        raise WrongTypeError(value=value, vtype=vtype)

    return result


def validate_length(value: Iterable, length: int, excpt: bool = False) -> bool:
    """
        Validates if the given iterable value has the given length.

        :param value: The value to be validated.

        :param length: The expected length of the iterable.

        :param excpt: If the exception should be raised or not.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Auxiliary variables.
    length_iterable: int = 0

    # Validate the function values are the correct type.
    validate_type(value, Iterable, True)
    validate_type(length, int, True)

    # Extract the length of the iterable and validate.
    for _ in value:
        length_iterable += 1

    result: bool = length_iterable == length

    # Raise the exception if needed.
    if not result and excpt:
        raise WrongLengthError(length_iterable=length_iterable, length=length)

    return result
