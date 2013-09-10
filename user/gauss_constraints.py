def get():
    return {
            'Mh125': {
                'function_name': 'gauss',
                'mu': 125.0,
                'sigmas': [1.0, 2.5],
                'observable_ids': {
                    'mc_old': 'mh'
                    },
                },
            'chi2Oh2': {
                'function_name': 'gauss',
                'mu': 0.1109,
                'sigmas': [0.0056, 0.012],
                'observable_ids': {
                    'mc_old': 'Oh^2',
                    'mcpp': ('Micromegas', 'Omega')
                    },
                },
            'chi2-Mt': {
                'function_name': 'gauss',
                'mu': 173.2,
                'sigmas': [0.78],
                'observable_ids': {
                    'mcpp':('SMINPUTS','in_Mt'),
                    },
                },
            'chi2-MZ': {
                'function_name': 'gauss',
                'mu':91.1875 ,
                'sigmas': [0.0021],
                'observable_ids': {
                    'mcpp':('SMINPUTS','mod_MZ'),
                    },
                },
            'chi2-Dalpha-had': {
                'function_name': 'gauss',
                'mu': 0.02756,
                'sigmas': [0.0001],
                'observable_ids': {
                    'mcpp':('SUSY-POPE', 'DAlpha_had_in'),
                    },
                },
            'g-2': {
                'function_name': 'gauss',
                'mu': 3.02e-09,
                'sigmas': [8.8e-10, 2e-10],
                'observable_ids': {
                    'mc_old': 'Delta(g-2)'
                    },
                },
            }
