"""
    Custom types.
"""


# #############################################################################
# Imports
# #############################################################################


# Standard Library.
from numbers import Real
from typing import Union, Type


# #############################################################################
# Types
# #############################################################################


# built-in types.
builtin_collections = Union[dict, frozenset, list, set, tuple]
builtin_numbers = Union[complex, float, int]

builtin = Union[builtin_collections, builtin_numbers, str]

# Tuple types.
tbool = tuple[bool, bool]
treal = tuple[Real, Real]
