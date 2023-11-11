"""
    File that cotains the collection of context managers.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General
import os

from datetime import datetime
from pathlib import Path


# ##############################################################################
# Temporary File
# ##############################################################################


class TempFile:
    """
        Context manager that create a temporary file with the given content and
        potentially removes it when the context is exited.
    """

    # //////////////////////////////////////////////////////////////////////////
    # Dunder Methods
    # //////////////////////////////////////////////////////////////////////////

    def __enter__(self) -> str:
        """
            Creates the temporary file with the given content and returns the
            path to the closed file.

            :return: The full path to the file.
        """
        # Set the file name.
        tdate = datetime.now().strftime("%Y%m%d%H%M%S.%f")
        tdate = "".join(
            [x if i == 0 else x[1] for i, x in enumerate(tdate.split("."))]
        )
        tpath = Path(self.path).absolute().resolve()
        self.file = f"{tpath / f'temp_file_{tdate}.{self.extension}'}"

        # Create the file with the given content.
        with open(self.file, mode="w") as fl:
            fl.write(self.content)

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
            Performs the operations before exiting the context manager. In this
            case, removes the file, if requested.

            :param exc_type: The object with the exception types.

            :param exc_val: The object with the exception values.

            :param exc_tb: The object with the exception tracebacks.
        """
        # Remove the file.
        if self.remove and (tpath := Path(self.file)).is_file():
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

            if value[1] is str and isinstance(value[0], str) and value[0].strip() == "":
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


# ##############################################################################
# Working Directory
# ##############################################################################


class WorkingDirectory:
    """
        Temporarily changes the working directory and restores it on exit.
    """

    # //////////////////////////////////////////////////////////////////////////
    # Dunder
    # //////////////////////////////////////////////////////////////////////////

    def __enter__(self) -> str:
        """
            Sets the working directory.

            :return: The directory set as the working directory.
        """
        # Set the working directory.
        os.chdir(self.new)

        return f"{Path(os.getcwd()).absolute().resolve()}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
            Performs the operations before exiting the context manager. In this
            case, removes the file, if requested.

            :param exc_type: The object with the exception types.

            :param exc_val: The object with the exception values.

            :param exc_tb: The object with the exception tracebacks.
        """
        # Remove the file.
        os.chdir(self.old)

    # //////////////////////////////////////////////////////////////////////////
    # Methods
    # //////////////////////////////////////////////////////////////////////////

    # --------------------------------------------------------------------------
    # '_check' Methods
    # --------------------------------------------------------------------------

    def _check_parameters(self) -> None:
        """
            Checks that the parameters are the correct type and contain valid
            values.
        """
        # Validate the parameters.
        if not isinstance(self.new, str):
            raise TypeError(
                f"The \"directory\" parameter is not a string. It must be a "
                f"string: {type(self.new)}"
            )

        if not Path(self.new).is_dir():
            raise NotADirectoryError(
               f"The directory to be set as the working directory is not "
               f"valid: {self.new}"
            )

    # //////////////////////////////////////////////////////////////////////////
    # Constructor
    # //////////////////////////////////////////////////////////////////////////

    def __init__(self, directory: str):
        """
            Sets the initial variables.

            :param directory: The directory to be set as the working directory.
        """
        self.new = directory
        self.old = os.getcwd()

        # Validate the parameters
        self._check_parameters()


# ##############################################################################
# Working Directory
# ##############################################################################


if __name__ == "__main__":
    ...
