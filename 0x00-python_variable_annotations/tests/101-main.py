#!/usr/bin/env python3
from __helper import import_module

safely_get_value = import_module('../101-safely_get_value').safely_get_value
annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print( ("{}: {}".format(k, v)))
