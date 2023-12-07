#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function that takes list of ints and floats
    returns:
        float as sum of each sumber
    """
    total: float = 0.0

    for num in mxd_lst:
        total += num
    return total
