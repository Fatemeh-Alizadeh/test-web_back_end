#!/usr/bin/env python3
"""
Asynchronous coroutine that collects 10 random numbers from async_generator.
"""

import asyncio
import importlib.util

spec = importlib.util.spec_from_file_location("custom_name", "./0-async_generator.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
async_generator = module.async_generator


async def async_comprehension():
    """
    Asynchronous coroutine that collects 10 random numbers from async_generator.

    Uses an async comprehension to asynchronously iterate over async_generator
    and collect the yielded random integers into a list.

    Returns:
        List[int]: A list of 10 random integers between 0 and 10.
    """
    return [numbers async for numbers in async_generator()]
