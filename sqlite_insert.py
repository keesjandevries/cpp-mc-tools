#! /usr/bin/env python
import os
import argparse
import sqlite3
from py_modules.CtypesWrappers import insert_root_into_sqlite 
from py_modules.tools import get_all_but_the_last_root_files

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rootfiles',nargs='+',help='')
    parser.add_argument('--sqlite-db',help='')
    parser.add_argument('--files-dir-and-prefix',help='specify directories and prefix. The last file in each directory is omitted',nargs='+')
    return parser.parse_args()


def get_inserted_files(db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("create table if not exists inserted_files(path text);")
    conn.commit()
    cur.execute("select path from inserted_files;")
    inserted_files=[]
    for row in cur.fetchall():
        inserted_files.append(row[0])
    conn.close()
    return inserted_files

#FIXME: in later collections will contain more columns
def get_collection_rowid(db,filename):
    directory, _ = os.path.split(filename)
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("create table if not exists collections(directory text);")
    conn.commit()
    cur.execute("select rowid from collections where directory=?",(directory,))
    row=cur.fetchone()
    if row is None:
        cur.execute("insert into collections values(?)",(directory,))
        conn.commit()
        cur.execute("select rowid from collections where directory=?",(directory,))
        row=cur.fetchone()
    conn.close()
    return row[0]

if __name__ == '__main__':
    args=parse_args()
    db=args.sqlite_db
    inserted_files=get_inserted_files(db)

    #specific root files are given
    if args.rootfiles is not None:
        rootfiles=args.rootfiles
    elif args.files_dir_and_prefix is not None:
        basedirs=args.files_dir_and_prefix[:-1]
        prefix=args.files_dir_and_prefix[-1]
        rootfiles=[]
        print(basedirs)
        for basedir in basedirs:
            rootfiles+=get_all_but_the_last_root_files(basedir,prefix)

    conn=sqlite3.connect(db)
    cur=conn.cursor()
    #loop over root files
    for rootfile in rootfiles:
        if not rootfile in inserted_files:
            collection_rowid=get_collection_rowid(db,rootfile)
            insert_root_into_sqlite(rootfile,args.sqlite_db,collection_rowid)
            cur.execute("insert into inserted_files values(?)",(rootfile,))
            conn.commit()
    conn.close()
