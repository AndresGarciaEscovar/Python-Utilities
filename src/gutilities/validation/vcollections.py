"""
    Contains the collection validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any, Collection

# User.
from gutilities.exceptions.ecollections import NotInCollectionError


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _parameters_validate_in(collection: Collection, exception: bool) -> None:
    """
        Validates the parameters for the validate_in function are of the
        correct type.

        :param collection: The collection in which the object should be found.

        :param exception: A boolean flag indicating if an exception should be
         raised.

        :raise ValueError: If any of the parameters do not have the proper type
         or value.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the parameters.
    if not isinstance(collection, Collection):
        message += "The \"collection\" must be a collection. "

    if not isinstance(exception, bool):
        message += "The \"excp\" must be a boolean value."

    # Raise the error as needed.
    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_in(
    vobject: Any,
    collection: Collection,
    exception: bool = False
) -> bool:
    """
        Validates that the given item is in the collection.

        :param vobject: The object to be validated.

        :param collection: The collection in which the object should be found.

        :param exception: A boolean flag indicating if an exception should be
         raised.

        :return: A boolean value indicating if the object is in the collection.

        :raise NotInCollectionError: If the object is not in the collection and
         the "exception" flag is set to True.
    """
    # Validate the parameters.
    _parameters_validate_in(collection, exception)

    # Get the result.
    result: bool = vobject in collection

    # Raise an exception if necessary.
    if not result and exception:
        raise NotInCollectionError(None, vobject, collection)

    return result
