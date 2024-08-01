#!/usr/bin/env python3
from __helper import import_module
add = import_module('../0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

