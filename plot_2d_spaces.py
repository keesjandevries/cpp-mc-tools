#! /usr/bin/env python
#python core
import argparse
#third party
import numpy
from numpy import ma
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as col
#private
import py_modules.CtypesWrappers as cw
import user.spaces
import user.axes
import user.figure_options
import user.layer_options

def parse_args():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            fromfile_prefix_chars='@')
    parser.add_argument('--rootfiles',nargs='+', help='define input root file')
    parser.add_argument('--spaces-axes', help='use axes corresponding to axes from user/spaces.py')
    parser.add_argument('--axes',nargs=2,help='define inividual axes')
    parser.add_argument('--zaxes',nargs='+',default=['chi2'],help='zaxis as in the name of figures')
    parser.add_argument('--layer-options',default=[None],nargs='+', help='select options from user/layer_options.py')
    parser.add_argument('--figure-options', help='select options from user/figure_options.py')
    parser.add_argument('--prefix', help='prefix for figure name')
    parser.add_argument('--extension', help='extension for figure name',default='pdf')
    return parser.parse_args()

def my_cmap():
    # create the color map
    lr,ly,lg=[col.colorConverter.to_rgba(c,alpha=0.7) for c in ['r','gold','g']]
    cmaplist=[lr,ly,lg,'g','gold','r']
    cmap = col.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, 6)
    cmap.set_over('none')
    cmap.set_under('none')
    return cmap

def prepare_figures_details(args):
    #prepare axes details
    if args.spaces_axes is not None:
        spaces=user.spaces.get_spaces(args.spaces_axes)
        figures_axes_names=[space['axes'] for space in spaces if isinstance(space['axes'],list) 
                and len(space['axes'])==2]
    elif args.axes is not None:
        if len(args.axes)==2:
            figures_axes_names=[args.axes]
    figures_axes_details=[]
    all_axes_details=user.axes.get()
    for axes_names in figures_axes_names:
        axes_details=[]
        for axis_name in axes_names:
            axis_details=all_axes_details[axis_name]
            axis_details.update({'name':axis_name})
            axes_details.append(axis_details)
        figures_axes_details.append(axes_details)
    nfigures=len(figures_axes_names)
    #prepare layer options, rootfile names and plotnames
    rootfiles=args.rootfiles
    layer_options_names=args.layer_options
    layer_options=[user.layer_options.get().get(name,{}) for name in layer_options_names]
    zaxes=args.zaxes
    nlayers=max([
        len(rootfiles),
        len(layer_options),
        len(args.zaxes)
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
    if len(zaxes)==1:
        figures_plotnames=[['{}_{}_{}'.format(*(axes_names+zaxes))]*nlayers for axes_names in figures_axes_names]
        figures_zaxes=[zaxes*nlayers]*nfigures
    else:
        figures_plotnames=[['{}_{}_{}'.format(*(axes_names+[zaxis])) for zaxis in zaxes] for axes_names in figures_axes_names]
        figures_zaxes=[zaxes]*nfigures
    fignames=['{}_{}_{}_{}.{}'.format(args.prefix,*(axes_names+[zaxes[-1],args.extension])) for axes_names in figures_axes_names]
    
    figures_layers_details=zip(figures_rootfiles,figures_plotnames,figures_layer_options,figures_zaxes)
    return [ (fignames[i], figures_axes_details[i], layers_details) for i, layers_details in enumerate(figures_layers_details)]

if __name__ == '__main__':
    args=parse_args()
    figure_options=user.figure_options.get().get(args.figure_options,{})
    for (figname, axes_details, layers_details) in prepare_figures_details(args):
        binnings=[axis['binning'] for axis in axes_details]
        #nxbins and nybins
        nxbins=binnings[0]['nbins']
        nybins=binnings[1]['nbins']
        #extent
        ext=[binnings[0]['low'],binnings[0]['high'],binnings[1]['low'],binnings[1]['high']]
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
        #start figure
        X,Y=numpy.meshgrid(bin_centres[0],bin_centres[1])
        fig=plt.figure()
        axes=fig.add_axes(figure_options.get('axes_rect',[0.17, 0.15, 0.77, 0.75]))
        axes.tick_params(axis='both',which='major',labelsize=20)
        xlabel=axes_details[0].get('texname',axes_details[0]['name'])
        ylabel=axes_details[1].get('texname',axes_details[1]['name'])
        label_fontsize=figure_options.get('label_fontsize',20)
        axes.set_xlabel(xlabel,fontsize=label_fontsize)
        axes.set_ylabel(ylabel,fontsize=label_fontsize)
        axes.set_xlim([binnings[0]['low'],binnings[0]['high']])
        axes.set_ylim([binnings[1]['low'],binnings[1]['high']])
        if binnings[0]['type'] == 'log':
            axes.set_xscale('log')
        if binnings[1]['type'] == 'log':
            axes.set_yscale('log')
        if not figure_options.get('suppress_ticks_from_axes',False):
            if axes_details[0].get('xticks',False) and binnings[0]['type']=='linear':
                low,high,step=binnings[0]['low'],binnings[0]['high'],axes_details[0]['xticks']
                axes.set_xticks(numpy.arange(low,high*1.001,step))
            if axes_details[1].get('yticks',False) and binnings[1]['type']=='linear':
                low,high,step=binnings[0]['low'],binnings[0]['high'],axes_details[1]['yticks']
                axes.set_xticks(numpy.arange(low,high*1.001,step))
        #FIXME: there might be a better way of zipping an unzipping
        if figure_options.get('text_box',False):
            args=figure_options['text_box'].get('args')
            kwargs={'verticalalignment':'top','transform':axes.transAxes,'fontsize':20,'horizontalalignment':'left'}
            kwargs.update(figure_options['text_box'].get('kwargs',{}))
            axes.text(*args,**kwargs)
        filenames, plotnames, layers_options, layers_zaxis = layers_details
        for filename, plotname, layer_options, layer_zaxis in zip(filenames, plotnames, layers_options, layers_zaxis):
            plot=cw.get_2d_hist(filename,plotname,nxbins,nybins)
            entries_plotname='{}_entries'.format('_'.join([axis['name'] for axis in axes_details]))
            entries_plot=cw.get_2d_hist(filename,entries_plotname,nxbins,nybins)
            chi2_plotname='{}_chi2'.format('_'.join([axis['name'] for axis in axes_details]))
            chi2_plot=cw.get_2d_hist(filename,chi2_plotname,nxbins,nybins)
            if layer_options.get('colz',False):
                #mask where rowid == -1 (not filled)
                plot=ma.masked_where(entries_plot==-1,plot)
                if layer_options.get('mask_dchi2_gt'):
                    dchi2_max=layer_options.get('mask_dchi2_gt')
                    chi2_minimum=layer_options.get('chi2_minimum',numpy.min(chi2_plot))
                    plot=ma.masked_where(chi2_plot>chi2_minimum+dchi2_max,plot)
                if layer_options.get('dchi2_mode',False):
                    chi2_minimum=layer_options.get('chi2_minimum',numpy.min(plot))
                    plot=plot-chi2_minimum
                #get options
                vmin=layer_options.get('vmin')
                vmax=layer_options.get('vmax')
                if vmin=='zaxis_binning_low':
                    vmin=user.axes.get()[layer_zaxis]['binning']['low']
                if vmax=='zaxis_binning_high':
                    vmax=user.axes.get()[layer_zaxis]['binning']['high']
                if vmin=='zaxis_vmin':
                    vmin=user.axes.get()[layer_zaxis]['vmin']
                if vmax=='zaxis_vmax':
                    vmax=user.axes.get()[layer_zaxis]['vmax']
                cmap=layer_options.get('cmap','jet')
                if cmap=='my_cmap':
                    cmap=my_cmap()
                else:
                    plt.get_cmap(cmap)
                cax=axes.imshow(plot,vmin=vmin,vmax=vmax,origin='lower',interpolation='nearest',aspect='auto',extent=ext,cmap=cmap)
                if layer_options.get('colorbar'):
                    bar=fig.colorbar(cax)
                    if layer_options.get('bar_label') is not None:
                        bar_label=layer_options.get('bar_label')
                        if bar_label=='zaxis_texname':
                            bar_label=user.axes.get()[layer_zaxis]['texname']
                        bar.set_label(bar_label,fontsize=20)
                    if layer_options.get('zaxis_colorbar_ticks'):
                        ticks=layer_options.get('zaxis_colorbar_ticks')
                        ticks=user.axes.get()[layer_zaxis]['colorbar_ticks']
                        bar.set_ticks(ticks)
                    if layer_options.get('zaxis_colorbar_ticklabels'):
                        ticklabels=layer_options.get('zaxis_colorbar_ticklabels')
                        ticklabels=user.axes.get()[layer_zaxis]['colorbar_ticklabels']
                        bar.set_ticklabels(ticklabels)
            if layer_options.get('contours',False):
                plot=ma.masked_where(entries_plot==-1,plot)
                if layer_options.get('mask_dchi2_gt'):
                    dchi2_max=layer_options.get('mask_dchi2_gt')
                    chi2_minimum=layer_options.get('chi2_minimum',numpy.min(chi2_plot))
                    plot=ma.masked_where(chi2_plot>chi2_minimum+dchi2_max,plot)
                if layer_options.get('mask_dchi2_st'):
                    dchi2_min=layer_options.get('mask_dchi2_st')
                    chi2_minimum=layer_options.get('chi2_minimum',numpy.min(chi2_plot))
                    plot=ma.masked_where(chi2_plot<chi2_minimum+dchi2_min,plot)
                levels=layer_options.get('levels')
                colors=layer_options.get('contour_colors')
                if layer_options.get('dchi2_mode',False):
                    chi2_minimum=layer_options.get('chi2_minimum',numpy.min(plot))
                    plot=plot-chi2_minimum
                #for the contours, set 'empty' points to chi2=100
                plot[entries_plot==-1]=100
                #we want control over the segments, 
                #so we delete the contours for the plot and plot the segments individually
                cs=axes.contour(X,Y,plot,levels=levels)
                allsegs=cs.allsegs
                for level,color in zip(allsegs,colors):
                    for segment in level:
                        if len(segment)>layer_options.get('min_segment_length',0):
                            linestyle=layer_options.get('contour_linestyle')
                            axes.plot(segment[:,0],segment[:,1],c=color,linewidth=2,linestyle=linestyle)
                for coll in cs.collections:
                    coll.remove()
            if layer_options.get('plot_chi2_minimum',False):
                fill_color=layer_options.get('chi2_minimum_fill_color')
                edge_color=layer_options.get('chi2_minimum_edge_color')
                id=numpy.where((plot==numpy.min(plot)) & (entries_plot!=-1))
                axes.plot(X[id],Y[id],marker='*',color=fill_color,markeredgecolor=edge_color,
                        markersize=20,markeredgewidth=2,zorder=10,linestyle='none')
            if layer_options.get('plot_rowid',False):
                fill_color=layer_options.get('rowid_fill_color')
                edge_color=layer_options.get('rowid_edge_color')
                id=numpy.where(entries_plot==layer_options['plot_rowid'])
                axes.plot(X[id],Y[id],marker='*',color=fill_color,markeredgecolor=edge_color,
                        markersize=20,markeredgewidth=2,zorder=10,linestyle='none')
        print(figname)
        if figure_options.get('solid_dashed_contours_legend'):
            solid_label,dashed_label=figure_options['solid_dashed_contours_legend']
            solid_1 = plt.Line2D((0,1),(0,0), color='r',linewidth=2, linestyle='solid')
            solid_2 = plt.Line2D((0,1),(0,0), color='b',linewidth=2, linestyle='solid')
            dashed_1 = plt.Line2D((0,1),(0,0), color='r',linewidth=2, linestyle='dashed')
            dashed_2 = plt.Line2D((0,1),(0,0), color='b',linewidth=2, linestyle='dashed')
            bf1 = plt.Line2D((0,1),(0,0), color='g',marker='*',markeredgewidth=1.5,
                    markeredgecolor='g',markersize=15, linestyle='')
            bf2 = plt.Line2D((0,1),(0,0), color='none',marker='*',markeredgewidth=1.5,
                    markeredgecolor='g',markersize=15, linestyle='')
            handles=[solid_1,solid_2,dashed_1,dashed_2,bf1,bf2]
            dchi2_1,dchi2_2=r' $\Delta\chi^2=2.30$',r' $\Delta\chi^2=5.99$'
            labels=[solid_label+dchi2_1,solid_label+dchi2_2,dashed_label+dchi2_1,dashed_label+dchi2_2,
                    solid_label+' best fit',dashed_label+' best fit']
            axes.legend(handles,labels,loc='lower left',fontsize=10,numpoints=1,frameon=False)
        if figure_options.get('title'):
            axes.set_title(figure_options.get('title'),fontsize=20)
        plt.savefig(figname)
