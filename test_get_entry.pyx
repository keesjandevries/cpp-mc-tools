# distutils: language = c++
# distutils: include_dirs = include /usr/include/root/
# distutils: libraries = Core Cint RIO Net Hist Graf Graf3d Gpad Tree Rint Postscript Matrix Physics MathCore Thread  m dl 
# distutils: library_dirs =  /usr/lib64/root/
# distutils: sources = src/GetEntry.cpp

import cython
from libc.stdlib cimport malloc, free

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
