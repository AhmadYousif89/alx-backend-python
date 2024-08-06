#!/usr/bin/env python3
"""Create an async generator"""

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """Create an async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
