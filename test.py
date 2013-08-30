#! /usr/bin/env python
#import test_vars_lookup
from ctypes import cdll, c_int, c_double
import MyCythonWrappers
lib=cdll.LoadLibrary('lib/libmylib.so')

int_array=c_int*2
array_ids=int_array(0,1)

lib.add_vars_lookup('name1'.encode('ascii'),5)
lib.add_vars_function('name2'.encode('ascii'),array_ids,2,'average'.encode('ascii'))
lib.add_chi2_calculator('chi2'.encode('ascii'))
lib.add_constraint_to_chi2_calculator('name1'.encode('ascii'),'chi2'.encode('ascii'))
lib.add_constraint_to_chi2_calculator('name2'.encode('ascii'),'chi2'.encode('ascii'))
lib.add_axis('axis1'.encode('ascii'),'name1'.encode('ascii'))
lib.add_axis_with_binning('axis2'.encode('ascii'),'name2'.encode('ascii'),'log'.encode('ascii'),c_double(1.),c_double(1000.),c_int(3))

lib.test()


#my=MyCythonWrappers.PyGetEntry('/vols/cms04/kjd110/budapest_pre_lhc_boxes/cmssm-boxes-combined-pre-lhc.root')
#vars=my.get_vars(0)
#print( vars)
#my=MyCythonWrappers.PyVarsLookup(2)
#print(my.get_value(vars))
