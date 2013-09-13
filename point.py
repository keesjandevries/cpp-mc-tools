#! /usr/bin/env python
#python modules
import argparse
#own modules
#import test_vars_lookup
import MyCythonWrappers as cyw
import py_modules.CtypesWrappers as ctw
import py_modules.oldarrayindices 
from py_modules.tools import *
#user options
import user.mc_old_setup
import user.axes
import user.spaces
import user.vars_lookups
import user.vars_functions
import user.gauss_constraints
import user.contour_constraints
import user.constraints_sets
import user.contours
import user.parameters

#NOTE: this is a rather serious attempt to create a very useful tool
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('rootfile', help='define input root file')
    parser.add_argument('-n','--entry',type=int,help='entry number in the root file')
    parser.add_argument('-v','--verbose',nargs='+',default=[],help='entry number in the root file')
    parser.add_argument('--mc-old-setup', help='select array indices setup from user/mc_old_setup.py')
    parser.add_argument('--storage-dict', help='specify json file containing a list [(oid1,oid2,array_id), ... ]')
    parser.add_argument('--parameters', help='specify parameters as defined in user/parameters.py')
    parser.add_argument('--breakdown', help='specify chi2 breakdown according to user/constratins_sets.py')
    return parser.parse_args()

if __name__=='__main__':
    args=parse_args()
    #FIXME: better name for object
    object=cyw.PyGetEntry(args.rootfile)
    if args.entry is not None:
        vars=object.get_vars(args.entry)
    else:
        print('ERROR: this is actually fine for now')
    #establish lookup
    if args.mc_old_setup:
        array_ids_dict=get_mc_old_array_ids_dict(user.mc_old_setup.get(args.mc_old_setup))
        style='mc_old'
    elif args.storage_dict:
        array_ids_dict=array_ids_dict_from_json_file(args.storage_dict)
        style='mcpp'
    # populate vars_lookups, vars_functions, and gauss_constraints with array ids
    vars_lookups={name: {'observable_ids': oids} for name, oids in user.vars_lookups.get().items()}
    vars_lookups=populate_with_array_ids(vars_lookups,style,array_ids_dict)
    vars_functions=populate_with_array_ids(user.vars_functions.get(),style,array_ids_dict)
    gauss_constraints=populate_with_array_ids((user.gauss_constraints.get()),style,array_ids_dict)
    contour_constraints=populate_with_array_ids((user.contour_constraints.get()),style,array_ids_dict)
    # populate contours and add to managers
    contours=populate_contours(user.contours.get())
    add_contours(contours)
    # now add values to the managers
    add_vars_lookups(vars_lookups) 
    add_vars_functions(vars_functions) 
    add_gauss_constraints(gauss_constraints)
    add_contour_constraints(contour_constraints)
    if args.breakdown:
        # look for chi2 calculators
        constraints=user.constraints_sets.get(args.breakdown)
        add_chi2_calculator(args.breakdown,constraints)
        format='{:<30}: {}'
        print(format.format('constraint','chi2'))
        for constraint in constraints:
            chi2=ctw.get_value(constraint,vars)
            constraint=constraint.replace('chi2-','')
            print(format.format(constraint,chi2))
        print(format.format('total',ctw.get_value(args.breakdown,vars)))
    if args.parameters:
        parameters=user.parameters.get(args.parameters)
        values=[str(ctw.get_value(parameter,vars)) for parameter in parameters]
        print(' '.join(values))

