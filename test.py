#! /usr/bin/env python
#import test_vars_lookup
import MyCythonWrappers

my=MyCythonWrappers.PyGetEntry('/vols/cms04/kjd110/budapest_pre_lhc_boxes/cmssm-boxes-combined-pre-lhc.root')
vars=my.get_vars(0)
print( vars)
my=MyCythonWrappers.PyVarsLookup(2)
print(my.get_value(vars))
