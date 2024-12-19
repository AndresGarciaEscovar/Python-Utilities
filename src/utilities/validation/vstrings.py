"""
    Contains the string validation functions.
"""


# #############################################################################
# Imports
# #############################################################################


# User.
import utilities.validation.vgeneral as vgeneral


# ##############################################################################
# Parameter Validation
# ##############################################################################


def parameters_validate_string_empty(
        notempty: bool = False, sstrip: bool = False, excpt: bool = False
) -> None:
    """
        Validates the parameters for the validate_string_empty function are of
        the correct type.

        :param notempty: A boolean flag indicating if the string should not be
        empty. If True, the string must not be empty. If False, the string must
        be empty. Default is False.

        :param sstrip: A boolean flag indicating if the string should be
        stripped before validation. True, if the string should be stripped;
        False, otherwise. Default is False.

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails. True, if an exception should be raised;
        False, otherwise. Default is False.

        :raises AssertionError: If the parameters are not of the correct type.
    """
    # Message for the "notempty" parameter.
    mnotempty: str = "The expected type of \"notempty\" must be a boolean."

    # Check the parameters are of the correct type.
    assert isinstance(notempty, bool), mnotempty

    # Message for the "sstrip" parameter.
    msstrip: str = "The expected type of \"sstrip\" must be a boolean."

    assert isinstance(sstrip, bool), msstrip

    # Message for the "excpt" parameter.
    mexcpt: str = "The expected type of \"excpt\" must be a boolean."

    assert isinstance(excpt, bool), mexcpt


# ##############################################################################
# Functions
# ##############################################################################


def validate_string_empty(
    value: str, notempty: bool = False, sstrip: bool = False,
    excpt: bool = False
) -> bool:
    """
        Validates the string is empty.

        :param value: The string to be validated.

        :param notempty: A boolean flag indicating if the string should not be
        empty. If True, the string must not be empty. If False, the string must
        be empty. Default is False.

        :param sstrip: A boolean flag indicating if the string should be
        stripped before validation. Default is False.

        :param excpt: A boolean flag indicating if an exception should be
        raised if validation fails.

        :raises ValueError: If the validation fails and the excpt flag is True.
    """
    # Validate the parameters.
    parameters_validate_string_empty(notempty, sstrip, excpt)

    # Check that the object to validate is a string.
    vgeneral.validate_type(value, str, False)

    # Get the validation.
    tvalue: str = value.strip() if sstrip else value
    result: bool = tvalue != "" if notempty else tvalue == ""

    # Raise the exception if necessary.
    if not result and excpt:
        # Messages.
        string0 = " " if notempty else " not "
        string1 = " not " if notempty else " "

        # Exception message.
        mlength: str = f"The string is{string0}empty; it must be{string1}empty."

        # Raise the exception.
        raise ValueError(mlength)

    return result
