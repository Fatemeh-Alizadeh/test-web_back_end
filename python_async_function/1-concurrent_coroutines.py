#!/usr/bin/env python3
"""
Run wait_random n times concurrently with a given max_delay,
and return the list of delays in the order they are completed.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently with a given max_delay,
    and return the list of delays in the order they are completed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
