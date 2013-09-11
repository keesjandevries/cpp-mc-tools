#! /usr/bin/env python
import argparse

from py_modules.tools import *
import py_modules.CtypesWrappers as cw
import user.gauss_constraints
import user.contour_constraints
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--constraint',
            help='name of constraint as defined in user/gauss_constraints.py or user/contour_constraints.py')
    parser.add_argument('--values',type=float,nargs='+',help='values')
    parser.add_argument('--style',default='mcpp',choices=['mcpp','mc-old'],
            help='style of observable ids')
    parser.add_argument('--print-all-gauss-constraints',action='store_true')
    return parser.parse_args()


if __name__=='__main__':
    args=parse_args()
    if args.print_all_gauss_constraints:
        pp(list(user.gauss_constraints.get().keys()))

    name=args.constraint
    gauss_constraint=user.gauss_constraints.get().get(name)
    if gauss_constraint is not None:
        n_observables=len(gauss_constraint['observable_ids'][args.style])
        if not n_observables==len(args.values):
            print('ERROR: need {} values, {} were provided\nExiting'.format(n_observables,len(args.values)))
            exit()
        gauss_constraint['observable_ids']['array_ids']=range(n_observables)
        add_gauss_constraints({name:gauss_constraint})
    else:
        print('{} not found in gauss or contour constraints.\Exiting'.format(name))
        exit()
    vars=args.values 
    value=cw.get_value(name,vars)
    print('{:<20} :{}'.format(name,value))
    
