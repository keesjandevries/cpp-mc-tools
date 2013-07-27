#! /usr/bin/env python
#import test_vars_lookup
from ctypes import cdll
#import MyCythonWrappers
lib=cdll.LoadLibrary('lib/libmylib.so')

lib.add_vars_lookup('name'.encode('ascii'),5)
lib.test('name'.encode('ascii'))


#my=MyCythonWrappers.PyGetEntry('/vols/cms04/kjd110/budapest_pre_lhc_boxes/cmssm-boxes-combined-pre-lhc.root')
#vars=my.get_vars(0)
#print( vars)
#my=MyCythonWrappers.PyVarsLookup(2)
#print(my.get_value(vars))
