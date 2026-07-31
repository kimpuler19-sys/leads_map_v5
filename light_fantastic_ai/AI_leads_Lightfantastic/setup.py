from setuptools import setup
from Cython.Build import cythonize
import os

# List all .py files to compile
py_files = []
for f in os.listdir('.'):
    if f.endswith('.py') and f != 'setup.py':
        py_files.append(f)

setup(
    name="ProtectedApp",
    ext_modules=cythonize(
        py_files,
        compiler_directives={
            'language_level': 3,
            'boundscheck': False,
            'wraparound': False,
            'initializedcheck': False,
            'nonecheck': False
        }
    )
)
