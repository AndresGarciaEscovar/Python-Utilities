"""
    File that contains auxiliary and general utilities to help with the tests.
"""

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from typing import Any, Type, Union


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RaisesException:
    """
        Class to test an exception has been thrown.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __enter__(self) -> None:
        """
            Sets up the variables when entering the context manager.
        """

    def __exit__(self, exc_typ: Any, exc_val: Any, _: Any) -> bool:
        """
            Performs the operations before exiting the context manager. In this
            case, removes the file, if requested.

            :param exc_typ: The object with the exception types.

            :param exc_val: The object with the exception values.

            :param _: The object with the exception tracebacks.
        """
        # Auxiliary variables.
        extra: str = self.message if isinstance(self.message, str) else ""
        message: str = ""

        # Check the properties.
        if self.exp_excp != exc_typ:
            message += (
                f"The expected exception, {self.exp_excp.__name__}, "
                f"has not been raised; raised exception: {exc_typ.__name__}. "
            )

        elif isinstance(self.exp_mssg, str) and self.exp_mssg != f"{exc_val}":
            message = (
                f"The expected exception message does not match the raised "
                f"exception message:\nexpected: \"{self.exp_mssg}\". "
            )

        # Raise an exception if needed.
        flag: bool = message == ""

        # Append the final message if needed.
        if not flag:
            exc_val.add_note(f"{message} {extra}".rstrip())

        return flag

    # /////////////////////////////////////////////////////////////////////////
    # Constructor.
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self,
        expected_exp: Type,
        expected_msg: Union[None, str] = None,
        message: str = ""
    ) -> None:
        """
            Initializes the parameters.

            :param excepted_exp: The expected exception type.

            :param expected_msg: The expected message from the exception.

            :param message: A custom message if validation fails.
        """
        # Initialize the variables.
        self.exp_excp: Type = expected_exp
        self.exp_mssg: Union[None, str] = expected_msg
        self.message: str = message
