#! /usr/bin/env python3
"""
This modules can be used to produce 2-d plots based on ouput of e.g.
"new_sqlite_make_plots.py".
"""
#python core
import copy
import argparse
#third party
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.image as mpimg
#private
import py_modules.CtypesWrappers as cw

def parse_args():
    """Function parses command line options"""
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            fromfile_prefix_chars='@')
    parser.add_argument('--rootfiles', nargs='+', help='define input root file')
    parser.add_argument('--axes-file', default='user/new_axes.py',
            help='Specify file that contains dictionary with axes')
    parser.add_argument('--spaces-axes',
            help='Plot all spaces specified by <path>:<key>')
    parser.add_argument('--axes', nargs=2, help='define inividual axes')
    parser.add_argument('--zaxes', nargs='+', default=['chi2'],
            help='zaxis as in the name of figures')
    parser.add_argument('--layer-options', default=[None], nargs='+',
            help='Plot layers with options as defined in <path>:<key>')
    parser.add_argument('--figure-options',
            help='Plot figure with options as defined in <path>:<key>')
    parser.add_argument('--prefix', help='prefix for figure name')
    parser.add_argument('--extension', help='extension for figuren name',
            default='pdf')
    return parser.parse_args()

def transparent_cmap(color, alpha=0.7):
    # create the color map
    opaque_color = col.colorConverter.to_rgba(color, alpha=alpha)
    transparent_color = col.colorConverter.to_rgba(color, alpha=0.0)
    cmaplist = [opaque_color, opaque_color]
    cmap = col.LinearSegmentedColormap.from_list('Custom cmap', cmaplist, 256)
    cmap.set_over(transparent_color)
    cmap.set_under(opaque_color)
    return cmap

def add_contour_legend_line(ax, y, linestyle, name, markercolor,
        contouralpha=1.0, markeralpha=1.0, linewidth=2, fontsize=15, 
        markeredgecolor='g'):
    ax.plot((0.5), (y), marker='*', linestyle='none', alpha=markeralpha,
            markeredgecolor=markeredgecolor, markersize=10, color=markercolor)
    ax.plot((1, 1.6), (y, y), linestyle=linestyle, color='r',
            linewidth=linewidth, alpha=contouralpha)
    ax.plot((2, 2.6), (y, y), linestyle=linestyle, color='b',
            linewidth=linewidth, alpha=contouralpha)
    ax.text(2.75, y, name, verticalalignment='center', fontsize=fontsize)
    return ax

def value_from_path_key(path_key):
    """
    Takes string of the form "/path/to/options.py:key" and returns corresponding
    value.
    """
    path, key = path_key.split(':')
    with open(path, 'r') as file:
        string = file.read()
        evaluated_dict = eval(string)
    return evaluated_dict[key]

def get_plot_options_list(rootfiles, axes_file, axes, spaces_axes, zaxes,
        layer_options, figure_options, prefix, extension):
    """
    Returns:
        list of dictionaries with agruments for produce_plot(...)
    """
    #get axes options dict
    with open(axes_file) as file:
        axes_options_dict = eval(file.read())
    #get list of axes for 2d plots
    if axes:
        axes_list = [axes]
    elif spaces_axes:
        axes_list = []
        spaces = value_from_path_key(spaces_axes)
        for space in spaces:
            if isinstance(space['axes'], list):
                if len(space['axes']) == 2:
                    axes_list.append(space['axes'])
    #if only one of rootfile, layer_option and/or zaxis is given: assume that
    #all layers will have the same rootfile, layer_option and/or zaxis
    nlayers = max([len(rootfiles), len(layer_options), len(zaxes)])
    if len(rootfiles) == 1:
        rootfiles = rootfiles*nlayers
    if len(layer_options) == 1:
        layer_options = layer_options*nlayers
    if len(zaxes) == 1:
        zaxes = zaxes*nlayers
    #get the figure options
    if figure_options:
        figure_options = value_from_path_key(figure_options)
    #put everything together
    plot_options_list = []
    # layer options list that need to be copied for each plot
    base_layer_options_list = []
    for opts in layer_options:
        if opts:
            base_layer_options_list.append(value_from_path_key(opts))
        else:
            print('ERROR: No layer options were given\nExiting')
            exit()
    #add zaxis names and rootfiles to layer options
    for i in range(nlayers):
        base_layer_options_list[i]['zaxis'] = zaxes[i]
        base_layer_options_list[i]['rootfile'] = rootfiles[i]
    for xaxis, yaxis in axes_list:
        figname = '{}_{}_{}_{}.{}'.format(prefix, xaxis, yaxis, zaxes[-1],
                extension)
        #get axes options
        axes_options = {}
        axes_options['xaxis_options'] = axes_options_dict[xaxis]
        axes_options['xaxis_options']['name'] = xaxis
        axes_options['yaxis_options'] = axes_options_dict[yaxis]
        axes_options['yaxis_options']['name'] = yaxis
        #get the layer options
        layer_options_list = copy.deepcopy(base_layer_options_list)
        plot_options_list.append({
            'figname': figname,
            'figure_options': figure_options,
            'axes_options': axes_options,
            'layer_options_list': layer_options_list,
            })
    return plot_options_list

def get_ax(fig, axes_rect, xaxis_options, yaxis_options):
    """
    Function taking care of labels, binning, ticks, log scale, etc.

    Arguments:
        axes_rect: list of four floats l, h, w, h that define the axes
        xaxis_options: dictionary as is 'user/axes.py'
        yaxis_options: dictionary as is 'user/axes.py'

    Returns:
        Axes instance which has been added to the fig
    """
    ax = fig.add_axes(axes_rect)
    ax.tick_params(axis='both', which='major', labelsize=20)
    #set labels
    xlabel = xaxis_options.get('texname', xaxis_options['name'])
    ylabel = yaxis_options.get('texname', yaxis_options['name'])
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    #options from binnin: xlim, ylim, log scale
    xbinning = xaxis_options['binning']
    ybinning = yaxis_options['binning']
    xlow, xhigh = xbinning['low'], xbinning['high']
    ylow, yhigh = ybinning['low'], ybinning['high']
    ax.set_xlim([xlow, xhigh])
    ax.set_ylim([ylow, yhigh])
    ax.set_xscale(xbinning['type'])
    ax.set_yscale(ybinning['type'])
    #ticks
    xticks = xaxis_options.get('xticks')
    yticks = yaxis_options.get('yticks')
    if xticks and xbinning['type'] == 'linear':
        ax.set_xticks(np.arange(xlow, xhigh*1.001, xticks))
    if yticks and ybinning['type'] == 'linear':
        ax.set_yticks(np.arange(ylow, yhigh*1.001, yticks))
    return ax

def get_bin_centres_from_axis_options(axis_options):
    """Function takes axis options and returns the 1d-array of bin edges."""
    bin_centres = None
    binning = axis_options['binning']
    nbins = binning['nbins']
    binning_type = binning['type']
    if binning_type == 'linear':
        low = binning['low']
        high = binning['high']
        bin_edges = np.linspace(low, high, nbins+1)
        bin_centres = (bin_edges[:-1] + bin_edges[1:])/2
    elif binning_type == 'log':
        low = np.log10(binning['low'])
        high = np.log10(binning['high'])
        half_bin = 0.5*(high-low)/nbins
        bin_centres = np.logspace(low+half_bin, high-half_bin, nbins)
    return bin_centres

def get_x_y_mesh(xaxis_options, yaxis_options):
    """Function takes x and y axis options and returns the meshgrid according to
    the bin centers."""
    xbin_centres = get_bin_centres_from_axis_options(xaxis_options)
    ybin_centres = get_bin_centres_from_axis_options(yaxis_options)
    #start figure
    return np.meshgrid(xbin_centres, ybin_centres)

def get_plot(rootfile, xaxis_options, yaxis_options, zaxis):
    """Function gets the 2d-numpy array from the rootfile"""
    nxbins = xaxis_options['binning']['nbins']
    nybins = yaxis_options['binning']['nbins']
    xaxis = xaxis_options['name']
    yaxis = yaxis_options['name']
    plotname = '_'.join([xaxis, yaxis, zaxis])
    return cw.get_2d_hist(rootfile, plotname, nxbins, nybins)

def get_overflow_edges(rootfile, xaxis_options, yaxis_options):
    """Function gets the 4 1d-numpy array corresponding to the overflow bins
    from the rootfile"""
    nxbins = xaxis_options['binning']['nbins']
    nybins = yaxis_options['binning']['nbins']
    xaxis = xaxis_options['name']
    yaxis = yaxis_options['name']
    plotname = '_'.join([xaxis, yaxis, 'chi2'])
    return cw.get_2d_overflow_edges(rootfile, plotname, nxbins, nybins)

def get_min_chi2(rootfile, xaxis_options, yaxis_options):
    """Function gets the minimum chi2 from the rootfile"""
    nxbins = xaxis_options['binning']['nbins']
    nybins = yaxis_options['binning']['nbins']
    xaxis = xaxis_options['name']
    yaxis = yaxis_options['name']
    plotname = '_'.join([xaxis, yaxis, 'chi2'])
    return cw.get_2d_hist_minimum(rootfile, plotname, nxbins, nybins)

def plot_contour(ax, zaxis_plot, chi2_plot, entries_plot, x_mesh, y_mesh,
        min_chi2,
        levels, colors, dchi2_mode=False, linewidth=2.0, alpha=1.0,
        linestyle='solid', min_segment_length=0, mask_dchi2_gt=None):
    """Function plots contours

    Return:
        Updated Axes instance
    """
    if dchi2_mode:
        zaxis_plot = zaxis_plot - min_chi2
    if mask_dchi2_gt:
        mask_criterium = chi2_plot - min_chi2 > mask_dchi2_gt
        zaxis_plot = np.ma.masked_where(mask_criterium, zaxis_plot)
    #we want control over the segments,
    #so we delete the contours for the plot and plot the segments individually
    cs = ax.contour(x_mesh, y_mesh, zaxis_plot, levels=levels)
    allsegs = cs.allsegs
    for i, level in enumerate(allsegs):
        for segment in level:
            if len(segment) > min_segment_length:
                ax.plot(segment[:, 0], segment[:, 1], linestyle=linestyle,
                    c=colors[i], alpha=alpha, linewidth=linewidth)
    for coll in cs.collections:
        coll.remove()
    return ax

def plot_contourf(ax, zaxis_plot, chi2_plot, entries_plot, x_mesh, y_mesh,
        min_chi2,
        levels, colors, alpha=1.0, mask_dchi2_gt=None):
    zaxis_plot = np.ma.masked_where(entries_plot == -1, zaxis_plot)
    if mask_dchi2_gt:
        mask_criterium = chi2_plot - min_chi2 > mask_dchi2_gt
        zaxis_plot = np.ma.masked_where(mask_criterium, zaxis_plot)
    ax.contourf(x_mesh, y_mesh, zaxis_plot, levels=levels, colors=colors,
            interpolation='nearest', alpha=alpha)
    return ax

def plot_colorbar(fig, cax, label=None, fontsize=20):
    bar = fig.colorbar(cax)
    if label:
        bar.set_label(label, fontsize=fontsize)
    return cax

def plot_colz(fig, ax, zaxis_plot, chi2_plot, entries_plot, x_mesh, y_mesh,
        min_chi2,
        cmap='jet', mask_dchi2_gt=None, alpha=1.0, vmin=None, vmax=None,
        interpolation='nearest', dchi2_mode=False, colorbar_options=None,
        cmap_over=None):
    ext = [np.min(x_mesh), np.max(x_mesh), np.min(y_mesh), np.max(y_mesh)]
    zaxis_plot = np.ma.masked_where((entries_plot == -1) | (chi2_plot > 1e9), 
            zaxis_plot)
    if mask_dchi2_gt:
        mask_criterium = chi2_plot - min_chi2 > mask_dchi2_gt
        zaxis_plot = np.ma.masked_where(mask_criterium, zaxis_plot)
    if isinstance(cmap, dict):
        transparent_cmap_options = cmap.get('transparent')
        if isinstance(transparent_cmap_options, dict):
            cmap = transparent_cmap(**transparent_cmap_options)
    else:
        cmap = plt.get_cmap(cmap)
    cmap.set_over(cmap_over)
    if dchi2_mode:
        zaxis_plot = zaxis_plot - min_chi2
    cax = ax.imshow(zaxis_plot, vmin=vmin, vmax=vmax, origin='lower',
            interpolation=interpolation, aspect='auto', extent=ext, cmap=cmap)
    if colorbar_options:
        cax = plot_colorbar(fig, cax, **colorbar_options)
    return ax

def plot_chi2_minimum(fig, ax, chi2_plot, entries_plot, chi2_min,
        chi2_overflow_edges, x_mesh, y_mesh,
        fill_color='g', edge_color='g', alpha=1.0):
    """
    Function plots a star for the  point of minimum chi2. If the minimum is
    outside the the  plot, then it plots the point with an arrow where it is
    hiding.

    Args:
        fig (Figure instance)
        ax (Axes instance)
        chi2_plot (2d numpy array)
        entries_plot (2d numpy array)
        chi2_min (float)
        chi2_overflow_edges (list of 4 1d numpy arrays)
        x_mesh (2d numpy array)
        y_mesh (2d numpy array)
        fill_color
        edge_color
        alpha

    Returns:
        updated Axes instance.
    """
    #if the minimum chi2 point is inside the plot simply plot it
    if np.min(chi2_plot) == chi2_min:
        point_id = np.where((chi2_plot == chi2_min) & (entries_plot != -1))
        ax.plot(x_mesh[point_id], y_mesh[point_id], marker='*',
                color=fill_color, alpha=alpha, markeredgecolor=edge_color,
                markersize=20, markeredgewidth=1, zorder=10, linestyle='none')
    #else plot an arrow that indicates where it is
    else:
        #first find the bin with minimum chi2
        for i in range(4):
            chi2_edge_min = np.min(chi2_overflow_edges[i])
            if chi2_edge_min == chi2_min:
                minimum_edge_number = i
                minimum_bin_number = np.where(chi2_overflow_edges[i] == \
                        chi2_min)[0][0]
        # in coordinates relative to the axes
        nxbins, nybins = chi2_plot.shape
        arrow_origin = [
                (minimum_bin_number/nxbins, 0.0),
                (minimum_bin_number/nxbins, 1.0),
                (0.0, minimum_bin_number/nybins),
                (1.0, minimum_bin_number/nybins),
                ][minimum_edge_number]
        # in absolute coordinates
        arrow_origin = ax.transAxes.transform(arrow_origin)
        # in figure coordinates
        arrow_origin = fig.transFigure.inverted().transform(arrow_origin)
        # define new axes
        x_arrow, y_arrow = arrow_origin
        arrow_rect = [
                [x_arrow-0.05, y_arrow, 0.1, -0.05],
                [x_arrow-0.05, y_arrow, 0.1, 0.05],
                [x_arrow, y_arrow-0.05, -0.05, 0.1],
                [x_arrow, y_arrow-0.05, 0.05, 0.1],
                ][minimum_edge_number]
        ax_arrow = fig.add_axes(arrow_rect, frameon=False)
        # switch off all the ticks
        ax_arrow.tick_params(which='both', bottom='off', left='off',
                right='off', top='off', labelbottom='off',
                labelleft='off')
        # draw arrow and star
        ax_arrow.set_ylim([-1.0, 1.0])
        ax_arrow.set_xlim([-1.0, 1.0])
        star_x, star_y, xy, xytext = [
                [-0.5, 0.0, (0.0, 0.8), (0.0, -0.8)],
                [-0.5, 0.0, (0.0, 0.8), (0.0, -0.8)],
                [0.0, 0.5, (0.8, 0.0), (-0.8, 0.0)],
                [0.0, 0.5, (0.8, 0.0), (-0.8, 0.0)],
                ][minimum_edge_number]
        ax_arrow.annotate('', xy=xy, xycoords='data',
                xytext=xytext, textcoords='data',
                arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc3"))
        ax_arrow.plot(star_x, star_y, marker='*', color=fill_color,
                alpha=alpha, markeredgecolor=edge_color,
                markersize=15, markeredgewidth=1, zorder=10,
                linestyle='none')
    return ax

def plot_contour_legend(fig, ax, legend_line_options_list=None, xmin=-2.0):
    pos = ax.get_position()
    l, b, w, h = pos.x0, pos.y0, pos.width, pos.height
    ax2 = fig.add_axes([l, b+h+0.01, w, 1-(b+h+0.04)], frameon=False)
    ax2.tick_params(which='both', bottom='off', left='off', right='off',
            top='off', labelbottom='off', labelleft='off')
    ax2.set_xlim([xmin, 8.0])
    ax2.set_ylim([0.5, len(legend_line_options_list) + 0.5])
    for legend_line_options in legend_line_options_list:
        ax2 = add_contour_legend_line(ax2, **legend_line_options)
    return ax

def plot_color_legend(ax, line_options_list=None, labels=None, 
        loc='lower center', ncol=1, markerscale=2.5):
    if line_options_list and labels:
        handles = []
        for line_options in line_options_list:
            handle = plt.Line2D((0,1),(0,0), **line_options)
            handles.append(handle)
        ax.legend(handles, labels, loc=loc, numpoints=1, frameon=False, 
                ncol=ncol, markerscale=markerscale)
    return ax

def plot_layer(fig, ax, xaxis_options, yaxis_options, rootfile, zaxis,
        colz_options=None, contour_options=None, chi2_minimum_options=None,
        contourf_options=None, min_chi2=None):
    """
    Function plots all layers

    Args:
        fig (Figure instance)
        ax (Axes instance)
        xaxis_options (dict)
        yaxis_options (dict)
        rootfile (string)
        zaxis (string)
        colz_options (dict)
        contour_options (dict)
        chi2_minimum_options (dict)

    Returns:
        updated Axes instance.
    """
    chi2_plot = get_plot(rootfile, xaxis_options, yaxis_options, 'chi2')
    entries_plot = get_plot(rootfile, xaxis_options, yaxis_options, 'entries')
    zaxis_plot = get_plot(rootfile, xaxis_options, yaxis_options, zaxis)
    chi2_overflow_edges = get_overflow_edges(rootfile, xaxis_options,
            yaxis_options)
    if not min_chi2:
        min_chi2 = get_min_chi2(rootfile, xaxis_options, yaxis_options)
    x_mesh, y_mesh = get_x_y_mesh(xaxis_options, yaxis_options)
    if contour_options:
        ax = plot_contour(ax, zaxis_plot, chi2_plot, entries_plot, x_mesh,
                y_mesh, min_chi2, **contour_options)
    if colz_options:
        ax = plot_colz(fig, ax, zaxis_plot, chi2_plot, entries_plot, x_mesh,
                y_mesh, min_chi2, **colz_options)
    if contourf_options:
        ax = plot_contourf(ax, zaxis_plot, chi2_plot, entries_plot, x_mesh,
                y_mesh, min_chi2, **contourf_options)
    if chi2_minimum_options:
        ax = plot_chi2_minimum(fig, ax, chi2_plot, entries_plot, min_chi2,
                chi2_overflow_edges, x_mesh, y_mesh, **chi2_minimum_options)
    return ax

def plot_image(ax, filename, alpha=1.0):
    img = mpimg.imread(filename)
#    img = img[::-1]
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.imshow(img, zorder=0, aspect='auto', extent=[xmin, xmax, ymin, ymax], 
            interpolation='nearest', alpha=alpha)
    return ax

def plot_figure_options(fig, ax,
        contour_legend_options=None, color_legend_options=None, 
        image_options=None, **kwargs):
    if contour_legend_options:
        ax = plot_contour_legend(fig, ax, **contour_legend_options)
    if color_legend_options:
        ax = plot_color_legend(ax, **color_legend_options)
    if image_options:
        ax = plot_image(ax, **image_options)
    return ax

def produce_plot(figname, figure_options, axes_options, layer_options_list):
    """
    Function that produces each individual plot of the list provided by
    get_plot_options_list().
    """
    if figure_options is None:
        figure_options = {}
    figsize = figure_options.get('figsize', [8, 6])
    axes_rect = figure_options.get('axes_rect', [0.17, 0.15, 0.77, 0.75])
    fig = plt.figure(figsize=figsize)
    ax = get_ax(fig, axes_rect=axes_rect, **axes_options)
    xaxis_options = axes_options['xaxis_options']
    yaxis_options = axes_options['yaxis_options']
    #loop over layers to produce the plot
    for layer_options in layer_options_list:
        ax = plot_layer(fig, ax, xaxis_options, yaxis_options, **layer_options)
    ax = plot_figure_options(fig, ax, **figure_options)
    print(figname)
    transparent = figure_options.get('transparent', False)
    plt.savefig(figname, transparent=transparent)

def main(main_options):
    """
    'main' function gets executed when this module is run standalone
    """
    plot_options_list = get_plot_options_list(**main_options)
    for plot_options in plot_options_list:
        produce_plot(**plot_options)

if __name__ == "__main__":
    MAIN_OPTIONS = vars(parse_args())
    main(MAIN_OPTIONS)
