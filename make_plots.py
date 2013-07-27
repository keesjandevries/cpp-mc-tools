#! /usr/bin/env python
# python modules
import argparse, json, pprint
from ctypes import cdll
from py_modules.tools import *
# user defined 
import user.axes
import user.spaces
import user.files
import user.file_properties
import user.constraints
# shared library objects
runlib=cdll.LoadLibrary('lib/libmylib.so')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('rootfile', help='define input root file')
    parser.add_argument('--file-setup', help='array indices setup')
    parser.add_argument('--nentries', help='number of entries to plot',type=int)
    return parser.parse_args()

if __name__ == '__main__':
    args=parse_args()
    if args.file_setup:
        file_info=get_file_info(args.file_setup,user.file_properties.get_file_properties())
    else:
        file_info=get_file_info(args.rootfile,user.files.get_files())
    array_ids_dict,style=get_array_ids_dict_style(file_info)
    axes=populate_axes(style,array_ids_dict,user.axes.get_axes())
    spaces=populate_spaces(axes,user.spaces.get_spaces())
    constraints=populate_constraints(style,array_ids_dict,user.constraints.get_constraints())
    #FIXME: this should be replaced by files that get deleted after running plotting from python
    with open(axes_file,'w') as json_file:
        json.dump(axes,json_file,indent=3)
    with open(spaces_file,'w') as json_file:
        json.dump(spaces,json_file,indent=3)
    with open(constraints_file,'w') as json_file:
        json.dump(constraints,json_file,indent=3)
    if args.nentries:
        runlib.run_n(args.rootfile.encode('ascii'),axes_file.encode('ascii'),spaces_file.encode('ascii'),
                constraints_file.encode('ascii'),args.nentries)
    else:
        runlib.run(args.rootfile.encode('ascii'),axes_file.encode('ascii'),spaces_file.encode('ascii'),constraints_file.encode('ascii'))
        

