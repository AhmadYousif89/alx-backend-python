#!/usr/bin/env python3
"""
Type-annotated function sum_list which takes (input_list: List[float])
as argument and returns the sum as -> float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the list of floats."""
    return sum(input_list)
