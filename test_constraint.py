#! /usr/bin/env python
import argparse

from py_modules import tools
import py_modules.CtypesWrappers as cw
import matplotlib.pyplot as plt
import user.gauss_constraints
import user.contour_constraints
import user.mneu_mg_m12g_m3g_X2_lookups
import user.contours

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--constraint',
            help='name of constraint as defined in user/gauss_constraints.py or user/contour_constraints.py')
    parser.add_argument('--values',type=float,nargs='+',help='values')
    parser.add_argument('--plot-ssi',action='store_true',help='')
    parser.add_argument('--style',default='mcpp',choices=['mcpp','mc-old'],
            help='style of observable ids')
    parser.add_argument('--print-all-gauss-constraints',action='store_true')
    return parser.parse_args()

def add_array_ids(constraint,style):
    n_observables=len(constraint['observable_ids'][style])
    constraint['observable_ids']['array_ids']=range(n_observables)
    return constraint

def setup_constraint(name,style):
    gauss_constraint=user.gauss_constraints.get().get(name)
    contour_constraint=user.contour_constraints.get().get(name)
    mneu_mg_m12g_m3g_X2_lookup=user.mneu_mg_m12g_m3g_X2_lookups.get().get(name)
    if gauss_constraint is not None:
        gauss_constraint=add_array_ids(gauss_constraint,style)
        tools.add_gauss_constraints({name:gauss_constraint})
    elif contour_constraint is not None:
        contours=tools.populate_contours(user.contours.get())
        tools.add_contours(contours)
        contour_constraint=add_array_ids(contour_constraint,style)
        tools.add_contour_constraints({name:contour_constraint})
    elif mneu_mg_m12g_m3g_X2_lookup is not None:
        mneu_mg_m12g_m3g_X2_lookup=add_array_ids(mneu_mg_m12g_m3g_X2_lookup,style)
        lookups={name:mneu_mg_m12g_m3g_X2_lookup}
        lookups=tools.populate_mneu_mg_m12g_m3g_X2_lookups(lookups)
        tools.add_mneu_mg_m12g_m3g_X2_lookups(lookups)
    else:
        print('{} not found in gauss or contour constraints.\Exiting'.format(name))
        exit()

if __name__=='__main__':
    args=parse_args()
    if args.print_all_gauss_constraints:
        pp(list(user.gauss_constraints.get().keys()))
    name=args.constraint
    if not 'chi2-' in name:
        print('adding prefix chi2- to the name of the constraint')
        name='chi2-{}'.format(name)
    setup_constraint(name,args.style)
    vars=args.values 
    value=cw.get_value(name,vars)
    print('{:<20} :{}'.format(name,value))
