# distutils: language = c++
# distutils: include_dirs = include /usr/include/root/
# distutils: libraries = Core Cint RIO Net Hist Graf Graf3d Gpad Tree Rint Postscript Matrix Physics MathCore Thread  m dl 
# distutils: library_dirs =  /usr/lib64/root/
# distutils: sources = src/GetEntry.cpp  src/VarsLookup.cpp src/BaseGetValueFunction.cpp

import cython
from libc.stdlib cimport malloc, free

#Get Entry
cdef extern from "GetEntry.h":
    cdef cppclass GetEntry:
        GetEntry(const char *)
        double * GetVars(int)
        int GetNVars()

cdef class PyGetEntry:
    cdef GetEntry *thisptr
    def __cinit__(self,filename):
        byte_filename=filename.encode('UTF-8')
        cdef const char *c_filename = byte_filename
        #FIXME: build in safety
        self.thisptr = new GetEntry(c_filename)
        #FIXME: this should be part of the routine
#        self._nvars=self.thisptr.GetNVars()
    def __dealloc__(self):
        del self.thisptr
    def get_vars(self,entry):
        cdef int c_entry=entry #NOTE: this step could be ommited
        cdef double * c_vars=self.thisptr.GetVars(c_entry)
        #FIXME: may want to make _nvars an attribute instead of using it here
        return [c_vars[i] for i in range(self.thisptr.GetNVars())]

# vars lookup
cdef extern from "VarsLookup.h":
    cdef cppclass VarsLookup:
        VarsLookup(int)
        double get_value(double *)

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
