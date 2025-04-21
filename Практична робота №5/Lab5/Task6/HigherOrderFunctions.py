from Task5.TimingDecorator import timing
from functools import reduce
import time
import math

@timing
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

@timing
def my_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

@timing
def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for item in it:
        value = func(value, item)
    return value

@timing
def builtin_map(func, iterable):
    return list(map(func, iterable))

@timing
def builtin_filter(func, iterable):
    return list(filter(func, iterable))

@timing
def builtin_reduce(func, iterable):
    return reduce(func, iterable)

def slow_factorial(n):
    time.sleep(0.001)
    return math.factorial(n)

def is_even(n):
    time.sleep(0.001)
    return n % 2 == 0

def add(x, y):
    time.sleep(0.001)
    return x + y