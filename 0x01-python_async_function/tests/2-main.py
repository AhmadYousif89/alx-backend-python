#!/usr/bin/env python3
from __helper import import_module

measure_time = import_module('../2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
