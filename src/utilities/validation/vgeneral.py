"""
    Contains the general validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any, Collection, Type

# User.
from src.utilities.exceptions.ecollections import WrongLengthError
from src.utilities.exceptions.etypes import WrongTypeError


# #############################################################################
# Parameter Validation
# #############################################################################


def parameters_validate_length(
    value: Collection, length: int, excpt: bool = False
) -> None:
    """
        Validates the parameters for the validate_length function are of the
        correct type.

        :param value: A collection with the items to be validated.

        :param length: The expected length of the collection

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails.

        :raises AssertionError: If the parameters are not of the correct type.
    """
    # Messages.
    mvtype: str = "The expected type of \"value\" must be a \"Collection\"."
    mltype: str = "The expected type of \"length\" must be a positive \"int\"."
    mvalue: str = "The value is not of the correct type; must be a boolean."

    # Check the parameters are of the correct type.
    assert isinstance(value, Collection), mvtype
    assert isinstance(length, int) and length >= 0, mltype
    assert isinstance(excpt, bool), mvalue


def parameters_validate_type(vtype: Type | None, excpt: bool) -> None:
    """
        Validates the parameters for the validate_type function are of the
        correct type.

        :param vtype: The expected type of the value; it can be None.

        :param excpt: If the exception should be raised or not.

        :raises AssertionError: If the parameters are not of the correct type.
    """
    # Messages.
    mvtype: str = "The expected value of \"vtype\" must be \"Type\" or None."
    mvalue: str = "The value is not of the correct type; must be a boolean."

    # Check the parameters are of the correct type.
    if vtype is not None:
        assert isinstance(vtype, vtype), mvtype

    assert isinstance(excpt, bool), mvalue


# #############################################################################
# Functions
# #############################################################################


def validate_length(
    value: Collection, length: int, excpt: bool = False
) -> bool:
    """
        Validates if the given collection of elements has the given length.

        :param value: A collection with the items to be validated.

        :param length: The expected length of the collection

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Validate parameters.
    parameters_validate_length(value, length, excpt)

    # Length of the collection.
    clength: int = sum(1 for _ in value)
    result: bool = clength == length

    # Raise the exception if needed.
    if not result and excpt:
        raise WrongLengthError(clength=clength, elength=length)

    return result


def validate_type(value: Any, vtype: Type | None, excpt: bool = False) -> bool:
    """
        Validates if the given value is of the expected type.

        :param value: The value to be validated.

        :param vtype: The expected type of the value; it can be None.

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Validate parameters.
    parameters_validate_type(vtype, excpt)

    # Validate the type.
    result: bool = value is None if vtype is None else isinstance(value, vtype)

    # Raise the exception if needed.
    if not result and excpt:
        raise WrongTypeError(value=value, vtype=vtype)

    return result
