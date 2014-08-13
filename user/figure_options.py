def get():
    return {
            'get_chi2_eq_4_limit':{
                'chi2_eq_4_limit':True,
                },
            'preliminary':{
                'text_box':[
                    {
                    'args':[0.05,0.95,'Not even preliminary!!'],
                    },
                    ]
                },
            'preliminary_1d':{
                'text_boxes':[
                    {
                    'args':[0.95,0.97,'Not even preliminary!!'],
                    'kwargs':{'horizontalalignment':'right'}
                    }
                    ],
                },
            'mc9lux_legend':{
                'solid_dashed_contours_legend':['ATLAS8','ATLAS7']
                },
            'pmssm_workshop_legend':{
                'solid_dashed_contours_legend':['w LHC@7TeV','w/o LHC@7TeV']
                },
            'Mitesh_legend':{
                'solid_dashed_contours_legend':[r'w $B_s\to\mu\mu$',r'w/o $B_s\to\mu\mu$'],
                'title':'cMSSM July 2012',
                },
            'transparent':{
                'transparent':True
                },
            'snowmass':{
                'snowmass':True
                },
            'g-2':{
                'vertical_line': {
                    'x':0.0,
                    'color':'g'
                    },
                'experimental_band': {
                    'min': 2.117e-9 , 
                    'max': 3.922e-9, 
                    },
                },
            'mc10_g-2':{
                'legend': [
                    {
                        'label': 'NUHM2',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'solid',
                            },
                        },
                    {
                        'label': 'NUHM1',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dashed',
                            },
                        },
                    {
                        'label': 'CMSSM',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dotted',
                            },
                        },
                    {
                        'label': 'constraint',
                        'line_2d_kwargs': {
                            'color': 'r',
                            },
                        },
                    ],
                'g-2_constraint': True,
#                'text_boxes':[
#                        {'args':[0.48,0.05,'measurement'],
#                        'kwargs':{'horizontalalignment':'left','fontsize':12},
#                        }
#                    ],
#                'experimental_band': {
#                    'min': 2.117e-9 , 
#                    'max': 3.922e-9, 
#                    },
                },
            'mc10-1d-nuhm2-nuhm1-cmssm-legends':{
                'legend': [
                    {
                        'label': 'NUHM2',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'solid',
                            },
                        },
                    {
                        'label': 'NUHM1',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dashed',
                            },
                        },
                    {
                        'label': 'CMSSM',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dotted',
                            },
                        },
                    ]
                
                },
            'bsmm_ratio_band':{
                'experimental_band': {
                    'min': 0.720720720721,
                    'max': 1.12912912913
                    },
                'legend': [
                    {
                        'label': 'NUHM2',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'solid',
                            },
                        },
                    {
                        'label': 'NUHM1',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dashed',
                            },
                        },
                    {
                        'label': 'CMSSM',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dotted',
                            },
                        },
                    {
                        'label': 'pMSSM10',
                        'line_2d_kwargs': {
                            'color': 'k',
                            'linewidth': 2,
                            'linestyle': 'solid',
                            },
                        },
                    {
                        'label': 'measurement',
                        'patch_kwargs': {
                            'color': 'r',
                            'alpha': 0.5,
                            },
                        },
                    ],
                },
            'bsmm_ratio_constraint':{
                'bsmm_ratio_constraint': True,
                'legend': [
                    {
                        'label': 'NUHM2',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'solid',
                            },
                        },
                    {
                        'label': 'NUHM1',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dashed',
                            },
                        },
                    {
                        'label': 'CMSSM',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dotted',
                            },
                        },
                    {
                        'label': 'pMSSM10',
                        'line_2d_kwargs': {
                            'color': 'k',
                            'linewidth': 2,
                            'linestyle': 'solid',
                            },
                        },
                    {
                        'label': 'constraint',
                        'line_2d_kwargs': {
                            'color': 'r',
                            },
                        },
                    ],
                },
            'mc10_bsmm_ratio_constraint':{
                'bsmm_ratio_constraint': True,
                'legend': [
                    {
                        'label': 'NUHM2',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'solid',
                            },
                        },
                    {
                        'label': 'NUHM1',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dashed',
                            },
                        },
                    {
                        'label': 'CMSSM',
                        'line_2d_kwargs': {
                            'color': 'b',
                            'linewidth': 2,
                            'linestyle': 'dotted',
                            },
                        },
                    {
                        'label': 'constraint',
                        'line_2d_kwargs': {
                            'color': 'r',
                            },
                        },
                    ],
                },
            'mc10-contours':{
                'legend':{ 
                    'handles_labels': [
                        {
                            'label': r'$1\/\sigma$',
                            'line_2d_kwargs': {
                                'color': 'r',
                                'linewidth': 2,
                                'linestyle': 'solid',
                                },
                            },
                        {
                            'label': r'$2\/\sigma$',
                            'line_2d_kwargs': {
                                'color': 'b',
                                'linewidth': 2,
                                'linestyle': 'solid',
                                },
                            },
                        {
                            'label': 'best fit',
                            'line_2d_kwargs': {
                                'markeredgecolor': 'g',
                                'markersize': 15,
                                'color': 'g',
                                'marker': '*',
                                'linestyle': 'none'
                                },
                            },
                        ],
                    }
                },
            'mc10-contours-v2':{
                'legend':{ 
                    'handles_labels': [
                        {
                            'label': '',
                            'line_2d_kwargs': {
                                'markeredgecolor': 'g',
                                'markersize': 15,
                                'color': 'g',
                                'marker': '*',
                                'linestyle': 'none'
                                },
                            },
                        {
                            'label': '',
                            'line_2d_kwargs': {
                                'markeredgecolor': 'g',
                                'markersize': 15,
                                'color': 'lightgreen',
                                'marker': '*',
                                'linestyle': 'none'
                                },
                            },
                        {
                            'label': '',
                            'line_2d_kwargs': {
                                'color': 'r',
                                'linewidth': 2,
                                'linestyle': 'solid',
                                },
                            },
                        {
                            'label': '/',
                            'line_2d_kwargs': {
                                'color': 'b',
                                'linewidth': 2,
                                'linestyle': 'dashed',
                                },
                            },
                        {
                            'label': '',
                            'line_2d_kwargs': {
                                'color': 'b',
                                'linewidth': 2,
                                'linestyle': 'solid',
                                },
                            },
                        {
                            'label': '',
                            'line_2d_kwargs': {
                                'markeredgecolor': 'g',
                                'markersize': 15,
                                'color': 'w',
                                'marker': '*',
                                'linestyle': 'none'
                                },
                            },
                        {
                            'label': r'NUHM2: best fit, $1\sigma$, $2\sigma$',
                            'line_2d_kwargs': {
                                'color': 'w',
                                'linewidth': 2,
                                },
                            },
                        {
                            'label': r'NUHM1 / CMSSM: best fit, $2\sigma$',
                            'line_2d_kwargs': {
                                'color': 'b',
                                'linewidth': 2,
                                'linestyle': 'dotted',
                                },
                            },
                        ],
                    'kwargs':{
                        'bbox_to_anchor': (0., 1.02, 1., .102),
                        'ncol': 4,
                        'fontsize': 10,
                        'loc': 'center',
                        },
                    },
                },
                'mc10-nuhm2-nuhm1-cmssm-contours-legend':{
                        'figsize': [8,7],
                        'axes_rect':[0.17, 0.15, 0.77, 0.70],
                        'custom_legend':{
                            'legend_line_kwargs':[
                                {
                                    'y':3, 
                                    'linestyle':'solid', 
                                    'markercolor': 'g',
                                    'name':r'NUHM2: best fit, $1\sigma$, $2\sigma$',
                                    },
                                {
                                    'y':2, 
                                    'linestyle':'dashed', 
                                    'markercolor': 'lightgreen',
                                    'name':r'NUHM1: best fit, $1\sigma$, $2\sigma$',
                                    'linewidth': 1,
                                    'contouralpha': 0.5,
                                    'markeralpha': 0.5,
                                    },
                                {
                                    'y':1, 
                                    'linestyle':'dotted', 
                                    'markercolor': 'none',
                                    'name':r'CMSSM: best fit, $1\sigma$, $2\sigma$',
                                    'linewidth': 1,
                                    'contouralpha': 0.5,
                                    'markeralpha': 0.5,
                                    },
                                ]
                            }
                    },
                'mc10-nuhm2-nuhm1-cmssm-contours-legend-snowmass':{
                        'figsize': [8,7],
                        'axes_rect':[0.17, 0.15, 0.77, 0.70],
                        'text_boxes':[
                            {'args':[0.05,0.97,'LUX & Xenon100 excluded'],
                            'kwargs':{'horizontalalignment':'left','fontsize':12}
                            },
                            {'args':[0.95,0.07,'atmospheric neutrinos'],
                                'kwargs':{'horizontalalignment':'right','fontsize':12}
                            },
                            ],
                        'snowmass': True,
                        'custom_legend':{
                            'legend_line_kwargs':[
                                {
                                    'y':3, 
                                    'linestyle':'solid', 
                                    'markercolor': 'g',
                                    'name':r'NUHM2: best fit, $1\sigma$, $2\sigma$',
                                    },
                                {
                                    'y':2, 
                                    'linestyle':'dashed', 
                                    'markercolor': 'lightgreen',
                                    'name':r'NUHM1: best fit, $1\sigma$, $2\sigma$',
                                    'linewidth': 1,
                                    'contouralpha': 0.5,
                                    'markeralpha': 0.5,
                                    },
                                {
                                    'y':1, 
                                    'linestyle':'dotted', 
                                    'markercolor': 'none',
                                    'name':r'CMSSM: best fit, $1\sigma$, $2\sigma$',
                                    'linewidth': 1,
                                    'contouralpha': 0.5,
                                    'markeralpha': 0.5,
                                    },
                                ]
                            }
                    },
                'mc10-nuhm2-contours-legend':{
                        'figsize': [8,7],
                        'axes_rect':[0.17, 0.15, 0.77, 0.70],
                        'custom_legend':{
                            'legend_line_kwargs':[
                                {
                                    'y':1, 
                                    'linestyle':'solid', 
                                    'markercolor': 'g',
                                    'name':r'NUHM2: best fit, $1\sigma$, $2\sigma$',
                                    },
                                ]
                            }
                    },
            }



