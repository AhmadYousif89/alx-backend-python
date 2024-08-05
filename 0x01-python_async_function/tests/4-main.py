#!/usr/bin/env python3

import asyncio
from __helper import import_module

task_wait_n = import_module('../4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
