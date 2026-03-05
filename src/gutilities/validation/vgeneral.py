"""
    Contains the general validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any, Collection, Type, Union

# User.
from gutilities.exceptions.ecollections import WrongLengthError
from gutilities.exceptions.etypes import WrongTypeError


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _parameters_validate_length(
    value: Any,
    length: Any,
    exception: Any
) -> None:
    """
        Validates the parameters for the validate_length function are of the
        correct type.

        :param value: A collection with the items to be validated.

        :param length: The expected length of the collection

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises ValueError: If any of the values does not have the correct
         type or takes an invalid value.
    """
    # Messages.
    message: str = ""

    # Check the parameters are of the correct type.
    if not isinstance(value, Collection):
        message += "The expected type of \"value\" must be a \"Collection\". "

    if not (isinstance(length, int) and length >= 0):
        message += (
            "The expected type of \"length\" must be a positive \"int\". "
        )

    if not isinstance(exception, bool):
        message += "The value is not of the correct type; must be a boolean."

    # Raise an exception if needed.
    if message != "":
        raise ValueError(message.strip())


def _parameters_validate_type(vtype: Any, exception: Any) -> None:
    """
        Validates the parameters for the validate_type function are of the
        correct type.

        :param vtype: The expected type of the value; it can be None.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises ValueError: If any of the values does not have the correct
         type or takes an invalid value.
    """
    # Auxiliary variables.
    message: str = ""

    # Check the parameters are of the correct type.
    if not (vtype is None or isinstance(vtype, Type)):
        message += "The expected value of \"vtype\" must be \"Type\" or None. "

    if not isinstance(exception, bool):
        message += "The value is not of the correct type; must be a boolean."

    # Raise an exception if needed.
    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_length(
    value: Collection,
    length: int,
    exception: bool = False
) -> bool:
    """
        Validates if the given collection of elements has the given length.

        :param value: A collection with the items to be validated.

        :param length: The expected length of the collection

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Validate parameters.
    _parameters_validate_length(value, length, exception)

    # Length of the collection.
    clength: int = sum(1 for _ in value)
    result: bool = clength == length

    # Raise the exception if needed.
    if not result and exception:
        raise WrongLengthError(clength=clength, elength=length)

    return result


def validate_type(
    value: Any,
    vtype: Union[None, Type],
    exception: bool = False
) -> bool:
    """
        Validates if the given value is of the expected type.

        :param value: The value to be validated.

        :param vtype: The expected type of the value; it can be None.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Validate parameters.
    _parameters_validate_type(vtype, exception)

    # Validate the type.
    result: bool = value is None if vtype is None else isinstance(value, vtype)

    # Raise the exception if needed.
    if not result and exception:
        raise WrongTypeError(value=value, vtype=vtype)

    return result
