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


def sindent(
    level: int = 0, base: int = 1, spaces: int = 4, istab: bool = False
) -> str:
    """
        Gets the indentation spaces for the given level; with the given base
        indentation level, i.e., the number of spaces for each indentation
        level is 4 by default, the base indentation level is 1, and each extra
        level is controlled by the level parameter. In the case of using tabs,
        the base indentation level is 1 tab.

        :param level: The requested indentation level; zero by default.

        :param base: The base indentation level.

        :param spaces: The number of spaces for each indentation level.

        :param istab: A boolean flag that indicates if the indentation is done
        using tabs or spaces. True if tabs are used; False otherwise. False by
        default.

        :return: The indentation string.
    """
    # Set the indentation character.
    character: str = "\t" if istab else " " * spaces

    return character * (base + level)


def normalize(
    string: str, indent: int = 0, chars: int = 60, include: bool = False
) -> str:
    """
        Gets the normalized string of the string; i.e., the string indented by
        the given number of indentation levels. Each line cannot exceed the
        given number of characters; NOT including the indentation level. If
        you wish to include the indentation level in the character count, then
        set the include flag to True.

        :param string: The string to be normalized.

        :param indent: The number of indentation levels for the string; and
        only used if the string exceeds the given number of characters per
        line.

        :param chars: The maximum number of characters per line.

        :param include: A boolean flag that indicates if the indentation level
        is included in the character count. True if the indentation level is
        included; False otherwise.

        :return: The string representation of the object.
    """
    # Auxiliary variables.
    indnt: str = sindent(indent, base=0)
    tlines: list = []

    # Split the string into lines.
    lines: list = string.split("\n")

    # Iterate over the lines.
    for line in lines:
        # Reset the line string.
        words: list = line.replace("\t", sindent()).split(" ")
        tstring: str = f"{words[0]}" if len(words) > 0 else ""

        # Split the line into words.
        for i, word in enumerate(words):
            # No need to check the first word.
            if i == 0:
                continue

            # Append the word to the line.
            ttstring: str = f"{tstring} {word}"

            # Append the word to the line.
            if len(f"{indnt}{ttstring}" if include else ttstring) <= chars:
                tstring = ttstring
                continue

            if len(word) / chars <= 0.2:
                # Append the line, deleting trailing spaces.
                tlines.append(f"{indnt}{tstring}".rstrip())
                tstring = f"{word}"
                continue

            # Fit letter by letter into the line.
            tstring = f"{tstring} {word[0]}"

            # Get the excess characters to complete the line.
            for j, letter in enumerate(word):
                # No need to check the first letter.
                if j == 0:
                    continue

                # Append the letter to the line.
                srepr = tstring + letter
                srepr = f"{indnt}{srepr}" if include else srepr

                if len(srepr) <= chars:
                    tstring += letter
                    continue

                # Append the line.
                tlines.append(f"{indnt}{tstring}")
                tstring = f"{letter}"

        # Append the last line, deleting trailing spaces.
        tlines.append(f"{indnt}{tstring}".rstrip())

    return f"\n".join(tlines)


def normalize_repr(
    string: str, indent: int = 0, chars: int = 60, include: bool = False
) -> str:
    """
        Gets the normalized string representation of the string; i.e., the
        string is placed into parentheses in different lines and indented by
        the given number of indentation levels. Each line cannot exceed the
        given number of characters.

        If the word is 20% of the line, and adding the word to the line exceeds
        the character limit, then the word will be split into several lines;
        even if not aesthetically pleasing.

        :param string: The string to be normalized.

        :param indent: The number of indentation levels for the string; and
        only used if the string exceeds the given number of characters per
        line.

        :param chars: The maximum number of characters per line.

        :param include: A boolean flag that indicates if the indentation level
        is included in the character count. True if the indentation level is
        included; False otherwise.

        :return: The string representation of the object.
    """
    # Auxiliary variables.
    indnt: str = sindent(indent + 1, base=0)
    tlines: list = []

    # Split the string into lines.
    lines: list = string.split("\n")

    # Iterate over the lines.
    for line in lines:
        # Reset the line string.
        words: list = line.replace("\t", sindent()).split(" ")
        tstring: str = f"{words[0]}" if len(words) > 0 else ""

        # Split the line into words.
        for i, word in enumerate(words):
            # No need to check the first word.
            if i == 0:
                continue

            # Append the word to the line.
            ttstring: str = f"{tstring} {word}"
            srepr: str = repr(ttstring)

            if len(f"{indnt}{srepr}" if include else srepr) <= chars:
                tstring = ttstring
                continue

            if len(word) / chars <= 0.2:
                # Append the line, deleting trailing spaces.
                tlines.append(f"{indnt}{repr(tstring)}")
                tstring = f"{word}"
                continue

            # Fit letter by letter into the line.
            tstring = f"{tstring} {word[0]}"

            # Get the excess characters to complete the line.
            for j, letter in enumerate(word):
                # No need to check the first letter.
                if j == 0:
                    continue

                # Append the letter to the line.
                srepr = tstring + letter
                srepr = f"{indnt}{repr(srepr)}" if include else repr(srepr)

                if len(srepr) <= chars:
                    tstring += letter
                    continue

                # Append the line.
                tlines.append(f"{indnt}{repr(tstring)}")
                tstring = f"{letter}"

        # Append the last line, deleting trailing spaces.
        tstring = repr(tstring.rstrip() + '\n')
        tlines.append(f"{indnt}{tstring}")

    # Check if the string has more than one line.
    flag: bool = len(tlines) > 1
    indnt = sindent(indent, base=0)

    # Check if the string has more than one line and indent as needed.
    if flag:
        tstring = f"{indnt}(\n" + f"\n".join(tlines) + f"\n{indnt})"

    else:
        tstring = f"{indnt}{tlines[0].strip()}"

    return tstring
