#! /usr/bin/env python
import argparse
import json
import sqlite3

import numpy
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sqlite-db',help='')
    return parser.parse_args()


if __name__ == '__main__':
    args=parse_args()
    # mcpp_observabe_ids table
    data=[]
    data+=[('f1','MINPAR','in_M0')]
    data+=[('f2','MINPAR','in_M12')]
    #insert into sqlite db
    conn=sqlite3.connect(args.sqlite_db)
    cur=conn.cursor()
    try:
        cur.execute('create table if not exists mcpp_observable_ids(points_column_name text, key1 text, key2 text)')
        conn.commit()
        cur.executemany('insert into mcpp_observable_ids values(?,?,?)',data)
        conn.commit()
    except sqlite3.Error as e:
        print('ERROR: {}'.format(e.args[0]))
    try:
        cur.execute('create table  if not exists points(collection_rowid integer, f1 real, f2 real)')
        conn.commit()
        data=[(1,v[0],v[1]) for v in 4000*numpy.random.rand(10000,2)]
        cur.executemany('insert into points values(?,?,?)',data)
        conn.commit()
    except sqlite3.Error as e:
        print('ERROR: {}'.format(e.args[0]))
    finally:
        if conn:
            conn.close()

