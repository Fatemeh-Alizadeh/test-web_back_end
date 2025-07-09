#!/usr/bin/env python3
"""
Returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by the given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
                                 the product as a float.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
