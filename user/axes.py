def get_axes():
    return {
        'chi2_mh':{
            'gauss_constraint':'Mh125',
            },
        'chi2_oh2':{
            'gauss_constraint':'Oh2',
            },
        'chi2_g-2':{
            'gauss_constraint':'g-2',
            },
        'chi2_jad':{
            'contour_constraint':'universal_limits',
            },
        'chi2_m3g_only':{
            'contour_constraint':'m3g_universal_limits',
            },
        'chi2_mg_only':{
            'contour_constraint':'mg_universal_limits',
            },
        'mstop1':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 6000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'stop1',
                }
            },
        'mg':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 6000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'gluino',
                }
            },
        'jadmg':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 1600. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'gluino',
                }
            },
        'msq12':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 5000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'msq12',
                }
            }, 
        'msq3' :{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'msq3',
                }
            },
        'jadmsq3' :{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 900. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'msq3',
                }
            },
        'msl'  :{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'msl',
                }
            },
        'A'    :{
            'binning':{
                'type'  :'linear',
                'low'   : -5000.,
                'high'  : 5000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'A',
                }
            },
        'M1'   :{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'M1',
                }
            },
        'M2'   :{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'M2',
                }
            },
        'M3'   :{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'M3',
                }
            },
        'in_mu':{
            'binning':{
                'type'  :'linear',
                'low'   : -5000.,
                'high'  : 5000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'in_mu',
                }
            },
        'in_ma':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'in_ma',
                }
            },
        'mneu1':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'neu1',
                }
            }, 
        'mneu1_900':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 900. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'neu1',
                }
            }, 
        'jadmgmneu1':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 1600. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'neu1',
                }
            }, 
        'jadmsq3mneu1':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 900. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'neu1',
                }
            }, 
        'chi2':{
            'binning':{
                'type'  :'linear',
                'low'   : 30. ,
                'high'  : 300. ,
                'nbins' : 500 ,
                },
            'vars_lookup' :{
                'array_id':0,
                }
            },
        'm0':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 4000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'m0',
                'mcpp':('MINPAR','M0'),
                }
            },
        'm12':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'m12',
                'mcpp':('MINPAR','M12'),
                }
            },
        'MA':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 4000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'MA',
                'mcpp' :('MASS','MA0'),
                }
            },
        'A0':{
            'binning':{
                'type'  :'linear',
                'low'   : -5000. ,
                'high'  : 5000. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
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
            'vars_lookup' :{
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
            'vars_lookup' :{
                'mc_old':'tanb',
                'mcpp' :('MINPAR','TB'),
                }
            },
        'mh':{
            'binning':{
                'type'  :'linear',
                'low'   : 105. ,
                'high'  : 130. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'mh',
                }
            },
        'ssmh':{
            'binning':{
                'type'  :'linear',
                'low'   : 105. ,
                'high'  : 130. ,
                'nbins' : 100 ,
                },
            'vars_lookup' :{
                'mc_old':'ssmh',
                }
            },
        'BsmmRatio':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 3. ,
                'nbins' : 100 ,
                },
            'vars_function' :{
                'observable_ids':{
                    'mc_old':'bsmm',
                },
                'name': 'bsmm_ratio',
             },
        },
        'm3g':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_function' :{
                'observable_ids':{
                    'mc_old':['stop1','stop2' ,  'sbottom1','sbottom2'],
                },
                'name': 'average',
             },
        },
        'm12g':{
            'binning':{
                'type'  :'linear',
                'low'   : 0. ,
                'high'  : 2500. ,
                'nbins' : 100 ,
                },
            'vars_function' :{
                'observable_ids':{
                    'mc_old':['squark_l','squark_r'],
                },
                'name': 'average',
             },
        },
        'mh2_m0^2_Ratio':{
            'binning':{
                'type'  :'linear',
                'low'   : -3. ,
                'high'  : 3. ,
                'nbins' : 100 ,
                },
            'vars_function' :{
                'observable_ids':{
                    'mc_old':['mh2','m0'],
                },
                'name': 'var1_over_var2_square',
             },
         },
        }
