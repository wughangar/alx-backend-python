#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    function that takes list and returns a list from tuple
    """
    return [(i, len(i)) for i in lst]
