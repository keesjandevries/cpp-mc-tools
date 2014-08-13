#! /usr/bin/env python
#python modules
import argparse
import sqlite3
#own modules
#import test_vars_lookup
#import MyCythonWrappers as cyw
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
import user.mneu_mg_m12g_m3g_X2_lookups
import user.constraints_sets
import user.contours
import user.inputs
import user.array
import user.parameters
import user.observables

def get_parser():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            fromfile_prefix_chars='@')
    parser.add_argument('--sqlite-db', help='define input root file')
    parser.add_argument('--rowid',type=int,help='rowid of point')
    parser.add_argument('--database-info', action='store_true',help='specify inputs as defined in user/inputs.py')
    parser.add_argument('--mc9-table1-data', action='store_true',help='print data from table 1 in mc9')
    parser.add_argument('--pvalue', action='store_true')
    parser.add_argument('--inputs', help='specify inputs as defined in user/inputs.py')
    parser.add_argument('--array', help='specify array as defined in user/array.py')
    parser.add_argument('--parameters', help='specify parameters as defined in user/parameters.py')
    parser.add_argument('--observables', help='specify observables as defined in user/observables.py')
    parser.add_argument('--breakdown', help='specify chi2 breakdown according to user/constratins_sets.py')
    parser.add_argument('--ndigits', help='number of digits for floats',type=int,default=2)
    return parser

def get_array_ids_and_style(db):
    #FIXME: also include mc_old 
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    array_ids_dict={}
    cur.execute('select * from mcpp_observable_ids;')
    for row in cur.fetchall():
        coln,key1,key2=row
        array_id=int(coln.replace('f',''))-1
        array_ids_dict[(key1,key2)]=array_id
    conn.close()
    return array_ids_dict,'mcpp'

def get_vars_from_db(db,rowid):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute('select * from points where rowid=?',(rowid,))
    row=cur.fetchone()
    if row is not None:
        collection_rowid=row[0]
        vars=row[1:]
        conn.close()
        return vars,collection_rowid
    else:
        return None

def main(args):
    db=args.sqlite_db
    #establish lookup
    array_ids_dict, style=get_array_ids_and_style(db)
    vars,collection_rowid=get_vars_from_db(db,args.rowid)
    # populate values as usual previously
    # populate vars_lookups, vars_functions, and gauss_constraints with array ids
    vars_lookups={name: {'observable_ids': oids} for name, oids in user.vars_lookups.get().items()}
    vars_lookups=populate_with_array_ids(vars_lookups,style,array_ids_dict)
    vars_functions=populate_with_array_ids(user.vars_functions.get(),style,array_ids_dict)
    gauss_constraints=populate_with_array_ids((user.gauss_constraints.get()),style,array_ids_dict)
    contour_constraints=populate_with_array_ids((user.contour_constraints.get()),style,array_ids_dict)
    mneu_mg_m12g_m3g_X2_lookups=populate_with_array_ids((user.mneu_mg_m12g_m3g_X2_lookups.get()),style,array_ids_dict)
    # pupulate mneu_mg_m12g_m3g_X2_lookups with the lookup data
    mneu_mg_m12g_m3g_X2_lookups=populate_mneu_mg_m12g_m3g_X2_lookups(mneu_mg_m12g_m3g_X2_lookups)
    # populate contours and add to managers
    contours=populate_contours(user.contours.get())
    add_contours(contours)
    # now add values to the managers
    add_vars_lookups(vars_lookups) 
    add_vars_functions(vars_functions) 
    add_gauss_constraints(gauss_constraints)
    add_contour_constraints(contour_constraints)
    add_mneu_mg_m12g_m3g_X2_lookups(mneu_mg_m12g_m3g_X2_lookups)
    #
    format='{:<30}: {:30}'
    number_format='{:<30}: {:<5.'+str(args.ndigits)+'f}'
    float_format='{:<30}: {:<5.3e}'
    if args.database_info:
        print('='*50)
        print(format.format('Data base info',''))
        print('='*50)
        print(format.format('Rowid',str(args.rowid)))
        print(format.format('Database',db))
        print(format.format('Collection rowid',str(collection_rowid)))
    if args.parameters:
        parameters=user.parameters.get(args.parameters)
        print('='*50)
        print(format.format('parameters','value'))
        print('='*50)
        for parameter in parameters:
            value=ctw.get_value(parameter,vars)
            print(number_format.format(parameter,value))
    if args.observables:
        observables=user.observables.get(args.observables)
        print('='*50)
        print(format.format('observables','value'))
        print('='*50)
        for observable in observables:
            value=ctw.get_value(observable,vars)
            if not ('ssi' in observable) and not ('bsmm' in observable) \
                and not (observable=='g-2'):
                print(number_format.format(observable,value))
            else:
                print(float_format.format(observable,value))

    if args.breakdown:
        # look for chi2 calculators
        constraints=user.constraints_sets.get(args.breakdown)
        add_chi2_calculator(args.breakdown,constraints)
        print('='*50)
        print(format.format('constraint','chi2'))
        print('='*50)
        nmeas=0
        for constraint in constraints:
            chi2=ctw.get_value(constraint,vars)
            if chi2 > 0:
                nmeas+=1
            constraint=constraint.replace('chi2-','')
            print(number_format.format(constraint,chi2))
        print('='*50)
        print(number_format.format('total',ctw.get_value(args.breakdown,vars)))
        print(number_format.format('nmeas',nmeas))
        print('='*50)
        if args.mc9_table1_data and args.parameters is not None:
            print(format.format('table data',''))
            print('='*50)
            m0=int(round(ctw.get_value('m0',vars),-1))
            m12=int(round(ctw.get_value('m12',vars),-1))
            A0=int(round(-ctw.get_value('A0',vars),-1))
            tanb=int(round(ctw.get_value('tanb',vars),0))
            chi2=round(ctw.get_value(args.breakdown,vars),1)
            nparameters=len(user.inputs.get(args.inputs))
            ndof=nmeas-nparameters
            cl=round(ctw.chi2_ndof_to_cl(chi2,ndof)*100,1)
            print('{}/{} & {}\% &{} &{} & {} & {}\\\\'.format(chi2,ndof,cl,m0,m12,A0,tanb))
        if args.pvalue and args.parameters is not None:
            print(format.format('table data',''))
            print('='*50)
            chi2=round(ctw.get_value(args.breakdown,vars),1)
            nparameters=len(user.inputs.get(args.inputs))
            ndof=nmeas-nparameters
            cl=round(ctw.chi2_ndof_to_cl(chi2,ndof)*100,1)
            print('{}/{}:  {}%'.format(chi2,ndof,cl))
#    if args.inputs is not None and args.parameters is not None:
    if args.inputs is not None :
        inputs=user.inputs.get(args.inputs)
        values=[str(ctw.get_value(parameter,vars)) for parameter in inputs]
        print('='*50)
        print(format.format('Input to run point',''))
        print('='*50)
        print(' '.join(values))
    if args.array is not None :
        array=user.array.get(args.array)
        values=[str(ctw.get_value(element,vars)) for element in array]
        print(' '.join(values))

if __name__=='__main__':
    args=get_parser().parse_args()
    main(args)
