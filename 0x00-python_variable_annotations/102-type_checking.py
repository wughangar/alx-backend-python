#!/usr/bin/env python3
"""
type checking
"""
from typing import Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    function that returns a tuple of integers
    """
    zoomed_in: Tuple[int, ...] = tuple(
         [item for item in lst for _ in range(factor)]
         )
    return zoomed_in

array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

