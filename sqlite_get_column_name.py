#! /usr/bin/env python
import argparse
import json
import sqlite3
import user.vars_lookups

import numpy
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sqlite-db',help='')
    parser.add_argument('--vars-lookup',help='provide key corresponding to user/vars_lookups.py')
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

if __name__ == '__main__':
    args=parse_args()
    # mcpp_observabe_ids table
    db=args.sqlite_db
    obs_name=args.vars_lookup
    oid_column_dict, style = get_oid_column_dict_and_style(db)
    vars_lookup=user.vars_lookups.get().get(obs_name)
    if vars_lookup is not None:
        oid=vars_lookup[style]
        print('Column name of "{}" in table "points" is : "{}"'.format(obs_name,oid_column_dict.get(oid,'NOT FOUND')))
