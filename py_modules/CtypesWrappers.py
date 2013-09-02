from ctypes import cdll, c_int, c_double, c_char_p
lib=cdll.LoadLibrary('lib/libmylib.so')

def add_vars_lookup(name,array_id):
    lib.add_vars_lookup(name.encode('ascii'),array_id)

def add_axis(axis_name,value_function_name):
    c_axis_name=axis_name.encode('ascii')
    c_value_function_name=value_function_name.encode('ascii')
    lib.add_axis(c_axis_name,c_value_function_name)

def add_axis_with_binning(axis_name,value_function_name,binning_type,low,high,nbins):
    c_axis_name=axis_name.encode('ascii')
    c_value_function_name=value_function_name.encode('ascii')
    c_binning_type=binning_type.encode('ascii')
    c_low=c_double(low)
    c_high=c_double(high)
    lib.add_axis_with_binning(c_axis_name,c_value_function_name,c_binning_type,c_low,c_high,nbins)

def add_space(axes_names,zaxes_names,reference_function):
    #make appropriate ctypes
    axes_strings=c_char_p*len(axes_names)
    zaxes_strings=c_char_p*len(zaxes_names)
    c_reference_function=reference_function.encode('ascii')
    #fill them
    c_axes_names=axes_strings(*[name.encode('ascii') for name in axes_names])
    c_zaxes_names=zaxes_strings(*[name.encode('ascii') for name in zaxes_names])
    #add space
    lib.add_space(c_axes_names,len(axes_names),c_zaxes_names,len(zaxes_names),c_reference_function)

