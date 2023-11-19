"""
    File that contains the functions to validate the input data and the
    different parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User defined.
import latex_maker.src.data_files as dfiles

# Third party.
import yaml

from pathlib import Path

# General
from importlib.resources import files


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Special Configurations
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_validate' Function
# ------------------------------------------------------------------------------


def _validate(configuration: dict) -> None:
    """
        Checks that all the keys are present in the configuration file and
        that the general types are correct.

        :param configuration: Dictionary with the configuration data.

        :raises KeyError: If any of the keys is missing.

        :raises TypeError: If any of the types is incorrect.
    """
    # If the configuration is not a dictionary, raise an error.
    if not isinstance(configuration, dict):
        raise TypeError(
            f"The configuration is not a dictionary. Current type: "
            f"\"{type(configuration).__name__}\""
        )

    # Load the validation dictionary.
    name = "configuration_types.yaml"
    with files(dfiles.__name__).joinpath(name).open() as file:
        vdictionary = yaml.safe_load(file)

    # Check that all the keys are present.
    current = set(configuration.keys())
    expected = set(vdictionary.keys())
    if not current == expected:
        raise KeyError(
            "The first level keys are missing."
        )

    # Check all the subkeys and the types.
    for key, value in configuration.items():
        # Must be a dictionary.
        if not isinstance(value, dict):
            raise TypeError(
                f"The type of the key \"{key}\" is incorrect, it must"
                f"be a dictionary. Current type: \"{type(value).__name__}\"."
            )

        # Check the subkeys.
        current = set(value.keys())
        expected = set(vdictionary[key].keys())
        if not current == expected:
            raise KeyError(
                f"The subkeys of the key \"{key}\" are missing. Current: "
                f"{current}, expected: {expected}."
            )

        # Check the types.
        for key0, value0 in value.items():
            if type(value0).__name__ not in vdictionary[key][key0]:
                raise TypeError(
                    f"The type of the key \"{key0}\" is incorrect, it must "
                    f"be a \"{vdictionary[key][key0]}\". Current type: "
                    f"\"{type(value0).__name__}\"."
                )


def _validate_build(configuration: dict) -> None:
    """
        Validates some of the build parameters tame a specific form.

        :param configuration: Dictionary with the configuration data.

        :raises TypeError: If any of the types is incorrect.
    """
    # Validate that the command is one of the allowed ones.
    allowed = {"pdflatex", "xelatex", "latex"}
    if (command := configuration["command"].strip()) not in allowed:
        raise ValueError(
            f"The build command is not one of the allowed ones. Allowed "
            f"commands: {allowed}. Current command: {command}."
        )

    # Validate that the flags are a list of strings.
    if not all(isinstance(x, str) for x in configuration["flags"]):
        raise TypeError(
            f"The build flags must be a list of strings. Current types: "
            f"{tuple(type(x).__name__ for x in configuration['flags'])}."
        )


def _validate_main(configuration: dict) -> None:
    """
        Validates some of the main parameters take a specific form.

        :param configuration: Dictionary with the configuration data.

        :raises TypeError: If any of the types is incorrect.
    """
    # //////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions
    # //////////////////////////////////////////////////////////////////////////

    def _s_entry_first(vobject: list, name: str) -> None:
        """
            Validates that the first entry of the list is a string.

            :param vobject: List to validate.

            :param name: Name of the list.

            :raises TypeError: If the first entry of the list is not a
             string.
        """
        # No need to raise an exception.
        if isinstance((fentry := vobject[0]), str):
            return

        if name == "document_class":
            message = (
                f"The first element of the \"document_class\" list must be a "
                f"string that represents the document class. First entry "
                f"current type: {type(fentry).__name__}, first value: {fentry}"
            )

        else:
            message = (
                f"There is a sublist in the \"packages\" list that doesn't "
                f"have a string as its first element, that must be the name of "
                f"the package. First entry current type: "
                f"{type(fentry).__name__}, first value: {fentry}"
            )

        raise ValueError(message)

    def _s_entry_second(vobject: list, name: str) -> None:
        """
            Validates that the second entry of the list is a list of strings.

            :param vobject: List to validate.

            :param name: Name of the list.

            :raises TypeError: If the second entry of the list is not a
             list of strings.
        """
        # No need to raise an exception.
        flag0 = isinstance(vobject[1], list)
        if flag0 and all(isinstance(x, str) for x in vobject[1]):
            return

        # Get the appropriate message.
        if not flag0:
            message = (
                f"The second element of the given list is not a list, it must "
                f"be a list. Current type: {type(vobject[1]).__name__}, "
                f"values: {vobject[1]}"
            )

        else:
            message = (
                f"The second element of the list is not a list of strings, it "
                f"must be a list of strings. Current types: "
                f"{tuple(type(x).__name__ for x in vobject[1])}, values: "
                f"{vobject[1]}."
            )

        # Set the proper message.
        if name == "document_class":
            message = (
                f"The second element of the \"document_class\" has a problem. "
                f"{message}"
            )

        else:
            message = (
                f"There is a sublist in the \"packages\" list that has a "
                f"problem. {message}"
            )

        raise ValueError(message)

    def _s_validate_length(vobject: list, name: str) -> None:
        """
            Validates that the length of list is exactly 2.

            :param vobject: List to validate.

            :param name: Name of the list.

            :raises ValueError: If the length is not 2.
        """
        # No need to raise an exception.
        if (length := len(vobject)) == 2:
            return

        if name == "document_class":
            message = (
                "The \"document_class\" list doesn't have a length of 2. It "
                f"must be a list of two entries. Current length: {length}"
            )

        else:
            message = (
                f"There is a sublist in the \"packages\" list that doesn't "
                f"have a length of 2. List: {vobject}, list length: "
                f"{length}"
            )

        raise ValueError(message)

    # //////////////////////////////////////////////////////////////////////////
    # Implementation
    # //////////////////////////////////////////////////////////////////////////

    # Check the document class.
    if isinstance(configuration["document_class"], list):
        tvalue = configuration["document_class"]
        _s_validate_length(tvalue, "document_class")
        _s_entry_first(tvalue, "document_class")
        _s_entry_second(tvalue, "document_class")

    # Check the packages.
    for value in configuration["packages"]:
        if isinstance(value, str):
            continue

        _s_validate_length(value, "packages")
        _s_entry_first(value, "packages")
        _s_entry_second(value, "packages")


def _validate_save(configuration: dict) -> None:
    """
        Validates the save parameters are correct.

        :param configuration: Dictionary with the configuration data.

        :raises TypeError: If any of the types is incorrect.
    """

    # Check the document class.
    path = Path(configuration["path"]).absolute().resolve()
    if not path.is_dir():
        raise TypeError(
            f"The path to save the files is not a directory. Make sure the "
            f"directory exists to resolve this error. Requested absolute path: "
            f"{path}."
        )


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'validate' Function
# ------------------------------------------------------------------------------


def validate(configuration: dict) -> None:
    """
        Function that validates that the input data is consistent; i.e, the
        data is the correct type and the parameters are in the correct range.

        :param configuration: Dictionary with the configuration data.
    """
    # Validate the different quantities.
    ic("HERE")

    _validate(configuration)
    _validate_build(configuration["build"])
    _validate_main(configuration["main"])
    _validate_save(configuration["save"])
