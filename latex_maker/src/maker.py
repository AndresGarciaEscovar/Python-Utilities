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
    # Open the configuration file.
    name = "configuration.yaml"
    if config is None:
        with files(dfiles.__name__).joinpath(name).open() as file:
            config = yaml.safe_load(file)

    # Validate the configuration.
    validator.validate(config)

    text = formatter.get_text(config["main"])



# ##############################################################################
# Main Program
# ##############################################################################


if __name__ == "__main__":
    get_text(None)
