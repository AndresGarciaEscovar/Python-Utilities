"""
    Different string manipulation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def _normalize_append(
    line: str,
    word: str,
    chars: int,
    offset: int,
    index: int
) -> str:
    """
        Appends the word to the given line, if the line with the appended word
        does not exceed the maximum number of characters.

        :param line: The line where the word must be appended.

        :param word: The word to be appended to the line.

        :param chars: The maximum number of characters.

        :param offset: The number by which the length of the line must be
         offset.

        :return: The string with the word appended, or not.
    """
    # Auxiliary variables.
    newline: str = f"{word}" if index == 0 else f"{line} {word}"

    # Check the line is the correct length.
    if len(newline) + offset > chars:
        newline = line

    return newline


def _normalize_get_words(line: str, ) -> list:
    """
        From the given line, replaces all the tabs with the spaces and then
        splits the line into words; i.e., the line split using spaces.

        :param line: The line from where the words must be obtained.
    """
    return line.replace("\t", sindent()).split(" ")


def _normalize_string(line: str, word: str, chars: int, offset: int) -> tuple:
    """
        Creates as many strings as needed to fit the word, provided that there
        is still 20 percent of the string to fill, or the word takes at least
        20% of the remaining string.

        :param line: The line where the word must be appended.

        :param word: The word to be appended to the line.

        :param chars: The maximum number of characters.

        :param offset: The number by which the length of the line must be
         offset.

        :return: The string with the word appended, or not.
    """
    # Auxiliary variables.
    final_line: str = line
    final_word: str = word

    flag: bool = final_word.strip() == ""
    lines: list = []
    total: int = chars + offset
    remaining: int = total - len(f"{final_line} ")

    # Fix as needed.
    if flag or len(final_word) / total <= 0.2 or remaining / total <= 0.1:
        # No need to fix.
        lines = [line]

    else:
        # Must be fixed.
        while len(final_word) > total:
            # Remaining characters.
            final_line = f"{final_line} ".lstrip()
            final_index: int = total - len(final_line)

            # Get the proper final line.
            final_line = f"{final_line} {final_word[:final_index]}".strip()

            # Append the line.
            lines.append(final_line)

            # Calculate again.
            final_line = ""
            final_word = final_word[final_index:]

    return lines, final_word


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
    offset: int = len(base) if include else 0

    # For each line.
    for line in text.split("\n"):
        # Reset the line string.
        string: str = ""
        strings: list = []

        # Split the line into words.
        for i, word in enumerate(_normalize_get_words(line)):
            temp: str = _normalize_append(string, word, chars, offset, i)

            # Word could not be appended.
            if string == temp:
                results: tuple = _normalize_string(string, word, chars, offset)
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
    string: str,
    indent: int = 0,
    chars: int = 60,
    include: bool = False
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
    # Validate the parameters.
    _parameters_normalize(string, indent, chars, include)

    # Auxiliary variables.
    indnt: str = sindent(indent + 1, base=0)
    tlines: list = []

    # Split the string into lines.
    lines: list = string.split("\n")

    # Iterate over the lines.
    for line in lines:
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

            # Remaining characters.
            srepr = f"{indnt}{repr(tstring)}" if include else repr(tstring)
            remaining: int = chars - len(srepr)

            if len(word) / chars <= 0.2 or remaining / chars <= 0.2:
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
        tstring = f"{indnt}(\n" + "\n".join(tlines) + f"\n{indnt})"

    else:
        tstring = f"{indnt}{tlines[0].strip()}"

    return tstring


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


if __name__ == "__main__":
    string_: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consequat non augue sed faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut vitae tellus vitae dolor mattis commodo at vitae tortor. Morbi posuere enim eget magna fringilla, vitae cursus odio luctus. Curabitur molestie neque nulla, non interdum elit gravida a. Etiam scelerisque fermentum dolor, consectetur pellentesque nibh pulvinar ut. Aliquam luctus posuere risus, et pulvinar purus vulputate mattis. Nullam sit amet pretium velit, vel consectetur dui.

Nam mollis, odio et accumsan finibus, erat metus gravida lectus, sed facilisis orci leo eu mi. Pellentesque leo felis, consectetur quis dictum in, ullamcorper quis tortor. Phasellus egestas facilisis feugiat. Curabitur vulputate laoreet lorem, in consectetur odio mattis porttitor. Integer pharetra lorem et pharetra pellentesque. Maecenas in diam sit amet justo faucibus hendrerit eu a leo. Donec feugiat elit sit amet tempus cursus. Sed tincidunt rutrum neque vitae pellentesque. Vestibulum at ex sed felis pharetra mattis. Maecenas ut metus feugiat, fringilla felis sed, finibus purus. Morbi nec lobortis velit, quis finibus orci. Etiam malesuada, nibh ut hendrerit pharetra, mauris nunc faucibus tortor, eget efficitur mi ante vel tellus. Nulla nisl eros, finibus et semper quis, euismod ut nisi. Integer interdum, nulla at egestas mattis, sem urna mattis nisl, at ullamcorper felis massa ut risus.

In hac habitasse platea dictumst. Quisque sed felis non ipsum porta dapibus. Pellentesque euismod ut metus a suscipit. Nulla vitae ipsum dui. Nam consequat in lectus sed fringilla. Proin rhoncus augue vel pretium gravida. Donec neque felis, gravida at commodo eget, feugiat nec augue. Sed et ultrices lorem. Mauris vitae erat mi. Maecenas consequat orci nulla, quis aliquet ligula posuere sit amet. Nunc auctor lorem non iaculis pellentesque. Pellentesque blandit volutpat urna, quis maximus mauris facilisis ut. Pellentesque elementum eleifend metus ut laoreet. Cras aliquam ullamcorper semper. Aenean tincidunt egestas tempus.

Etiam ante mi, tempus quis iaculis quis, scelerisque non odio. Suspendisse ut fermentum tellus, ac molestie diam. Sed in sem dignissim, rutrum lorem id, consequat est. Aenean leo mi, aliquam tristique ex id, consectetur congue ligula. Maecenas nisl nisl, bibendum at mi nec, suscipit luctus diam. Nam tempor euismod orci, vitae faucibus eros laoreet eu. Etiam id dapibus ante.

Phasellus malesuada ornare purus, vel pulvinar sem semper eget. Ut at nulla lacus. Cras et mi ut enim ornare congue. Etiam eu varius velit. Nam elementum pharetra ipsum, sit amet auctor augue ultrices at. Donec a magna finibus, faucibus urna quis, pulvinar leo. Curabitur feugiat nisi vehicula placerat varius. Mauris ex sapien, porttitor vitae tortor vel, semper vulputate nunc. Nam efficitur, turpis ut imperdiet luctus, sem ligula efficitur ligula, non commodo libero justo eget lectus. In ut sagittis nisl.
    """.strip()

    print(normalize_repr(string_, indent=1, include=False))
