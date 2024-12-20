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
builtin = Union[
    bool, complex, dict, float, frozenset, int, list, set, str, tuple
]

# Tuple types.
tbool = tuple[bool, bool]
treal = tuple[Real, Real]


class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

if __name__ == "__main__":

    dog = Dog("Fido", 5)
    print(isinstance(dog, builtin))
