from ctypes import cdll, c_int, c_double, c_char_p
import numpy

lib=cdll.LoadLibrary('lib/libmylib.so')

def add_vars_lookup(name,array_id):
    lib.add_vars_lookup(name.encode('ascii'),array_id)

def add_vars_function(name,array_ids,function_name):
    c_array_ids=(c_int*len(array_ids))(*array_ids)
    lib.add_vars_function(name.encode('ascii'),c_array_ids,len(array_ids),function_name.encode('ascii'))

def add_gauss_constraint(name,array_ids,mu,sigmas,function_name):
    c_name=name.encode('ascii')
    c_array_ids=(c_int*len(array_ids))(*array_ids)
    c_mu=c_double(mu)
    c_sigmas=(c_double*len(sigmas))(*sigmas)
    c_function_name=function_name.encode('ascii')
    lib.add_gauss_constraint(c_name,c_array_ids,len(c_array_ids),c_mu,c_sigmas,len(c_sigmas),c_function_name)

def add_contour_constraint(name,array_ids,contour_names,function_name):
    c_name=name.encode('ascii')
    c_array_ids=(c_int*len(array_ids))(*array_ids)
    contour_strings=c_char_p*len(contour_names)
    c_contour_names=contour_strings(*[name.encode('ascii') for name in contour_names])
    c_function_name=function_name.encode('ascii')
    lib.add_contour_constraint(c_name,c_array_ids,len(c_array_ids),c_contour_names,len(c_contour_names),c_function_name)

def add_mneu_mg_m12g_m3g_X2_lookup(name,array_ids,default_X2,mneu_mg_m12g_m3g_X2_table):
    c_array_ids=(c_int*len(array_ids))(*array_ids)
    n=5*len(mneu_mg_m12g_m3g_X2_table)
    values=sum(mneu_mg_m12g_m3g_X2_table,[])
    c_mneu_mg_m12g_m3g_X2_table=(c_double*n)(*values)
    lib.add_mneu_mg_m12g_m3g_X2_lookup(name.encode('ascii'),c_array_ids,len(c_array_ids),c_double(default_X2),
            c_mneu_mg_m12g_m3g_X2_table,n)

def add_chi2_calculator(name):
    lib.add_chi2_calculator(name.encode('ascii'))

def add_constraint_to_chi2_calculator(constraint_name,calculator_name):
    lib.add_constraint_to_chi2_calculator(constraint_name.encode('ascii'),calculator_name.encode('ascii'))

def get_value(name,vars):
    lib.get_value.restype=c_double
    c_name=name.encode('ascii')
    c_vars=(c_double*len(vars))(*vars)
    return lib.get_value(c_name,c_vars)

def get_min_reference(filename):
    lib.get_min_reference.restype=c_double
    c_filename=filename.encode('ascii')
    return lib.get_min_reference(c_filename)

def get_min_reference_rowid(filename):
    c_filename=filename.encode('ascii')
    return lib.get_min_reference_rowid(c_filename)

def get_contour_value(name,parameter):
    lib.get_contour_value.restype=c_double
    c_name=name.encode('ascii')
    c_parameter=c_double(parameter)
    return lib.get_contour_value(c_name,c_parameter)

def add_contour(name,xs,ys,type):
    c_name=name.encode('ascii')
    c_xs=(c_double*len(xs))(*xs)
    c_ys=(c_double*len(ys))(*ys)
    c_type=type.encode('ascii')
    lib.add_contour(c_name,c_xs,c_ys,len(c_xs),c_type)

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

def add_cut(name,array_ids,function_name):
    c_array_ids=(c_int*len(array_ids))(*array_ids)
    lib.add_cut(name.encode('ascii'),c_array_ids,len(array_ids),function_name.encode('ascii'))

def make_plots(infiles, outfile, nentries, dir_in_root,cuts=[] ):
    infiles_c_strings=c_char_p*len(infiles)
    c_infiles=infiles_c_strings(*[name.encode('ascii') for name in infiles])
    c_outfile=outfile.encode('ascii')
    c_dir_in_root=dir_in_root.encode('ascii')
    cuts_c_strings=c_char_p*len(cuts)
    c_cuts=cuts_c_strings(*[name.encode('ascii') for name in cuts])
    lib.make_plots(c_infiles, len(c_infiles), c_outfile,nentries,c_dir_in_root,c_cuts,len(c_cuts))

def sqlite_reduce_db(input_name,output_name,select_query,chi2_function_name,max_chi2):
    c_input_name=input_name.encode('ascii')
    c_output_name=output_name.encode('ascii')
    c_select_query=select_query.encode('ascii')
    c_chi2_function_name=chi2_function_name.encode('ascii')
    c_max_chi2=c_double(max_chi2)
    lib.sqlite_reduce_db(c_input_name,c_output_name,c_select_query,len(c_select_query),c_chi2_function_name,c_max_chi2)

def sqlite_make_plots(sqlite_db_file, query,outfile_name,reference_name):
    c_query=query.encode('ascii')
    c_sqlite_db_file=sqlite_db_file.encode('ascii')
    c_outfile_name=outfile_name.encode('ascii')
    c_reference_name=reference_name.encode('ascii')
    lib.sqlite_make_plots(c_sqlite_db_file, c_query,len(c_query),c_outfile_name,c_reference_name)

def insert_root_into_sqlite(root_file_name, sqlite_db, collection_rowid):
    lib.insert_root_into_sqlite(root_file_name.encode('ascii'),sqlite_db.encode('ascii'),collection_rowid)

def get_2d_hist(root_file_name,hist_name,nx,ny):
    n=(nx+2)*(ny+2)
    double_array=(c_double*n)(*([0.]*n))
    lib.get_2d_hist_content(root_file_name.encode('ascii'),hist_name.encode('ascii'),n,double_array)
    array=numpy.array([v for v in double_array])
    array=array.reshape(nx+2,ny+2)
    return array[1:-1,1:-1]

def get_2d_hist_minimum(root_file_name,hist_name,nx,ny):
    n=(nx+2)*(ny+2)
    double_array=(c_double*n)(*([0.]*n))
    lib.get_2d_hist_content(root_file_name.encode('ascii'),hist_name.encode('ascii'),n,double_array)
    array=numpy.array([v for v in double_array])
    return numpy.min(array)

def get_2d_overflow_edges(root_file_name,hist_name,nx,ny):
    n=(nx+2)*(ny+2)
    double_array=(c_double*n)(*([0.]*n))
    lib.get_2d_hist_content(root_file_name.encode('ascii'),hist_name.encode('ascii'),n,double_array)
    array=numpy.array([v for v in double_array])
    array=array.reshape(nx+2,ny+2)
    bottom = array[0,:] 
    top = array[-1,:] 
    left = array[:,0] 
    right = array[:,-1] 
    return bottom, top, left, right


def get_1d_hist(root_file_name,hist_name,nbins):
    n=nbins+2
    double_array=(c_double*n)(*([0.]*n))
    lib.get_1d_hist_content(root_file_name.encode('ascii'),hist_name.encode('ascii'),n,double_array)
    array=numpy.array([v for v in double_array])
    return array[1:-1]

def get_1d_minimum(root_file_name,hist_name,nbins):
    n=nbins+2
    double_array=(c_double*n)(*([0.]*n))
    lib.get_1d_hist_content(root_file_name.encode('ascii'),hist_name.encode('ascii'),n,double_array)
    array=numpy.array([v for v in double_array])
    return numpy.min(array)

def chi2_ndof_to_cl(chi2, ndof):
    lib.chi2_ndof_to_cl.restype=c_double
    return lib.chi2_ndof_to_cl(c_double(chi2),ndof)
