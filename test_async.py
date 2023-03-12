#!/usr/bin/python
# coding: utf8


import random
import asyncio
import async

from async import *

from ayo.scope import *
from ayo.utils import *

print 'Test async'

async def zzz():
    time = random.randint(0, 15)
    await asyncio.sleep(time)
    print("Slept for  {} seconds".format(time))

with ayo.scope(max_concurrency=10, timeout=12) as run:
    for _ in range(20):
        run << zzz()