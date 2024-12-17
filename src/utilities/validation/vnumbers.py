"""
    File that contains the utility functions for validating numerical values.
"""

# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real

# User.
from utilities.exceptions.enumbers import NotInRangeError
from utilities.general.gtypes import tbool, treal


# #############################################################################
# Parameter Validation
# #############################################################################


def parameters_validate_in_range(
    value: Real, crange: treal, include: tbool = None, excpt: bool = False
) -> None:
    """
        Validates the parameters for the validate_in_range function are of the
        correct type.

        :param value: The value to be validated.

        :param crange: The range of the value; inclusive.

        :param include: A tuple that indicates if the lower and upper bounds.

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails.
    """
    # "value" validation.
    flag: bool = True
    message: str = "The \"value\" is not a Real number."

    assert isinstance(value, Real), message

    # "crange" validation.
    message = "The \"crange\" must be a tuple with two Real numbers."

    flag = flag and isinstance(crange, tuple)
    flag = flag and all(isinstance(x, Real) for x in crange)
    flag = flag and len(crange) == 2

    assert flag and crange[0] <= crange[1], message

    # "include" validation.
    message = "The \"include\" must be a tuple with two boolean values."

    flag = isinstance(include, tuple)
    flag = flag and all(isinstance(val, bool) for val in include)

    assert include is None or (flag and len(include) == 2), message

    # "excpt" validation.
    message = "The \"excpt\" must be a boolean value."

    assert isinstance(excpt, bool), message


# #############################################################################
# Functions
# #############################################################################


def validate_in_range(
    value: Real, crange: treal, include: tbool = None, excpt: bool = False
) -> bool :
    """
        Validates if the number

        :param value: The value to be validated.

        :param crange: The range of the value; inclusive.

        :param include: A tuple that indicates if the lower and upper bounds
        are included in the range; if None, both are included, otherwise both
        values must be specified.

        :param excpt: The range of the value; inclusive.

        :raises IsNotInError: If the number is not of the expected sign.
    """
    # Validate the parameters.
    parameters_validate_in_range(value, crange, include, excpt)

    if include is None:
        include = (True, True)

    # Adjust the range and the include tuple.
    left: bool = crange[0] <= value if include[0] else crange[0] < value
    right: bool = value <= crange[1] if include[1] else value < crange[1]
    result: bool = left and right

    if not result and excpt:
        raise NotInRangeError(value=value, vrange=crange, include=include)

    return result
