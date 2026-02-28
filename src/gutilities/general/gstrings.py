"""
    Different string manipulation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _normalize_append(
    line: str,
    word: str,
    maximum: int,
    irepr: bool =  False
) -> str:
    """
        Appends the word to the given line, if the line with the appended word
        does not exceed the maximum number of characters.

        :param line: The line where the word must be appended.

        :param word: The word to be appended to the line.

        :param maximum: The maximum length of the string.

        :param irepr: A boolean flag indicating whether the representation is
         needed or the text string. True, if the representation (repr) is
         needed; False, if the regular text string is enough. False, by
         default.

        :return: The string with the word appended, or not.
    """
    # Auxiliary variables.
    char: str = " " if irepr else ""
    newline: str = f"{word}{char}" if line == "" else f"{line} {word}{char}"
    length: int = len(repr(newline)) if irepr else len(newline)

    # Check the line is the correct length.
    if length > maximum:
        newline = line

    return newline

def _normalize_get_words(line: str, irepr: bool =  False) -> list:
    """
        From the given line, replaces all the tabs with the spaces and then
        splits the line into words; i.e., the line split using spaces.

        :param line: The line from where the words must be obtained.

        :param irepr: A boolean flag indicating whether the representation is
         needed or the text string. True, if the representation (repr) is
         needed; False, if the regular text string is enough. False, by
         default.
    """
    # If it is a representation.
    if irepr:
        return line.split(" ")

    return line.replace("\t", sindent()).split(" ")


def _normalize_string(line: str, word: str, maximum: int) -> tuple:
    """
        Creates as many strings as needed to fit the word, provided that there
        is still 20 percent of the string to fill, or the word takes at least
        20% of the remaining string.

        :param line: The line where the word must be appended.

        :param word: The word to be appended to the line.

        :param maximum: The maximum length of the string.

        :return: The string with the word appended, or not.
    """
    # Auxiliary variables.
    final_line: str = line
    final_word: str = word

    flag: bool = final_word.strip() == ""
    lines: list = []
    remaining: int = maximum - len(f"{final_line} ")

    # Fix as needed.
    if flag or len(final_word) / maximum <= 0.2 or remaining / maximum <= 0.1:
        # No need to fix.
        lines = [line]

    else:
        # Must be fixed.
        while len(final_word) > maximum:
            # Remaining characters.
            final_line = f"{final_line} ".lstrip()
            final_index: int = maximum - len(final_line)

            # Get the proper final line.
            final_line = f"{final_line} {final_word[:final_index]}".strip()

            # Append the line.
            lines.append(final_line)

            # Calculate again.
            final_line = ""
            final_word = final_word[final_index:]

    return lines, final_word


def _normalize_string_repr(line: str, word: str, maximum: int) -> tuple:
    """
        Creates as many strings as needed to fit the word, provided that there
        is still 20 percent of the string to fill, or the word takes at least
        20% of the remaining string.

        :param line: The line where the word must be appended.

        :param word: The word to be appended to the line.

        :param maximum: The maximum length of the string.

        :return: The string with the word appended, or not.
    """
    # Auxiliary variables.
    final_line: str = line
    final_word: str = word

    lines: list = []
    new_word: bool = False
    remaining: int = maximum - len(repr(f"{final_line} "))

    # Fix as needed.
    if len(final_word) / maximum <= 0.2 or remaining / maximum <= 0.1:
        # No need to fix.
        lines = [line]
        new_word = True

    else:
        # Must be fixed.
        while len(final_word) > maximum:
            # Remaining characters.
            final_line = f"{final_line} "
            final_index: int = maximum - len(repr(final_line))

            # Get the proper final line.
            final_line = f"{final_line} {final_word[:final_index]}"

            # Append the line.
            lines.append(final_line)

            # Calculate again.
            final_line = ""
            final_word = final_word[final_index:]

    return lines, final_word, new_word


def _parameters_messages_concat(base: str, message: str) -> None:
    """
        Validates the parameters for the messages_concat function are of the
        correct type; i.e., strings.

        :param base: The base message to which the message will be appended.

        :param message: The message to be appended.

        :raises TypeError: If the parameters are not strings.
    """
    # Check the parameters are strings.
    if not isinstance(base, str):
        raise TypeError("The base message is not a string.")

    if not isinstance(message, str):
        raise TypeError("The message is not a string.")


def _parameters_normalize(
    string: str,
    indent: int = 0,
    chars: int = 60,
    include: bool = False
) -> None:
    """
        Validates the parameters for the normalize function are of the correct
        type; i.e., strings and integers.

        :param string: The string to be normalized.

        :param indent: The number of indentation levels for the string; and
         only used if the string exceeds the given number of characters per
         line.

        :param chars: The maximum number of characters per line.

        :param include: A boolean flag that indicates if the indentation level
         is included in the character count. True if the indentation level is
         included; False otherwise.

        :raises TypeError: If the parameters are not of the correct type.
    """
    # Auxiliary variables.
    message: str = ""

    if not isinstance(string, str):
        message += "The string is not a string. "

    if not (isinstance(indent, int) and indent >= 0):
        message += (
            "The indent is not an integer greater than or equal to zero. "
        )

    if not (isinstance(chars, int) and chars >= 1):
        message += "The chars is not an integer greater than or equal to one. "

    if not isinstance(include, bool):
        message += "The include is not a boolean. "

    if message != "":
        raise TypeError(message.strip())

    # Finish validating.
    if include and len(sindent(indent + 1, base=0)) >= chars:
        message += (
            "The indentation level exceeds the maximum number of characters "
            "per line."
        )

    if message != "":
        raise TypeError(message.strip())


def _parameters_sindent(
    level: int = 0,
    base: int = 1,
    spaces: int = 4,
    istab: bool = False
) -> None:
    """
        Validates the parameters for the sindent function are of the correct
        type; i.e., integers and booleans.

        :param level: The requested indentation level; zero by default.

        :param base: The base indentation level.

        :param spaces: The number of spaces for each indentation level.

        :param istab: A boolean flag that indicates if the indentation is done
         using tabs or spaces. True if tabs are used; False otherwise. False by
         default.

        :return: The indentation string.

        :raise ValueError: If any of the values are not the correct type or
         the correct value.
    """
    # Check the level is an integer.
    message: str = ""

    if not (isinstance(level, int) and level >= 0):
        message += "The level isn't an integer greater than or equal to zero. "

    if not (isinstance(base, int) and base >= 0):
        message += "The base is not an integer greater than or equal to zero. "

    if not isinstance(istab, bool):
        message += " The istab is not a boolean. "

    # Raise the error if needed.
    if message != "":
        raise ValueError(message)

    # Finish checking, if needed.
    if not istab and not (isinstance(spaces, int) and spaces >= 1):
        message += "The spaces is not an integer greater than or equal to one."

    if message != "":
        raise ValueError(message)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def messages_concat(base: str, message: str) -> str:
    """
        Concatenates the message to the base message.

        :param base: The base message to which the message will be appended.

        :param message: The message to be appended.

        :return: The concatenated message.
    """
    # Validate the parameters.
    _parameters_messages_concat(base, message)

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


def normalize(
    text: str,
    indent: int = 0,
    chars: int = 60,
    include: bool = False
) -> str:
    """
        Gets the normalized string of the string; i.e., the string indented by
        the given number of indentation levels. Each line cannot exceed the
        given number of characters; NOT including the indentation level. If the
        indentation level must be included in the character count, set the
        include flag to True. Uses the number of characters for a tab as 4.

        :param text: The string to be normalized.

        :param indent: The number of indentation levels for the string; and
         only used if the string exceeds the given number of characters per
         line.

        :param chars: The maximum number of characters per line.

        :param include: A boolean flag that indicates if the indentation level
         is included in the character count. True if the indentation level is
         included; False otherwise.

        :return: The string representation of the object.
    """
    # Validate the parameters.
    _parameters_normalize(text, indent, chars, include)

    # Auxiliary variables.
    fixed: list = []
    base: str = f"{sindent(indent, base=1)}"
    total: int = chars + (len(base) if include else 0)

    # For each line.
    for line in text.split("\n"):
        # Reset the line string.
        string: str = ""
        strings: list = []

        # Split the line into words.
        for word in _normalize_get_words(line):
            temp: str = _normalize_append(string, word, total)

            # Word could not be appended.
            if string == temp:
                results: tuple = _normalize_string(string, word, total)
                strings.extend(results[0])
                string = results[1].strip()
                continue

            # Replace the string and continue.
            string = temp.lstrip()

        # Append the final string.
        if string.rstrip() != "":
            strings.append(string.rstrip())

        # Extend the list of strings.
        fixed.extend(strings)

    return f"{base}" + f"\n{base}".join(x.rstrip() for x in fixed)


def normalize_repr(
    text: str,
    indent: int = 0,
    chars: int = 60,
    include: bool = False
) -> str:
    """
        Gets the normalized string representation of the string; i.e., the
        string is placed into parentheses in different lines and indented by
        the given number of indentation levels. Each line cannot exceed the
        given number of characters. If the indentation level must be included
        in the character count, set the include flag to True. Uses the number
        of characters for a tab as 4. The string is faithfully kept.

        If the word is 20% of the line, and adding the word to the line exceeds
        the character limit, then the word will be split into several lines;
        even if not aesthetically pleasing.

        :param text: The string to be normalized.

        :param indent: The number of indentation levels for the string; and
         only used if the string exceeds the given number of characters per
         line.

        :param chars: The maximum number of characters per line.

        :param include: A boolean flag that indicates if the indentation level
         is included in the character count. True if the indentation level is
         included; False otherwise.

        :return: The string representation of the object.
    """
    # Validate the parameters.
    _parameters_normalize(text, indent, chars, include)

    # Auxiliary variables.
    fixed: list = []
    base: str = f"{sindent(indent, base=0)}"
    basi: str = f"{sindent(indent + 1, base=0)}"
    maximum: int =  chars - (len(basi) if include else 0)

    # For each line.
    for line in text.split("\n"):
        # No need to inquire further.
        if line == "":
            fixed.append("\n")
            continue

        # Auxiliary variables for storing strings temporarily.
        string: str = ""
        strings: list = []

        words: list = _normalize_get_words(line, True)
        words[-1] += "\n"

        for word in words:
            # Get the new string
            newstring: str = _normalize_append(string, word, maximum, True)

            # String doesn't fit anymore.
            if string == newstring:
                strings.append(newstring + " ")
                newstring = f"{word} "

            # Update the string.
            string = newstring[:-1]

        # Add the new line.
        if string != "":
            strings.append(string)

        # Append the new strings.
        fixed.extend(strings)

    # Finalize joining the strings.
    string = f"{base}(\n"
    string += basi + f"\n{basi}".join(repr(x) for x in fixed)

    return string + f"\n{base})"


def sindent(
    level: int = 0,
    base: int = 1,
    spaces: int = 4,
    istab: bool = False
) -> str:
    """
        Gets the indentation spaces for the given level; with the given base
        indentation level, i.e., the number of spaces for each indentation
        level is 4 by default, the base indentation level is 1, and each extra
        level is controlled by the level parameter. In the case of using tabs,
        the base indentation level is 1 tab.

        :param level: The requested indentation level; zero by default.

        :param base: Tnewlinehe base indentation level.

        :param spaces: The number of spaces for each indentation level.

        :param istab: A boolean flag that indicates if the indentation is done
         using tabs or spaces. True if tabs are used; False otherwise. False by
         default.

        :return: The indentation string.
    """
    # Validate the parameters.
    _parameters_sindent(level, base, spaces, istab)

    # Set the indentation character.
    character: str = "\t" if istab else " " * spaces

    return character * (base + level)


# #############################################################################
# TO DELETE                                                                   #
# #############################################################################


def run() -> None:
    """
        Runs the  temporary function.
    """
    # Auxiliary variables.
    sixty: str = "Lq9vT7bP2mXz4nYd6rWk3sFj8cH0gA5uQp1BcN9dE7fXh2iYjR4kLoPmQ"
    string = "palo quemado chulo herido"
    total: int =  70

    # Line for the output.
    output: tuple = _normalize_string_repr(string, sixty, total)

    print("")
    print(output[0])
    print(output[1])
    print(output[2])
    print("")

# #############################################################################
# TO DELETE - Main Program                                                    #
# #############################################################################


if __name__ == "__main__":
    run()
