"""
    Contains the collection validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from typing import Any, Collection

# User.
from utilities.exceptions.ecollections import NotInCollectionError


# #############################################################################
# Parameter Validation
# #############################################################################


def parameters_validate_in(
    collection: Collection, excpt: bool = False
) -> None:
    """
        Validates the parameters for the validate_in function are of the
        correct type.

        :param collection: The collection in which the object should be found.

        :param excpt: A boolean flag indicating if an exception should be
        raised.

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails.
    """
    # "base" validation.
    message: str = "The \"collection\" must be a collection."

    assert isinstance(collection, Collection), message

    # "excp" validation.
    message = "The \"excp\" must be a boolean value."

    assert isinstance(excpt, bool), message


# #############################################################################
# Functions
# #############################################################################


def validate_in(
    vobject: Any, collection: Collection, excpt: bool = False
) -> bool:
    """
        Validates that the given item is in the collection.

        :param vobject: The object to be validated.

        :param collection: The collection in which the object should be found.

        :param excpt: A boolean flag indicating if an exception should be
        raised.

        :return: A boolean value indicating if the object is in the collection.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Implementation
    # /////////////////////////////////////////////////////////////////////////

    # Validate the parameters.
    parameters_validate_in(collection, excpt)

    # Get the result.
    result: bool = vobject in collection

    # Raise an exception if necessary.
    if not result and excpt:
        raise NotInCollectionError(None, vobject, collection)

    return result
