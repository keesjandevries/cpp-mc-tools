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
import user.mneu_mg_m12g_m3g_X2_lookups
import user.constraints_sets
import user.contours

# shared library objects
runlib=cdll.LoadLibrary('lib/libmylib.so')

def parse_args():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            fromfile_prefix_chars='@')
    parser.add_argument('--sqlite-db',help='sqlite database')
    parser.add_argument('--outfile',help='output root file')
    parser.add_argument('--reference', default='chi2-chi2',
        help='Usually chi-functions, but in general the function that is mimimised to project the spaces')
    parser.add_argument('--spaces', help='select plots from user/spaces.py')
    parser.add_argument('--sql-where',help='provide the "where-part" of the sql statement')
    parser.add_argument('--reduced-db',action='store_true',
            help='Select if file was produced with sqlite_reduce_db.py. This is needed for the preparation of the sql query')
    return parser.parse_args()

def get_oid_column_dict_and_style(db):
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
    
def get_array_ids_dict(value_names,value_dict_list,style):
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
    array_ids_dict=OrderedDict([(key,'a') for key in oids_list])
    for array_id, oid in enumerate(array_ids_dict.keys()):
        array_ids_dict[oid]=array_id
    return array_ids_dict
        
if __name__ == '__main__':
    args=parse_args()
    db=args.sqlite_db
    # get array ids
    oid_column_dict, style=get_oid_column_dict_and_style(db)
    # get spaces for which axis names are defined spaces
    spaces=prepare_spaces(user.spaces.get_spaces(args.spaces),args.reference)
    axes=prepare_axes(user.axes.get(),spaces)
    values=[axis['value'] for axis in axes.values()]
    if  args.reference == 'chi2-chi2':
        values+=['chi2-chi2']
    else:
        values+=user.constraints_sets.get(args.reference)
    # populate vars_lookups, vars_functions, and gauss_constraints with array ids
    vars_lookups={name: {'observable_ids': oids} for name, oids in user.vars_lookups.get().items()}
    vars_functions=user.vars_functions.get()
    gauss_constraints=user.gauss_constraints.get()
    contour_constraints=user.contour_constraints.get()
    mneu_mg_m12g_m3g_X2_lookups=user.mneu_mg_m12g_m3g_X2_lookups.get()
    # get all possible values
    value_dict_list=[vars_lookups,vars_functions,gauss_constraints,contour_constraints,mneu_mg_m12g_m3g_X2_lookups]
    array_ids_dict=get_array_ids_dict(values,value_dict_list,style) 
    # prepare select statement
    if not args.reduced_db:
        first_two_columns=['rowid','collections_rowid']
    else:
        first_two_columns=['points_rowid','rowid']
    columns=','.join(first_two_columns+[ oid_column_dict[oid] for oid in array_ids_dict.keys()])
    sql_where=''
    if args.sql_where is not None:
        sql_where='where ' + args.sql_where
    sql_selection='select  {} from points {};'.format(columns,sql_where)
    print('the sql query is:\n{}'.format(sql_selection))
    # get unique items in the list ordered
    vars_lookups=tools.populate_with_array_ids(vars_lookups,style,array_ids_dict)
    vars_functions=tools.populate_with_array_ids(vars_functions,style,array_ids_dict)
    gauss_constraints=tools.populate_with_array_ids(gauss_constraints,style,array_ids_dict)
    contour_constraints=tools.populate_with_array_ids(contour_constraints,style,array_ids_dict)
    mneu_mg_m12g_m3g_X2_lookups=tools.populate_with_array_ids(mneu_mg_m12g_m3g_X2_lookups,style,array_ids_dict)
    # pupulate mneu_mg_m12g_m3g_X2_lookups with the lookup data
    mneu_mg_m12g_m3g_X2_lookups=tools.populate_mneu_mg_m12g_m3g_X2_lookups(mneu_mg_m12g_m3g_X2_lookups)
    # populate contours and add to managers
    contours=tools.populate_contours(user.contours.get())
    tools.add_contours(contours)
    # now add values to the managers
    tools.add_vars_lookups(vars_lookups) 
    tools.add_vars_functions(vars_functions) 
    tools.add_gauss_constraints(gauss_constraints)
    tools.add_contour_constraints(contour_constraints)
    tools.add_mneu_mg_m12g_m3g_X2_lookups(mneu_mg_m12g_m3g_X2_lookups)
    # look for chi2 calculators
    if args.reference in user.constraints_sets.constraints.keys():
        tools.add_chi2_calculator(args.reference,user.constraints_sets.get(args.reference))
    # axes and spaces to managers
    tools.add_axes(axes)
    tools.pp(spaces)
    tools.add_spaces(spaces)
    # input and output files
    outfile=args.outfile
    #finally make the plots
    cw.sqlite_make_plots(args.sqlite_db,sql_selection,outfile,args.reference)
