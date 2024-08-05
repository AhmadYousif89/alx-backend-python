#!/usr/bin/env python3
"""Returns a asyncio.Task"""
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Returns a asyncio.Task"""
    task = create_task(wait_random(max_delay))
    return task
