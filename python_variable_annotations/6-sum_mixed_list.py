#!/usr/bin/env python3
"""
Calculate the sum of a list containing integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (list[int | float]): List of integers and floats.

    Returns:
        float: The sum of all numbers in the list as a float.
    """
    return sum(mxd_lst)
