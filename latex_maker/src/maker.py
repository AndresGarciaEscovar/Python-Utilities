"""
    Test to create a LaTeX file from a Python script and then compile it using
    the subprocess module.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User defined.
import latex_maker.src.data_files as dfiles
import latex_maker.src.tools.format as formatter
import latex_maker.src.tools.validate as validator

# General
import copy as cp
import yaml

from importlib.resources import files
from pathlib import Path
from typing import Union

# Thrid party
from icecream import ic, install
install()
ic.configureOutput(
    includeContext=True,
)


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

    return cp.deepcopy(tconfig)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def get_text(config: Union[dict, None] = None) -> Union[None, str]:
    """
        Runs the main program.

        :param config: The configuration dictionary to use. If None, the default
         configuration will be used.

        :return: The text of the LaTeX file, if requested. None, otherwise.
    """
    # Run the program.
    tconfig = _validate_configuration(config)
    text = formatter.get_text(tconfig["main"])

    return text


# ##############################################################################
# Main Program
# ##############################################################################


if __name__ == "__main__":
    get_text(None)
