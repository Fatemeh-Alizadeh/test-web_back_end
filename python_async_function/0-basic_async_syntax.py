#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay
between 0 and max_delay seconds and returns the delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and returns the delay.
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
