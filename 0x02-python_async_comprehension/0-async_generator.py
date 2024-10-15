#!/usr/bin/env python3
'''Task 0
'''
import asyncio
import random
from typing import Generator


async def async_generator()-> Generator[float, None, None]:
    '''Generates a sequence of numbers.
    '''
    for_in range(10):
        await asyncio.sleep(1) # wait for 1 second.
        yield random.uniform() *10 # yield random number from 0 to 10.
