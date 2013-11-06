#! /usr/bin/env python
import argparse
from ctypes import cdll, c_int, c_double, c_char_p
#user defined
import user.spaces

lib=cdll.LoadLibrary('lib/libmylib.so')

def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('rootfiles',nargs='+')
    parser.add_argument('--outfile')
    parser.add_argument('--spaces')
    return parser.parse_args()

def root_merge_2d(infiles,outfile,reference_path):
    infiles_c_strings=c_char_p*len(infiles)
    c_infiles=infiles_c_strings(*[name.encode('ascii') for name in infiles])
    c_outfile=outfile.encode('ascii')
    c_reference_path=reference_path.encode('ascii')
    lib.root_merge_2d(c_infiles,len(c_infiles),c_outfile,c_reference_path)

def root_merge_space_2d(infiles,outfile,reference_path,other_hist_paths):
    infiles_c_strings=c_char_p*len(infiles)
    c_infiles=infiles_c_strings(*[name.encode('ascii') for name in infiles])
    c_outfile=outfile.encode('ascii')
    c_reference_path=reference_path.encode('ascii')
    other_hist_paths_c_strings=c_char_p*len(other_hist_paths)
    c_other_hist_paths=other_hist_paths_c_strings(*[name.encode('ascii') for name in other_hist_paths])
    lib.root_merge_spaces_2d(c_infiles,len(c_infiles),c_outfile,c_reference_path,c_other_hist_paths,len(c_other_hist_paths))

def root_merge_space_1d(infiles,outfile,reference_path,other_hist_paths):
    infiles_c_strings=c_char_p*len(infiles)
    c_infiles=infiles_c_strings(*[name.encode('ascii') for name in infiles])
    c_outfile=outfile.encode('ascii')
    c_reference_path=reference_path.encode('ascii')
    other_hist_paths_c_strings=c_char_p*len(other_hist_paths)
    c_other_hist_paths=other_hist_paths_c_strings(*[name.encode('ascii') for name in other_hist_paths])
    lib.root_merge_spaces_1d(c_infiles,len(c_infiles),c_outfile,c_reference_path,c_other_hist_paths,len(c_other_hist_paths))

args=parse_args()
spaces=user.spaces.get_spaces(args.spaces)

for space in spaces:
    axes=space['axes']
    if not isinstance(axes,list):
        axes=[axes]
    if len(axes) == 1:
        reference_path='{}_chi2'.format(*axes)
        other_hist_paths=[]
        zaxes=list(space.get('zaxes',[]))
        for zaxis in zaxes:
            other_hist_paths.append('{}_{}'.format(axes[0],zaxis))
        print('Merging space {}, and zaxes {}'.format(reference_path,zaxes))
        root_merge_space_1d(args.rootfiles,args.outfile,reference_path,other_hist_paths)
    if len(axes) == 2:
        reference_path='{}_{}_chi2'.format(*axes)
        other_hist_paths=[]
        zaxes=list(space.get('zaxes',[]))
        for zaxis in zaxes:
            other_hist_paths.append('{}_{}_{}'.format(axes[0],axes[1],zaxis))
        print('Merging space {}, and zaxes {}'.format(reference_path,zaxes))
        root_merge_space_2d(args.rootfiles,args.outfile,reference_path,other_hist_paths)

