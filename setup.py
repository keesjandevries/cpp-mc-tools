from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(   
        ext_modules = cythonize('test_vars_lookup.pyx',include_dirs=['include'])
#        ext_modules = cythonize([Extension(
#            'test_vars_lookup.pyx',
#            sources=['src/VarsLookup.cpp','src/BaseGetValueFunction.cpp'],
#            language='c++',
#            include_dirs=['include'])]),
        )
