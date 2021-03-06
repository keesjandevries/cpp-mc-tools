def get():
    return{
            'stau_coannihilation_measure':{
                'name':'coannihilation_measure',
                'observable_ids':{
                    'mcpp':[('MASS', 'MSf(1,2,3)'), ('MASS','MNeu(1)')]
                    },
                },
            'stop_coannihilation_measure':{
                'name':'coannihilation_measure',
                'observable_ids':{
                    'mcpp':[('MASS', 'MSf(1,3,3)'), ('MASS','MNeu(1)')]
                    },
                },
            'neu2_coannihilation_measure':{
                'name':'coannihilation_measure',
                'observable_ids':{
                    'mcpp':[('MASS', 'MNeu(2)'), ('MASS','MNeu(1)')]
                    },
                },
            'char_coannihilation_measure':{
                'name':'coannihilation_measure',
                'observable_ids':{
                    'mcpp':[('MASS', 'MCha(1)'), ('MASS','MNeu(1)')]
                    },
                },
            'A_funnel_measure':{
                'name':'funnel_measure',
                'observable_ids':{
                    'mcpp':[('MASS', 'MA0'), ('MASS','MNeu(1)')]
                    },
                },
            'focus_point_measure': {
                'name': 'abs_var1_over_var2',
                'observable_ids': {
                    'mcpp': [('HMIX', 'MUE'), ('MASS','MNeu(1)'), ('MASS', 'MA0')],
                    }
                },
            'Xt':{
                'name':'var1_minus_var2_over_var3',
                'observable_ids': {
                    'mcpp':[('AU','Af(3,3)'),('HMIX','MUE'),('HMIX','TB')],
                    },
                },
            'abs_mneu1': {
                'name': 'abs',
                'observable_ids': {
                    'mcpp':[('MASS', 'MNeu(1)')],
                    }
                },
            'abs_mneu2': {
                'name': 'abs',
                'observable_ids': {
                    'mcpp':[('MASS', 'MNeu(2)')],
                    }
                },
            'abs_mg': {
                'name': 'abs',
                'observable_ids': {
                    'mcpp':[('MASS', 'MGl')],
                    }
                },
            'abs_mchar1': {
                'name': 'abs',
                'observable_ids': {
                    'mcpp':[('MASS', 'MCha(1)')],
                    }
                },
            'A0_over_m0': {
                'name': 'var1_over_var2',
                'observable_ids': {
                    'mc_old': ['A0', 'm0']
                    }
                },
            'BsmmRatio': {
                'name': 'bsmm_ratio',
                'observable_ids': {
                    'mc_old': 'bsmm',
                    'mcpp': ('BPhysics', 'Psll')
                    }
                },
            'C9': {
                'name': 'C9_straub',
                'observable_ids': {
                    'mc_old': ['mtop', 'mH+-', 'tanb']
                    }
                },
            'ssicm2': {
                'name': 'pb_to_cm2',
                'observable_ids': {
                    'mc_old': 'sigma_pp^SI',
                    'mcpp': ('Micromegas', 'sigma_p_si'),
                    }
                },
            'ssikocm2': {
                'name': 'pb_to_cm2',
                'observable_ids': {
                    'mcpp': ('LSP scattering', 's3out'),
                    'mc_old': 'KOsigma_pp^SI',
                    }
                },
            'Dssikocm2': {
                'name': 'pb_to_cm2',
                'observable_ids': {
                    'mcpp': ('LSP scattering', 'ss3out'),
                    }
                },
            'm12g': {
                'name': 'average',
                'observable_ids': {
                    'mc_old': ['squark_l', 'squark_r'],
                    'mcpp': [('MASS', 'MSf(1,3,1)'), ('MASS', 'MSf(1,3,2)'),('MASS', 'MSf(1,4,1)'),('MASS', 'MSf(1,4,2)'),
                        ('MASS', 'MSf(2,3,1)'),('MASS', 'MSf(2,3,2)'),('MASS', 'MSf(2,4,1)'),('MASS', 'MSf(2,4,2)')]
                    }
                },
            'm3g': {
                'name': 'm3g',
                'observable_ids': {
                    'mc_old': ['stop1','stop2','sbottom1','sbottom2'],
                    'mcpp': [('MASS', 'MSf(1,3,3)'),('MASS', 'MSf(2,3,3)'),('MASS', 'MSf(1,4,3)'),('MASS', 'MSf(2,4,3)')]
                    }
                },
            'm3g_new': {
                'name': 'power_4_weighted_average',
                'observable_ids': {
                    'mc_old': ['stop1','stop2','sbottom1','sbottom2'],
                    'mcpp': [('MASS', 'MSf(1,3,3)'),('MASS', 'MSf(2,3,3)'),('MASS', 'MSf(1,4,3)'),('MASS', 'MSf(2,4,3)')]
                    }
                },
            'sigma_m3g': {
                'name': 'standard_deviation',
                'observable_ids': {
                    'mc_old': ['stop1','stop2','sbottom1','sbottom2'],
                    'mcpp': [('MASS', 'MSf(1,3,3)'),('MASS', 'MSf(2,3,3)'),('MASS', 'MSf(1,4,3)'),('MASS', 'MSf(2,4,3)')]
                    }
                },
            'mh2_m0^2_Ratio': {
                'name': 'var1_over_var2_square',
                'observable_ids': {
                    'mc_old': ['mh2', 'm0']
                    }
                },
            'mh_over_m0': {
                    'name': 'sqrt_var1_over_var2',
                    'observable_ids': {
                        'mc_old': ['mh2', 'm0']
                        }
                    },
            'msqr': {
                    'name': 'average',
                    'observable_ids': {
                        'mc_old': ['squark_r'],
                        'mcpp': [('MASS', 'MSf(2,3,1)'),('MASS', 'MSf(2,3,2)'),('MASS', 'MSf(2,4,1)'),('MASS', 'MSf(2,4,2)')]
                        }
                    },
            'mstop2-mstop1': {
                    'name': 'difference',
                    'observable_ids': {
                        'mc_old': ['stop2','stop1'],
                        'mcpp': [('MASS', 'MSf(2,3,3)'),('MASS', 'MSf(1,3,3)')]
                        }
                    },
            'mstau1-mneu1': {
                    'name': 'difference',
                    'observable_ids': {
                        'mcpp': [('MASS', 'MSf(1,2,3)'),('MASS', 'MNeu(1)')],
                        }
                    },
            'mchar1-mneu1': {
                    'name': 'difference',
                    'observable_ids': {
                        'mcpp': [('MASS', 'MCha(1)'),('MASS', 'MNeu(1)')],
                        }
                    },
            'MA-2mneu1': {
                    'name': 'x_minus_2y',
                    'observable_ids': {
                        'mcpp': [('MASS', 'MA0'),('MASS', 'MNeu(1)')],
                        }
                    },
            'fh-ss': {
                    'name': 'difference',
                    'observable_ids': {
                        'mcpp': [('FeynHiggs', 'mh'),('MASS', 'Mh0')]
                        }
                    },
            'A0_ko': {
                    'name':'negative',
                    'observable_ids': {
                        'mcpp': [('MINPAR', 'in_A')],
                        },
                    }
            }

