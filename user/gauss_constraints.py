def get():
    return {
            'Mh125': {
                'function_name': 'gauss',
                'mu': 125.0,
                'sigmas': [1.0, 2.5]
                'observable_ids': {
                    'mc_old': 'mh'
                    },
                },
            'Oh2': {'function_name': 'gauss',
                'mu': 0.1109,
                'observable_ids': {
                    'mc_old': 'Oh^2',
                    'mcpp': ('Micromegas', 'Omega')
                    },
                'sigmas': [0.0056, 0.012]
                },
            'g-2': {
                'function_name': 'gauss',
                'mu': 3.02e-09,
                'sigmas': [8.8e-10, 2e-10]
                'observable_ids': {
                    'mc_old': 'Delta(g-2)'
                    },
                }
            }
