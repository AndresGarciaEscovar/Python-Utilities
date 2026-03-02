"""
    File that contains the utility functions for validating numerical values.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from numbers import Real
from typing import Any, Union

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

        :param bound: The lower bound of the value; non-inclusive by default.

        :param include: A boolean flag indicating if the lower bound is
        inclusive. True, if inclusive; False, if non-inclusive. False by
        default.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.
    """
    # "value" validation.
    message: str = "The \"value\" parameter is not a Real number."

    assert isinstance(value, Real), message

    # "bound" validation.
    message = "The \"bound\" parameter is not a Real number."

    assert isinstance(bound, Real), message

    # "include" validation.
    message = "The \"include\" parameter must be a boolean flag."

    assert isinstance(include, bool), message

    # "exception" validation.
    message = "The \"exception\" must be a boolean value."

    assert isinstance(exception, bool), message


def parameters_validate_in_range(
    value: Real,
    crange: tuple[Real, Real],
    include: Union[None, tuple[bool, bool]] = None,
    exception: bool = False
) -> None:
    """
        Validates the parameters for the validate_in_range function are of the
        correct type.

        :param value: The value to be validated.

        :param crange: The range of the value; inclusive.

        :param include: A tuple that indicates if the lower and upper bounds.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.
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

    # "exception" validation.
    message = "The \"exception\" must be a boolean value."

    assert isinstance(exception, bool), message


# #############################################################################
# Functions
# #############################################################################


def validate_greater_than(
    value: Real, bound: Real, include: bool = False, exception: bool = False
) -> bool :
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
    parameters_validate_comparison(value, bound, include, exception)

    # Adjust the range and the include tuple.
    result: bool = value > bound if not include else value >= bound

    if not result and exception:
        raise AboveBelowBoundError(
            value=value, bound=bound, include=include, greater=True
        )

    return result


def validate_in_range(
    value: Real, crange: tuple[Real, Real], include: tuple[bool, bool] = None, exception: bool = False
) -> bool :
    """
        Validates if the number

        :param value: The value to be validated.

        :param crange: The range of the value; inclusive.

        :param include: A tuple that indicates if the lower and upper bounds
        are included in the range; if None, both are included, otherwise both
        values must be specified.

        :param exception: A boolean flag indicating if an exception should be
         raised if validation fails. True, if the exception must be thrown;
         False, otherwise. False by default.

        :raises IsNotInError: If the number is not of the expected sign.
    """
    # Validate the parameters.
    parameters_validate_in_range(value, crange, include, exception)

    if include is None:
        include = (True, True)

    # Adjust the range and the include tuple.
    left: bool = crange[0] <= value if include[0] else crange[0] < value
    right: bool = value <= crange[1] if include[1] else value < crange[1]
    result: bool = left and right

    if not result and exception:
        raise NotInRangeError(value=value, vrange=crange, include=include)

    return result


def validate_less_than(
    value: Real, bound: Real, include: bool = False, exception: bool = False
) -> bool :
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
    parameters_validate_comparison(value, bound, include, exception)


    # Adjust the range and the include tuple.
    result: bool = value < bound if not include else value <= bound

    if not result and exception:
        raise AboveBelowBoundError(
            value=value, bound=bound, include=include, greater=False
        )

    return result
