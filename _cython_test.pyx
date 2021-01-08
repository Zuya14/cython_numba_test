cimport cython

cpdef float calc_c(float a, float b):
    return a + b

cpdef float calc_c_n(float a, float b, int n):
    cdef float result = 0
    cdef int i
    for i in range(n):
        result += a + b + i
    return result

    