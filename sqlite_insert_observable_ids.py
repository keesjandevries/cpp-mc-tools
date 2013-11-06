#! /usr/bin/env python
import argparse
import json
import sqlite3

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sqlite-db',help='')
    parser.add_argument('--storage-dict',help='')
    return parser.parse_args()

def parse_json_file(filename):
    with open(filename,'r') as f:
        array_ids_list=json.load(f)
    return [('f{}'.format(array_id+1),oid1,oid2)  for oid1, oid2, array_id in array_ids_list]

if __name__ == '__main__':
    args=parse_args()
    if args.storage_dict is not None:
        #get data from json file
        data=parse_json_file(args.storage_dict)
        #insert into sqlite db
        conn=sqlite3.connect(args.sqlite_db)
        cur=conn.cursor()
        try:
            cur.execute('create table mcpp_observable_ids(points_column_name text, key1 text, key2 text)')
            conn.commit()
            cur.executemany('insert into mcpp_observable_ids values(?,?,?)',data)
            conn.commit()
        except sqlite3.Error as e:
            print('ERROR: {}'.format(e.args[0]))
        finally:
            if conn:
                conn.close()

