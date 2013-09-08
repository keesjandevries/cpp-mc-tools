def get():
    return{
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
                    'mcpp': ('Micromegas', 'sigma_p_si')
                    }
                },
            'ssikocm2': {
                'name': 'pb_to_cm2',
                'observable_ids': {
                    'mcpp': ('LSP scattering', 's3out')
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
                'name': 'average',
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
                        'mc_old': ['mstop2','mstop1'],
                        'mcpp': [('MASS', 'MSf(2,3,3)'),('MASS', 'MSf(1,3,3)')]
                        }
                    }
            }

