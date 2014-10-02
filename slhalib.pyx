# distutils: language = c++
# distutils: include_dirs = SLHALib-2.2/x86_64-linux/include/ 
# distutils: libraries = SLHA
# distutils: library_dirs = SLHALib-2.2/x86_64-linux/lib/

cdef extern from "CSLHA.h":
    cdef int nslhadata
    cdef void SLHAWrite(int *, const double complex *, const char *)
    cdef void SLHARead(int *, double complex *, const char *, const int )

cdef class SlhaFile:
    #FIXME: had to hard wire the number (nslhadata in SLHADefs.h)
    cdef double complex _slhadata[5558]
    def __cinit__(self):
        pass
    def __dealloc__(self):
        pass


