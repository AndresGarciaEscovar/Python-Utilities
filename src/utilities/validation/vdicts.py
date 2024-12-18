"""
    Contains the dictionary validation functions.
"""

# #############################################################################
# Imports
# #############################################################################


# User.
from utilities.exceptions.edicts import WrongKeysError


# #############################################################################
# Parameter Validation
# #############################################################################


def parameters_validate_keys(
    base: dict, dictionary: dict, depth: int, excpt: bool = False
) -> None:
    """
        Validates the parameters for the validate_keys function are of the
        correct type.

        :param base: The keys that the dictionary must have.

        :param dictionary: The dictionary to be validated.

        :param depth: The depth to which the validation should be performed;
        the default value is 0, i.e., the shallowest level. Must be an integer
        greater than or equal to 0.

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails.
    """
    # "base" validation.
    flag: bool = True
    message: str = "The \"base\" must be a dictionary."

    assert isinstance(base, dict), message

    # "dictionary" validation.
    message = "The \"dictionary\" must be a dictionary."
    flag = flag and isinstance(dictionary, dict)

    assert flag, message

    # "depth" validation.
    if depth is not None:
        message = "The \"depth\" must be a positive integer, or zero."
        assert isinstance(depth, int) and depth >= 0, message

    # "excp" validation.
    message = "The \"excp\" must be a boolean value."

    assert isinstance(excpt, bool), message


# #############################################################################
# Functions
# #############################################################################


def validate_keys_equal(
    base: dict, dictionary: dict, depth: int = None, excpt: bool = False
) -> bool:
    """
        Validates that the given dictionary has the exact same keys as the base
        dictionary, down to the specified depth. If the depth is negative, the
        validation is performed to the deepest level of the base dictionary.

        :param base: The keys that the dictionary must have.

        :param dictionary: The dictionary to be validated.

        :param depth: The depth to which the validation should be performed;

        :param excpt: A boolean flag indicating if an exception should be
        raised.

        :return: A boolean value indicating if the dictionary has the same keys
        as the base dictionary. True if the dictionary has the same keys as the
        base dictionary, False otherwise.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Inner Functions
    # /////////////////////////////////////////////////////////////////////////

    def validate_keys_(dict_: dict, base_: dict, depth_: int) -> bool:
        """
            Validates the keys of the dictionary.

            :param dict_: The dictionary to be validated.

            :param base_: The keys that the dictionary must have.

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

    # /////////////////////////////////////////////////////////////////////////
    # Implementation
    # /////////////////////////////////////////////////////////////////////////

    # Validate the parameters.
    parameters_validate_keys(base, dictionary, depth, excpt)

    # Get the result.
    tdepth: int = depth if depth is None else 0
    result: bool = validate_keys_(dictionary, base, tdepth)

    # Raise an exception if necessary.
    if not result and excpt:
        raise WrongKeysError(None, base, dictionary, depth)

    return result
