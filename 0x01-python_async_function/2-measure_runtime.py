#!/usr/bin/env python3
"""Measure runtime for wait_n(n, max_delay)"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def mesure_time(n: int, max_delay: int) -> float:
    """Measures the runtime of wait_n"""
    start = time()
    await run(wait_n(n, max_delay))
    end = time()
    elapsed = end - start
    return elapsed / n
