#! /usr/bin/env python
# python modules
import argparse, json
from ctypes import cdll
# custum modules
import  py_modules.oldarrayindices 
# dictionaries
import user.axes
import user.spaces
import user.files
import user.constraints
# shared library objects
runlib=cdll.LoadLibrary('lib/libmylib.so')
# some definitions 
axes_file='user/temp_axes.json'
spaces_file='user/temp_spaces.json'
constraints_file='user/temp_constraints.json'


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('rootfile', help='define input root file')
    return parser.parse_args()

def get_file_info(filename):
    try:
        file_info=user.files.get_files()[filename]
    except KeyError:
        print("ERROR: file \"{}\" not found in user/files.py. Exiting program".format(filename))
        exit(1)
    return file_info

def get_array_ids_dict_style(file_info):
    try:
        observable_ids=file_info['observable_ids']
    except KeyError:
        print("ERROR: key \"{}\" not found in file_info. Change in \"user/files.py\" Exiting program".format('observable_ids'))
        exit(1)
    #Check both, they cannot both be true
    old_oids= observable_ids.get('mc_old')
    mcpp_oids= observable_ids.get('mcpp')
    if old_oids and mcpp_oids: 
        print("ERROR: in file \"user/files.py \", both mc_old and mcpp observable ids are defined")
        exit(1)
    if old_oids:
        array_ids_dict= py_modules.oldarrayindices.get_array_ids(old_oids['prediction_index'],old_oids['spectrum_index'])
        style='mc_old'
    elif mcpp_oids:
        print("NOTE: atm not implemented. Exiting program")
        exit(1)
    return array_ids_dict, style

def handle_vars_lookup(name,axis,array_ids_dict, style):
    if axis['vars_lookup'].get('array_id') is not None:
        pass
    else:
        try:
            oid=axis['vars_lookup'][style]
            axis['vars_lookup'].update({'array_id':array_ids_dict[oid]})
        except KeyError:
            print('ERROR: observable id {} not found for axis {}. \nExiting program'.format(oid,name))
            exit(1)
    return axis

def handle_vars_function(name,axis,array_ids_dict,style):
    if axis['vars_function'].get('observable_ids') is not None:
        if not axis['vars_function']['observable_ids'].get('array_ids')==None:
            pass
        else:
            oids=axis['vars_function']['observable_ids'][style]
            if not isinstance(oids, list): oids=[oids]
            try:
                array_ids=[array_ids_dict[oid] for oid in oids]
            except KeyError:
                print('ERROR: observable id {} not found for axis {}. \nExiting program'.format(oid,name))
                exit(1)
            axis['vars_function']['observable_ids'].update({'array_ids':array_ids})
    else:
        print('ERROR: observable_ids not found for axis {}. \nExiting program'.format(name))
        exit(1)
    return axis

def populate_axes(style,array_ids_dict,axes):
    for name, axis in axes.items():
        if axis.get('gauss_constraint') is not None:
            continue
        elif axis.get('vars_lookup') is not None:
            axis=handle_vars_lookup(name,axis,array_ids_dict,style)
        elif axis.get('vars_function') is not None:
            axis=handle_vars_function(name,axis,array_ids_dict,style)

#        elif not axis['observable_ids'].get('array_ids')==None:
#            continue 
#        else:
#            oids=axis['observable_ids'][style]
#            if not isinstance(oids, list): oids=[oids]
#            array_ids=[array_ids_dict[oid] for oid in oids]
#            axis['observable_ids'].update({'array_ids':array_ids})
    return axes

def populate_constraints(style,array_ids_dict,constraints):
    for name, constraint in constraints.items():
        if not constraint['observable_ids'].get('array_ids')==None:
            continue 
        else:
            oids=constraint['observable_ids'][style]
            if not isinstance(oids, list): oids=[oids]
            array_ids=[array_ids_dict[oid] for oid in oids]
            constraint['observable_ids'].update({'array_ids':array_ids})
    return constraints

def check_axes_defined(axes, axes_names):
    defined=True
    name=None
    if axes:
        if not isinstance(axes, list):
            axes=[axes]
        for axis in axes:
            if not axis in axes_names:
                defined=False
                name=axis
                break
    else:
        defined=False
    return defined, name

def populate_spaces(axes_dict):
    spaces=user.spaces.get_spaces()
    axes_names=axes_dict.keys()
    for space in spaces:
        defined, name= check_axes_defined(space.get('axes'),axes_names)
        if not defined:
            print('ERROR: \"{}\" not defined in user/axes.py . Exiting program'.format(name))
            exit(1)
        defined, name= check_axes_defined(space.get('zaxes'),axes_names)
        if (not defined) and name:
            print('ERROR: \"{}\" not defined in user/axes.py . Exiting program'.format(name))
            exit(1)
    return spaces


if __name__ == '__main__':
    args=parse_args()
    file_info=get_file_info(args.rootfile)
    array_ids_dict,style=get_array_ids_dict_style(file_info)
    axes=populate_axes(style,array_ids_dict,user.axes.get_axes())
    spaces=populate_spaces(axes)
    constraints=populate_constraints(style,array_ids_dict,user.constraints.get_constraints())
    #FIXME: this should be replaced by files that get deleted after running plotting from python
    with open(axes_file,'w') as json_file:
        json.dump(axes,json_file,indent=3)
    with open(spaces_file,'w') as json_file:
        json.dump(spaces,json_file,indent=3)
    with open(constraints_file,'w') as json_file:
        json.dump(constraints,json_file,indent=3)
#    runlib.run(args.rootfile.encode('ascii'),axes_file.encode('ascii'),spaces_file.encode('ascii'),constraints_file.encode('ascii'))
        

