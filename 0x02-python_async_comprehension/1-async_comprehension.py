#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """
    function that returns 10 random numbers from async_generator
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
