"""
    File that contains the functions to compile the LaTeX code.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# General
import subprocess
import warnings

from pathlib import Path


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
    # Global variables.
    global _PATHLATEX

    # Extract the command.
    mcommand = configuration["command"]
    pcommand = f"{Path(_PATHLATEX, configuration['command'])}"

    flags = configuration["flags"]
    sescapte = configuration["shell-escape"]

    # Commands to try.
    for command in (mcommand, pcommand):
        # Get the command.
        tcommand = _get_command(command, flags, path, sescapte, False)
        if _compile_run(tcommand):
            print(
                f"    Compilation successful! Find the output in the "
                f"directory: {Path(path).parent}"
            )
            return

    # If the code did not compile, try with the 'which' command.
    tcommand = _get_command(mcommand, flags, path, sescapte, True)
    if _compile_run(tcommand):
        print(
            f"    Compilation successful! Find the output in the "
            f"directory: {Path(path).parent}"
        )
    return


def _compile_run(command: list) -> bool:
    """
        Compiles the code using the given command and returns a boolean flag
        indicating whether the code compiled successfully.

        :param command: The list with the command to use.

        :return: A boolean flag indicating whether the code compiled
         successfully.
    """
    # Run the command.
    try:
        print(f"Compiling using the command: {' '.join(command)}")
        for i in range(3):
            print(f"    Run ({i + 1}/3) ...")
            subprocess.run(command, capture_output=True, shell=False)

    except FileNotFoundError:
        print(
            f"    The command \"{command[0]}\" was not found and the file "
            f"\"{command[-1]}\" could not be compiled using the command: "
            f"{' '.join(command)}."
        )
        return False

    return True


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_command(
    command: str, flags: list, path: str, shell: bool, which: bool
) -> list:
    """
        Gets the list with the given command to compile the code.

        :param command: The string with the command to use.

        :param flags: The list with the flags to use.

        :param path: The string with the path to the file to compile.

        :param shell: Whether to use the -shell-escape command to use.

        :param which: A boolean flag that indicates whether to use the 'which'
         command to get the path of the compilation command.

        :return: A list with the command to compile the code.
    """
    # Get the path to the command.
    tcommand = command
    if which:
        # Get the which command.
        tcommand = _get_which(command)
        tcommand = command if tcommand == "" else tcommand

    # Format the flags.
    tflags = flags
    if shell:
        while "-shell-escape" in tflags:
            tflags.remove("-shell-escape")
        tflags = ["-shell-escape"] + tflags

    return [tcommand, *tflags, path]


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


def _get_current_files(path: str, configuration: dict) -> set:
    """
        Gets the list of the existing files in the given path. Will be used to
        remove them after compiling the code.

        :param path: The string with the ABSOLUTE path to the file.

        :param configuration: The dictionary with the configuration.

        :return: The set of exiting files in the parent directory of the given
         path. An empty set, if the files should not be removed.
    """
    # Check if the files should be removed.
    if not configuration["remove_files"]:
        return set()

    # Get the list of files.
    return set(f"{x}" for x in Path(path).parent.glob("*"))


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
        print(
            f"WARNING: The TeX compilation command \"{command}\" was not found "
            f"using the \"which\" command. This was the last attempt to find "
            f"the path of the command \"{command}\". Please provide the "
            f"correct path to the compiler for the \"{command}\" compiler."
        )

    return cpath


# ------------------------------------------------------------------------------
# '_remove' Functions
# ------------------------------------------------------------------------------


def _remove_files(olist: set, flist: set) -> None:
    """
        Removes the files that were created during the compilation process.

        :param olist: The list of files before compiling the code.

        :param flist: The list of files after compiling the code.
    """
    # Exceptions.
    fexceptions = ".tex", ".pdf", ".dvi", ".ps"

    # Check if the files should be removed.
    remv = flist - olist
    remv = set(
        Path(x) for x in remv if not any(x.endswith(y) for y in fexceptions)
    )

    # Nothing to remove.
    if len(remv) == 0:
        print("No files to remove.")
        return

    # Remove the files.
    print("Removing files:")
    for x in remv:
        print(f"    Removing file: {x}")
        x.unlink()


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
    olist = _get_current_files(path, configuration)

    # Compile the file.
    _compile(path, configuration)

    flist = _get_current_files(path, configuration)
    _remove_files(olist, flist)
