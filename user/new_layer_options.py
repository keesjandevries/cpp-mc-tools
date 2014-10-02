{
'colz_dchi2':{
    'colz_options': {
        'vmin': 0,
        'vmax': 9,
        'dchi2_mode': True,
        'cmap_over': '0.75',
        'colorbar_options':{
            'label': r'$\Delta\chi^2$'
            },
        },
    },
'colz_chi2_20':{
    'colz_options': {
        'vmin': 20,
        'vmax': 30,
        'cmap_over': '0.75',
        'colorbar_options':{
            'label': r'$\chi^2$'
            },
        },
    },
'solid_contours_bf_21': {
    'min_chi2': 21.0,
    'contour_options': {
        'levels':[5.99, 2.30],
        'colors':['b','r'],
        'dchi2_mode': True,
        'linestyle':'solid',
        },
    },
'solid_contours': {
    'contour_options': {
        'levels':[5.99, 2.30],
        'colors':['b','r'],
        'dchi2_mode': True,
        'min_segment_length':10,
        'linestyle':'solid',
        },
    'chi2_minimum_options':{
        'fill_color':'g',
        'edge_color':'g',
        },
    },
'dashed_contours': {
    'contour_options': {
        'levels':[5.99, 2.30],
        'colors':['b','r'],
        'dchi2_mode': True,
        'min_segment_length':10,
        'linestyle':'dashed',
        },
    'chi2_minimum_options':{
        'fill_color':'none',
        'edge_color':'g',
        },
    },
'dotted_contours': {
    'contour_options': {
        'levels':[5.99, 2.30],
        'colors':['b','r'],
        'dchi2_mode': True,
        'min_segment_length':10,
        'linestyle':'dotted',
        },
    'chi2_minimum_options':{
        'fill_color':'none',
        'edge_color':'g',
        },
    },
'solid_contours_no_star': {
    'contour_options': {
        'levels':[5.99, 2.30],
        'colors':['b','r'],
        'dchi2_mode': True,
        'min_segment_length':10,
        'linestyle':'solid',
        },
    },
'stau_coannihilation': {
    'contourf_options': {
        'levels': [0.0, 0.15],
        'colors': ['red'],
        'alpha': 0.5,
        'mask_dchi2_gt': 6.1,
        },
    'contour_options': {
        'levels': [0.15],
        'colors': ['red'],
        'linestyle': 'dotted',
        'linewidth': 5.0,
        'mask_dchi2_gt': 6.1,
        'min_segment_length': 10,
        },
    },
'char_coannihilation': {
    'contourf_options': {
        'levels': [0.0, 0.1],
        'colors': ['green'],
        'alpha': 0.5,
        'mask_dchi2_gt': 6.1,
        },
    'contour_options': {
        'levels': [0.1],
        'colors': ['green'],
        'linestyle': 'dotted',
        'linewidth': 5.0,
        'mask_dchi2_gt': 6.1,
        'min_segment_length': 10,
        },
    },
'stop_coannihilation': {
    'contourf_options': {
        'levels': [0.0, 0.2],
        'colors': ['black'],
        'alpha': 0.5,
        'mask_dchi2_gt': 6.1,
        },
    'contour_options': {
        'levels': [0.2],
        'colors': ['black'],
        'linestyle': 'dotted',
        'linewidth': 5.0,
        'mask_dchi2_gt': 6.1,
        'min_segment_length': 10,
        },
    },
'a_funnel': {
    'contourf_options': {
        'levels': [0.0, 0.4],
        'colors': ['blue'],
        'alpha': 0.5,
        'mask_dchi2_gt': 6.1,
        },
    'contour_options': {
        'levels': [0.4],
        'colors': ['blue'],
        'linestyle': 'dotted',
        'linewidth': 5.0,
        'mask_dchi2_gt': 6.1,
        'min_segment_length': 10,
        },
    },
'focus_point': {
    'contourf_options': {
        'levels': [0.0, 0.3],
        'colors': ['cyan'],
        'alpha': 0.5,
        'mask_dchi2_gt': 6.1,
        },
    'contour_options': {
        'levels': [0.3],
        'colors': ['cyan'],
        'linestyle': 'dotted',
        'linewidth': 5.0,
        'mask_dchi2_gt': 6.1,
        'min_segment_length': 10,
        },
    },
}
