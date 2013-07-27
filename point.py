#! /usr/bin/env python
#python modules
import argparse
#own modules
import test_vars_lookup
import test_get_entry
import py_modules.oldarrayindices 
import py_modules.tools as tools
#user defined
import user.files 
import user.file_properties 

#NOTE: this is a rather serious attempt to create a very useful tool
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('rootfile', help='define input root file')
    parser.add_argument('-n','--entry',type=int,help='entry number in the root file')
    parser.add_argument('-v','--verbose',nargs='+',default=[],help='entry number in the root file')
    parser.add_argument('--file-setup', help='array indices setup')
    return parser.parse_args()

if __name__=='__main__':
    args=parse_args()
    #FIXME: better name for object
    object=test_get_entry.PyGetEntry(args.rootfile)
    if args.entry is not None:
        vars=object.get_vars(args.entry)
    else:
        print('ERROR: this is actually fine for now')


    #get array ids dict
    if args.file_setup:
        file_info=tools.get_file_info(args.file_setup,user.file_properties.get_file_properties())
    else:
        file_info=tools.get_file_info(args.rootfile,user.files.get_files())
    #{'observable_ids': {'mc_old': {'spectrum_index': 79, 'prediction_index': 15}}}
    try:
        indices=file_info['observable_ids']['mc_old']
        array_ids_dict=py_modules.oldarrayindices.get_array_ids(indices['prediction_index'],indices['spectrum_index'])
    except KeyError:
        print('ERROR there was a problem\nExiting program')
        exit(1)
    if 'mc_point' in args.verbose:
#        try:
        oids=file_info['mc_point_inputs']
        flag=file_info['mc_point_flag']
        print('./mc_point.py {} {}'.format(flag, ' '.join([ str(vars[array_ids_dict[oid]]) for oid in oids] )))
#        except:
#            print('ERROR: FIXME')

