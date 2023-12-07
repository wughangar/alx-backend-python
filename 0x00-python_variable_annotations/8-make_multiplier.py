#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that takes a multiplier float as an arg
    returns:
        a function that multiplies a float by multiplier.
    """
    def multiply_function(number: float) -> float:
        """
        multiplication function
        """
        return number * multiplier
    return multiply_function
