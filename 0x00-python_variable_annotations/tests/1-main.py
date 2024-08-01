#!/usr/bin/env python3
from __helper import import_module
concat = import_module('../1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
