#!/usr/bin/env python3
"""
Type-annotated function safely_get_value that takes a (dict, str) as argument
and returns the value linked to key if exists, otherwise None.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
D = Union[T, None]
R = Union[Any, T]

def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    """Returns the value linked to key in a dict or None."""    
    return dct[key] if key in dct else default
