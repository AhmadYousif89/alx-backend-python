#!/usr/bin/env python3
"""
Type-annotated function element_length that takes a (input_list: List[str]) as argument
and returns a Tuple containing a string and a float.
"""

from typing import List, Tuple, Sequence, Iterable

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing a string and its length."""
    return [(i, len(i)) for i in lst]
