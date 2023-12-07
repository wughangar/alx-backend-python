#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function that takes str, float or int and returns tuple
    """
    value: float = float(v) ** 2
    return k, value
