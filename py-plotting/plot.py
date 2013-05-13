#! /usr/bin/env python
import pylab
import matplotlib.pyplot as plt
import ROOT
import numpy
from numpy import ma
import matplotlib
import matplotlib.pyplot as plt
import rootplot.root2matplotlib as r2m
def plot_colors(hist,options={}):

    Za=ma.array(hist.content)
    default=options.get('default',1e6)
    Zm=ma.masked_where(Za>default, Za) #FIXME: there must be a better way of doing this

    palette=plt.get_cmap(options.get('cmap','jet'))
    palette.set_bad(alpha=0.0)

    # xmin, xmax, ymin, ymax
    ext=[hist.xedges[0],hist.xedges[-1],hist.yedges[0], hist.yedges[-1]]

    # collecting arguments
    imshow_args={
            'interpolation' : 'nearest',
            'extent'        : ext,
            'aspect'        : 'auto',
            'origin'        : 'lower',
            'cmap'          : palette,
            }
    # the real function call
    plot = plt.imshow(Zm,**imshow_args)
    # also plot the bar
    plt.colorbar(plot)

    plt.clim( *options.get("zrange",[30.,45.]) )

#f=r2m.RootFile('/vols/cms04/kjd110/nuhm1_mc8_boxes/bak_nuhm1-boxesmc8.root')
f=r2m.RootFile('/vols/cms04/kjd110/nuhm1_mc8_boxes_mh2/nuhm1-boxesmc8.root')
hist=f.get('m0_m12_chi2')
plot_colors(hist)

plotfile='plot.pdf'
print('saving plot: {}'.format(plotfile))
pylab.savefig(plotfile)
