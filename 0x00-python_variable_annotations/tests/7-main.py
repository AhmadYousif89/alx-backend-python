#!/usr/bin/env python3
from __helper import import_module

to_kv = import_module('../7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
