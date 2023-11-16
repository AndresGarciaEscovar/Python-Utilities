"""
    File that contains the functions to format the LaTeX code and, thus, produce
    a minimimum working LaTeX file.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_packages(configuration: dict) -> str:
    """
        Generates the packages preamble.

        :param configuration: The dictionary with the configuration of the
         lattice.
    """
    # Get the packages.
    text = []
    for package in configuration["packages"]:
        if isinstance(package, str):
            text.append(f"\\usepackage{{{package}}}")

        else:
            text.append(f"\\usepackage[{','.join(package[1])}]{{{package[0]}}}")

    text = f"\n".join(text)
    return f"% Packages.\n{text}"


def _get_document_class(configuration: dict) -> str:
    """
        Generates the document class preamble.

        :param configuration: The dictionary with the configuration of the
         lattice.
    """
    # Auxiliary variables.
    dname = "document_class"

    # Get the document class.
    dclass = configuration[dname]

    # Get the text.
    if isinstance(dclass, str):
        text = [r"\documentclass{", f"{dclass}", "}"]

    else:
        text = [
            r"\documentclass[", f"{','.join(dclass[1])}", "]{", f"{dclass[0]}",
            "}"
        ]

    return f"% Document class.\n{''.join(text)}"


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


def get_text(configuration: dict) -> str:
    """
        Using the variables in the configuration dictionary, generates the
        string of the text that will form the LaTeX file.

        :param configuration: The dictionary with the configuration of the
         lattice.
    """
    # Get the valid configuration.
    text: list = [
        _get_document_class(configuration),
        _get_packages(configuration),
    ]

    return "\n\n".join(text)
