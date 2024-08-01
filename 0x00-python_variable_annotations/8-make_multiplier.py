#!/usr/bin/env python3
"""
Type-annotated function make_multiplier that takes a (multiplier: float)
as argument and returns a function that multiplies a float by the multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the multiplier."""
    def multiply(n: float) -> float:
        """Returns the product of a float and the multiplier."""
        return n * multiplier
    return multiply
