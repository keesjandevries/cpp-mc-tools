#! /usr/bin/env python
# python modules
import argparse
import json
import pprint
from ctypes import cdll
# private modules
from py_modules.tools import *
# user defined 
import user.mc_old_setup
import user.axes
import user.spaces
import user.gauss_constraints
import user.vars_lookups
import user.vars_functions
# shared library objects
runlib=cdll.LoadLibrary('lib/libmylib.so')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('rootfile', help='define input root file')
    parser.add_argument('--nentries', default=-1,help='number of entries to plot',type=int)
    parser.add_argument('--reference', default='chi2',
        help='Usually chi-functions, but in general the function that is mimimised to project the spaces')
    parser.add_argument('--mc-old-setup', help='select array indices setup from user/mc_old_setup.py')
    parser.add_argument('--dir-in-root', default='',
            help='choose directory in which the plots are stored within the root file')
    parser.add_argument('--storage-dict', help='specify json file containing a list [(oid1,oid2,array_id), ... ]')
    parser.add_argument('--spaces', help='select plots from user/spaces.py')
    return parser.parse_args()

if __name__ == '__main__':
    args=parse_args()
    if args.mc_old_setup:
        array_ids_dict=get_mc_old_array_ids_dict(user.mc_old_setup.get(args.mc_old_setup))
        style='mc_old'
    elif args.storage_dict:
        array_ids_dict=array_ids_dict_from_json_file(args.storage_dict)
        style='mcpp'
    # get spaces for which axis names are defined spaces
    spaces=populate_spaces(user.axes.get(),user.spaces.get_spaces(args.spaces),args.reference)
    # populate vars_lookups, vars_functions, and gauss_constraints with array ids
    vars_lookups={name: {'observable_ids': oids} for name, oids in user.vars_lookups.get().items()}
    vars_lookups=populate_with_array_ids(vars_lookups,style,array_ids_dict)
    vars_functions=populate_with_array_ids(user.vars_functions.get(),style,array_ids_dict)
    gauss_constraints=populate_with_array_ids((user.gauss_constraints.get()),style,array_ids_dict)
    # get axes that are in the spaces
    axes_list=get_axes_list_from_spaces(spaces)
    # for now the "valid" value functions are those for which array_ids are specified
    valid_values_list=list(gauss_constraints.keys())+list(vars_lookups.keys())+list(vars_functions.keys())
    # populate the valid-and-required-by-spaces axes
    axes=populate_axes(user.axes.get(),valid_values_list,axes_list)
    # now add values to the managers
    add_vars_lookups(vars_lookups) 
    add_vars_functions(vars_functions) 
    add_gauss_constraints(gauss_constraints)
    # axes and spaces to managers
    add_axes(axes)
    pp(spaces)
    add_spaces(spaces)
    #finally make the plots
    runlib.make_plots_in_directory(args.rootfile.encode('ascii'),args.nentries,args.dir_in_root.encode('ascii'))
