#! /usr/bin/env python
# python modules
import argparse
import sqlite3
# private modules
import py_modules.tools as tools
import py_modules.CtypesWrappers as cw
# user defined 
import user.gauss_constraints
import user.contour_constraints
import user.contours
import user.constraints_sets

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db-in',help='sqlite database')
    parser.add_argument('--db-out',help='sqlite database')
    parser.add_argument('--reference', required=True,
        help='Usually chi-functions, but in general the function that is mimimised to project the spaces')
    parser.add_argument('--max-chi2',type=float,default=100)
    parser.add_argument('--sql-where')
    return parser.parse_args()

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

def create_mcpp_observable_ids(db_in,db_out):
    conn_in=sqlite3.connect(db_in)
    conn_out=sqlite3.connect(db_out)
    cur_in=conn_in.cursor()
    cur_out=conn_out.cursor()
    cur_out.execute('create table if not exists mcpp_observable_ids(points_column_name text, key1 text, key2 text)')
    conn_out.commit()
    cur_out.execute('select * from mcpp_observable_ids;')
    if len(cur_out.fetchall())==0:
        cur_in.execute('select * from mcpp_observable_ids;')
        for row in cur_in.fetchall():
            cur_out.execute('insert into mcpp_observable_ids values(?,?,?)',row)
        conn_out.commit()
    conn_in.close() 
    conn_out.close() 


if __name__ == '__main__':
    #get arguments
    args=parse_args()
    input_name=args.db_in
    output_name=args.db_out
    max_chi2=args.max_chi2
    chi2_function_name=args.reference
    # create mcpp_observable_ids in new database
    create_mcpp_observable_ids(input_name,output_name)
    # get array ids
    array_ids_dict, style=get_array_ids_and_style(input_name)
    # populate vars_lookups, vars_functions, and gauss_constraints with array ids
    gauss_constraints=tools.populate_with_array_ids((user.gauss_constraints.get()),style,array_ids_dict)
    contour_constraints=tools.populate_with_array_ids((user.contour_constraints.get()),style,array_ids_dict)
    # populate contours and add to managers
    contours=tools.populate_contours(user.contours.get())
    tools.add_contours(contours)
    # now add values to the managers
    tools.add_gauss_constraints(gauss_constraints)
    tools.add_contour_constraints(contour_constraints)
    # look for chi2 calculators
    if args.reference in user.constraints_sets.constraints.keys():
        tools.add_chi2_calculator(args.reference,user.constraints_sets.get(args.reference))
    # make selection query
    sql_where=''
    if args.sql_where is not None:
        sql_where='where ' + args.sql_where
    select_query='select rowid, * from points {};'.format(sql_where)
    #finally make the plots
    cw.sqlite_reduce_db(input_name,output_name,select_query,chi2_function_name,max_chi2)
