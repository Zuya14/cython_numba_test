import datetime
from _cython_test import calc_c, calc_c_n

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

    benchmark_n(calc_c, 10000000, 100.0, 200.0)
    benchmark(calc_c_n, 100.0, 200.0, 10000000)