#!/usr/bin/env python3
"""Basic asynchronous function"""

import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async function that waits for a random delay
    between 0 and max_delay seconds and returns it.
    """
    delay = random.uniform(0, max_delay)
    return delay
