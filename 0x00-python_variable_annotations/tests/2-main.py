#!/usr/bin/env python3
from __helper import import_module
import math

floor = import_module('../2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
