"""
    Contains the class and functions to create a HTML page.
"""


# #############################################################################
# Imports
# #############################################################################


# User.
import utilities.validation.vgeneral as vgeneral


# #############################################################################
# Global variables
# #############################################################################


# HTML Page Basic Structure.
BODY: str = """
</head>
<body>
""".lstrip()

FOOTER: str = """
</body>
</html>
""".strip()

HEADER: str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
""".lstrip()


# #############################################################################
# Classes
# #############################################################################


class PageHTML:
    """
    Class to create a HTML page.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Properties
    # /////////////////////////////////////////////////////////////////////////

    @property
    def title(self) -> str:
        """
            Returns the title of the page.

            :return: The title of the page.
        """
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        """
            Sets the title of the page.

            :param title: The title of the page.
        """
        # Validate the title is a string.
        vgeneral.validate_type(title, str)

        self.__title = title

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, title: str) -> None:
        """
            Builds the main container for a web page.

            :param title: The title of the page.
        """
        # Initialize the mangled variables.
        self.__title: str = ""

        # Use the setters to validate the input.
        self.title = title


# #############################################################################
# Main Program
# #############################################################################


if __name__ == "__main__":
    tpage: PageHTML = PageHTML("Test Page")
