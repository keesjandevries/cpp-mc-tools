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
import user.constraints
import user.vars_lookups
import user.vars_functions
# shared library objects
runlib=cdll.LoadLibrary('lib/libmylib.so')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('rootfile', help='define input root file')
    parser.add_argument('--nentries', help='number of entries to plot',type=int)
    parser.add_argument('--mc-old-setup', help='select array indices setup from user/mc_old_setup.py')
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
    spaces=populate_spaces(user.axes.get(),user.spaces.get_spaces(args.spaces))
    # get axes that are in the spaces
    axes_list=get_axes_list_from_spaces(spaces)
    axes=populate_axes(user.axes.get(),axes_list)
    # populate vars_lookups, vars_functions, and constraints with array ids
    constraints=populate_with_array_ids((user.constraints.get_constraints()),style,array_ids_dict)
    vars_lookups={name: {'observable_ids': oids} for name, oids in user.vars_lookups.get().items()}
    vars_lookups=populate_with_array_ids(vars_lookups,style,array_ids_dict)
    vars_functions=populate_with_array_ids(user.vars_functions.get(),style,array_ids_dict)
    #FIXME: this should be replaced by files that get deleted after running plotting from python
    with open(axes_file,'w') as json_file:
        json.dump(axes,json_file,indent=3)
    with open(spaces_file,'w') as json_file:
        json.dump(spaces,json_file,indent=3)
    with open(constraints_file,'w') as json_file:
        json.dump(constraints,json_file,indent=3)
    # making spaces 
    pp.pprint(spaces)
    if args.nentries:
        runlib.run_n(args.rootfile.encode('ascii'),axes_file.encode('ascii'),spaces_file.encode('ascii'),
                constraints_file.encode('ascii'),args.nentries)
    else:
        runlib.run(args.rootfile.encode('ascii'),axes_file.encode('ascii'),spaces_file.encode('ascii'),constraints_file.encode('ascii'))
