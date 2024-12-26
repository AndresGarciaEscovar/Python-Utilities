"""
    Contains the unittests for the string validation errors/exceptions.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
import unittest

# User.
import utilities.general.gstrings as gstrings


# #############################################################################
# Classes
# #############################################################################


class TestMessageConcat(unittest.TestCase):
        """
            Tests for the message concatenation function.
        """
        # /////////////////////////////////////////////////////////////////////
        # Test Methods
        # /////////////////////////////////////////////////////////////////////

        def test_message_concat_no_base_message(self):
            """
                Tests the messages are properly appended when the base message
                does not end with a period.
            """
            # Auxiliary variables.
            sbase: str = f""
            smessage: str = f"This is a message."

            # The resultant and expected messages.
            rmessage: str = gstrings.messages_concat(sbase, smessage)
            emessage: str = f"{smessage}"

            # When the base message is not a string.
            mmessage: str = (
                "The concatenated message should be the extra message, since "
                "there is no base message."
            )

            # Messages must match.
            self.assertEqual(rmessage, emessage, mmessage)

        def test_message_concat_no_extra_message(self):
            """
                Tests the messages are properly appended when the base message
                does not end with a period.
            """
            # Auxiliary variables.
            sbase: str = f"This is the base message"
            smessage: str = f""

            # The resultant and expected messages.
            rmessage: str = gstrings.messages_concat(sbase, smessage)
            emessage: str = f"{sbase}"

            # When the base message is not a string.
            mmessage: str = (
                "The concatenated message should be the base message, since "
                "there is no extra message."
            )

            # Messages must match.
            self.assertEqual(rmessage, emessage, mmessage)

        def test_message_concat_no_period_end(self):
            """
                Tests the messages are properly appended when the base message
                does not end with a period.
            """
            # Auxiliary variables.
            smessage: str = f"This is a message."

            for char in (" ", "\t", "\n", "\r"):
                # Set the base message.
                sbase: str = f"This is a test{char}"

                # The resultant and expected messages.
                rmessage: str = gstrings.messages_concat(sbase, smessage)
                emessage: str = f"{sbase}. {smessage}"

                # When the base message is not a string.
                mmessage: str = (
                    "The concatenated message should be the base message with"
                    "a period at the end, followed by the message."
                )

                # Messages must match.
                self.assertEqual(rmessage, emessage, mmessage)

        def test_message_concat_period_end(self):
            """
                Tests the messages are properly appended when the base message
                ends with a period.
            """
            # Auxiliary variables.
            sbase: str = "This is a test."
            smessage: str = "This is a message."

            # The resultant and expected messages.
            rmessage: str = gstrings.messages_concat(sbase, smessage)
            emessage: str = f"{sbase} {smessage}"

            # When the base message is not a string.
            mmessage: str = (
                "The concatenated message should be the base message followed "
                "by the message."
            )

            # Messages must match.
            self.assertEqual(rmessage, emessage, mmessage)

        def test_message_concat_period_space_end(self):
            """
                Tests the messages are properly appended when the base message
                ends with a period, when right-stripped.
            """
            # Auxiliary variables.
            smessage: str = f"This is a message."

            for char in (" ", "\t", "\n", "\r"):
                # Set the base message.
                sbase: str = f"This is a test.{char}"

                # The resultant and expected messages.
                rmessage: str = gstrings.messages_concat(sbase, smessage)
                emessage: str = f"{sbase}{smessage}"

                # When the base message is not a string.
                mmessage: str = (
                    "The concatenated message should be the base message "
                    "followed by the message."
                )

                # Messages must match.
                self.assertEqual(rmessage, emessage, mmessage)

        def test_message_concat_wrong_type(self):
            """
                Tests there are assertion errors when the inputs are not
                strings.
            """
            # Auxiliary variables.
            string_none: str | None = None
            string_blank: str = ""

            # When the base message is not a string.
            mmessage: str = (
                "An AssertionError should be raised since the base message is "
                "not a string."
            )

            with self.assertRaises(AssertionError, msg=mmessage):
                gstrings.messages_concat(string_none, string_blank)

            # When the base message is not a string.
            mmessage: str = (
                "An AssertionError should be raised since the message is "
                "not a string."
            )

            with self.assertRaises(AssertionError, msg=mmessage):
                gstrings.messages_concat(string_blank, string_none)


class TestNormalize(unittest.TestCase):
    """
        Tests for the message normalization function.
    """

    # /////////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////////

    def test_normalize_indent_tool_long(self):
        """
            Tests that an AssertionError is raised when the input of the
            "indent" parameter is too long and exceeds the number of maximum
            characters allowed.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": 10,
            "chars": 5,
            "include": True,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the indent is too long "
            "and exceeds the number of maximum characters."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize(**parameters)

        # Set the correct type.
        parameters["indent"] = 4
        parameters["chars"] = 60

        gstrings.normalize(**parameters)

    def test_normalize_wrong_type(self):
        """
            Tests that an AssertionError is raised when the input is not a
            string.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": 10,
            "indent": 0,
            "chars": 60,
            "include": False,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input is not a "
            "string."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize(**parameters)

        # Set the correct type.
        parameters["string"] = "This is a test."

        gstrings.normalize(**parameters)

    def test_normalize_wrong_type_chars(self):
        """
            Tests that an AssertionError is raised when the input of the
            "chars" parameter is not an integer greater than or equal to 1.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": 2,
            "chars": 0,
            "include": False,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input of the "
            "\"char\" parameter is not an integer greater than or equal to 1."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize(**parameters)

        # Set the correct type.
        parameters["chars"] = 60

        gstrings.normalize(**parameters)

    def test_normalize_wrong_type_include(self):
        """
            Tests that an AssertionError is raised when the input of the
            "include" parameter is not a boolean.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": 0,
            "chars": 60,
            "include": "False",
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input of the "
            "\"include\" parameter is not a boolean."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize(**parameters)

        # Set the correct type.
        parameters["include"] = False

        gstrings.normalize(**parameters)

    def test_normalize_wrong_type_indent(self):
        """
            Tests that an AssertionError is raised when the input of the
            "indent" parameter is not an integer.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": "0",
            "chars": 60,
            "include": False,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input of the "
            "\"indent\" parameter is not an integer."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize(**parameters)

        # Set the correct type.
        parameters["indent"] = 4

        gstrings.normalize(**parameters)


class TestNormalizeRepr(unittest.TestCase):
    """
        Tests for the message normalization function that uses the repr
        function instead of the str function.
    """

    # /////////////////////////////////////////////////////////////////////////
    # Test Methods
    # /////////////////////////////////////////////////////////////////////////

    def test_normalize_repr_indent_tool_long(self):
        """
            Tests that an AssertionError is raised when the input of the
            "indent" parameter is too long and exceeds the number of maximum
            characters allowed.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": 10,
            "chars": 5,
            "include": True,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the indent is too long "
            "and exceeds the number of maximum characters."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize_repr(**parameters)

        # Set the correct type.
        parameters["indent"] = 4
        parameters["chars"] = 60

        gstrings.normalize_repr(**parameters)

    def test_normalize_repr_wrong_type(self):
        """
            Tests that an AssertionError is raised when the input is not a
            string.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": 10,
            "indent": 0,
            "chars": 60,
            "include": False,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input is not a "
            "string."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize_repr(**parameters)

        # Set the correct type.
        parameters["string"] = "This is a test."

        gstrings.normalize_repr(**parameters)

    def test_normalize_repr_wrong_type_chars(self):
        """
            Tests that an AssertionError is raised when the input of the
            "chars" parameter is not an integer greater than or equal to 1.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": 2,
            "chars": 0,
            "include": False,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input of the "
            "\"char\" parameter is not an integer greater than or equal to 1."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize_repr(**parameters)

        # Set the correct type.
        parameters["chars"] = 60

        gstrings.normalize_repr(**parameters)

    def test_normalize_repr_wrong_type_include(self):
        """
            Tests that an AssertionError is raised when the input of the
            "include" parameter is not a boolean.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": 0,
            "chars": 60,
            "include": "False",
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input of the "
            "\"include\" parameter is not a boolean."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize_repr(**parameters)

        # Set the correct type.
        parameters["include"] = False

        gstrings.normalize_repr(**parameters)

    def test_normalize_repr_wrong_type_indent(self):
        """
            Tests that an AssertionError is raised when the input of the
            "indent" parameter is not an integer.
        """
        # Auxiliary variables.
        parameters : dict = {
            "string": "This is a test.",
            "indent": "0",
            "chars": 60,
            "include": False,
        }

        # Message.
        mmessage: str = (
            "An AssertionError should be raised since the input of the "
            "\"indent\" parameter is not an integer."
        )

        with self.assertRaises(AssertionError, msg=mmessage):
            gstrings.normalize_repr(**parameters)

        # Set the correct type.
        parameters["indent"] = 4

        gstrings.normalize_repr(**parameters)


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
