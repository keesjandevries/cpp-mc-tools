cdef extern from "VarsLookup.h":
    cdef cppclass VarsLookup:
        VarsLookup(int)
        float temp_get_value(float *) 

cdef class PyVarsLookup:
    cdef VarsLookup *thisptr
    def __cinit__(self, int array_index):
        self.thisptr = new VarsLookup(array_index)
    def __dealloc__(self):
        del self.thisptr
    def get_value(vars):
        cdef float[len(vars)] c_vars
        return self.thisptr.temp_get_value(c_vars)
