#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function that exeutes multiple coroutines at the same timw with async
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
