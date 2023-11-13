"""
    Test to create a LaTeX file from a Python script and then compile it using
    the subprocess module.
"""
# ##############################################################################
# Imports
# ##############################################################################


# General
import argparse
import copy as cp
import os
import subprocess
import sys
import warnings
import yaml


from pathlib import Path
from typing import Union

# Thrid party
from icecream import ic
ic.configureOutput(
    includeContext=True,
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Global Variables
# ##############################################################################


# Configuration of the program.
_CONFIG = {
    "build": {
        "command": "pdflatex",
        "compile": False,
        "flags": [],
        "remove_files": False,
        "shell-escape": False,
    },
    "main": {
        "author": "",
        "date": "",
        "document_class": "article",
        "packages": [],
        "other_preamble": "",
        "text": "",
        "title": "",
    },
    "save": {
        "name": "test.tex",
        "overwrite": False,
        "path": ".",
        "print": False,
        "return": True,
        "save":  True,

    }
}

# Base configuration of the program.
_CONFIG_BASE = {
    "build": {
        "command": str,
        "compile": bool,
        "flags": list,
        "remove_files": bool,
        "shell-escape": bool,
    },
    "main": {
        "author": str,
        "date": str,
        "document_class": (str, list),
        "other_preamble": str,
        "packages": list,
        "text": str,
        "title": str,
    },
    "save": {
        "name": str,
        "overwrite": bool,
        "path": str,
        "print": bool,
        "return": bool,
        "save":  bool,
    }
}

# Path to the PDFLATEX compiler.
_PDFLATEX = "/usr/local/texlive/2023/bin/x86_64-linux/pdflatex"


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_compile' Functions
# ------------------------------------------------------------------------------

def _compile_latex_file(path: str, configuration: dict) -> None:
    """
        Compiles the LaTeX file using the given configuration. Removes the
        auxiliary files if requested.

        :param path: The path to the LaTeX file.

        :param configuration: The configuration dictionary.

        :raise ValueError: If the LaTeX compiler is not found after trying to
         find it in the PATH and the default path.
    """
    # Global variables.
    global _PDFLATEX

    # //////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions
    # //////////////////////////////////////////////////////////////////////////

    def get_compilation_command(tcommand: str) -> list:
        """
            Gets the compilation command to use.

            :param tcommand: The command to use.

            :return: The list with the complete command to use, including all
             relevant flags.
        """
        # Command to run.
        fcommand = [tcommand] + configuration["flags"]
        if configuration["shell-escape"]:
            fcommand += ["-shell-escape"]
        fcommand += [path]

        return fcommand

    def get_which_command() -> str:
        """
            Returns the path to the "pdflatex" command, if found.

            :return: The path to the command, if found.
        """
        # Run the command.
        cpath = subprocess.run(
            ["which", "pdflatex"], shell=False, capture_output=True
        )
        return cpath.stdout.decode("utf-8").strip()

    def run_command(tcommand: list, ntimes: int = 3) -> bool:
        """
            Returns the boolean value when the given command is run.

            :param tcommand: The list with the command to run.

            :param ntimes: The number of times to run the command.

            :return: A boolean flag that indicates whether the command was
             successfully run. True, if the command was successfully run;
             False, otherwise.
        """
        # Auxiliary variables.
        terror = ""

        # The number of times to run the command.
        tnumber = ntimes if isinstance(ntimes, int) and ntimes > 0 else 1

        # Run the command.
        try:
            for ci in range(tnumber):
                print(f"    Compiling file ({ci + 1}/{ntimes})")
                result = subprocess.run(
                    tcommand, shell=False, capture_output=True
                )
                if result.returncode != 0:
                    terror = result.stderr.decode("utf-8")
                    raise FileNotFoundError("")

        except FileNotFoundError:
            terror = terror if terror == "" else f"Error log:\n{terror}."
            print(
                f"The command subprocess.run({tcommand}, shell=False) was "
                f"not successful.{terror}"
            )
            return False

        return True

    def run_compilation() -> bool:
        """
            Attempst to run the basic command, that is, the command that
            compiles the LaTeX file without looking for the compiler.

            :return: A boolean flag that indicates whether the command was
             successfully run.
        """
        # If the previous command was successfully run.
        pcommand = get_compilation_command(configuration["command"])
        tflag = run_command(pcommand)

        # Try to find the path.
        if not tflag:
            print("Looking for the compilation command using \"which\".")
            tcommand = get_which_command()
            if tcommand == "":
                tflag = False
                print(
                    "The path to the \"pdflatex\" command was not found by "
                    "using the \"which\" command. Will not try to compile the "
                    "LaTeX file."
                )

            else:
                pcommand = get_compilation_command(tcommand)
                tflag = run_command(pcommand)

        #  Try the default path.
        if not tflag:
            pcommand = get_compilation_command(_PDFLATEX)
            tflag = run_command(pcommand)

        return tflag

    def validate_command(tcommand: str) -> None:
        """
            Validates that the command exists.

            :param tcommand: The command to validate.

            :raise ValueError: If the compiler is not supported.
        """
        # If the command is not found, raise an error.
        if not tcommand == "pdflatex":
            raise ValueError(
                f"The only supported command to compile the LaTeX files,  at "
                f"this time is pdflatex. Current command: {tcommand}."
            )

    # //////////////////////////////////////////////////////////////////////////
    # Implementation
    # //////////////////////////////////////////////////////////////////////////

    # Validate the command is found.
    command = configuration["command"]
    validate_command(command)

    # Get the list of current files.
    flist = []
    if configuration["remove_files"]:
        flist = set(f"{x}" for x in Path(path).parent.glob("*"))

    # Try running the commands in order.
    flag = run_compilation()

    # Compilation failed, there might have been files created.
    if not flag:
        print(
            f"The LaTeX file was not compiled. Please, check the files produced "
            f"in the directory: {Path(path).parent}."
        )
        return

    # Remove the auxiliary files.
    if configuration["remove_files"]:
        # Get the list of new files.
        nlist = set(f"{x}" for x in Path(path).parent.glob("*"))
        nlist = nlist.difference(flist)
        nlist = list(
            x for x in nlist if not (x.endswith(".pdf") or x.endswith(".tex"))
        )

        for file in nlist:
            Path(file).unlink()


# ------------------------------------------------------------------------------
# '_exit' Functions
# ------------------------------------------------------------------------------


def _exit_program() -> None:
    """
        Print a message to the user and exits the program.
    """
    print("Exiting program.")
    sys.exit(0)


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_args() -> Union[dict, None]:
    """
        Gets the argument values from the console.

        :return: The configuration dictionary, if any. None, otherwise.
    """
    # Create the parser.
    parser = argparse.ArgumentParser(
        description=(
            "Generates a LaTeX file from a Python script, using the given "
            "configuration file. If no configuration file is given, then the "
            "default configuration will be used."
        )
    )

    # Add the arguments.
    parser.add_argument(
        "-c", "--config",
        type=str,
        help="The configuration file to use.",
        required=False
    )

    parser.add_argument(
        "-p", "--print",
        action="store_true",
        help="Prints the configuration to the console.",
        required=False
    )

    parser.add_argument(
        "-d", "--directory",
        help="When used, saves the sample configuration file to given "
             "directory as a yaml file.",
        type=str,
        required=False
    )

    # Retrieve the arguments.
    arguments = parser.parse_args()

    configuration = arguments.config
    configuration_print = arguments.print
    configuration_directory = arguments.directory

    # Print and/or save the configuration.
    if configuration_print:
        print_configuration(exits=True)

    if isinstance(configuration_directory, str):
        save_configuration_default(configuration_directory, exits=True)

    # Load the dictionary.
    dictionary = None
    if configuration is not None and isinstance(configuration, str):
        # Check that the file exists and it's a yaml file.
        flag = any(configuration.endswith(x) for x in {".yaml", ".yml"})
        flag = flag and Path(configuration).is_file()
        if not flag:
            raise ValueError(
                f"The configuration file must be a yaml file. Current file: "
                f"{configuration}, exists: {Path(configuration).is_file()}."
            )

        # Load the file.
        with open(configuration, mode="r") as file:
            dictionary = yaml.safe_load(file)

    return dictionary


def _get_latex_body(configuration: dict, maketitle: bool) -> str:
    """
        Returns the body of the LaTeX file.

        :param configuration: The configuration dictionary.

        :param maketitle: A boolean flag that indicates whether the title,
         author and date must be added to the LaTeX file; i.e., add the
         \\maketitle command.

        :return: The body of the LaTeX file.
    """
    # Strip the text.
    ttext: str = configuration["text"].strip()

    # Get the text to add.
    text: list[str, ...] = [r"\begin{document}"]
    text += [r"\maketitle"] if maketitle else []
    text += [ttext] if ttext.strip() != "" else []
    text += [r"\end{document}"]

    return "\n".join(text)


def _get_latex_preamble(configuration: dict) -> tuple[str, bool]:
    """
        Returns the header of the LaTeX file.

        :return: The opening statements of the LaTeX file, along with the flag
         that indicates whether the title, author and date were added.
    """
    # //////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions
    # //////////////////////////////////////////////////////////////////////////

    def get_package(tentry: Union[list, str]) -> str:
        """
            From the given entry, returns the package name, along with the
            package options, if any.

            :param tentry: The entry to process. If a string, then it is the
             package name. If a list, then the first entry is the package name
             and the second entry is the string with the package options.

            :return: The package name, along with the package options, if any.
        """
        # If it is a string, then it is the package name.
        if isinstance(tentry, str):
            return fr"\usepackage" r"{" f"{tentry}" "}"

        # If it is a list, then the first entry is the package name and the
        # second entry is the string with the package options.
        if isinstance(tentry, list):
            return fr"\usepackage[{tentry[1]}]" "{" f"{tentry[0]}" "}"

        # Raise an error.
        raise ValueError(
            f"The entry must be a string or a list. Current type: "
            f"{type(tentry)}."
        )

    # //////////////////////////////////////////////////////////////////////////
    # Main Function
    # //////////////////////////////////////////////////////////////////////////

    # Document class.
    text: str = f"% Document class\n"
    dclass: Union[list, str] = configuration["document_class"]

    if isinstance(configuration['document_class'], str):
        text += r"\documentclass{" f"{dclass}" "}"

    else:
        text += "".join([
            r"\documentclass",
            r"[",
            f"{', '.join(dclass[1])}",
            "]",
            r"{",
            f"{dclass[0]}",
            r"}",
        ]) + "\n\n"

    # Packages.
    if len(configuration["packages"]) > 0:
        text += f"% Packages\n"
        text += "\n".join([
            get_package(x) for x in configuration["packages"]
        ]) + "\n\n"

    # Other prelude.
    if configuration["other_preamble"].strip() != "":
        text += f"% Other.\n"
        text += configuration["other_preamble"] + "\n\n"

    # Title, author and date.
    flags: list = [
        configuration["title"].strip() == "",
        configuration["author"].strip() == "",
        configuration["date"].strip() == ""
    ]

    # If all are empty, don't add title information.
    if flag := (not all(flags)):
        text += f"% Title, author and date\n"
        text += "\n".join([
            r"\title{" f"{configuration['title']}" r"}",
            r"\author{" f"{configuration['author']}" r"}",
            r"\date{" f"{configuration['date']}" r"}",
        ]) + "\n\n"

    return text, flag


# ------------------------------------------------------------------------------
# '_save' Functions
# ------------------------------------------------------------------------------


def _save_latex_file(text: str, configuration: dict) -> str:
    """
        Saves the generated text to a latex file and returns the path where
        the file was generated.

        :param text: The LaTeX text to save.

        :param configuration: The configuration dictionary.
    """
    # //////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions
    # //////////////////////////////////////////////////////////////////////////

    def get_filename(tpath: str) -> str:
        """
            Gets the file name, provided the file is not going to be
            overwritten.

            :param tpath: The total path of the file.

            :return: The file where the LaTeX file will be saved.
        """
        # No need to continue.
        if configuration["overwrite"]:
            return tpath

        # Get the path.
        tcounter = 0
        while Path(tpath).is_file():
            tpath = Path(tpath).with_suffix("")
            tpath = f"{tpath}_{tcounter}.tex"
            tcounter += 1

        return tpath

    def get_path(tpath: str, tname: str) -> str:
        """
            Returns the path where to save the file.

            :param tpath: The path where to save the file. If None, the current
             directory will be used.

            :param tname: The name of the file.

            :return: The path where to save the file.
        """
        # If the file name doesn't end with .tex, raise an error.
        if not tname.endswith(".tex"):
            raise ValueError(
                f"The file name must end with \".tex\". Current file name: "
                f"{tname}."
            )

        # If the path is a blank string, use the current directory.
        rpath = tpath.strip()
        ppath = os.getcwd() if rpath == "" or rpath == "." else rpath
        del rpath

        # If the path is not None, then it must be a directory.
        ppath = Path(ppath).resolve()
        if not ppath.is_dir():
            raise ValueError(
                f"The path must be a valid directory. Current path: {ppath}."
            )

        return f"{ppath / tname}"

    # //////////////////////////////////////////////////////////////////////////
    # Implementation
    # //////////////////////////////////////////////////////////////////////////

    # If not saving just continue.
    if not configuration["save"]:
        return ""

    # Correct the path.
    path: str = get_filename(
        get_path(configuration["path"], configuration["name"])
    )

    # Write the file.
    with open(path, mode="w", newline="\n") as file:
        file.write(text)

    return path


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_configuration(configuration: dict) -> dict:
    """
        Validates that the configuration is a valid configuration by checking
        that the keys are the same as thast  of the base configuration and that
        the values are of the correct type.

        :param configuration: The configuration to validate.

        :return: The final configuration with all the needed parameters to
         generate, save and compile the LaTeX file.

        :raise TypeError: If the configuration is not a dictionary or the value
         of the keys are not dictionaries. If the value of the keys are not of
         the correct type.

        :raises ValueError: If there is a mismatch between the keys of the
         configuration and the default configuration.
    """
    # Global variables.
    global _CONFIG, _CONFIG_BASE

    # Validate the configuration is a dictionary.
    if not isinstance(configuration, dict):
        raise TypeError(
            f"The configuration must be a dictionary. Current type: "
            f"{type(configuration)}."
        )

    # Copies.
    cconfig = cp.deepcopy(_CONFIG)
    fconfig = cp.deepcopy(configuration)

    # Must be subset of the default configuration.
    skeys = set(cconfig.keys())
    fkeys = set(fconfig.keys())

    if len(fkeys) > 0 and not fkeys.issubset(skeys):
        wrong = set(x for x in fconfig if x not in cconfig)
        raise ValueError(
            f"The configuration has keys that are not in the default "
            f"configuration. Valid keys: {skeys}, current keys: "
            f"{fkeys}, wrong keys: {wrong}."
        )

    # If the key doesn't exist, add it.
    for key, value in cconfig.items():
        # Add the key.
        if key not in fkeys:
            fconfig[key] = value
            continue

        # Validate the value is a dictionary.
        if not isinstance(fconfig[key], dict):
            raise TypeError(
                f"The value of the key {key} must be a dictionary. Current "
                f"type: {type(fconfig[key])}."
            )

        # Subkeys.
        cskeys = set(cconfig[key].keys())
        fskeys = set(fconfig[key].keys())

        if len(fskeys) > 0 and not fskeys.issubset(cskeys):
            wrong = set(x for x in fskeys if x not in cskeys)
            raise ValueError(
                f"The configuration has keys that are not in the default "
                f"configuration. Valid keys for \"{key}\": {cskeys}, current "
                f"keys: {fskeys}, wrong keys: {wrong}."
            )

        for skey, svalue in value.items():
            # Add the subkey if it doesn't exist.
            if skey not in fskeys:
                fconfig[key][skey] = svalue
                continue

            # Validate the type of the value.
            if not isinstance(fconfig[key][skey], _CONFIG_BASE[key][skey]):
                raise TypeError(
                    f"The value of the key \"{skey}\" for the key \"{key}\" "
                    f"must be of type {_CONFIG_BASE[key][skey]}. Current type: "
                    f"{type(fconfig[key][skey])}."
                )

    # Check that the compilation flags are all strings.
    flags = fconfig["build"]["flags"]
    if len(flags) > 0 and not all(isinstance(x, str) for x in flags):
        raise TypeError(
            f"The compilation flags must be a list of strings. Current type: "
            f"{set(type(x) for x in flags)}."
        )

    # Check that the packages are all strings or list of strings.
    for value in fconfig["main"]["packages"]:
        if isinstance(value, str):
            continue

        if not isinstance(value, list):
            packages = list(type(x) for x in fconfig["main"]["packages"])
            raise TypeError(
                f"The packages configuration['main']['packages'] entry must be "
                f"a list of strings or lists, or a combination of eachs. "
                f"Current types: {packages}."
            )

        if not (len(value) == 2 and all(isinstance(x, str) for x in value)):
            dtypes = list(type(x) for x in value)
            raise TypeError(
                f"If a list is provided, it must be of length 2 where the "
                f"first entry is the package name and the second entry is the "
                f"string with the package options. Where both entries"
                f"must be strings. Current list: {value}, types: {dtypes}."
            )

        # Check that the document class has the proper format, if it's a list.
        pconfig = fconfig["main"]["document_class"]
        if isinstance(pconfig, list):
            if not len(pconfig) == 2:
                raise ValueError(
                    f"If the \"document_class\" variable is a variable, there "
                    f"must be exactly 2 entries. Current: {len(pconfig)}."
                )

            tflag = isinstance(pconfig[0], str) and isinstance(pconfig[1], list)
            if not tflag:
                raise TypeError(
                    f"The first entry of the document class list must be a "
                    f"string with the name of the package and the second entry "
                    f"must be a list of strings with the package options. "
                    f"Current types: {[type(x) for x in pconfig]}"
                )

            # All the options must be strings.
            if not all(isinstance(x, str) for x in pconfig[1]):
                raise TypeError(
                    f"All the options in the \"document_class\" option must be "
                    f"strings. Current types {[type(x) for x in pconfig[1]]}"
                )

    return fconfig


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_configuration() -> dict:
    """
        Returns a copy of the configuration of the program.

        :return: The configuration of the program.
    """
    # Global variables.
    global _CONFIG

    return cp.deepcopy(_CONFIG)


# ------------------------------------------------------------------------------
# 'print' Functions
# ------------------------------------------------------------------------------


def print_configuration(exits: bool = False) -> None:
    """
        Prints the configuration of the program to the console in the form of a
        yaml file.

        :param exits: A boolean flag that indicates whether the program must exit
         at the en. If True, if the program must exit the program at the end.
         False, otherwise. True by default.

    """
    # Global variables.
    global _CONFIG

    for key, value in _CONFIG.items():
        print(f"{key}:")
        for k, v in value.items():
            v = "''" if isinstance(v, str) and v.strip() == "" else v
            print(f"  {k}: {v}")

    # Exit the program.
    if exits:
        _exit_program()


# ------------------------------------------------------------------------------
# 'save' Functions
# ------------------------------------------------------------------------------


def save_configuration_default(path: str, exits: bool = False) -> None:
    """
        Saves the configuration to the given path. WILL EXIT THE PROGRAM AT THE
        END.

        :param path: The where path to save the configuration. Must be a valid
         yaml file with a valid path.

        :param exits: A boolean flag that indicates whether the program must exit
         at the en. If True, if the program must exit the program at the end.
         False, otherwise. True by default.
    """
    # Check it is a valid yaml file, i.e., file ends with .yaml or .yml.
    if not any(path.endswith(x) for x in {".yaml", ".yml"}):
        raise ValueError(
            f"The path where to save the file must be a yaml file; i.e., end "
            f"with \".yaml\" or \".yml\". Current path: {path}."
        )

    # Make sure the path is valid.
    path = Path(path).resolve()
    if not path.parent.is_dir():
        raise ValueError(
            f"The directory {path.parent} does not exist. Choose a different "
            f"and valid directory where to save the file."
        )
    path = f"{path}"

    # Save the file to a yaml file.
    with open(path, mode="w") as file:
        yaml.dump(_CONFIG, file)

    # Message to the user.
    print(f"Saved configuration to {Path(f'{path}').resolve()}.")

    # Exit the program.
    if exits:
        _exit_program()


# ##############################################################################
# Main Function
# ##############################################################################


def main_run(config: Union[dict, None] = None) -> Union[None, str]:
    """
        Runs the main program.

        :param config: The configuration dictionary to use. If None, the default
         configuration will be used.

        :return: The text of the LaTeX file, if requested. None, otherwise.
    """
    # Get the configuration dictionary.
    vconfig = _validate_configuration(
        get_configuration() if config is None else cp.deepcopy(config)
    )

    # Set the LaTeX strings.
    text, add_title = _get_latex_preamble(vconfig["main"])
    text += _get_latex_body(vconfig["main"], add_title)

    # Print the text if requested.
    if vconfig["save"]["print"]:
        print(text)

    # Save the file if requested.
    path = _save_latex_file(text, config["save"])

    # to the dictionary.
    if vconfig["build"]["compile"] and not vconfig["save"]["save"]:
        warnings.warn(
            "The LaTeX file will not be compiled since the file is not being "
            "saved."
        )

    elif vconfig["build"]["compile"]:
        _compile_latex_file(path, vconfig["build"])

    # Return the text if requested.
    if vconfig["save"]["return"]:
        return text


# ##############################################################################
# Main Program
# ##############################################################################
    

if __name__ == "__main__":
    __config = _get_args()
    main_run(__config)
