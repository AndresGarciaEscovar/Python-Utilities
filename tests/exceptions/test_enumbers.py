"""
    Contains the tests for the numerical validation errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from gutilities.exceptions.enumbers import (
    AboveBelowBoundError, NotInRangeError
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def test_number_errors_abovebelowbounderror():
    """
        Tests the AboveBelowBoundError exception.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "message": None,
        "value": 7.6,
        "bound": 8,
        "include_greater": (True, True),
    }

    # ---------------------------------------------------------------------
    # Test 1: The error message must match the expected message.
    # ---------------------------------------------------------------------

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The message is not the expected one; value is greater "
        "than or equal."
    )

    # Expected message.
    expected: str = (
        f"The value is not in the expected range. The given value "
        f"({kwargs['value']}) is NOT greater than, or equal to, the "
        f"bound. The bound is {kwargs['bound']}."
    )

    # Error class.
    error: AboveBelowBoundError = AboveBelowBoundError(**kwargs)

    assert error.message == expected, message

    # ---------------------------------------------------------------------
    # Test 2: The error message must match the expected message.
    # ---------------------------------------------------------------------

    # Set the message in case an error happens.
    message = (
        "Test 2: The message is not the expected one; value is greater "
        "than."
    )

    # Change the parameters as needed.
    kwargs["include_greater"] = (False, True)

    # Expected message.
    expected = (
        f"The value is not in the expected range. The given value "
        f"({kwargs['value']}) is NOT greater than the bound. The "
        f"bound is {kwargs['bound']}."
    )

    # Error class.
    error = AboveBelowBoundError(**kwargs)

    assert error.message == expected, message

    # ---------------------------------------------------------------------
    # Test 3: The error message must match the expected message.
    # ---------------------------------------------------------------------

    # Set the message in case an error happens.
    message = (
        "Test 3: The message is not the expected one; value is less than "
        "or equal."
    )

    # Change the parameters as needed.
    kwargs["value"] = 9
    kwargs["include_greater"] = (True, False)

    # Expected message.
    expected = (
        f"The value is not in the expected range. The given value "
        f"({kwargs['value']}) is NOT less than, or equal to, the "
        f"bound. The bound is {kwargs['bound']}."
    )

    # Error class.
    error = AboveBelowBoundError(**kwargs)

    assert error.message == expected, message

    # ---------------------------------------------------------------------
    # Test 4: The error message must match the expected message.
    # ---------------------------------------------------------------------

    # Set the message in case an error happens.
    message = (
        "Test 4: The message is not the expected one; value is less than."
    )

    # Change the parameters as needed.
    kwargs["include_greater"] = (False, False)

    # Expected message.
    expected = (
        f"The value is not in the expected range. The given value "
        f"({kwargs['value']}) is NOT less than the bound. The bound "
        f"is {kwargs['bound']}."
    )

    # Error class.
    error = AboveBelowBoundError(**kwargs)

    assert error.message == expected, message


def test_number_errors_notinrangeerror():
    """
        Tests the NotInRangeError exception.
    """
    # Auxiliary variables.
    kwargs: dict = {
        "message": None,
        "value": 7.6,
        "vrange": (8, 12),
        "include": (False, True)
    }

    # ---------------------------------------------------------------------
    # Test 1: The error message must match the expected message.
    # ---------------------------------------------------------------------

    # Set the message in case an error happens.
    message: str = (
        "Test 1: The expected message is not the same as the current "
        "message."
    )

    # Expected message.
    expected: str = (
        f"The value is not in the expected range. Current value type: "
        f"{type(kwargs['value']).__name__}. Expected range: "
        f"{kwargs['vrange']}. Included (lower, upper)? "
        f"{kwargs['include']}."
    )

    # Error class.
    error: NotInRangeError = NotInRangeError(**kwargs)

    assert error.message == expected, message
