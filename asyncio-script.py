#!/usr/bin/python
# coding: utf8

""" Testing asyncio functions"""

import asyncio

print("Asyncio functions test")

async def display_hello():
    print("Hello")
    await asyncio.sleep(2)
    print(" World ...")

asyncio.run(display_hello())
