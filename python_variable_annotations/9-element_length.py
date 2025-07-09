#!/usr/bin/env python3
"""
Takes an iterable of sequences and returns a list
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains the sequence and its length.

    Args:
        lst (Iterable[Sequence]).

    Returns:
        List[Tuple[Sequence, int]].
    """
    return [(i, len(i)) for i in lst]
