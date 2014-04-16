#! /usr/bin/env python
#python core
import argparse
#third party
import numpy
from numpy import ma
import matplotlib
import matplotlib.pyplot as plt
#private
import py_modules.CtypesWrappers as cw
import user.spaces
import user.axes
import user.figure_options
import user.layer_options
import scipy.interpolate

#WARINING THIS IS UGLY MAYBE NEEDS CLEANUP
def parse_args():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            fromfile_prefix_chars='@')
    parser.add_argument('--rootfiles',nargs='+', help='define input root file')
    parser.add_argument('--dirs-in-rootfile',default=[''],nargs='+', help='define directory(ies) in input root file where plots are saved')
    parser.add_argument('--zaxes',nargs='+',default=['chi2'],help='zaxis as in the name of figures')
    parser.add_argument('--layer-options',default=[None],nargs='+', help='select options from user/layer_options.py')
    parser.add_argument('--spaces-xaxes', help='use axes corresponding to axes from user/spaces.py')
    parser.add_argument('--xaxis',help='define inividual xaxis')
    parser.add_argument('--figure-options', help='select options from user/figure_options.py')
    parser.add_argument('--prefix', help='prefix for figure name')
    parser.add_argument('--extension', help='extension for figure name',default='pdf')
    return parser.parse_args()


def prepare_figures_details(args):
    #prepare axes details
    figures_xaxis_names=[]
    if args.spaces_xaxes is not None:
        spaces=user.spaces.get_spaces(args.spaces_xaxes)
        for space in spaces:
            if isinstance(space['axes'],list) and len(space['axes'])==1:
                xaxis_name=space['axes'][0]
            elif not isinstance(space['axes'],list):
                xaxis_name=space['axes']
            figures_xaxis_names.append(xaxis_name)
    elif args.xaxis is not None:
        figures_xaxis_names=[args.xaxis]
    figures_xaxis_details=[]
    all_xaxis_details=user.axes.get()
    for xaxis_name in figures_xaxis_names:
        xaxis_details=all_xaxis_details[xaxis_name]
        xaxis_details.update({'name':xaxis_name})
        figures_xaxis_details.append(xaxis_details)
    nfigures=len(figures_xaxis_names)
    #prepare layer options, rootfile names and plotnames
    rootfiles=args.rootfiles
    dirs_in_rootfile=args.dirs_in_rootfile
    layer_options_names=args.layer_options
    layer_options=[user.layer_options.get().get(name,{}) for name in layer_options_names]
    zaxes=args.zaxes
    nlayers=max([
        len(rootfiles),
        len(layer_options),
        len(args.zaxes),
        len(dirs_in_rootfile)
        ])
    fignames=[]
    if len(rootfiles)==1:
        figures_rootfiles=[rootfiles*nlayers]*nfigures
    else :
        figures_rootfiles=[rootfiles]*nfigures
    if len(layer_options)==1:
        figures_layer_options=[layer_options*nlayers]*nfigures
    else :
        figures_layer_options=[layer_options]*nfigures
    if len(zaxes)==1 and len(dirs_in_rootfile)==1:
        dir=dirs_in_rootfile[0]
        zaxis=zaxes[0]
        figures_plotnames=[['{}{}_{}'.format(dir,xaxis_name,zaxis)]*nlayers for xaxis_name in figures_xaxis_names]
    elif len(zaxes)==1:
        zaxis=zaxes[0]
        figures_plotnames=[['{}{}_{}'.format(dir,xaxis_name,zaxis) for dir in dirs_in_rootfile ] for xaxis_name in figures_xaxis_names]
    elif len(dirs_in_rootfile)==1:
        dir=dirs_in_rootfile[0]
        figures_plotnames=[['{}{}_{}'.format(dir,xaxis_name,zaxis) for zaxis in zaxes] for xaxis_name in figures_xaxis_names]
    else:
        figures_plotnames=[['{}{}_{}'.format(dir,xaxis_name,zaxis) for dir, zaxis in zip(dirs_in_rootfile, zaxes)] 
                for xaxis_name in figures_xaxis_names]
    fignames=['{}_{}_{}.{}'.format(args.prefix,xaxis_name,zaxes[-1],args.extension) for xaxis_name in figures_xaxis_names]
    figures_layers_details=zip(figures_rootfiles,figures_plotnames,figures_layer_options)
    return [ (fignames[i], figures_xaxis_details[i], layers_details) for i, layers_details in enumerate(figures_layers_details)]



if __name__ == '__main__':
    args=parse_args()
    figure_options=user.figure_options.get().get(args.figure_options,{})
    for (figname, xaxis_details, layers_details) in prepare_figures_details(args):
        binning=xaxis_details['binning'] 
        #nxbins and nybins
        nxbins=binning['nbins']
        #bin edges
        if binning['type']=='linear':
            low,high,nbins=binning['low'],binning['high'],binning['nbins']
            half_bin=0.5*(high-low)/nbins
            bin_edges=numpy.linspace(low,high,nbins+1)
            bin_centres=numpy.linspace(low+half_bin,high-half_bin,nbins)
        elif binning['type']=='log':
            low,high,nbins=numpy.log10(binning['low']), numpy.log10(binning['high']), binning['nbins']
            half_bin=0.5*(high-low)/nbins
            bin_edges=numpy.logspace(low,high,nbins+1)
            bin_centres=numpy.logspace(low+half_bin,high-half_bin,nbins)
        #start figure
        fig=plt.figure()
        axes=fig.add_axes(figure_options.get('axes_rect',[0.17, 0.15, 0.77, 0.75]))
        axes.tick_params(axis='both',which='major',labelsize=20)
        xlabel=xaxis_details.get('texname',xaxis_details['name'])
        label_fontsize=figure_options.get('label_fontsize',20)
        axes.set_xlabel(xlabel,fontsize=label_fontsize)
        axes.set_xlim([binning['low'],binning['high']])
        if binning['type'] == 'log':
            axes.set_xscale('log')
        if not figure_options.get('suppress_ticks_from_axes',False):
            if xaxis_details.get('xticks',False) and binning['type']=='linear':
                low,high,step=binning['low'],binning['high'],xaxis_details['xticks']
                axes.set_xticks(numpy.arange(low,high*1.001,step))
        if figure_options.get('text_box',False):
            args=figure_options['text_box'].get('args')
            kwargs={'verticalalignment':'top','transform':axes.transAxes,'fontsize':20,'horizontalalignment':'left'}
            kwargs.update(figure_options['text_box'].get('kwargs',{}))
            axes.text(*args,**kwargs)
        #FIXME: there might be a better way of zipping an unzipping
        filenames, plotnames, layers_options = layers_details
        for filename, plotname, layer_options in zip(filenames, plotnames, layers_options):
            plot=cw.get_1d_hist(filename,plotname,nxbins)
            entries_plotname='{}_entries'.format(xaxis_details['name'])
            entries_plot=cw.get_1d_hist(filename,entries_plotname,nxbins)
            if layer_options.get('dchi2_mode',False):
                chi2_minimum=layer_options.get('chi2_minimum',numpy.min(plot))
                plot=plot-chi2_minimum
            color=layer_options.get('color')
            linestyle=layer_options.get('linestyle')
            linewidth=layer_options.get('linewidth',2)
            axes.plot(bin_centres,plot,linewidth=linewidth,c=color,linestyle=linestyle)
            #FIXME: maybe ylim shouldn't be a property of the layer
            axes.set_ylim([layer_options.get('ymin',0),layer_options.get('ymax',9)])
            axes.set_ylabel(layer_options.get('ylabel',''),fontsize=20)
            #FIXME: this is an ugly way to get the 95% CL lower limit out
            if figure_options.get('chi2_eq_4_limit'):
                f=scipy.interpolate.interp1d(bin_centres,plot)
                xnew=numpy.linspace(bin_centres[0],bin_centres[-1],1000)
                ynew=f(xnew)
                try:
                    for i in range(999):
                        if ynew[i]>4 and ynew[i+1]<4:
                            print('{}:{}'.format(xaxis_details['name'],int(xnew[i+1])))
                    axes.plot(xnew[i+1],ynew[i+1],'o')
                except IndexError:
                    print('limit not found for {}'.format(xaxis_details['name']))

        if not figure_options.get('chi2_eq_4_limit'):
            print(figname)
        plt.savefig(figname)
