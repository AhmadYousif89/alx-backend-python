#!/usr/bin/env python3
from __helper import import_module

zoom_array =  import_module('../102-type_checking').zoom_array

print(zoom_array.__annotations__)
