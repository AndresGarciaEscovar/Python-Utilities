"""
    File that contains the functions to compile the LaTeX code.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# General
import copy as cp
import subprocess
import warnings

from pathlib import Path
from typing import Union


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Global Variables
# ##############################################################################


_PATHLATEX = "/usr/local/texlive/2023/bin/x86_64-linux"

# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_compile' Functions
# ------------------------------------------------------------------------------


def _compile(path: str, configuration: dict) -> None:
    """
        Compiles the code in the given path. Attempts to compile the code with
        different commands until it finds one that works. If after trying all
        commands, the code still does not compile, it raises an exception.

        :param path: The path of the file to compile.

        :param configuration: The dictionary with the configuration.
    """
    return None


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_continue(configuration: dict, save: bool) -> bool:
    """
        Gets the boolean flag indicating whether the program must continue to
        run.

        :param configuration: The dictionary with the configuration.

        :param save: Whether the content was saved.

        :return: A boolean flag indicating whether to continue with the
         compilation process, or not. True, if the program must continue to run;
         False, otherwise.
    """
    # Check there is a request to compile.
    if not configuration["compile"]:
        return configuration["compile"]

    # If the file was not saved, raise a warning.
    if not save:
        warnings.warn(
            "The file was not saved. The content might not be able to compile!",
            RuntimeWarning,
        )

    return configuration["compile"]


def _get_current_files(path: str, configuration: dict) -> Union[None, set]:
    """
        Gets the list of the existing files in the given path. Will be used to
        remove them after compiling the code.

        :param path: The string with the ABSOLUTE path to the file.

        :param configuration: The dictionary with the configuration.

        :return: The list of exiting files in the parent directory of the given
         path. None, if the files should not be removed.
    """
    # Check if the files should be removed.
    if not configuration["remove_files"]:
        return None

    # Get the list of files.
    return set(f"{x}" for x in Path(path).parent.glob("*") if x.is_file())


def _get_which(command: str) -> str:
    """
        Gets the path of the given command using the 'which' command and returns
        it. A warning is raised if the command is not found.

        :param command: The string with the command to find.

        :return: The string with the path of the command.
    """
    # Auxiliary variables.
    command_list = ["which", command]
    result = subprocess.run(command_list, capture_output=True, shell=False)

    if (cpath := result.stdout.decode("utf-8").strip()) == "":
        warnings.warn(
            f"The TeX compilation command \"{command}\" was not found using "
            f"the \"which\" command. Alternative commands will be used."
            , RuntimeWarning
        )

    return cpath


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'compile' Functions
# ------------------------------------------------------------------------------


def compile_file(path: str, configuration: dict, save: bool) -> None:
    """
        Compiles the code in the given path.

        :param path: The path of the file to compile.

        :param configuration: The configuration dictionary to use.

        :param save: Whether the content was saved.
    """
    # Global variables.
    global _PATHLATEX

    # Check that compilation must be done.
    if not _get_continue(configuration, save):
        return

    # Store the list of current files.
    flist = _get_current_files(path, configuration)

    # Compile the file.
    _compile(path, configuration)









