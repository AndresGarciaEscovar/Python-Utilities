"""
    Contains the general validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# #############################################################################
# Functions
# #############################################################################


def validate_type(value: Any, vtype: Any, excpt: bool = False) -> None:
    """
        Validates if the given value is of the expected type.

        :param value: The value to be validated.

        :param vtype: The expected type of the value.

        :param excpt: If the exception should be raised or not.

        :raises WrongTypeError: If the value is not of the expected type.
    """
    # Validate the type.
    if isinstance(value, vtype):
        return

    if excpt:
        raise WrongTypeError(value=value, vtype=vtype)
