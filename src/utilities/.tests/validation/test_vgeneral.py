"""
    Contains the unittests for the general errors/exceptions.
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


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    unittest.main()
