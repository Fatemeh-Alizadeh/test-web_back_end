#!/usr/bin/env python3
"""
Run wait_random n times concurrently with a given max_delay,
and return the list of delays in the order they are completed.
"""
import asyncio
from typing import List
import importlib.util

spec = importlib.util.spec_from_file_location("custom_name", "./0-basic_async_syntax.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

wait_random = module.wait_random


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
