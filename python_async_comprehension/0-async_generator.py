#!/usr/bin/env python3
"""
Asynchronous generator that yields a random integer between 0 and 10.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields a random integer between 0 and 10.

    This coroutine runs a loop 10 times. In each iteration, it:
    - Asynchronously waits for 1 second.
    - Yields a random integer in the range [0, 10].

    Yields:
        int: A random integer between 0 and 10.
    """

    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
