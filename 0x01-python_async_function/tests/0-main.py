#!/usr/bin/env python3

import asyncio
from __helper import import_module

wait_random = import_module('../0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
