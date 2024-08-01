#!/usr/bin/env python3
from __helper import import_module

make_multiplier = import_module('../8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
