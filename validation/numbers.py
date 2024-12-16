"""
    File that contains the utility functions for validating numerical values.
"""

# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real

# User.
import validation.general as ugeneral


# #############################################################################
# Types
# #############################################################################

tbool = tuple[bool, bool]
treal = tuple[Real, Real]

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
    ugeneral.validate_type(value, Real, excpt=True)
    ugeneral.validate_length(crange, 2, excpt=True)

    if include is not None:
        ugeneral.validate_length(include, 2, excpt=True)

    # Adjust the range and the include tuple.
    crange = tuple(func(crange) for func in (min, max))
    include = (True, True) if include is None else include

    # Validate the range.
    flag_less: bool = crange[0] < value if include[0] else crange[0] <= value
    flag_more: bool = value < crange[1] if include[1] else value <= crange[1]

    result: bool = flag_less and flag_more

    if not result and excpt:
        raise NotInRangeError(value=value, vrange=crange, include=include)
