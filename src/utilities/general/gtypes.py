"""
    Custom types.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real
from typing import Any, Union, Type


# #############################################################################
# Types
# #############################################################################


# built-in types.
builtin_collections = Union[dict, frozenset, list, set, tuple]
builtin_numbers = Union[complex, float, int]

builtin = Union[builtin_collections, builtin_numbers, str]

# Tuple types.
TBool: Any = Union[None, tuple[bool, bool]]
TReal: Any = Union[None, tuple[Real, Real]]

# Union types.
UBool: Any = Union[bool, None]
UReal: Any = Union[None, Real]
