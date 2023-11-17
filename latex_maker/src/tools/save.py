"""
    File that contains the functions to save and print the LaTeX code.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# General.
from pathlib import Path


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_unique_name(name: str, path: str) -> str:
    """
        Gets a unique name for the file by appending a suffix.

        :param name: The name of the file.

        :param path: The path where the file will be saved.

        :return: The unique name of the file.
    """
    # Auxiliary variables.
    tpath = Path(path, name).absolute().resolve()
    counter = 0

    # Update the name if the file already exists by appending a suffix.
    while tpath.is_file():
        tpath = Path(path, name).absolute().resolve()
        tpath = tpath.with_suffix('') / f"({counter})"
        counter += 1

    # Remove variables.
    del counter

    return tpath.name


# ------------------------------------------------------------------------------
# '_print' Functions
# ------------------------------------------------------------------------------


def _print(text: str, configuration: dict) -> None:
    """
        Prints the generated text to the console.
        
        :param text: The text to print.
        
        :param configuration: The configuration dictionary.
    """
    if configuration["print"]:
        print(text)


# ------------------------------------------------------------------------------
# '_save' Functions
# ------------------------------------------------------------------------------


def _save(text: str, configuration: dict) -> str:
    """
        Saves the generated text to a file.

        :param text: The text to save.

        :param configuration: The configuration dictionary.

        :return: The path to the file where the text was saved.
    """
    # Return an empty string if the file is not to be saved.
    if not configuration["save"]:
        print("Text will not be saved to a file.")
        return ""

    # Auxiliary variables.
    name = configuration["name"]
    path = configuration["path"]

    # Validate the name.
    _validate_name(name)

    # Raise an error if the path is not a directory.
    if not Path(path).is_dir():
        raise NotADirectoryError(
            f"{path} is not a directory. The LaTeX file cannot be saved."
        )

    # Get a new name if the file already exists by appending a suffix.
    if Path(path, name).resolve().is_file() and not configuration["overwrite"]:
        name = _get_unique_name(name, path)

    # Save the file.
    with open(f"{Path(path, name).resolve()}", "w") as file:
        file.write(text)

    # Message to the user.
    pth = f"{Path(path, name).resolve()}"
    print(
        f"File has been saved to the path: {pth}"
    )

    return pth


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_name(name: str) -> None:
    """
        Checks that the name of the file is valid.

        :param name: The name of the file.

        :raises ValueError: If the name does not have a ".tex" suffix.
    """
    # Check that the name has a ".tex" suffix.
    if not name.endswith(".tex"):
        raise ValueError(
            f"The file name must have a \".tex\" suffix. Current suffix: "
            f"{Path(name).suffix}, file name: {name}."
        )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'save' Functions
# ------------------------------------------------------------------------------


def save(text: str, configuration: dict) -> str:
    """
        Saves the generated text to a file and/or prints the text to the
        console.
    """
    # Perform the actions.
    _print(text, configuration)

    return _save(text, configuration)
