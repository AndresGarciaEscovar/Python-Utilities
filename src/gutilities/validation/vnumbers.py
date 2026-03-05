"""
    File that contains the utility functions for validating numerical values.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from numbers import Real
from typing import Any

# User.
from gutilities.exceptions.enumbers import (
    AboveBelowBoundError, NotInRangeError
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _parameters_validate_comparison(
    value: Any,
    bound: Any,
    include: Any,
    exception: Any
) -> None:
    """
        Validates the parameters for the validate_comparison function are of
        the correct type.

        :param value: The value to be validated.

        :param bound: The lower bound of the value.

        :param include: A boolean flag indicating if the lower bound is
         inclusive. True, if inclusive; False, if non-inclusive. False by
         default.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raise ValueError: If any of the types or values of the variables are
         not the expected ones.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the quantities.
    if not isinstance(value, Real):
        message += "The \"value\" parameter is not a Real number. "

    if not isinstance(bound, Real):
        message += "The \"bound\" parameter is not a Real number. "

    if not isinstance(include, bool):
        message += "The \"include\" parameter must be a boolean flag. "

    if not isinstance(exception, bool):
        message += "The \"exception\" must be a boolean value."

    #  Raise an error if needed.
    if message != "":
        raise ValueError(message.strip())


def _parameters_validate_in_range(
    value: Any,
    crange: Any,
    include: Any,
    exception: Any
) -> None:
    """
        Validates the parameters for the validate_in_range function are of the
        correct type.

        :param value: The value to be validated.

        :param crange: A 2-tuple with real numbers, where the first number
         represents the lower bound of the range and the second number
         represents the upper bound of the range.

        :param include: A 2-tuple with boolean flags, where each boolean flag
         indicates whether the lower value (first value) and the upper value
         (second value) are included in the range. True, if the value is
         included in the range; False, otherwise.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raise ValueError: If any of the types or values of the variables are
         not the expected ones.
    """
    # Auxiliary variables.
    message: str = ""

    # Validate the quantities.
    if not isinstance(value, Real):
        message += "The \"value\" is not a Real number. "

    if not isinstance(crange, tuple):
        message += "The \"crange\" must be a tuple with two Real numbers. "

    elif not len(crange) == 2:
        message += "The \"crange\" must be a tuple with two Real numbers. "

    elif not all(isinstance(x, Real) for x in crange):
        message += "The \"crange\" must be a tuple with two Real numbers. "

    elif not crange[0] < crange[1]:
        message = (
            "The \"crange\" must be a tuple with two Real numbers, where the "
            "first number is strictly less than the second one. "
        )

    if not isinstance(include, tuple):
        message += "The \"include\" must be a tuple with two boolean values. "

    elif not len(include) == 2:
        message += "The \"crange\" must be a tuple with two Real numbers. "

    elif not all(isinstance(val, bool) for val in include):
        message += "The \"include\" must be a tuple with two boolean values. "

    if not isinstance(exception, bool):
        message += "The \"exception\" must be a boolean value. "

    # Raise an exception if needed.
    if message != "":
        raise ValueError(message.strip())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_greater_than(
    value: Real,
    bound: Real,
    include: bool = False,
    exception: bool = False
) -> bool:
    """
        Validates if the value is greater than the bound; non-inclusive by
        default. It can be inclusive if the "include" flag is set to True.

        :param value: The value to be validated.

        :param bound: The lower bound of the value; non-inclusive by default.

        :param include: A boolean flag indicating if the lower bound is
         inclusive. True, if inclusive; False, if non-inclusive. False by
         default.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises AboveBelowBoundError: If the number is not correctly ordered
         with respect to the bound.
    """
    # Validate the parameters.
    _parameters_validate_comparison(value, bound, include, exception)

    # Adjust the range and the include tuple.
    result: bool = value > bound if not include else value >= bound

    # Raise an error if needed.
    if not result and exception:
        raise AboveBelowBoundError(
            value=value,
            bound=bound,
            include_greater=(include, True)
        )

    return result


def validate_in_range(
    value: Real,
    crange: tuple[Real, Real],
    include: tuple[bool, bool] = (True, True),
    exception: bool = False
) -> bool:
    """
        Validates if the number

        :param value: The value to be validated.

        :param crange: The range of the value; inclusive.

        :param include: A tuple that indicates if the lower and upper bounds
         are included in the range; both bounds ARE included, by default.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises IsNotInError: If the number is not of the expected sign.
    """
    # Validate the parameters.
    _parameters_validate_in_range(value, crange, include, exception)

    # Adjust the range and the include tuple.
    left: bool = crange[0] <= value if include[0] else crange[0] < value
    right: bool = value <= crange[1] if include[1] else value < crange[1]
    result: bool = left and right

    # Raise an error if needed.
    if not result and exception:
        raise NotInRangeError(value=value, vrange=crange, include=include)

    return result


def validate_less_than(
    value: Real,
    bound: Real,
    include: bool = False,
    exception: bool = False
) -> bool:
    """
        Validates if the value is less than the bound; non-inclusive by
        default. It can be inclusive if the "include" flag is set to True.

        :param value: The value to be validated.

        :param bound: The upper bound of the value; non-inclusive by default.

        :param include: A boolean flag indicating if the upper bound is
         inclusive. True, if inclusive; False, if non-inclusive. False by
         default.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises AboveBelowBoundError: If the number is not correctly ordered
         with respect to the bound.
    """
    # Validate the parameters.
    _parameters_validate_comparison(value, bound, include, exception)

    # Adjust the range and the include tuple.
    result: bool = value < bound if not include else value <= bound

    # Raise an error if needed.
    if not result and exception:
        raise AboveBelowBoundError(
            value=value,
            bound=bound,
            include_greater=(include, False)
        )

    return result
