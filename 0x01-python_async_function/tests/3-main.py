#!/usr/bin/env python3

import asyncio
from __helper import import_module

task_wait_random = import_module('../3-tasks').task_wait_random


async def test(max_delay: int):
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)


asyncio.run(test(5))
