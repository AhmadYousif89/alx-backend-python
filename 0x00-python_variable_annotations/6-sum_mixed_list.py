#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list which takes a
(mxd_lst: List[Union[int, float]]) as argument and returns the sum as -> float.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the list of mixed integers and floats."""
    return sum(mxd_lst)
