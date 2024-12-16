"""
    Different string manipulation functions.
"""


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
    # Edge cases.
    if message is None or message == "":
        return base

    if base.endswith("."):
        return f"{base} {message}"

    if base.strip().endswith("."):
        return f"{base}{message}"

    return f"{base}. {message}"
