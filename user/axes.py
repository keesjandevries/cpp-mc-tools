def get_axes():
    return {
        'm0':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 4000. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'mc_old':'m0',
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
                'mc_old':'m12',
                }
            },
        'MA':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 4000. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'mc_old':'MA',
                }
            },
        'A0':{
            'binning':{
                'type'  :'linear',
                'low'   : -5000. ,
                'high'  : 5000. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'mc_old':'A0',
                }
            },
        'mh2':{
            'binning':{
                'type'  :'linear',
                'low'   : -1e7 ,
                'high'  : 1e7 ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'mc_old':'mh2',
                }
            },
        'tanb':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 60. ,
                'nbins' : 100 ,
                },
            'observable_ids' :{
                'mc_old':'tanb',
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
                'mc_old':'mh',
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
                'mc_old':'bsmm',
                },
            'function_name': 'bsmm_ratio',
            },
        }
