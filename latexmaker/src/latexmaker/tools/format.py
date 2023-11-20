"""
    File that contains the functions to format the LaTeX code and, thus, produce
    a minimimum working LaTeX file.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Private Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_document_class(configuration: dict) -> str:
    """
        Generates the document class preamble.

        :param configuration: The dictionary with the configuration of the
         lattice.

        :return: The string with the document class preamble.
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


def _get_document_close() -> str:
    """
        Gets the text that closes the document.

        :return: The text that closes the document, if it is specified.
    """
    return "\n".join([
        r"% End document.",
        r"\end{document}"
    ])


def _get_document_start(configuration: dict) -> str:
    """
        Gets the text that starts the document.

        :param configuration: The dictionary that contains the document start
         configuration.

        :return: The text that starts the document, including the \\maketitle
         command, if it is specified.
    """
    flag = True
    flag = flag and configuration["author"].strip() == ""
    flag = flag and configuration["date"].strip() == ""
    flag = flag and configuration["title"].strip() == ""

    # Get the text.
    return "\n".join([
        r"% Begin document.",
        r"\begin{document}",
        r"\maketitle" f"\n" r"\newpage" if not flag else "",
    ])


def _get_document_text(configuration: dict) -> str:
    """
        Gets the text of the document, if there is any.

        :param configuration: The dictionary with the configuration of the
         LaTeX file.

        :return: The string with the main text of the document.
    """
    return configuration["text"]


def _get_other_preamble(configuration: dict) -> str:
    """
        Sets the other preamble variables for the LaTeX file.

        :param configuration: The dictionary with the configuration of the
         lattice.

        :return: The string with the other preamble variables.
    """
    # Get the text.
    text = ""
    if configuration["other_preamble"].strip() != "":
        text = "\n".join([
            "% Other preamble.",
            configuration["other_preamble"]
        ])

    return text


def _get_packages(configuration: dict) -> str:
    """
        Generates the packages preamble.

        :param configuration: The dictionary with the configuration of the
         lattice.

        :return: The string with the packages preamble.
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


def _get_title_author_date(configuration: dict) -> str:
    """
        Gets the title, author and date of the LaTeX file.

        :param configuration: The dictionary with the configuration of the
         author, title and date.

        :return: The string with the title, author and date; if all of the items
         are blank, an empty string is returned.
    """
    # Validate the configuration.
    flag = True
    flag = flag and configuration["author"].strip() == ""
    flag = flag and configuration["date"].strip() == ""
    flag = flag and configuration["title"].strip() == ""

    # Blank text.
    return "" if flag else "\n".join([
        "% Title, author and date.",
        f"\\title{{{configuration['title']}}}",
        f"\\author{{{configuration['author']}}}",
        f"\\date{{{configuration['date']}}}",
    ])


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Public Interface
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


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
        _get_other_preamble(configuration),
        _get_title_author_date(configuration),
        _get_document_start(configuration),
        _get_document_text(configuration),
        _get_document_close(),
    ]

    return "\n\n".join([x.strip() for x in text if x.strip() != ""])
