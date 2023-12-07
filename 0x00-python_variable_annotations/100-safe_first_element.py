#!/usr/bin/env python3
"""
10. Duck typing - first element of a sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function that retuns list
    """
    if lst:
        return lst[0]
    else:
        return None
