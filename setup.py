from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("_cython_test.pyx")
)

#python setup.py build_ext --inplace