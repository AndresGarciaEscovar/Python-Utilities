"""
    Contains the dictionary validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any

# User.
from gutilities.exceptions.edicts import WrongKeysError


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _dictionary_validate_keys_(
    object_0: Any,
    object_1: Any,
    depth: int
) -> bool:
    """
        Recursively validates the keys of the dictionary.

        :param object_0: The dictionary to be validated.

        :param object_0: The keys that the dictionary must have.

        :param depth_: The current depth of the validation.

        :return: A boolean value indicating if the dictionary has the same
        keys as the base dictionary. True if the dictionary has the same
        keys as the base dictionary, False otherwise.
    """
    # Check they are both dictionaries.
    dict_0_: bool = isinstance(dict_, dict)
    dict_1_: bool = isinstance(base_, dict)

    # Several exit conditions.
    if (depth is not None and depth_ > depth) or not (dict_0_ or dict_1_):
        return True

    if not (dict_0_ and dict_1_):
        return False

    if dict_.keys() != base_.keys():
        return False

    # Free memory.
    del dict_0_, dict_1_

    # Recursive call.
    flg_: bool = True
    depth_ = None if depth_ is None else depth_ + 1

    for key in dict_.keys():
        flg_ = flg_ and validate_keys_(dict_[key], base_[key], depth_)

    return flg_

def _parameters_validate_keys(
    base: dict,
    dictionary: dict,
    depth: int,
    exception: bool = False
) -> None:
    """
        Validates the parameters for the validate_keys function are of the
        correct type.

        :param base: The keys that the dictionary must have.

        :param dictionary: The dictionary to be validated.

        :param depth: The depth to which the validation should be performed;
         the default value is 0, i.e., the shallowest level. Must be an integer
         greater than or equal to 0.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the different quantities.
    if not isinstance(base, dict):
        message += "The \"base\" must be a dictionary. "

    if not isinstance(dictionary, dict):
        message += "The \"dictionary\" must be a dictionary. "

    if depth is not None and not (isinstance(depth, int) and depth >= 0):
        message += "The \"depth\" must be a positive integer, or zero. "

    if not isinstance(exception, bool):
        message += "The \"exception\" must be a boolean value."

    # Raise the error as needed.
    if message != "":
        raise ValueError(message.strip())


# #############################################################################
# Functions
# #############################################################################


def validate_keys_equal(
    base: dict,
    dictionary: dict,
    depth: int = 0,
    exception: bool = False
) -> bool:
    """
        Validates that the given dictionary has the exact same keys as the base
        dictionary, down to the specified depth. If the depth is negative, the
        validation is performed to the deepest level of the base dictionary.

        :param base: The keys that the dictionary **must** have.

        :param dictionary: The dictionary to be validated.

        :param depth: The depth to which the validation should be performed.

        :param exception: A boolean flag indicating if an exception should be
         raised. True, if the exception must be thrown; False, otherwiswe.
         False by default.

        :return: A boolean value indicating if the dictionary has the same keys
         as the base dictionary. True if the dictionary has the same keys as
         the base dictionary, False otherwise.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Inner Functions
    # /////////////////////////////////////////////////////////////////////////



    # /////////////////////////////////////////////////////////////////////////
    # Implementation
    # /////////////////////////////////////////////////////////////////////////

    # Validate the parameters.
    _parameters_validate_keys(base, dictionary, depth, excpt)

    # Get the result.
    tdepth: int = depth if depth is None else 0
    result: bool = validate_keys_(dictionary, base, tdepth)

    # Raise an exception if necessary.
    if not result and exception:
        raise WrongKeysError(None, base, dictionary, depth)

    return result
