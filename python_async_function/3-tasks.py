#!/usr/bin/env python3
"""Creates and returns an asyncio.Task for wait_random"""
import asyncio
import importlib.util

spec = importlib.util.spec_from_file_location("custom_name", "./0-basic_async_syntax.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task for wait_random"""
    return asyncio.create_task(wait_random(max_delay))
