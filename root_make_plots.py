#! /usr/bin/env python
# python modules
import argparse
import json
import pprint
from ctypes import cdll
# private modules
from py_modules.tools import *
import py_modules.CtypesWrappers as cw
# user defined 
import user.mc_old_setup
import user.axes
import user.spaces
import user.vars_lookups
import user.vars_functions
import user.cuts
import user.gauss_constraints
import user.contour_constraints
import user.mneu_mg_m12g_m3g_X2_lookups
import user.constraints_sets
import user.cuts_sets
import user.contours
# shared library objects
runlib=cdll.LoadLibrary('lib/libmylib.so')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rootfiles', help='define input root file',nargs='+')
    parser.add_argument('--files-dir-and-prefix',help='specify directory and prefix',nargs='+')
    parser.add_argument('--outfile',help='output root file')
    parser.add_argument('--nentries', default=-1,help='number of entries to plot',type=int)
    parser.add_argument('--cuts', default='',help='specify from user/cuts_sets.py')
    parser.add_argument('--reference', default='chi2-chi2',
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
    contour_constraints=populate_with_array_ids((user.contour_constraints.get()),style,array_ids_dict)
    mneu_mg_m12g_m3g_X2_lookups=populate_with_array_ids((user.mneu_mg_m12g_m3g_X2_lookups.get()),style,array_ids_dict)
    # pupulate mneu_mg_m12g_m3g_X2_lookups with the lookup data
    mneu_mg_m12g_m3g_X2_lookups=populate_mneu_mg_m12g_m3g_X2_lookups(mneu_mg_m12g_m3g_X2_lookups)
    # populate cuts
    cuts=populate_with_array_ids(user.cuts.get(),style,array_ids_dict)
    # populate contours and add to managers
    contours=populate_contours(user.contours.get())
    add_contours(contours)
    # get axes that are in the spaces
    axes_list=get_axes_list_from_spaces(spaces)
    # for now the "valid" value functions are those for which array_ids are specified
    valid_values_list=list(vars_lookups.keys())+list(vars_functions.keys())+ \
        list(gauss_constraints.keys())+list(contour_constraints.keys())+\
        list(mneu_mg_m12g_m3g_X2_lookups.keys())+[args.reference]
    # populate the valid-and-required-by-spaces axes
    axes=populate_axes(user.axes.get(),valid_values_list,axes_list)
    # now add values to the managers
    add_vars_lookups(vars_lookups) 
    add_vars_functions(vars_functions) 
    add_gauss_constraints(gauss_constraints)
    add_contour_constraints(contour_constraints)
    add_mneu_mg_m12g_m3g_X2_lookups(mneu_mg_m12g_m3g_X2_lookups)
    # add cuts to manager
    add_cuts(cuts) 
    # look for chi2 calculators
    if args.reference in user.constraints_sets.constraints.keys():
        add_chi2_calculator(args.reference,user.constraints_sets.get(args.reference))
    # look for cut sets
    cuts_names=user.cuts_sets.get(args.cuts)
    # axes and spaces to managers
    add_axes(axes)
    pp(spaces)
    add_spaces(spaces)
    # input and output files
    outfile=args.outfile
    if args.rootfiles is not None:
        infiles=args.rootfiles
        if (len(args.rootfiles)==1) and (outfile is None):
            outfile=args.rootfiles[0]
    elif args.files_dir_and_prefix is not None:
        basedirs=args.files_dir_and_prefix[:-1]
        prefix=args.files_dir_and_prefix[-1]
        infiles=[]
        print(basedirs)
        for basedir in basedirs:
            infiles+=get_all_but_the_last_root_files(basedir,prefix)
    #finally make the plots
    cw.make_plots(infiles,outfile,args.nentries,args.dir_in_root,cuts_names)
