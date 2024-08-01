#!/usr/bin/env python3
"""
Type-annotated function safe_first_element that takes a lst of any type
and returns its first element if exists, otherwise None.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence or None."""    
    return lst[0] if lst else None
        
