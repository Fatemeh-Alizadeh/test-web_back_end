#!/usr/bin/env python3
"""
Return a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the first element as the string key and the second
    element as the square of the value, cast to float.

    Args:
        k (str): The key string.
        v (int | float): The value to square.

    Returns:
        tuple[str, float]: A tuple of (k, v squared as float).
    """
    return (k, float(v ** 2))
