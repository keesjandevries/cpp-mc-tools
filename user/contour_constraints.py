def get():
    constraints={'chi2-{}'.format(name):details for name, details in contour_constraints.items()}
    return constraints

contour_constraints={
            'xenon100':{
                'observable_ids':{
                    'mcpp':[('MASS', 'MNeu(1)'),('Micromegas','sigma_p_si')],
                    'mc_old':['neu1','KOsigma_pp^SI']
                    },
                'contours':['xenon100_july_2012'],
                'function':'xenon100_jul_2012',
                },
            'xenon100_SpiN_unc':{
                'observable_ids':{
                    'mcpp':[('MASS', 'MNeu(1)'),('LSP scattering','s3out'),('LSP scattering','ss3out')] ,
                    },
                'contours':['xenon100_july_2012'],
                'function':'xenon100_jul_2012_Sigma_pi_N_unc',
                'info':'DONT USE: use 90CL instead. Only kept for compatibility'
                },
            'xenon100_90CL_ssi_unc':{
                'observable_ids':{
                    'mcpp':[('MASS', 'MNeu(1)'),('LSP scattering','s3out'),('LSP scattering','ss3out')] ,
                    },
                'contours':['xenon100_july_2012'],
                'function':'xenon100_Jul12_90CL_ssi_unc',
                },
            'lux131030_unc':{
                'observable_ids':{
                    'mcpp':[('MASS', 'MNeu(1)'),('LSP scattering','s3out'),('LSP scattering','ss3out')] ,
                    },
                'contours':['lux131030'],
                'function':'lux131030_90CL_ssi_unc',
                },
            'lux131030':{
                'observable_ids':{
                    'mcpp':[('MASS', 'MNeu(1)'),('LSP scattering','s3out')] ,
                    },
                'contours':['lux131030'],
                'function':'lux131030_90CL',
                },
            'MATANB':{
                'observable_ids':{
                    'mcpp':[('FeynHiggs', 'mA'),('MINPAR', 'TB')],
                    'mc_old':['MA','tanb'],
                    },
                'contours':['mc8_ma_tanb'],
                'function':'mc8_ma_tanb',
                },
            'atlas_susy2014_ma_tanb':{
                'observable_ids':{
                    'mcpp':[('FeynHiggs', 'mA'),('MINPAR', 'TB')],
                    'mc_old':['MA','tanb'],
                    },
                'contours':['atlas_susy2014_ma_tanb'],
                'function':'mc8_ma_tanb',
                },
            'atlas5_m0_m12':{
                'observable_ids':{
                    'mcpp':[('MINPAR', 'in_M0'),('MINPAR', 'in_M12')],
                    'mc_old':['m0','m12']
                    },
                'contours':['atlas_5fb_m0_m12'],
                'function':'m0_m12_power_4',
                },
            'atlas20_m0_m12':{
                'observable_ids':{
                    'mcpp':[('MINPAR', 'in_M0'),('MINPAR', 'in_M12')],
                    },
                'contours':['atlas_20fb_m0_m12'],
                'function':'m0_m12_power_4',
                },
            'atlas_ichep2014_m0_m12':{
                'observable_ids':{
                    'mcpp':[('MINPAR', 'in_M0'),('MINPAR', 'in_M12')],
                    },
                'contours':['atlas_ichep2014_m0_m12'],
                'function':'m0_m12_power_4',
                },
            'atlas20_m0_m12_pow8':{
                'observable_ids':{
                    'mcpp':[('MINPAR', 'in_M0'),('MINPAR', 'in_M12')],
                    },
                'contours':['atlas_20fb_m0_m12'],
                'function':'m0_m12_power_8',
                },
            'atlas_3000fb_14TeV_m0_m12':{
                'observable_ids':{
                    'mcpp':[('MINPAR', 'in_M0'),('MINPAR', 'in_M12')],
                    },
                'contours':['atlas_3000fb_14TeV_m0_m12'],
                'function':'m0_m12_power_4',
                },
            'atlas_putative_3000_msqr_mg':{
                'observable_ids':{
                    'mcpp': [('MASS', 'MGl'),('MASS', 'MSf(2,3,1)'),('MASS', 'MSf(2,3,2)'),
                        ('MASS', 'MSf(2,4,1)'),('MASS', 'MSf(2,4,2)')]
                    },
                'contours':['atlas_putative_3000fb_msqr_mg'],
                'function':'msqr_mg_power_4',
                },
            'mc8_bsmm':{
                'observable_ids':{
                    'mcpp':[('BPhysics','Psll')],
                    'mc_old':['bsmm'],
                    },
                'contours':['mc8_bsmm'],
                'function':'one_dim_chi2_lookup',
                },
            }
    #FIXME: tidy up
#    return {'m3g_universal_limits': {'contours': [{'coordinates': [[0.0, 500.0],
#                                                        [300.0, 400.0]],
#                                        'type': 'UniversalLimits'}],
#                          'function_name': 'm3g_universal_limits',
#                          'observable_ids': {'mc_old': ['neu1',
#                                                        'sbottom1',
#                                                        'sbottom2',
#                                                        'stop1',
#                                                        'stop2']}},
# 'mg_universal_limits': {'contours': [{'coordinates': [[0.0, 900.0],
#                                                       [400.0, 700.0],
#                                                       [450.0, 500.0]],
#                                       'type': 'UniversalLimits'}],
#                         'function_name': 'mg_universal_limits',
#                         'observable_ids': {'mc_old': ['neu1', 'gluino']}},
# 'universal_limits': {'contours': [{'coordinates': [[0.0, 900.0],
#                                                    [400.0, 700.0],
#                                                    [450.0, 500.0]],
#                                    'type': 'UniversalLimits'},
#                                   {'coordinates': [[0.0, 500.0],
#                                                    [300.0, 400.0]],
#                                    'type': 'UniversalLimits'}],
#                      'function_name': 'universal_limits',
#                      'observable_ids': {'mc_old': ['neu1',
#                                                    'gluino',
#                                                    'sbottom1',
#                                                    'sbottom2',
#                                                    'stop1',
#                                                    'stop2']}}}
#
