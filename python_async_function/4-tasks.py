#!/usr/bin/env python3
"""Spawns task_wait_random n times and returns the list of delays in order"""
import asyncio
from typing import List
import importlib.util

spec = importlib.util.spec_from_file_location("custom_name", "./3-tasks.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
task_wait_random = module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with max_delay, returns list of delays in ascending order"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
