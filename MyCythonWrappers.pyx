# distutils: language = c++
# distutils: include_dirs = include /usr/include/root/
# distutils: libraries = Core Cint RIO Net Hist Graf Graf3d Gpad Tree Rint Postscript Matrix Physics MathCore Thread  m dl 
# distutils: library_dirs =  /usr/lib64/root/

import cython
from cython.operator import dereference
from libcpp cimport bool
from libc.stdlib cimport malloc, free

cdef extern from "TFile.h":
    cdef cppclass TFile:
        TFile()
        TFile(const char *)
        TObject * Get(const char *)

cdef extern from "TDirectory.h":
    cdef cppclass TDirectory:
        TDirectory()

cdef extern from "Rtypes.h":
    ctypedef double Double_t
    ctypedef int Int_t
    ctypedef bool Bool_t

cdef extern from "TH1D.h":
    cdef cppclass TH1D:
        TH1D()
        TH1D(const TH1D&)
        TObject * Clone()
        Double_t GetBinContent(Int_t)
        SetDirectory(TDirectory *)
        AddDirectory(Bool_t)

cdef extern from "TObject.h":
    cdef cppclass TObject:
        TObject()
        TObject * Clone()


cdef class PyTFile:
    cdef TFile * thisptr
    def __cinit__(self, filename):
        byte_filename=filename.encode('UTF-8')
        cdef const char *c_filename = byte_filename
        self.thisptr = new TFile(c_filename)
    def __dealloc__(self):
        del self.thisptr
    def get_th1d(self, path):
        byte_path=path.encode('UTF-8')
        cdef const char *c_path = byte_path
        cdef TH1D * th1d_ptr = <TH1D * > self.thisptr.Get(c_path).Clone()
        py_th1d = PyTH1D()
        py_th1d.set_th1d(th1d_ptr)
        return py_th1d

cdef class PyTH1D:
    cdef TH1D * thisptr
    def __cinit__(self):
        self.thisptr = new TH1D()
    def __dealloc__(self):
        del self.thisptr
    cdef set_th1d(self, TH1D * h1d):
        del self.thisptr
        self.thisptr = <TH1D *> h1d.Clone()
        self.thisptr.AddDirectory(False)
    def get_bin_content(self, int i):
        return self.thisptr.GetBinContent(i)
#
##Get Entry
#cdef extern from "GetEntry.h":
#    cdef cppclass GetEntry:
#        GetEntry(const char *)
#        double * GetVars(int)
#        int GetNVars()
#
#cdef class PyGetEntry:
#    cdef GetEntry *thisptr
#    def __cinit__(self,filename):
#        byte_filename=filename.encode('UTF-8')
#        cdef const char *c_filename = byte_filename
#        #FIXME: build in safety
#        self.thisptr = new GetEntry(c_filename)
#        #FIXME: this should be part of the routine
##        self._nvars=self.thisptr.GetNVars()
#    def __dealloc__(self):
#        del self.thisptr
#    def get_vars(self,entry):
#        cdef int c_entry=entry #NOTE: this step could be ommited
#        cdef double * c_vars=self.thisptr.GetVars(c_entry)
#        #FIXME: may want to make _nvars an attribute instead of using it here
#        return [c_vars[i] for i in range(self.thisptr.GetNVars())]
#
## vars lookup
#cdef extern from "VarsLookup.h":
#    cdef cppclass VarsLookup:
#        VarsLookup(int)
#        double get_value(double *)
#
#cdef class PyVarsLookup:
#    cdef VarsLookup *thisptr
#    def __cinit__(self, int array_index):
#        self.thisptr = new VarsLookup(array_index)
#    def __dealloc__(self):
#        del self.thisptr
#    def get_value(self,vars):
#        cdef int len_vars=len(vars)
#        cdef double * c_vars= <double *>malloc(len_vars * cython.sizeof(double))
#        for i in xrange(len(vars)):
#            c_vars[i]=vars[i]
#        cdef double value 
#        value = self.thisptr.get_value(c_vars)
#        free( c_vars)
#        return value
##
##cdef extern from "GetValueManager.h":
##    cdef cppclass GetValueManager:
##        GetValueManager * GetInstance()
##        void AddVarsLookup(const char*,int)
##
##cdef class PyGetValueManager:
##    cdef GetValueManager * thisptr
##    def __cinit__(self):
##        self.thisptr = thisptr
##        self.thisptr=self.thisptr.GetInstance()
##    def __dealloc__(self):
##        del self.thisptr
##    def add_vars_lookup(self,name,array_id):
##        byte_name=name.encode('UTF-8')
##        cdef const char *c_name = byte_name
##        self.thisptr.AddVarsLookup(byte_name,array_id)
##        
