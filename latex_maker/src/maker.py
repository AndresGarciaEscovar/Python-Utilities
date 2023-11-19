"""
    Test to create a LaTeX file from a Python script and then compile it using
    the subprocess module.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User defined.
import latex_maker.src.data_files as dfiles
import latex_maker.src.tools.compile as compiler
import latex_maker.src.tools.format as formatter
import latex_maker.src.tools.save as saver
import latex_maker.src.tools.validate as validator
import latex_maker.src.tools.validate_parameters as vparameters

# General
import copy as cp
import yaml

from importlib.resources import files
from pathlib import Path
from typing import Union


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_text(config: dict) -> str:
    """
        Gets the text of the LaTeX file.

        :param config: The configuration dictionary to use.

        :return: The text of the LaTeX file.
    """
    return formatter.get_text(config["main"])


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_configuration(config: Union[dict, None]) -> dict:
    """
        Vakudates that the given configuration is valid and retuns the
        configuration for the main program.

        :param config: The configuration dictionary to validate. It can be None.

        :return: The configuration dictionary for the main program.
    """
    # For non-None values, validate the configuration.
    if config is not None:
        validator.validate(config)
        return cp.deepcopy(config)

    # Return the default configuration.
    with files(dfiles.__name__).joinpath("configuration.yaml").open() as file:
        tconfig = yaml.safe_load(file)
    validator.validate(tconfig)

    return cp.deepcopy(tconfig)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_configuration(
    path_save: str = None, dprint: bool = False, fmt_yaml: bool = False
) -> dict:
    """
        Gets the dictionary with the default configuration. Also, saves and/or
        prints to the screen the default configuration file with all the
        settings.

        :param path_save: A string with the path to save the default
         configuration. If None, the default configuration will not be saved.

        :param dprint: A boolean flags indicating whether to print the default
         configuration to the screen. True, if the default configuration will
         be printed to the screen. False, otherwise.

        :param fmt_yaml: A boolean flag indicating whether to format the
         screen output to that resembling a YAML file. True, if the screen
         output will be formatted to resemble a YAML file. False, if a
         traditional dictionary format is preferred.

        :return: The default configuration dictionary.
    """
    # Validate the parameters.
    vparameters.validate(path_save, dprint, fmt_yaml)

    # Get the default configuration.
    with files(dfiles.__name__).joinpath("configuration.yaml").open() as file:
        tconfig = yaml.safe_load(file)

    # Save if requested.
    if path_save is not None:
        # Don't overwrite existing files.
        tpath = Path(path_save)
        counter = 0

        # Get the new name.
        while tpath.is_file():
            suffix = tpath.suffix
            tpath = Path(path_save).with_suffix("")
            tpath = Path(f"{tpath}({counter}).{suffix}")
            counter += 1

        # Save the file.
        with open(f"{tpath}", "w") as file:

            yaml.dump(tconfig, file)

    # Print if requested.
    if dprint and fmt_yaml:
        for key, value in tconfig.items():
            print(f"{key}:")
            for key0, value0 in value.items():
                value0 = f"'{value0}'" if isinstance(value0, str) else value0
                print(f"  {key0}: {value0}")

    elif dprint:
        print(tconfig)

    return tconfig


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def text(config: Union[dict, None] = None) -> Union[None, str]:
    """
        Runs the main program.

        :param config: The configuration dictionary to use. If None, the default
         configuration will be used.

        :return: The text of the LaTeX file, if requested. None, otherwise.
    """
    # Run the program.
    tconfig = _validate_configuration(config)
    ptext = formatter.get_text(tconfig["main"])
    path = saver.save(ptext, tconfig["save"])
    compiler.compile_file(path, tconfig["build"], tconfig["save"]["save"])

    return ptext
