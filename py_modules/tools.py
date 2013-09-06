#FIXME: this module is called tools, but could easily be renamed!!!

# python modules
import pprint
import json
# custum modules
import  py_modules.oldarrayindices 
import py_modules.CtypesWrappers as cw
# some definitions 
axes_file='user/temp_axes.json'
spaces_file='user/temp_spaces.json'
constraints_file='user/temp_constraints.json'

pp=pprint.PrettyPrinter(indent=4).pprint

def get_mc_old_array_ids_dict(file_info):
    try:
        observable_ids=file_info['observable_ids']
    except KeyError:
        print("ERROR: key \"{}\" not found in file_info. Change in \"user/files.py\" Exiting program".format('observable_ids'))
        exit(1)
    #Check both, they cannot both be true
    old_oids= observable_ids.get('mc_old')
    if old_oids is not None:
        array_ids_dict= py_modules.oldarrayindices.get_array_ids(old_oids['prediction_index'],old_oids['spectrum_index'])
    return array_ids_dict

def get_axes_list_from_spaces(spaces):
    axes_list=[]
    if spaces is not None:
        for space in spaces:
            for axis in space['axes']:
                axes_list.append(axis)
            try:
                for axis in list(space.get('zaxes')):
                    axes_list.append(axis)
            except TypeError:
                continue
    return axes_list

def populate_axes(axes,valid_values_list,axes_list=None):
    #FIXME: may want to check that the gauss_constraint etc. are defined
    out_axes={}
    #only initialise axes that are defined in spaces
    if axes_list is not None:
        axes={name:axes[name] for name in axes_list}
    for name, axis in axes.items():
        if axis.get('value') in valid_values_list:
            out_axes[name]=axis
        else:
            print('WARNING: value \'{}\' not valid for axis \'{}\''.format(axis.get('value'),name))
    return out_axes

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

def populate_spaces(axes_dict,spaces,reference):
    #check if all 'axes' and 'zaxes' correspond to keys in the axes_dict
    #also transform e.g. {'axes':'mh'} into {'axes':['mh']}
    axes_names=axes_dict.keys()
    for space in spaces:
        #handle axes
        try:
            axes=space['axes']
            if not isinstance(axes,list):
                axes=[axes]
            for axis in axes:
                if not axis in axes_names:
                    print('ERROR: axis \'{}\' is does not exist\nEXITING'.format(axis))
                    exit(1)
            space.update({'axes':axes})
        except KeyError:
            print('ERROR: one of the spaces in does not have \'axes\'\nEXITING')
            exit(1)
        #handle zaxes
        zaxes=space.get('zaxes')
        if zaxes is not None:
            if not isinstance(zaxes,list):
                zaxes=[zaxes]
            for axis in zaxes:
                if not axis in axes_names:
                    print('ERROR: axis \'{}\' is does not exist\nEXITING'.format(axis))
                    exit(1)
            space.update({'zaxes':zaxes})
        space['reference_value']=reference
    return spaces

def array_ids_dict_from_json_file(filename):
    with open(filename,'r') as f:
        array_ids_list=json.load(f)
    return {(oid1,oid2): array_id for oid1, oid2, array_id in array_ids_list}

def get_array_ids(in_dict,style,array_ids_dict):
    array_ids=in_dict['observable_ids'].get('array_ids')
    if array_ids is None:
        try:
            oids=in_dict['observable_ids'][style]
        except KeyError:
            return None
        if not isinstance(oids, list): 
            oids=[oids]
        try:
            array_ids=[array_ids_dict[oid] for oid in oids]
        except KeyError:
            print('WARNING: observable id \"{}\" not defined for style \"{}\". \nExiting program'.format(oids,style))
    return array_ids


def recursive_insert_array_ids(in_dict, style, array_ids_dict):
    if 'observable_ids' in in_dict.keys():
        array_ids=get_array_ids(in_dict,style,array_ids_dict)
        if array_ids is not None:
            in_dict['observable_ids']['array_ids']=get_array_ids(in_dict,style,array_ids_dict)
            return in_dict
        else:
            return None
    else:
        for key, val in in_dict.items():
            if isinstance(val,dict):
                in_dict[key]=recursive_insert_array_ids(val,style,array_ids_dict)
                if in_dict[key] is None:
                    return None
            else:
                continue
        return in_dict

def populate_with_array_ids(in_dict,style,array_ids_dict):
    out_dict={}
    for key, val in in_dict.items():
        new_dict=recursive_insert_array_ids(val,style,array_ids_dict)
        if new_dict is not None:
            out_dict[key]=new_dict
    return out_dict

def add_vars_lookups(vars_lookups):
    for name, details in vars_lookups.items():
        array_id=details['observable_ids']['array_ids']
        if isinstance(array_id,list):
            array_id=array_id[0]
        cw.add_vars_lookup(name,array_id)

def add_vars_functions(vars_functions):
    for name, details in vars_functions.items():
        array_ids=details['observable_ids']['array_ids']
        function_name=details['name']
        cw.add_vars_function(name,array_ids,function_name)

def add_axes(axes):
    for name, details in axes.items():
        if details.get('binning') is not None:
            cw.add_axis_with_binning(name,details['value'],details['binning']['type'],
                    details['binning']['low'],details['binning']['high'],details['binning']['nbins'])
        else:
            cw.add_axis(name,details['value'])

def add_spaces(spaces):
    for space in spaces:
        axes=space['axes']
        zaxes=space.get('zaxes',[])
        reference=space['reference_value']
        cw.add_space(axes,zaxes,reference)
