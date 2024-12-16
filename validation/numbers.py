"""
    File that contains the utility functions for validating numerical values.
"""

# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real

# #############################################################################
# Types
# #############################################################################

tbool = tuple[bool, bool]
treal = tuple[Real, Real]

# #############################################################################
# Functions
# #############################################################################


def validate_type(value: , expected: type) -> None:

def validate_in_range(
    value: Real, crange: treal, include: tbool = None, excpt: bool = None
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
