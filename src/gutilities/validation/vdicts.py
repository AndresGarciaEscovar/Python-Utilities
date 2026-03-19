"""
    Contains the dictionary validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any, Callable, Type

# User.
from gutilities.validation.vgeneral import (
    validate_type
)
from gutilities.exceptions.edicts import (
    WrongKeysError,
    WrongKeysSubsetError
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


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

        :param exception: A boolean flag indicating if an exception must be
         raised if validation fails. True, if the exception must be raised;
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


def _parameters_validate_keys_and_types(
    base: Any,
    dictionary: Any,
    extract: Any,
    exception: Any
) -> None:
    """
        Validates the parameters for the validate_keys_equal function are of
        the correct type.

        :param base: The keys that the dictionary must have.

        :param dictionary: The dictionary to be validated.

        :param extract: A boolean flag indicating whether the data type of
         the base dictionary must be extracted rather than directly used.
         True, if the data type must be extracted; False, otherwise.

        :param exception: A boolean flag indicating if an exception must be
         raised if validation fails. True, if the exception must be raised;
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

    if not isinstance(extract, bool):
        message += string("extract", "boolean value", extract)

    if not isinstance(exception, bool):
        message += string("exception", "boolean value", exception)

    # Raise the error as needed.
    if message != "":
        raise ValueError(message.strip())


def _validate_keys_equal(
    object_0: Any,
    object_1: Any,
    depth_max: int,
    depth: int = 0
) -> bool:
    """
        Recursively validates the keys of both dictionaries are exactly the
        same.

        :param object_0: The dictionary to be validated.

        :param object_1: The keys that the dictionary must have.

        :param depth_max: The maximum validation depth.

        :param depth: The current depth of the validation. The user must NOT
         tamper with this parameter.

        :return: A boolean value indicating if the dictionary has the same
         keys as the base dictionary, to the given depth. True if the
         dictionary has the same keys as the base dictionary; False, otherwise.
    """
    # No need to continue.
    flag: bool = depth_max > -1

    if flag and depth > depth_max:
        return True

    # Check if the end has been reached.
    if not (isinstance(object_0, dict) or isinstance(object_1, dict)):
        return True

    # Both must be dictionaries.
    flag = isinstance(object_0, dict) and isinstance(object_1, dict)

    if not (flag and set(object_0.keys()) == set(object_1.keys())):
        return False

    # Recursive step.
    for key, value in object_0.items():
        flag = flag and _validate_keys_equal(
            value, object_1[key], depth_max, depth + 1
        )

    return flag


def _validate_keys_equal_and_type(
    object_0: Any,
    object_1: Any,
    extract: bool,
) -> bool:
    """
        Recursively validates the keys of both dictionaries are exactly the
        same keys, and the type of the entry of the dictionaries are the same
        as those at the end of the base dictionary.

        :param object_0: The dictionary to be validated.

        :param object_1: The base dictionary to be used as the comparison
         dictionary.

        :param extract: A boolean flag indicating whether the data type of
         the base dictionary must be extracted rather than directly used.
         True, if the data type must be extracted; False, otherwise.

        :return: A boolean value indicating if the dictionary has the same
         keys as the base dictionary, to the given depth. True if the
         dictionary has the same keys as the base dictionary; False, otherwise.
    """
    # Check the type when the end has been reached.
    if not isinstance(object_1, dict):
        dtype: Type = type(object_1) if extract else object_1
        return validate_type(object_0, dtype, exception=False)

    # Both must be dictionaries.
    flag: bool = isinstance(object_0, dict)

    if not (flag and set(object_0.keys()) == set(object_1.keys())):
        return False

    # Recursive step.
    for key, value in object_0.items():
        flag = flag and _validate_keys_equal_and_type(
            value,
            object_1[key],
            extract
        )

    return flag


def _validate_keys_subset(
    object_0: Any,
    object_1: Any,
    depth_max: int,
    depth: int = 0
) -> bool:
    """
        Recursively validates the first dictionary is a subset, or a proper
        subset, of the the second dictionary.

        :param object_0: The dictionary that must be a subset of the other one.

        :param object_1: The dictionary with the keys.

        :param depth_max: The maximum validation depth.

        :param depth: The current depth of the validation. The user must NOT
         tamper with this parameter.

        :return: A boolean value indicating if the first dictionary is a
         subset, or a proper subset, of the second one, to the given depth.
         True if the first dictionary is a subset, or a proper subset, of the
         second one; False, otherwise.
    """
    # No need to continue.
    flag: bool = depth_max > -1

    if flag and depth > depth_max:
        return True

    # Check if the end has been reached.
    if not (isinstance(object_0, dict) or isinstance(object_1, dict)):
        return True

    # Both must be dictionaries.
    flag = isinstance(object_0, dict) and isinstance(object_1, dict)

    if not (flag and set(object_0.keys()).issubset(set(object_1.keys()))):
        return False

    # Recursive step.
    for key, value in object_0.items():
        flag = flag and _validate_keys_equal(
            value, object_1[key], depth_max, depth + 1
        )

    return flag


def _validate_keys_subset_and_type(
    object_0: Any,
    object_1: Any,
    extract: bool,
) -> bool:
    """
        Recursively validates the first dictionary is a subset, or a proper
        subset, of the the second dictionary, and the type of the entry of
        the dictionaries are the same as those at the end of the base
        dictionary.

        :param object_0: The dictionary that must be a subset of the other one.

        :param object_1: The dictionary with the keys.

        :param extract: A boolean flag indicating whether the data type of
         the base dictionary must be extracted rather than directly used.
         True, if the data type must be extracted; False, otherwise.

        :return: A boolean value indicating if the dictionary has the same
         keys as the base dictionary, to the given depth. True if the
         dictionary has the same keys as the base dictionary; False, otherwise.
    """
    # Check the type when the end has been reached.
    if not isinstance(object_1, dict):
        dtype: Type = type(object_1) if extract else object_1
        return validate_type(object_0, dtype, exception=False)

    # Both must be dictionaries.
    flag: bool = isinstance(object_0, dict)

    if not (flag and set(object_0.keys()).issubset(set(object_1.keys()))):
        return False

    # Recursive step.
    for key, value in object_0.items():
        flag = flag and _validate_keys_subset_and_type(
            value,
            object_1[key],
            extract
        )

    return flag


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


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

        :param exception: A boolean flag indicating if an exception must be
         raised if validation fails. True, if the exception must be raised;
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


def validate_keys_equal_and_type(
    base: dict,
    dictionary: dict,
    extract: bool = False,
    exception: bool = False
) -> bool:
    """
        Validates that the given dictionary has the same structure as the base
        dictionary and the types of the dictionary are the same as those
        specified at the end of the base dictionary.

        :param base: The keys that the dictionary **must** have; where the
         final elements must be the intended data type(s) of the dictionary
         at that level.

        :param dictionary: The dictionary to be validated.

        :param extract: A boolean flag indicating whether the data type of
         the base dictionary must be extracted rather than directly used.
         True, if the data type must be extracted; False, otherwise.

        :param exception: A boolean flag indicating if an exception must be
         raised if validation fails. True, if the exception must be raised;
         False, otherwise. False by default.

        :return: A boolean value indicating if the dictionary has the same keys
         as the base dictionary. True if the dictionary has the same keys as
         the base dictionary, False otherwise.
    """
    # Validate the parameters.
    _parameters_validate_keys_and_types(base, dictionary, extract, exception)

    # # Compare the dictionaries.
    result: bool = _validate_keys_equal_and_type(dictionary, base, extract)

    raise NotImplementedError(
        "MUST WRITE THE TEST FUNCTIONS AN ERROR FUNCTIONS"
    )

    # # Raise an exception if necessary.
    # if not result and exception:
    #     raise WrongKeysError(None, base, dictionary, depth)

    return result


def validate_keys_subset(
    base: dict,
    dictionary: dict,
    depth: int = 0,
    exception: bool = False
) -> bool:
    """
        Validates that the given dictionary is a subset of the base dictionary,
        down to the specified depth. If the depth is negative, the validation
        is performed to the deepest level of the base dictionary.

        :param base: The dictionary with the keys that the dictionary **can**
         have.

        :param dictionary: The dictionary to be validated.

        :param depth: The depth to which the validation should be performed.

        :param exception: A boolean flag indicating if an exception must be
         raised if validation fails. True, if the exception must be raised;
         False, otherwise. False by default.

        :return: A boolean value indicating if the dictionary is a subset, or
         a proper subset, of  the base dictionary, in terms of the keys. True
         if the dictionary has the same keys as the base dictionary, False
         otherwise.
    """
    # Validate the parameters.
    _parameters_validate_keys(base, dictionary, depth, exception)

    # Compare the dictionaries.
    result: bool = _validate_keys_subset(dictionary, base, depth)

    # Raise an exception if necessary.
    if not result and exception:
        raise WrongKeysSubsetError(None, base, dictionary, depth)

    return result


def validate_keys_subset_and_type(
    base: dict,
    dictionary: dict,
    extract: bool = False,
    exception: bool = False
) -> bool:
    """
        Validates that the given dictionary is a subset of the base dictionary,
        and the types of the dictionary are the same as those specified at the
        end of the base dictionary.

        :param base: The dictionary with the keys that the dictionary **can**
         have.

        :param dictionary: The dictionary to be validated.

        :param extract: A boolean flag indicating whether the data type of
         the base dictionary must be extracted rather than directly used.
         True, if the data type must be extracted; False, otherwise.

        :param exception: A boolean flag indicating if an exception must be
         raised if validation fails. True, if the exception must be raised;
         False, otherwise. False by default.

        :return: A boolean value indicating if the dictionary has the same keys
         as the base dictionary. True if the dictionary has the same keys as
         the base dictionary, False otherwise.
    """
    # Validate the parameters.
    _parameters_validate_keys_and_types(base, dictionary, extract, exception)

    # # Compare the dictionaries.
    result: bool = _validate_keys_subset_and_type(dictionary, base, extract)

    raise NotImplementedError(
        "MUST WRITE THE TEST FUNCTIONS AN ERROR FUNCTIONS"
    )

    # # Raise an exception if necessary.
    # if not result and exception:
    #     raise WrongKeysError(None, base, dictionary, depth)

    return result
