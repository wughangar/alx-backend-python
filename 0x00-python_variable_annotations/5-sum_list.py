#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function that takes a list of floats and returns their sum as flaot
    """
    total: float = 0.0
    for num in input_list:
        total += num
    return total
