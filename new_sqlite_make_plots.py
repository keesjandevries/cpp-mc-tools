#! /usr/bin/env python
# python modules
import argparse
import sqlite3
from collections import OrderedDict
from ctypes import cdll
# private modules
import py_modules.tools as tools
import py_modules.CtypesWrappers as cw
# user defined 
import user.axes
import user.spaces
import user.vars_lookups
import user.vars_functions
import user.gauss_constraints
import user.contour_constraints
import user.constraints_sets
import user.contours
# shared library objects
runlib=cdll.LoadLibrary('lib/libmylib.so')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sqlite-db',help='sqlite database')
    parser.add_argument('--outfile',help='output root file')
    parser.add_argument('--reference', default='chi2-chi2',
        help='Usually chi-functions, but in general the function that is mimimised to project the spaces')
    parser.add_argument('--spaces', help='select plots from user/spaces.py')
    return parser.parse_args()

#def get_array_ids_and_style(db):
#    #FIXME: also include mc_old 
#    conn=sqlite3.connect(db)
#    cur=conn.cursor()
#    array_ids_dict={}
#    cur.execute('select * from mcpp_observable_ids;')
#    for row in cur.fetchall():
#        coln,key1,key2=row
#        array_id=int(coln.replace('f',''))-1
#        array_ids_dict[(key1,key2)]=array_id
#    conn.close()
#    return array_ids_dict,'mcpp'
def get_oid_column_dict_and_style():
    #FIXME: also include mc_old 
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    oid_column_dict={}
    cur.execute('select * from mcpp_observable_ids;')
    for row in cur.fetchall():
        coln,key1,key2=row
        oid_column_dict[(key1,key2)]=coln
    conn.close()
    return oid_column_dict,'mcpp'


def prepare_spaces(spaces,reference):
    #transform e.g. {'axes':'mh'} into {'axes':['mh']} and add reference
    for space in spaces:
        #handle axes
        try:
            axes=space['axes']
            if not isinstance(axes,list):
                axes=[axes]
            space.update({'axes':axes})
        except KeyError:
            print('ERROR: one of the spaces in does not have \'axes\'\nEXITING')
            exit(1)
        #handle zaxes
        zaxes=space.get('zaxes')
        if zaxes is not None:
            if not isinstance(zaxes,list):
                zaxes=[zaxes]
            space.update({'zaxes':zaxes})
        space['reference_value']=reference
    return spaces

def prepare_axes(axes,spaces):
    axes_names=[]
    for space in spaces:
        axes_names+=space['axes']+space.get('zaxes',[])
    return {name:axes[name] for name in axes_names}

#def get_values_list(axes):
#    return [axis['value'] for axis in axes.values()]
def recursively_get_oids(in_dict, style):
    if 'observable_ids' in in_dict.keys():
        return in_dict['observable_ids'][style]
    else:
        for key, val in in_dict.items():
            if isinstance(val,dict):
                oids=recursively_get_oids(val,style)
                if oids is None:
                   continue
            else:
                oids=None
                continue
        return oids
    
def get_oids_list(value_names,value_dict_list,style):
    value_dict={}
    oids_list=[]
    for d in value_dict_list:
        value_dict.update(d)
    for value_name in value_names:
        details=value_dict[value_name]
        oids=recursively_get_oids(details,style)
        if not isinstance(oids,list):
            oids=[oids]
        oids_list+=oids
    return oids_list

if __name__ == '__main__':
    args=parse_args()
    # get array ids
#    array_ids_dict, style=get_array_ids_and_style(args.sqlite_db)
    # get spaces for which axis names are defined spaces
    spaces=prepare_spaces(user.spaces.get_spaces(args.spaces),args.reference)
    axes=prepare_axes(user.axes.get(),spaces)
    values=[axis['value'] for axis in axes.values()]
    values+=user.constraints_sets.get(args.reference)
    # populate vars_lookups, vars_functions, and gauss_constraints with array ids
    vars_lookups={name: {'observable_ids': oids} for name, oids in user.vars_lookups.get().items()}
    vars_functions=user.vars_functions.get()
    gauss_constraints=user.gauss_constraints.get()
    contour_constraints=user.contour_constraints.get()
    # get all possible values
    value_dict_list=[vars_lookups,vars_functions,gauss_constraints,contour_constraints]
    oids_list=get_oids_list(values,value_dict_list,'mcpp') 
    # get unique items in the list ordered
    oids_list=list(OrderedDict([(key,'a') for key in oids_list]).keys())
#    vars_lookups=populate_with_array_ids(vars_lookups,style,array_ids_dict)
#    vars_functions=populate_with_array_ids(user.vars_functions.get(),style,array_ids_dict)
#    gauss_constraints=populate_with_array_ids((user.gauss_constraints.get()),style,array_ids_dict)
#    contour_constraints=populate_with_array_ids((user.contour_constraints.get()),style,array_ids_dict)
#    # populate contours and add to managers
#    contours=populate_contours(user.contours.get())
#    add_contours(contours)
#    # get axes that are in the spaces
#    axes_list=get_axes_list_from_spaces(spaces)
#    # for now the "valid" value functions are those for which array_ids are specified
#    valid_values_list=list(vars_lookups.keys())+list(vars_functions.keys())+ \
#        list(gauss_constraints.keys())+list(contour_constraints.keys())+\
#        [args.reference]
#    # populate the valid-and-required-by-spaces axes
#    axes=populate_axes(user.axes.get(),valid_values_list,axes_list)
#    # now add values to the managers
#    add_vars_lookups(vars_lookups) 
#    add_vars_functions(vars_functions) 
#    add_gauss_constraints(gauss_constraints)
#    add_contour_constraints(contour_constraints)
#    # look for chi2 calculators
#    if args.reference in user.constraints_sets.constraints.keys():
#        add_chi2_calculator(args.reference,user.constraints_sets.get(args.reference))
#    # axes and spaces to managers
#    add_axes(axes)
#    pp(spaces)
#    add_spaces(spaces)
#    # input and output files
#    outfile=args.outfile
#    #finally make the plots
#    cw.sqlite_make_plots(args.sqlite_db,'select * from points;',outfile)
