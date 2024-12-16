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

        :param include: The range of the value; inclusive.

        :param excpt: The range of the value; inclusive.

        :raises IsNotInError: If the number is not of the expected sign.
    """
    # Validate the parameters.
    ugeneral.validate_type(value, Real, excpt=True)
    ugeneral.validate_type(crange, tuple, excpt=True)
    ugeneral.validate_length(crange, 2, excpt=True)
