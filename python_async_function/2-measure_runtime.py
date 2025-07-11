#!/usr/bin/env python3
"""
Measure total runtime for async execution
"""
import time
import asyncio
import importlib.util

spec = importlib.util.spec_from_file_location("custom_name", "./1-concurrent_coroutines.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average runtime of calling wait_n"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start

    return total_time / n
