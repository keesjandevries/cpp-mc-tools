#! /usr/bin/env python
import json

axes={
        'm0':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 4000. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'array_ids'  :1,
                }
            },
        'm12':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 4000. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'array_ids'  :2,
                }
            },
        'mh':{
            'binning':{
                'type'  :'linear',
                'low'   : 105. ,
                'high'  : 130. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'array_ids'  :30,
                }
            },
        'BsmmRatio':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 3. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'array_ids'  :14,
                },
            'function_name': 'bsmm_ratio',
            },
        }

spaces=[{
    'axes':['m0','m12'],
    'zaxes':['mh','BsmmRatio'],
    },
    { 'axes':'mh' }, 
    { 'axes':'BsmmRatio' }, 
    {'axes':'m0'}
        ]

with open('user/example_axes.json','w') as json_file:
    json.dump(axes,json_file,indent=3)
with open('user/example_spaces.json','w') as json_file:
    json.dump(spaces,json_file,indent=3)

