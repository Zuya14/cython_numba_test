import datetime
from numba import jit
import numpy as np

def calc(a, b):
    return a + b

@jit
def calc_jit(a, b):
    return a + b

def calc_n(a, b, n):
    result = 0
    for i in range(n):
        result += a + b + i
    return result

@jit
def calc_n_jit(a, b, n):
    result = 0
    for i in range(n):
        result += a + b + i
    return result

def benchmark(method, *args):
    s_time = datetime.datetime.now()
    method(*args)
    e_time = datetime.datetime.now()
    print("end-start:", e_time-s_time)

def benchmark_n(method, n, *args):
    s_time = datetime.datetime.now()
    for _ in range(n):
        method(*args)
    e_time = datetime.datetime.now()
    print("end-start:", e_time-s_time)

if __name__ == '__main__':

    benchmark_n(calc, 10000000, 100.0, 200.0)
    benchmark(calc_n, 100.0, 200.0, 10000000)
    print()
    benchmark_n(calc_jit, 10000000, 100.0, 200.0)
    benchmark(calc_n_jit, 100.0, 200.0, 10000000)