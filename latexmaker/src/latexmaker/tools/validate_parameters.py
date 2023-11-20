"""
    File that contains the function to validate the parameters for the
    get_configuration function in the maker.py file.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# General
from pathlib import Path
from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_dprint(dprint: Any) -> None:
    """
        Validates that the "dprint" parameter is a boolean.

        :param dprint: The boolean flag to be validated.

        :raise TypeError: If the "dprint" parameter is not a boolean.
    """
    # The dprint parameter must be a boolean.
    if not isinstance(dprint, bool):
        raise TypeError(
            f"The \"dprint\" parameter must be a boolean, not {type(dprint)}."
        )


def _validate_fmt_yaml(fmt_yaml: Any) -> None:
    """
        Validates that the "fmt_yaml" parameter is a boolean.

        :param fmt_yaml: The boolean flag to be validated.

        :raise TypeError: If the "fmt_yaml" parameter is not a boolean.
    """
    # The fmt_yaml parameter must be a boolean.
    if not isinstance(fmt_yaml, bool):
        raise TypeError(
            f"The \"fmt_yaml\" parameter must be a boolean, not "
            f"{type(fmt_yaml)}."
        )


def _validate_path_save(path_save: Any) -> None:
    """
        Validates that the "path_save" parameter is a file and that its parent
        directory exists.

        :raise TypeError: If the path_save" parameter is not the correct type.

        :raise ValueError: If the "path_save" parameter is not a file or its
         parent directory does not exist.
    """
    # The path save must be None or a string.
    if not (path_save is None or isinstance(path_save, str)):
        raise TypeError(
            f"The \"path_save\" variable must be None or a string, not "
            f"{type(path_save)}."
        )

    # If the path_save parameter is a string, it must be a file.
    if path_save is None:
        return

    # Check it's a file.
    path_save = Path(path_save)
    if path_save.suffix.strip() == "":
        raise ValueError(
            f"The \"path_save\" parameter must be a file, not a directory."
        )

    # Check the parent directory exists.
    if not path_save.parent.is_dir():
        raise ValueError(
            f"The parent directory of the \"path_save\" parameter does not "
            f"exist: {path_save.parent}"
        )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate(path_save: Any, dprint: Any, fmt_yaml: Any) -> None:
    """
        Validates the parameters for the get_configuration function in the
        maker.py file.

        :param path_save: The path to the save directory.

        :param dprint: The debug print function.

        :param fmt_yaml: The YAML formatter function.
    """
    # Validate the different parameters.
    _validate_dprint(dprint)
    _validate_fmt_yaml(fmt_yaml)
    _validate_path_save(path_save)
