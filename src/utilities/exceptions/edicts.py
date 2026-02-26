"""
    Custom exceptions for dictionaries.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any, Union

# User.
import utilities.general.gstrings as ustrings


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes - Exceptions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class WrongKeysError(Exception):
    """
        Exception raised when the dictionary does not have the expected keys.

        PARAMETERS:
        ___________

        - self.depth: The depth to which the dictionary must be examined.

        - self.message: The custom message, if any.

        - self._messages: A list with the error messages.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The dictionary does not have the expected keys."

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _check_keys(
        self,
        base: Any,
        original: Any,
        depth: int,
        key: str
    ) -> None:
        """
            Recursively checks the keys in the dictionaries.

            :param base: The base dictionary.

            :param original: The original dictionary.

            :param depth: The depth to which the validation should be
             performed. If None, the validation is performed to the deepest
             level of the base dictionary.

            :param key: The key of the dictionary.
        """
        # Maximum depth reached.
        if self.depth is not None and depth > self.depth:
            return

        # Determine if the dictionaries are dictionaries.
        isdict_b: bool = isinstance(base, dict)
        isdict_o: bool = isinstance(original, dict)

        # Edge cases.
        if not (isdict_b or isdict_o):
            return

        if not isdict_b and isdict_o:
            self._messages.append((
                f"Depth: {depth},", f"Key: {key},",
                "Error: Original is a dictionary at this depth and key when "
                "it should not be."
            ))
            return

        if isdict_b and not isdict_o:
            self._messages.append((
                f"Depth: {depth},", f"Key: {key},",
                "Error: Original is NOT a dictionary at this depth and key "
                "when it should be."
            ))
            return

        # Missing and excess keys.
        missing: set = set(base.keys()) - set(original.keys())
        excess: set = set(original.keys()) - set(base.keys())

        if missing or excess:
            strm: str = f"{missing}" if len(missing) > 0 else "{}"
            stre: str = f"{excess}" if len(excess) > 0 else "{}"

            key_ = key if key != "" else "'root'"

            self._messages.append((
                f"Depth: {depth},", f"Key: {key_},",
                f"Error: Missing or excess keys; missing: {strm}, excess: "
                f"{stre}."
            ))

        # Adjust the depth and continue.
        ndepth: int = depth + 1

        for key_ in base.keys():
            if key_ not in original:
                continue

            tkey: str = f"'{key_}'" if isinstance(key_, str) else f"{key_}"
            tkey = f"{key}.{tkey}" if key != "" else f"{tkey}"

            self._check_keys(base[key_], original[key_], ndepth, tkey)

    def _customize_base(self) -> None:
        """
            Customizes the exception message when only the base dictionary is
            provided.
        """
        # Auxiliary variables.
        message: str = (
            "The base dictionary is not a dictionary; for futher "
            "comparison please provide both the original and base "
            "dictionaries."
        )

        # Concatenate the messages.
        self.message = ustrings.messages_concat(self.message, message)

    def _customize_both(self, base: dict, original: dict) -> None:
        """
            Customizes the exception message when both the original and base
            dictionaries are provided.

            :param base: The base dictionary.

            :param original: The original dictionary.
        """
        # Vaidate the dictionaries.
        self._messages: list = []

        # Check the keys.
        self._check_keys(base, original, 0, "")

        # Format the final message.
        self._messages = [" ".join(x) for x in self._messages]
        fmessage = "\nErrors:" + "\n- " + "\n- ".join(self._messages)

        # Concatenate the messages.
        self.message = ustrings.messages_concat(self.message, fmessage)

    def _customize_original(self) -> None:
        """
            Customizes the exception message when only the original dictionary
            is provided.
        """
        # Auxiliary variables.
        message: str = (
            "The original dictionary is not a dictionary; for futher "
            "comparison please provide both the original and base "
            "dictionaries."
        )

        # Concatenate the messages.
        self.message = ustrings.messages_concat(self.message, message)

    def _validate_depth(self) -> None:
        """
            Validates the depth attribute.

            :raises TypeError: If the depth is not an integer.

            :raises ValueError: If the depth is less than 0.
        """
        # Auxiliary variables.
        message: str = ""

        # Check the depth is an integer.
        if self.depth is not None and not isinstance(self.depth, int):
            message += "The depth must be provided and must be an integer."
            raise TypeError(message)

        # Check the depth is positive or zero.
        if self.depth is not None and self.depth < 0:
            message += "The depth must be greater than or equal to 0."
            raise ValueError(message)

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self,
        message: Union[None, str] = None,
        base: Union[dict, None] = None,
        original: Union[dict, None] = None,
        depth: Union[int, None] = None
    ):
        """
            Initializes the exception.

            :param message: The exception message.

            :param base: The base dictionary.

            :param original: The original dictionary.

            :param depth: The depth to which the validation should be
             performed. If None, the validation is performed to the deepest
             level of the base dictionary.
        """
        # Auxiliary variables.
        default: str = WrongKeysError.DEFAULT

        # Extract the parameters.
        self.depth: int = 0 if depth is None or depth <= 0 else int(depth)
        self.message: str = default if message is None else message
        self._messages: list = []

        # Set the attributes.
        isdict_orig: bool = isinstance(original, dict)
        isdict_base: bool = isinstance(base, dict)

        # Check the depth is passed as a parameter if needed.
        self._validate_depth()

        # Format the message accordingly.
        if isdict_orig and isdict_base:
            self._customize_both(base, original)

        if not isdict_base:
            self._customize_base()

        if not isdict_orig:
            self._customize_original()

        # Call the parent constructor.
        super().__init__(self.message)
