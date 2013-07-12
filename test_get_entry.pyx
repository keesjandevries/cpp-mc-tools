# distutils: language = c++
# distutils: include_dirs = include
# distutils: sources = src/VarsLookup.cpp src/BaseGetValueFunction.cpp

import cython
from libc.stdlib cimport malloc, free

cdef extern from "VarsLookup.h":
    cdef cppclass VarsLookup:
        VarsLookup(int)
        double get_value(double *)
#        double temp_get_value(double *) 

cdef class PyVarsLookup:
    cdef VarsLookup *thisptr
    def __cinit__(self, int array_index):
        self.thisptr = new VarsLookup(array_index)
    def __dealloc__(self):
        del self.thisptr
    def get_value(self,vars):
        cdef int len_vars=len(vars)
        cdef double * c_vars= <double *>malloc(len_vars * cython.sizeof(double))
        for i in xrange(len(vars)):
            c_vars[i]=vars[i]
        cdef double value 
        value = self.thisptr.get_value(c_vars)
        free( c_vars)
        return value
