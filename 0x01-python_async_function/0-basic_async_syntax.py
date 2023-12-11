#!/usr/bin/env python3
"""
0. The basics of async
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    function that waits for a random delay between 0 and max_delay
    and returns it
    args:
        max_delay: integer arg with default value of 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay