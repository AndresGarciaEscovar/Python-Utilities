"""
    Contains the dictionary validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any, Callable

# User.
from gutilities.exceptions.edicts import WrongKeysError


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _validate_keys_equal(
    object_0: Any,
    object_1: Any,
    depth_max: int,
    _depth: int = 0
) -> bool:
    """
        Recursively validates the keys of the dictionary.

        :param object_0: The dictionary to be validated.

        :param object_0: The keys that the dictionary must have.

        :param depth_max: The maximum validation depth.

        :param _depth: The current depth of the validation. The user must NOT
         tamper with this parameter.

        :return: A boolean value indicating if the dictionary has the same
         keys as the base dictionary, to the given depth. True if the
         dictionary has the same keys as the base dictionary; False, otherwise.
    """
    # No need to continue.
    flag: bool = depth_max > -1

    if flag and _depth > depth_max:
        return True

    # Check if the end has been reached.
    if not (isinstance(object_0, dict) or isinstance(object_1, dict)):
        return True

    # Both must be dictionaries.
    flag = isinstance(object_0, dict) and isinstance(object_1, dict)

    if not flag or object_0.keys() != object_1.keys():
        return False

    # Recursive step.
    for key, value in object_0.items():
        flag = flag and _validate_keys_equal(
            value, object_1[key], depth_max, _depth + 1
        )

    return flag


def _parameters_validate_keys(
    base: Any,
    dictionary: Any,
    depth: Any,
    exception: Any
) -> None:
    """
        Validates the parameters for the validate_keys_equal function are of
        the correct type.

        :param base: The keys that the dictionary must have.

        :param dictionary: The dictionary to be validated.

        :param depth: The depth to which the validation should be performed;
         the default value is 0, i.e., the shallowest level. Must be an integer
         greater than or equal to 0.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.
    """
    # Auxiliary variables.
    message: str = ""
    string: Callable = lambda x, y, z: (
        f"The \"{x}\" parameter must be a {y}; current type: "
        f"{type(z).__name__}."
    )

    # Validate the different quantities.
    if not isinstance(base, dict):
        message += string("base", "dictionary", base)

    if not isinstance(dictionary, dict):
        message += string("dictionary", "dictionary", dictionary)

    if not (isinstance(depth, int) and depth >= -1):
        message += string("depth", "positive integer or -1", depth)

    if not isinstance(exception, bool):
        message += string("exception", "boolean value", exception)

    # Raise the error as needed.
    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_keys_subset(
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
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :return: A boolean value indicating if the dictionary has the same keys
         as the base dictionary. True if the dictionary has the same keys as
         the base dictionary, False otherwise.
    """
    # Validate the parameters.
    _parameters_validate_keys(base, dictionary, depth, exception)

    # Compare the dictionaries.
    result: bool = _validate_keys_equal(dictionary, base, depth)

    # Raise an exception if necessary.
    if not result and exception:
        raise WrongKeysError(None, base, dictionary, depth)

    return result


def validate_keys_equal(
    base: dict,
    dictionary: dict,
    depth: int = 0,
    exception: bool = False
) -> bool:
    """
        Validates that the given dictionary is an exact subset of the base
        dictionary, down to the specified depth. If the depth is negative, the
        validation is performed to the deepest level of the base dictionary.

        :param base: The keys that the dictionary **must** have.

        :param dictionary: The dictionary to be validated.

        :param depth: The depth to which the validation should be performed.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :return: A boolean value indicating if the dictionary has the same keys
         as the base dictionary. True if the dictionary has the same keys as
         the base dictionary, False otherwise.
    """
    # Validate the parameters.
    _parameters_validate_keys(base, dictionary, depth, exception)

    # Compare the dictionaries.
    result: bool = _validate_keys_equal(dictionary, base, depth)

    # Raise an exception if necessary.
    if not result and exception:
        raise WrongKeysError(None, base, dictionary, depth)

    return result
