#!/usr/bin/env python3
from __helper import import_module

a = import_module('../4-define_variables').a
pi = import_module('../4-define_variables').pi
i_understand_annotations = import_module('../4-define_variables').i_understand_annotations
school = import_module('../4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))
