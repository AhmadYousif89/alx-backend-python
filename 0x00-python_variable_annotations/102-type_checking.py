#!/usr/bin/env python3
"""
Type-annotated function zoom_array that takes a (lst: Tuple, factor: int)
as arguments and returns -> List.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list of zoomed-in elements"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
