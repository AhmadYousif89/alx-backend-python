#!/usr/bin/env python3
from __helper import import_module

safe_first_element =  import_module('../100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)
