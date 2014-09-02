#! /usr/bin/env python
import argparse
import numpy as np
import matplotlib.pyplot as plt
import py_modules.CtypesWrappers as cw

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rootfile')
    parser.add_argument('--axes-file', default='user/new_axes.py')
    parser.add_argument('--main-axis')
    parser.add_argument('--other-axes', nargs='+')
    parser.add_argument('--prefix')
    parser.add_argument('--max-mass', type=float)
    parser.add_argument('--max-chi2', type=float, default=45)
    return parser.parse_args()

def plot_axes_range(ax, i, low, high):
    low = round(float(low))
    high = round(float(high))
    ax.annotate(low, xy=(i, 0),  xycoords='data', 
             xytext=(i+0.05, -0.10), textcoords='data', 
             arrowprops=dict(arrowstyle="->"))
    ax.annotate(high, xy=(i, 1),  xycoords='data', 
             xytext=(i+0.05, 1+0.10), textcoords='data', 
             arrowprops=dict(arrowstyle="->"))
    return ax

def main(rootfile, axes_file, main_axis, other_axes, prefix, max_mass, max_chi2):
    plot_content = {}
    with open(axes_file, 'r') as file:
        all_axes = eval(file.read())
    main_axis_details = all_axes[main_axis]
    binning = main_axis_details['binning'] 
    nbins = binning['nbins']
    main_entries = cw.get_1d_hist(rootfile, '{}_entries'.format(main_axis), 
            nbins)
    main_chi2 = cw.get_1d_hist(rootfile, '{}_chi2'.format(main_axis), 
            nbins)
    for axis in other_axes:
        plot_name = '{}_{}'.format(main_axis, axis)
        plot = cw.get_1d_hist(rootfile, plot_name, nbins)
        plot_content[axis] = plot
    cmap = plt.get_cmap('jet')
    fig = plt.figure()
    ax = fig.add_axes([0.17, 0.15, 0.77, 0.75])
    for i in range(nbins):
        if main_entries[i] != -1 and main_chi2[i] < max_chi2:
            line = [i/nbins]
            for j, axis in enumerate(other_axes):
                plot = plot_content[axis]
                if max_mass:
                    min_obs, max_obs = 0, max_mass 
                else:
                    min_obs, max_obs = np.min(plot), np.max(plot)
                value = (plot[i] - min_obs)/(max_obs - min_obs)
                line.append(value)
            ax.plot(line, c=cmap(i/nbins), marker='.')
    n_other_axes = len(other_axes)
    ax.set_xlim([-0.5, n_other_axes+0.5]) 
    ax.set_ylim([-0.15, 1.15]) 
    pos = range(n_other_axes+1)
    axes = [main_axis]+other_axes 
    ticknames = []
    for axis in axes:
        texname = all_axes[axis].get('texname')
        if texname:
            texname = texname.replace('[GeV]','')
            ticknames.append(texname)
        else:
            ticknames.append(axis)
    ax.set_xticks(pos)
    ax.set_yticks([])
    ax.set_xticklabels(ticknames, fontsize=25)
    for i in range(n_other_axes+1):
        ax.axvline(x=i, ymin=0.0, ymax=1.0 , color='k', linestyle='dashed')
    ax = plot_axes_range(ax, 0, binning['low'], binning['high'])
    for i, axis in enumerate(other_axes):
        plot = plot_content[axis]
        if max_mass:
            min_obs, max_obs = 0, max_mass 
        else:
            min_obs, max_obs = np.min(plot), np.max(plot)
        ax = plot_axes_range(ax, i+1, min_obs, max_obs)

    figname = '{}_{}_correlations.pdf'.format(prefix, main_axis)
    print(figname)
    plt.savefig(figname)


if __name__ == '__main__':
    MAIN_OPTIONS = vars(parse_args())
    main(**MAIN_OPTIONS)
