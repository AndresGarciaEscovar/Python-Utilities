"""
    Custom exceptions for dictionaries.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
from typing import Any, Type, Union

# User.
import gutilities.general.gstrings as ustrings
from gutilities.validation.vgeneral import (
    validate_type
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_types_name(dtype: Union[None, tuple, Type]) -> str:
    """
        Extracts the type name from the given object.

        :param dtype: The possible data type.

        :return: The string with the type name(s).
    """
    # Auxiliary variables.
    name: str = ""

    # Extract the type(s) from the proper structure.
    if isinstance(tuple):
        # Extract the values from the tuples.
        name += ", ".join(
            list(set("None" if x is None else type(x).__name__ for x in dtype))
        )

    elif dtype is None:
        # If the value is None.
        name += "None"

    else:
        # The value is of type "type."
        name = dtype.__name__

    return name


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
        path: str
    ) -> None:
        """
            Recursively checks the keys in the dictionaries.

            :param base: The base dictionary.

            :param original: The original dictionary.

            :param depth: The depth to which the validation should be
             performed. If None, the validation is performed to the deepest
             level of the base dictionary.

            :param path: The key of the dictionary.
        """
        # Maximum depth reached.
        flag: bool = self.depth is not None

        if flag and self.depth != -1 and depth > self.depth:
            return

        # Determine if the dictionaries are dictionaries.
        isdict_b: bool = isinstance(base, dict)
        isdict_o: bool = isinstance(original, dict)

        # Edge cases.
        if not (isdict_b or isdict_o):
            # Neither one is a dictionary, comparison has succeeded.
            return

        if not isdict_b and isdict_o:
            # The original object is a dictionary, when it shouldn't.
            self._messages.append((
                f"Depth: {depth},",
                f"Key: {path},",
                "Error: The original object is a dictionary at this depth and "
                "key when it should not be."
            ))
            return

        if isdict_b and not isdict_o:
            # The original object is NOT a dictionary, when it should be.
            self._messages.append((
                f"Depth: {depth},",
                f"Key: {path},",
                "Error: The original object is NOT a dictionary at this depth "
                "and key when it should be."
            ))
            return

        # Missing and excess keys.
        missing: set = set(base.keys()) - set(original.keys())
        excess: set = set(original.keys()) - set(base.keys())

        if missing or excess:
            self._messages.append((
                f"Depth: {depth},",
                f"Key: {path},",
                f"Error: Missing or excess keys; missing: {missing or '{}'}, "
                f"excess: {excess or '{}'}."
            ))

        # Next depth level.
        for key in base.keys():
            # Check if the key exits.
            if key not in original:
                continue

            # Extract the next key.
            tkey: str = f"'{key}'" if isinstance(key, str) else f"{key}"
            tkey = f"{path}.{tkey}" if path != "" else tkey

            # Recursive step.
            self._check_keys(base[key], original[key], depth + 1, tkey)

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
        # Auxiliary variables.
        self._messages: list = []

        # Check the keys.
        self._check_keys(base, original, 0, "'root'")

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

    def _set_message(self, base: Any, original: Any) -> None:
        """
            Sets the message properly.

            :param base: The base dictionary.

            :param original: The original dictionary.
        """
        # No need to set the message.
        if self.depth is None:
            return

        # Determine if dictionaries are needed.
        isdict_orig: bool = isinstance(original, dict)
        isdict_base: bool = isinstance(base, dict)

        # Format the message accordingly.
        if isdict_orig and isdict_base:
            self._customize_both(base, original)

        if not isdict_base:
            self._customize_base()

        if not isdict_orig:
            self._customize_original()

    def _validate_depth(self) -> None:
        """
            Validates the depth attribute.

            :raises TypeError: If the depth is not an integer.

            :raises ValueError: If the depth is less than -1.
        """
        # Auxiliary variables.
        message: str = ""

        # Check the depth properties.
        if self.depth is not None and not isinstance(self.depth, int):
            message += "The depth must be provided and must be an integer."

        if isinstance(self.depth, int) and self.depth < -1:
            message += "The depth must be greater than or equal to -1."

        # Raise an error, if needed.
        if message != "":
            raise ValueError(message.strip())

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
             performed. If None, the validation is NOT performed.
        """
        # Auxiliary variables.
        default: str = WrongKeysError.DEFAULT

        # Extract the parameters.
        self.depth: Union[int, None] = depth
        self.message: str = default if message is None else message
        self._messages: list = []

        # Validate the parameters before continuing.
        self._validate_depth()
        self._set_message(base, original)

        # Call the parent constructor.
        super().__init__(self.message)


class WrongKeysAndTypeError(Exception):
    """
        Exception raised when the dictionary does not have the expected keys,
        and the types at the branches of the base dictionary are the same
        as the requested key.

        PARAMETERS:
        ___________

        - self.extract: A boolean flag indicating whether the data type of the
          base dictionary must be extracted rather than directly used. True, if
          the data type must be extracted; False, otherwise.

        - self.message: The custom message, if any.

        - self._messages: A list with the error messages.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = (
        "The dictionary does not have the expected keys and the types at the "
        "ends are not the expected ones."
    )

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _check_keys(
        self,
        base: Any,
        original: Any,
        path: str
    ) -> None:
        """
            Recursively checks the keys in the dictionaries.

            :param base: The base dictionary.

            :param original: The original dictionary.

            :param depth: The depth to which the validation should be
             performed. If None, the validation is performed to the deepest
             level of the base dictionary.

            :param path: The key of the dictionary.
        """
        # Determine if the dictionaries are dictionaries.
        isdict_b: bool = isinstance(base, dict)
        isdict_o: bool = isinstance(original, dict)

        dtype: Type = type(base) if self.extract and not isdict_b else base

        # Edge cases.
        if not isdict_b:
            # Extract the types.
            flag: bool = original is None
            dtype_b: Union[tuple, Type] = type(base) if self.extract else base
            dtype_o: Union[None, Type] = None if flag else type(original)

            # If the types are not valid.
            if not validate_type(original, dtype):
                self._messages.append((
                    f"Key: {path},",
                    f"Error: The original object of the original dictionary "
                    f"is not of the requested type; requested type: "
                    f"{_get_types_name(dtype_b)}, current type: "
                    f"{_get_types_name(dtype_o)}."
                ))

            return

        if not isdict_o:
            # The original object is a NOT a dictionary, when it should.
            self._messages.append((
                f"Key: {path},",
                f"Error: The original object is a NOT dictionary when it "
                f"should; current type: {_get_types_name(type(isdict_o))}."
            ))
            return

        # Missing and excess keys.
        excess: set = set(original.keys()) - set(base.keys())
        missing: set = set(base.keys()) - set(original.keys())

        if excess or missing:
            self._messages.append((
                f"Key: {path},",
                f"Error: Missing or excess keys; missing: {missing or '{}'}, "
                f"excess: {excess or '{}'}."
            ))

        # Next depth level.
        for key in base.keys():
            # Check if the key exits.
            if key not in original:
                continue

            # Extract the next key.
            tkey: str = f"'{key}'" if isinstance(key, str) else f"{key}"
            tkey = f"{path}.{tkey}" if path != "" else tkey

            # Recursive step.
            self._check_keys(base[key], original[key], tkey)

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
        # Auxiliary variables.
        self._messages: list = []

        # Check the keys.
        self._check_keys(base, original, "'root'")

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

    def _set_message(self, base: Any, original: Any) -> None:
        """
            Sets the message properly.

            :param base: The base dictionary.

            :param original: The original dictionary.
        """
        # Determine if dictionaries are needed.
        isdict_orig: bool = isinstance(original, dict)
        isdict_base: bool = isinstance(base, dict)

        # Format the message accordingly.
        if isdict_orig and isdict_base:
            self._customize_both(base, original)

        if not isdict_base:
            self._customize_base()

        if not isdict_orig:
            self._customize_original()

    def _validate_extract(self) -> None:
        """
            Validates the extract attribute.

            :raises TypeError: If the extract parameter is not a boolean value.
        """
        # Check the extract property.
        if not isinstance(self.extract, bool):
            raise TypeError(
                f"The extract parameter must be a boolean value; current "
                f"type: {type(self.extract).__name__}."
            )

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self,
        message: Union[None, str] = None,
        base: Union[dict, None] = None,
        original: Union[dict, None] = None,
        extract: bool = False,
    ):
        """
            Initializes the exception.

            :param message: The exception message.

            :param base: The base dictionary.

            :param original: The original dictionary.

            :param extract: A boolean flag indicating whether the data type of
             the base dictionary must be extracted rather than directly used.
             True, if the data type must be extracted; False, otherwise.
        """
        # Auxiliary variables.
        default: str = WrongKeysAndTypeError.DEFAULT

        # Extract the parameters.
        self.extract: bool = extract
        self.message: str = default if message is None else message
        self._messages: list = []

        # Validate the parameters before continuing.
        self._validate_extract()
        self._set_message(base, original)

        # Call the parent constructor.
        super().__init__(self.message)


class WrongKeysSubsetError(Exception):
    """
        Exception raised when a dictionary is NOT a subset of a base
        dictionary, in relation to the keys.

        PARAMETERS:
        ___________

        - self.depth: The depth to which the dictionary must be examined.

        - self.message: The custom message, if any.

        - self._messages: A list with the error messages.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = "The dictionary is NOT a subset of the base dictionary."

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _check_keys(
        self,
        base: Any,
        original: Any,
        depth: int,
        path: str
    ) -> None:
        """
            Recursively checks the keys in the dictionaries.

            :param base: The base dictionary.

            :param original: The original dictionary.

            :param depth: The depth to which the validation should be
             performed. If None, the validation is performed to the deepest
             level of the base dictionary.

            :param path: The key of the dictionary.
        """
        # Maximum depth reached.
        flag: bool = self.depth is not None

        if flag and self.depth != -1 and depth > self.depth:
            return

        # Determine if the dictionaries are dictionaries.
        isdict_b: bool = isinstance(base, dict)
        isdict_o: bool = isinstance(original, dict)

        # Edge cases.
        if not (isdict_b or isdict_o):
            # Neither one is a dictionary, comparison has succeeded.
            return

        if not isdict_b and isdict_o:
            # The original object is a dictionary, when it shouldn't.
            self._messages.append((
                f"Depth: {depth},",
                f"Key: {path},",
                "Error: The original object is a dictionary at this depth and "
                "key when it should not be."
            ))
            return

        if isdict_b and not isdict_o:
            # The original object is NOT a dictionary, when it should be.
            self._messages.append((
                f"Depth: {depth},",
                f"Key: {path},",
                "Error: The original object is NOT a dictionary at this depth "
                "and key when it should be."
            ))
            return

        # Excess keys.
        excess: set = set(original.keys()) - set(base.keys())

        if excess:
            self._messages.append((
                f"Depth: {depth},",
                f"Key: {path},",
                f"Error: Excess keys: {excess or '{}'}."
            ))

        # Next depth level.
        for key in base.keys():
            # Check if the key exits.
            if key not in original:
                continue

            # Extract the next key.
            tkey: str = f"'{key}'" if isinstance(key, str) else f"{key}"
            tkey = f"{path}.{tkey}" if path != "" else tkey

            # Recursive step.
            self._check_keys(base[key], original[key], depth + 1, tkey)

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
        # Auxiliary variables.
        self._messages: list = []

        # Check the keys.
        self._check_keys(base, original, 0, "'root'")

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

    def _set_message(self, base: Any, original: Any) -> None:
        """
            Sets the message properly.

            :param base: The base dictionary.

            :param original: The original dictionary.
        """
        # No need to set the message.
        if self.depth is None:
            return

        # Determine if dictionaries are needed.
        isdict_orig: bool = isinstance(original, dict)
        isdict_base: bool = isinstance(base, dict)

        # Format the message accordingly.
        if isdict_orig and isdict_base:
            self._customize_both(base, original)

        if not isdict_base:
            self._customize_base()

        if not isdict_orig:
            self._customize_original()

    def _validate_depth(self) -> None:
        """
            Validates the depth attribute.

            :raises TypeError: If the depth is not an integer.

            :raises ValueError: If the depth is less than -1.
        """
        # Auxiliary variables.
        message: str = ""

        # Check the depth properties.
        if self.depth is not None and not isinstance(self.depth, int):
            message += "The depth must be provided and must be an integer."

        if isinstance(self.depth, int) and self.depth < -1:
            message += "The depth must be greater than or equal to -1."

        # Raise an error, if needed.
        if message != "":
            raise ValueError(message.strip())

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
             performed. If None, the validation is NOT performed.
        """
        # Auxiliary variables.
        default: str = WrongKeysSubsetError.DEFAULT

        # Extract the parameters.
        self.depth: Union[int, None] = depth
        self.message: str = default if message is None else message
        self._messages: list = []

        # Validate the parameters before continuing.
        self._validate_depth()
        self._set_message(base, original)

        # Call the parent constructor.
        super().__init__(self.message)


class WrongKeysSubsetAndTypeError(Exception):
    """
        Exception raised when a dictionary is NOT a subset of a base
        dictionary, in relation to the keys, and the types at the branches of
        the base dictionary are the same as the requested key.

        PARAMETERS:
        ___________

        - self.extract: A boolean flag indicating whether the data type of the
          base dictionary must be extracted rather than directly used. True, if
          the data type must be extracted; False, otherwise.

        - self.message: The custom message, if any.

        - self._messages: A list with the error messages.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    DEFAULT: str = (
        "The dictionary is NOT a subset of the base dictionary and the types "
        "at the ends are not the expected ones."
    )

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _check_keys(
        self,
        base: Any,
        original: Any,
        path: str
    ) -> None:
        """
            Recursively checks the keys in the dictionaries.

            :param base: The base dictionary.

            :param original: The original dictionary.

            :param depth: The depth to which the validation should be
             performed. If None, the validation is performed to the deepest
             level of the base dictionary.

            :param path: The key of the dictionary.
        """
        # Determine if the dictionaries are dictionaries.
        isdict_b: bool = isinstance(base, dict)
        isdict_o: bool = isinstance(original, dict)

        dtype: Type = type(base) if not isdict_b and self.extract else base

        # Edge cases.
        if not isdict_b:
            # Extract the types.
            flag: bool = original is None
            dtype_b: Union[tuple, Type] = type(base) if self.extract else base
            dtype_o: Union[None, Type] = None if flag else type(original)

            # If the types are not valid.
            if not validate_type(original, dtype):
                self._messages.append((
                    f"Key: {path},",
                    f"Error: The original object of the original dictionary "
                    f"is not of the requested type; requested type: "
                    f"{_get_types_name(dtype_b)}, current type: "
                    f"{_get_types_name(dtype_o)}."
                ))

            return

        if not isdict_o:
            # The original object is a NOT a dictionary, when it should.
            self._messages.append((
                f"Key: {path},",
                f"Error: The original object is a NOT dictionary when it "
                f"should; current type: {_get_types_name(type(isdict_o))}."
            ))
            return

        # Excess keys.
        excess: set = set(original.keys()) - set(base.keys())

        if excess:
            self._messages.append((
                f"Key: {path},",
                f"Error: Excess keys: {excess or '{}'}."
            ))

        # Next depth level.
        for key in base.keys():
            # Check if the key exits.
            if key not in original:
                continue

            # Extract the next key.
            tkey: str = f"'{key}'" if isinstance(key, str) else f"{key}"
            tkey = f"{path}.{tkey}" if path != "" else tkey

            # Recursive step.
            self._check_keys(base[key], original[key], tkey)

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
        # Auxiliary variables.
        self._messages: list = []

        # Check the keys.
        self._check_keys(base, original, "'root'")

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

    def _set_message(self, base: Any, original: Any) -> None:
        """
            Sets the message properly.

            :param base: The base dictionary.

            :param original: The original dictionary.
        """
        # Determine if dictionaries are needed.
        isdict_orig: bool = isinstance(original, dict)
        isdict_base: bool = isinstance(base, dict)

        # Format the message accordingly.
        if isdict_orig and isdict_base:
            self._customize_both(base, original)

        if not isdict_base:
            self._customize_base()

        if not isdict_orig:
            self._customize_original()

    def _validate_extract(self) -> None:
        """
            Validates the extract attribute.

            :raises TypeError: If the extract parameter is not a boolean value.
        """
        # Check the extract property.
        if not isinstance(self.extract, bool):
            raise TypeError(
                f"The extract parameter must be a boolean value; current "
                f"type: {type(self.extract).__name__}."
            )

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self,
        message: Union[None, str] = None,
        base: Union[dict, None] = None,
        original: Union[dict, None] = None,
        extract: bool = False
    ):
        """
            Initializes the exception.

            :param message: The exception message.

            :param base: The base dictionary.

            :param original: The original dictionary.

        - self.extract: A boolean flag indicating whether the data type of the
          base dictionary must be extracted rather than directly used. True, if
          the data type must be extracted; False, otherwise.
        """
        # Auxiliary variables.
        default: str = WrongKeysSubsetAndTypeError.DEFAULT

        # Extract the parameters.
        self.extract: bool = extract
        self.message: str = default if message is None else message
        self._messages: list = []

        # Validate the parameters before continuing.
        self._validate_extract()
        self._set_message(base, original)

        # Call the parent constructor.
        super().__init__(self.message)
