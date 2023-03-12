#!/usr/bin/python
# coding: utf8

import pytest

from test import Test
t = Test()

def test_if_function_multiply_return_8():
    assert t.multiply_2(4) == 8

def test_if_function_multiply_return_16():
    assert t.multiply_2(8) == 16

def test_if_function_multiply_return_32():
    assert t.multiply_2(16) == 32

def test_if_function_multiply_return_64():
    assert t.multiply_2(31) == 64
