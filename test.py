#! /usr/bin/env python
#import test_vars_lookup
from ctypes import cdll, c_int
#import MyCythonWrappers
lib=cdll.LoadLibrary('lib/libmylib.so')

int_array=c_int*2
array_ids=int_array(0,1)

lib.add_vars_lookup('name'.encode('ascii'),5)
lib.add_vars_function('name1'.encode('ascii'),array_ids,2,'average'.encode('ascii'))

lib.test('name'.encode('ascii'))


#my=MyCythonWrappers.PyGetEntry('/vols/cms04/kjd110/budapest_pre_lhc_boxes/cmssm-boxes-combined-pre-lhc.root')
#vars=my.get_vars(0)
#print( vars)
#my=MyCythonWrappers.PyVarsLookup(2)
#print(my.get_value(vars))
