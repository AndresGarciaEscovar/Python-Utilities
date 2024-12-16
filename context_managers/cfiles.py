"""
    Contains the context manager to temporarily create a file with the given
    content and remove it when the context is exited, on request.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from datetime import datetime
from pathlib import Path
from typing import Any, Union


# #############################################################################
# Classes
# #############################################################################


class FileTemp:
    """
        Context manager to temporarily create a file with the given content and
        remove it when the context is exited, on request.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    # Format and length of the date and time with microseconds.
    DFORMAT: str = "%Y%m%d%H%M%S%f"
    LENGTH = len(datetime.now().strftime(DFORMAT[:-2]))

    # /////////////////////////////////////////////////////////////////////////
    # Dunder Methods
    # /////////////////////////////////////////////////////////////////////////

    def __enter__(self) -> str:
        """
            Creates the temporary file with the given content and returns the
            path to the closed file.

            :return: The full path to the file.
        """
        # Set the file name.
        length: int = FileTemp.LENGTH + 1
        tdate: str = datetime.now().strftime(FileTemp.DFORMAT)[:length]

        suffix = f".{self.extension}"
        name = Path(f"temp_file_{tdate}").with_suffix(suffix)

        self.file = f"{Path(self.path).absolute().resolve() / name}"

        # Create the file with the given content.
        with open(self.file, mode="w") as fl:
            fl.write(self.content)

        return self.file

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        """
            Performs the operations before exiting the context manager. In this
            case, removes the file, if requested.

            :param exc_type: The object with the exception types.

            :param exc_val: The object with the exception values.

            :param exc_tb: The object with the exception tracebacks.
        """
        # Get the path to the file and remove it, if requested.
        tpath: Path = Path(self.file)

        if self.remove and tpath.is_file():
            tpath.unlink()

    # //////////////////////////////////////////////////////////////////////////
    # Methods
    # //////////////////////////////////////////////////////////////////////////

    # --------------------------------------------------------------------------
    # '_check' Methods
    # --------------------------------------------------------------------------

    def _check_parameters(self) -> None:
        """
            Checks the parameters are valid; i.e., they have the correct type
            and value.
        """
        # Auxiliary variables.
        message = ""
        parameters: dict = {
            "content": (self.content, str),
            "extension": (self.extension, str),
            "path": (self.path, str),
            "remove": (self.remove, bool),
        }

        # Check the parameters.
        for key, value in parameters.items():
            if not isinstance(value[0], value[1]):
                message += (
                    f"{key} must be of type {value[1]}. Current type: "
                    f"{type(value[0])}."
                )
                continue
            
            if value[1] is not str:
                continue

            blank = value[0].strip() == ""
            if value[1] is str and isinstance(value[0], str) and blank:
                message += f"{key} cannot be an empty string."
                continue
        
        # If there is a message, raise an error.
        if message != "":
            raise ValueError(message)

        # Check that the path is a directory.
        if not Path(self.path).is_dir():
            raise NotADirectoryError(
                f"The given path does not exist or is not a valid directory. "
                f"Choose a valid directory. Current directory path: {self.path}"
            )

    # //////////////////////////////////////////////////////////////////////////
    # Constructor
    # //////////////////////////////////////////////////////////////////////////

    def __init__(
        self, path: str, content: str, extension: str = "txt",
        remove: bool = True
    ):
        """
            Initializes the context manager.

            :param path: Path to the directory where the file will be created.

            :param content: Content of the file.
            
            :param extension: The extension of the file. "txt" by default.

            :param remove: A boolean flag indicating if the file to be removed
            when the context is exited. True, if the file is to be removed;
            False, otherwise. True by default.
        """
        # Set the attributes.
        self.content: str = content
        self.extension: str = extension
        self.path: str = path
        self.remove: bool = remove

        # Other attributes.
        self.file: str = ""

        # Validate the parameters.
        self._check_parameters()
