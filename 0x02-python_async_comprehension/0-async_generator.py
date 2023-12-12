#!/usr/bin/env python3
"""
0. Async Generator
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    function that loops 10times and returns a random number between 0, 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
