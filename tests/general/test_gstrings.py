"""
    Contains the tests for the string validation errors/exceptions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard Library.
import unittest

# User.
from gutilities.general.gstrings import (
    messages_concat, normalize, normalize_repr, sindent
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Test
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestMessageConcat(unittest.TestCase):
    """
        Tests for the message concatenation function.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_message_concat_no_base_message(self) -> None:
        """
            Tests the messages are properly appended when the base message
            does not end with a period.
        """
        # Auxiliary variables.
        message_base: str = ""
        message_other: str = "This is a message."

        # -------------------------------------------------------------------------
        # Test 1: Base message is a blank string and the other is not empty.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The concatenated message should be the extra message, "
            "since there is no base message."
        )

        # The resultant and expected messages.
        result: str = messages_concat(message_base, message_other)
        expected: str = message_other

        self.assertEqual(expected, result, message)

    def test_message_concat_no_extra_message(self) -> None:
        """
            Tests the messages are properly appended when the base message
            does not end with a period.
        """
        # Auxiliary variables.
        message_base: str = "This is the base message"
        message_other: str = ""

        # -------------------------------------------------------------------------
        # Test 1: Base message is not blank string and the other is empty.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The concatenated message should be the base message, "
            "since there is no extra message."
        )

        # The resultant and expected messages.
        result: str = messages_concat(message_base, message_other)
        expected: str = message_base

        self.assertEqual(expected, result, message)

    def test_message_concat_no_period_end(self) -> None:
        """
            Tests the messages are properly appended when the base message
            does not end with a period.
        """
        # Auxiliary variables.
        message_other: str = "This is a message."

        # -------------------------------------------------------------------------
        #  Test 1: The base ends with a blank character, but the end doesn't.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The concatenated message should be the base message with "
            "a period at the end, followed by the message."
        )

        for char in (" ", "\t", "\n", "\r"):
            # Set the base message.
            message_base: str = f"This is a test{char}"

            # The resultant and expected messages.
            result: str = messages_concat(message_base, message_other)
            expected: str = f"{message_base}. {message_other}"

            self.assertEqual(expected, result, message)

    def test_message_concat_period_end(self) -> None:
        """
            Tests the messages are properly appended when the base message
            ends with a period.
        """
        # Auxiliary variables.
        message_base: str = "This is a test."
        message_other: str = "This is a message."

        # -------------------------------------------------------------------------
        # Test 1: The base message ends in a period, the other message is not
        # empty.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The concatenated message should be the base message "
            "followed by the message."
        )

        # The resultant and expected messages.
        result: str = messages_concat(message_base, message_other)
        expected: str = f"{message_base} {message_other}"

        self.assertEqual(result, expected, message)

    def test_message_concat_period_space_end(self) -> None:
        """
            Tests the messages are properly appended when the base message
            ends with a period, when right-stripped.
        """
        # Auxiliary variables.
        message_other: str = "This is a message."

        # -------------------------------------------------------------------------
        # Test 1: The string must append correctly to a string ending in a
        # period.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: The concatenated message should be the base message "
            "followed by the message."
        )

        for char in (" ", "\t", "\n", "\r"):
            # Set the base message.
            message_base: str = f"This is a test.{char}"

            # The resultant and expected messages.
            result: str = messages_concat(message_base, message_other)
            expected: str = f"{message_base}{message_other}"

            self.assertEqual(result, expected, message)

    def test_message_concat_wrong_type(self) -> None:
        """
            Tests there are assertion errors when the inputs are not
            strings.
        """
        # Auxiliary variables.
        message_none: tuple = (None,)
        message_blank: str = ""

        # -------------------------------------------------------------------------
        # Test 1: The base message is None.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the base message is "
            "not a string."
        )

        with self.assertRaises(TypeError, msg=message):
            messages_concat(message_none[0], message_blank)

        # -------------------------------------------------------------------------
        # Test 2: The base message is None.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message = (
            "Test 2: A TypeError should be raised since the message is not a "
            "string."
        )

        with self.assertRaises(TypeError, msg=message):
            messages_concat(message_blank, message_none[0])


class TestNormalize(unittest.TestCase):
    """
        Tests for the message normalization function.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_normalize_indent_tool_long(self) -> None:
        """
            Tests that a TypeError is raised when the input of the
            "indent" parameter is too long and exceeds the number of maximum
            characters allowed.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": 10,
            "chars": 5,
            "include": True,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the indent is too "
            "long and exceeds the number of maximum characters."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["indent"] = 4
        parameters["chars"] = 60

        normalize(**parameters)

    def test_normalize_wrong_type(self) -> None:
        """
            Tests that a TypeError is raised when the input is not a
            string.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": 10,
            "indent": 0,
            "chars": 60,
            "include": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the input is not a "
            "string."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["text"] = "This is a test."

        normalize(**parameters)

    def test_normalize_wrong_type_chars(self) -> None:
        """
            Tests that a TypeError is raised when the input of the
            "chars" parameter is not an integer greater than or equal to 1.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": 2,
            "chars": 0,
            "include": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the input of the "
            "\"char\" parameter is not an integer greater than or equal to 1."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["chars"] = 60

        normalize(**parameters)

    def test_normalize_wrong_type_include(self) -> None:
        """
            Tests that a TypeError is raised when the input of the
            "include" parameter is not a boolean.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": 0,
            "chars": 60,
            "include": "False",
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "A TypeError should be raised since the input of the \"include\" "
            "parameter is not a boolean."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["include"] = False

        normalize(**parameters)

    def test_normalize_wrong_type_indent(self) -> None:
        """
            Tests that a TypeError is raised when the input of the "indent"
            parameter is not an integer.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": "0",
            "chars": 60,
            "include": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the input of the "
            "\"indent\" parameter is not an integer."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["indent"] = 4

        normalize(**parameters)


class TestNormalizeRepr(unittest.TestCase):
    """
        Tests for the message normalization function that uses the repr
        function instead of the str function.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_normalize_repr_indent_tool_long(self) -> None:
        """
            Tests that a TypeError is raised when the input of the "indent"
            parameter is too long and exceeds the number of maximum characters
            allowed.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": 10,
            "chars": 5,
            "include": True,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "A TypeError should be raised since the indent is too long "
            "and exceeds the number of maximum characters."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize_repr(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["indent"] = 4
        parameters["chars"] = 60

        normalize_repr(**parameters)

    def test_normalize_repr_wrong_type(self) -> None:
        """
            Tests that a TypeError is raised when the input is not a
            string.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": 10,
            "indent": 0,
            "chars": 60,
            "include": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the input is not a "
            "string."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize_repr(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["text"] = "This is a test."

        normalize_repr(**parameters)

    def test_normalize_repr_wrong_type_chars(self) -> None:
        """
            Tests that a TypeError is raised when the input of the
            "chars" parameter is not an integer greater than or equal to 1.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": 2,
            "chars": 0,
            "include": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the input of the "
            "\"char\" parameter is not an integer greater than or equal to 1."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize_repr(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["chars"] = 60

        normalize_repr(**parameters)

    def test_normalize_repr_wrong_type_include(self) -> None:
        """
            Tests that a TypeError is raised when the input of the
            "include" parameter is not a boolean.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": 0,
            "chars": 60,
            "include": "False",
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the input of the "
            "\"include\" parameter is not a boolean."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize_repr(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["include"] = False

        normalize_repr(**parameters)

    def test_normalize_repr_wrong_type_indent(self) -> None:
        """
            Tests that a TypeError is raised when the input of the
            "indent" parameter is not an integer.
        """
        # Auxiliary variables.
        parameters: dict = {
            "text": "This is a test.",
            "indent": "0",
            "chars": 60,
            "include": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Wrong types are chosen.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A TypeError should be raised since the input of the "
            "\"indent\" parameter is not an integer."
        )

        with self.assertRaises(TypeError, msg=message):
            normalize_repr(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: Correct types are chosen.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["indent"] = 4

        normalize_repr(**parameters)


class TestSindent(unittest.TestCase):
    """
        Tests for the sindent function.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_sindent_length(self) -> None:
        """
            Tests that the length of the string is consistent with the
            parameters when requesting an indentation with spaces.
        """
        # Auxiliary variables.
        parameters: dict = {
            "level": 0,
            "base": 0,
            "spaces": 4,
            "istab": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: No indents should exist.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = "Test 1: The indentation level is not correct."

        # The resultant and expected messages.
        message_result: str = sindent(**parameters)
        message_expected: str = ""

        # The length of the strings.
        result: int = len(message_result)
        expected: int = len(message_expected)

        self.assertEqual(result, expected, message)

        # -------------------------------------------------------------------------
        # Test 2: Should be 4 spaces long.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 2: The indentation level is not correct."

        # Reset the values.
        parameters["level"] = 1

        # The resultant and expected messages.
        message_result = sindent(**parameters)
        message_expected = " " * parameters["spaces"]

        # The length of the strings.
        result = len(message_result)
        expected = len(message_expected)

        self.assertEqual(result, expected, message)

        # -------------------------------------------------------------------------
        # Test 3: Should be 4 spaces long.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 3: The indentation level is not correct."

        # Reset the values.
        parameters["base"] = 1
        parameters["level"] = 0

        # The resultant and expected messages.
        message_result = sindent(**parameters)
        message_expected = " " * parameters["spaces"]

        # The length of the strings.
        result = len(message_result)
        expected = len(message_expected)

        self.assertEqual(result, expected, message)

        # -------------------------------------------------------------------------
        # Test 4: Should be 4 spaces long.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message = "Test 4: The indentation level is not correct."

        # Auxiliary variables.
        parameters["level"] = 1
        parameters["spaces"] = 2

        # The resultant and expected messages.
        message_result = sindent(**parameters)
        message_expected = " " * 2 * parameters["spaces"]

        # The length of the strings.
        result = len(message_result)
        expected = len(message_expected)

        self.assertEqual(result, expected, message)

    def test_sindent_wrong_type_base(self) -> None:
        """
            Tests that an ValueError is raised when the input of the
            "base" parameter is not a positive integer.
        """
        # Auxiliary variables.
        parameters: dict = {
            "level": 0,
            "base": -1,
            "spaces": 4,
            "istab": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Parameters have the wrong type.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A ValueError should be raised since the input of the "
            "\"base\" parameter is not a positive integer."
        )

        with self.assertRaises(ValueError, msg=message):
            sindent(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: All parameters are correct, must NOT throw any errors.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["base"] = 0

        sindent(**parameters)

    def test_sindent_wrong_type_istab(self) -> None:
        """
            Tests that a ValueError is raised when the input of the
            "istab" parameter is not a boolean.
        """
        # Auxiliary variables.
        parameters: dict = {
            "level": 0,
            "base": 0,
            "spaces": 4,
            "istab": 1,
        }

        # -------------------------------------------------------------------------
        # Test 1: Parameters have the wrong type.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: A ValueError should be raised since the input of the "
            "\"istab\" parameter is not a boolean."
        )

        with self.assertRaises(ValueError, msg=message):
            sindent(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: All parameters are correct, must NOT throw any errors.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["istab"] = True

        sindent(**parameters)

    def test_sindent_wrong_type_level(self) -> None:
        """
            Tests that an AssertionError is raised when the input of the
            "level" parameter is not a positive integer.
        """
        # Auxiliary variables.
        parameters: dict = {
            "level": -1,
            "base": 0,
            "spaces": 4,
            "istab": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Parameters have the wrong type.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "Test 1: An AssertionError should be raised since the input of "
            "the \"level\" parameter is not a positive integer."
        )

        with self.assertRaises(ValueError, msg=message):
            sindent(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: All parameters are correct, must NOT throw any errors.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["level"] = 0

        sindent(**parameters)

    def test_sindent_wrong_type_spaces(self) -> None:
        """
            Tests that a ValueError is raised when the input of the "spaces"
            parameter is not a positive integer greater than or equal to 1.
        """
        # Auxiliary variables.
        parameters: dict = {
            "level": 0,
            "base": 0,
            "spaces": 0,
            "istab": False,
        }

        # -------------------------------------------------------------------------
        # Test 1: Parameters have the wrong type.
        # -------------------------------------------------------------------------

        # Set the message in case an error happens.
        message: str = (
            "A ValueError should be raised since the input of the "
            "\"spaces\" parameter is not a positive integer greater than or "
            "equal to 1."
        )

        with self.assertRaises(ValueError, msg=message):
            sindent(**parameters)

        # -------------------------------------------------------------------------
        # Test 2: All parameters are correct, must NOT throw any errors.
        # -------------------------------------------------------------------------

        # Set the correct type.
        parameters["spaces"] = 1

        sindent(**parameters)
