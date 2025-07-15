#!/usr/bin/env python3
"""
Measure total runtime for async execution
"""

import asyncio
import importlib.util
import time

spec = importlib.util.spec_from_file_location("custom_name", "./1-async_comprehension.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
async_comprehension = module.async_comprehension


async def measure_runtime():
    """
    Measure total runtime for async execution
    """

    start = time.perf_counter_ns()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    end = time.perf_counter_ns()

    return end - start
