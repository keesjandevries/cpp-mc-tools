#! /usr/bin/env python
#import test_vars_lookup
from ctypes import cdll, c_int, c_double, c_char_p
import MyCythonWrappers
lib=cdll.LoadLibrary('lib/libmylib.so')

int_array=c_int*2
array_ids=int_array(0,1)

#lib.add_vars_lookup('name1'.encode('ascii'),5)
#lib.add_vars_function('name2'.encode('ascii'),array_ids,2,'average'.encode('ascii'))
#lib.add_chi2_calculator('chi2'.encode('ascii'))
#lib.add_constraint_to_chi2_calculator('name1'.encode('ascii'),'chi2'.encode('ascii'))
#lib.add_constraint_to_chi2_calculator('name2'.encode('ascii'),'chi2'.encode('ascii'))
#lib.add_axis('axis1'.encode('ascii'),'name1'.encode('ascii'))
#lib.add_axis_with_binning('axis2'.encode('ascii'),'name2'.encode('ascii'),'log'.encode('ascii'),c_double(1.),c_double(1000.),c_int(3))
#lib.add_axis_with_binning('axis3'.encode('ascii'),'name1'.encode('ascii'),'linear'.encode('ascii'),c_double(0.),c_double(100.),c_int(5))
def add_vars_lookup(name,array_id):
    lib.add_vars_lookup(name.encode('ascii'),array_id)

def add_axis(axis_name,value_function_name):
    c_axis_name=axis_name.encode('ascii')
    c_value_function_name=value_function_name.encode('ascii')
    lib.add_axis(c_axis_name,c_value_function_name)

def add_axis_with_binning(axis_name,value_function_name,binning_type,low,high,nbins):
    c_axis_name=axis_name.encode('ascii')
    c_value_function_name=value_function_name.encode('ascii')
    c_binning_type=binning_type.encode('ascii')
    c_low=c_double(low)
    c_high=c_double(high)
    lib.add_axis_with_binning(c_axis_name,c_value_function_name,c_binning_type,c_low,c_high,nbins)

def add_space(axes_names,zaxes_names,reference_function):
    #make appropriate ctypes
    axes_strings=c_char_p*len(axes_names)
    zaxes_strings=c_char_p*len(zaxes_names)
    c_reference_function=reference_function.encode('ascii')
    #fill them
    c_axes_names=axes_strings(*[name.encode('ascii') for name in axes_names])
    c_zaxes_names=zaxes_strings(*[name.encode('ascii') for name in zaxes_names])
    #add space
    lib.add_space(c_axes_names,len(axes_names),c_zaxes_names,len(zaxes_names),c_reference_function)

add_vars_lookup('chi2',0)
add_vars_lookup('lm0',2)
add_vars_lookup('lm12',1)
add_axis_with_binning('m0','lm0','linear',0.,4000.,100)
add_axis_with_binning('m12','lm12','linear',0.,4000.,100)
add_space(['m0','m12'],[],'chi2')
lib.make_plots('/vols/cms04/kjd110/cmssm_mc9_nuisance/cmssm_mc9_nuisance.root'.encode('ascii'),-1)
#lib.test()


#my=MyCythonWrappers.PyGetEntry('/vols/cms04/kjd110/budapest_pre_lhc_boxes/cmssm-boxes-combined-pre-lhc.root')
#vars=my.get_vars(0)
#print( vars)
#my=MyCythonWrappers.PyVarsLookup(2)
#print(my.get_value(vars))
