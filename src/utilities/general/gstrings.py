"""
    Different string manipulation functions.
"""


# #############################################################################
# Parameter Validation
# #############################################################################


def parameters_messages_concat(base: str, message: str) -> None:
    """
        Validates the parameters for the messages_concat function are of the
        correct type; i.e., strings.

        :param base: The base message to which the message will be appended.

        :param message: The message to be appended.

        :raises AssertionError: If the parameters are not strings.
    """
    # Messages.
    mbase: str = "The base message is not a string."
    mmessage: str = "The message is not a string."

    # Check the parameters are strings.
    assert isinstance(base, str), mbase
    assert isinstance(message, str), mmessage


# #############################################################################
# Functions
# #############################################################################


def messages_concat(base: str, message: str) -> str:
    """
        Concatenates the message to the base message.

        :param base: The base message to which the message will be appended.

        :param message: The message to be appended.

        :return: The concatenated message.
    """
    # Validate the parameters.
    parameters_messages_concat(base, message)

    # Edge cases.
    if message is None or message == "":
        return base

    if base.strip() == "":
        return message

    if base.endswith("."):
        return f"{base} {message}"

    if base.strip().endswith("."):
        return f"{base}{message}"

    return f"{base}. {message}"
