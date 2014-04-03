#! /usr/bin/env python
#python core
import argparse
import pprint
#third party
import numpy
from numpy import ma
import matplotlib.pyplot as plt
#private
import py_modules.CtypesWrappers as cw
import sqlite_point
import user.axes

pp=pprint.PrettyPrinter(indent=4).pprint

def parse_args():
    parser=argparse.ArgumentParser()
    parser=sqlite_point.get_parser()
    parser.add_argument('--root-file',help='')
    parser.add_argument('--axes',nargs='+',help='')
    parser.add_argument('--zrange',nargs=2,default=[30,45],type=float,help='')
    parser.add_argument('--best-fit',help='',action='store_true')
    return parser.parse_args()

args=parse_args()
rootfile=args.root_file
axes=args.axes
vmin,vmax=args.zrange
#prepare settings that hold for 1 and 2 d
plotname='_'.join(axes)
binnings=[user.axes.get()[axis]['binning'] for axis in axes ]
#bin edges
bin_edges=[]
bin_centres=[]
for b in binnings:
    if b['type']=='linear':
        low,high,nbins=b['low'],b['high'],b['nbins']
        half_bin=0.5*(high-low)/nbins
        bin_edges.append(numpy.linspace(low,high,nbins+1))
        bin_centres.append(numpy.linspace(low+half_bin,high-half_bin,nbins))
    elif b['type']=='log':
        low,high,nbins=numpy.log10(b['low']), numpy.log10(b['high']), b['nbins']
        half_bin=0.5*(high-low)/nbins
        bin_edges.append(numpy.logspace(low,high,nbins+1))
        bin_centres.append(numpy.logspace(low+half_bin,high-half_bin,nbins))
#plot settings
if binnings[0]['type'] == 'log':
    plt.xscale('log')
plt.xlabel(axes[0])
nxbins=binnings[0]['nbins']

#get points
if len(axes)==1:
    chi2_plot=cw.get_1d_hist(rootfile,'{}_chi2'.format(plotname),nxbins)
    entries_plot=cw.get_1d_hist(rootfile,'{}_entries'.format(plotname),nxbins)
    plt.plot(bin_centres[0],chi2_plot,'o')
    plt.ylim([vmin,vmax])
    if args.best_fit:
        chi2_min=numpy.min(chi2_plot)
        rowid=int(entries_plot[chi2_plot==numpy.min(chi2_plot)])
    else:
        [(x,y)]=plt.ginput(1)
        id=numpy.where(bin_edges[0]>x)[0][0]-1
        print('Clicked points: {}: {}  {}: {}'.format(axes[0],x,'chi2',y))
        rowid=int(entries_plot[id])

#get plots
elif len(axes)==2:
    nybins=binnings[0]['nbins']
    chi2_plot=cw.get_2d_hist(rootfile,'{}_chi2'.format(plotname),nxbins,nybins)
    entries_plot=cw.get_2d_hist(rootfile,'{}_entries'.format(plotname),nxbins,nybins)
    chi2_plot=ma.masked_where(entries_plot==-1,chi2_plot)
    ext=[binnings[0]['low'],binnings[0]['high'],binnings[1]['low'],binnings[1]['high']]
    if binnings[1]['type'] == 'log':
        plt.yscale('log')
    plt.imshow(chi2_plot,vmin=vmin,vmax=vmax,origin='lower',interpolation='nearest',extent=ext,aspect='auto')
    plt.colorbar()
    plt.ylabel(axes[1])
    #FIXME: the best fit point shouldn't come from a plane
    if  args.best_fit:
        chi2_min=numpy.min(chi2_plot)
        rowid=int(entries_plot[chi2_plot==numpy.min(chi2_plot)])
    else:
        [(x,y)]=plt.ginput(1)
        print('Clicked points: {}: {}  {}: {}'.format(axes[0],x,axes[1],y))
        xid,yid=numpy.where(bin_edges[0]>x)[0][0]-1, numpy.where(bin_edges[1]>y)[0][0]-1
        rowid=int(entries_plot[yid,xid])
args.rowid=rowid
if not rowid==-1 and args.sqlite_db is not None:
    sqlite_point.main(args)
elif rowid==-1:
    print('Selected invalid point o')
else:
    print('No sqlite database selected')
