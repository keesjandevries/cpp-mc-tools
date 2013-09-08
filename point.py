#! /usr/bin/env python
#python modules
import argparse
#own modules
#import test_vars_lookup
import test_get_entry
import py_modules.oldarrayindices 
import py_modules.tools as tools
#user defined
import user.mc_old_setup

#NOTE: this is a rather serious attempt to create a very useful tool
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('rootfile', help='define input root file')
    parser.add_argument('-n','--entry',type=int,help='entry number in the root file')
    parser.add_argument('-v','--verbose',nargs='+',default=[],help='entry number in the root file')
    parser.add_argument('--mc-old-setup', help='array indices setup')
    parser.add_argument('--storage-dict', help='storage dict')
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
    file_info = None #FIXME: this is for the program not to crash
    if args.mc_old_setup is not None:
        file_info=user.mc_old_setup.get(args.mc_old_setup)
        try:
            indices=file_info['observable_ids']['mc_old']
            array_ids_dict=py_modules.oldarrayindices.get_array_ids(indices['prediction_index'],indices['spectrum_index'])
        except KeyError:
            print('ERROR there was a problem\nExiting program')
            exit(1)
    elif args.storage_dict is not None:
        print('FIXME: this doensnt work now')
        exit()
        array_ids_dict=array_ids_dict_from_json_file(args.storage_dict)

    if 'mc_point' in args.verbose:
        oids=file_info['mc_point_inputs']
        flag=file_info['mc_point_flag']
        print('./mc_point.py {} {}'.format(flag, ' '.join([ str(vars[array_ids_dict[oid]]) for oid in oids] )))
    if 'info' in args.verbose:
        #FIXME: this should be shipped to user/info.py ...
        for oid in ['X2','m0','m12','A0','tanb','mh','ssmh','squark_l','squark_r','stop1','stop2' ,'sbottom1','sbottom2','gluino','neu1']:
            print(oid,vars[array_ids_dict[oid]])
