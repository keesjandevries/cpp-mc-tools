#! /usr/bin/env python
import test_vars_lookup
import test_get_entry

my=test_get_entry.PyGetEntry('/vols/cms04/kjd110/budapest_pre_lhc_boxes/cmssm-boxes-combined-pre-lhc.root')
print( my.get_vars(0))
#my=test_vars_lookup.PyVarsLookup(2)
#print(my.get_value([1,2,3,4,5]))
