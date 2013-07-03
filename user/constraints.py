def get_constraints():
    return {
        'Mh125':{
            'gauss_constraint':{
                'observable_ids' :{
                    'mc_old':'mh',
                    },
                'mu':125.,
                'sigmas':[1.0,2.5],
                'function_name':'gauss',
                },
            },
        'Oh2':{
            'gauss_constraint':{
                'observable_ids' :{
                    'mc_old':'Oh^2',
                    },
                'mu':0.1109,
                'sigmas':[ 0.0056, 0.012],
                'function_name':'gauss',
                },
            },
        'g-2':{
            'gauss_constraint':{
                'observable_ids' :{
                    'mc_old':'Delta(g-2)',
                    },
                'mu':3.02e-09,
                'sigmas':[ 8.8e-10, 2e-10],
                'function_name':'gauss',
                },
            },
        'mg_universal_limits':{
            'contour_constraint':{
                #for now directly give coordinates, later give file names
                'contours':[
                    {
                    'type':'UniversalLimits',
                    'coordinates':[
                            [0.,900.],
                            [400.,700.],
                            [450.,500.],
                            ]
                        },
                     ],
                'observable_ids':{
                    'mc_old':['neu1','gluino'],
                    },
                'function_name':'mg_universal_limits',
                },
            },
        'm3g_universal_limits':{
            'contour_constraint':{
                #for now directly give coordinates, later give file names
                'contours':[
                    {   
                    'type':'UniversalLimits',
                    'coordinates':[
                            [0.,500.],
                            [300.,400.],
                            ] 
                            },
                     ],
                'observable_ids':{
                    'mc_old':['neu1','sbottom1','sbottom2','stop1','stop2'],
                    },
                'function_name':'m3g_universal_limits',
                },
            },
        'universal_limits':{
            'contour_constraint':{
                #for now directly give coordinates, later give file names
                'contours':[
                    {
                    'type':'UniversalLimits',
                    'coordinates':[
                            [0.,900.],
                            [400.,700.],
                            [450.,500.],
                            ]
                        },
                    {   
                    'type':'UniversalLimits',
                    'coordinates':[
                            [0.,500.],
                            [300.,400.],
                            ] 
                            },
                     ],
                'observable_ids':{
                    'mc_old':['neu1','gluino','sbottom1','sbottom2','stop1','stop2'],
                    },
                'function_name':'universal_limits',
                },
            },
    }
