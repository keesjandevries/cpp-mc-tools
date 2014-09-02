#! /usr/bin/env python
#import test_vars_lookup
#from ctypes import cdll, c_int, c_double, c_char_p
from MyCythonWrappers import PyTFile
#import py_modules.CtypesWrappers as cw
#lib=cdll.LoadLibrary('lib/libmylib.so')

#int_array=c_int*2
#array_ids=int_array(0,1)

#lib.add_vars_lookup('name1'.encode('ascii'),5)
#lib.add_vars_function('name2'.encode('ascii'),array_ids,2,'average'.encode('ascii'))
#lib.add_chi2_calculator('chi2'.encode('ascii'))
#lib.add_constraint_to_chi2_calculator('name1'.encode('ascii'),'chi2'.encode('ascii'))
#lib.add_constraint_to_chi2_calculator('name2'.encode('ascii'),'chi2'.encode('ascii'))
#lib.add_axis('axis1'.encode('ascii'),'name1'.encode('ascii'))
#lib.add_axis_with_binning('axis2'.encode('ascii'),'name2'.encode('ascii'),'log'.encode('ascii'),c_double(1.),c_double(1000.),c_int(3))
#lib.add_axis_with_binning('axis3'.encode('ascii'),'name1'.encode('ascii'),'linear'.encode('ascii'),c_double(0.),c_double(100.),c_int(5))
#lib.test()
#cw.add_vars_lookup('chi2',0)
#cw.add_vars_lookup('lm0',2)
#cw.add_vars_lookup('lm12',1)
#cw.add_axis_with_binning('m0','lm0','linear',0.,4000.,100)
#cw.add_axis_with_binning('m12','lm12','linear',0.,4000.,100)
#cw.add_space(['m0','m12'],[],'chi2')
#lib.make_plots_in_directory('/vols/cms04/kjd110/cmssm_mc9_nuisance/cmssm_mc9_nuisance.root'.encode('ascii'),10,'hans'.encode('ascii'))
##lib.test()


#my=MyCythonWrappers.PyGetEntry('/vols/cms04/kjd110/budapest_pre_lhc_boxes/cmssm-boxes-combined-pre-lhc.root')
#vars=my.get_vars(0)
#print( vars)
#my=MyCythonWrappers.PyVarsLookup(2)
#print(my.get_value(vars))
def get_th1d():
    tfile = PyTFile('pmssm10_140826_mc10_lhc7.root')
    return tfile.get_th1d('g-2_chi2')
th1d = get_th1d()
print(th1d.get_bin_content(50))

