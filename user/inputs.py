def get(name):
    return parameters.get(name)

parameters={
        'cmssm':['m0','m12','tanb','A0','mtop','mz','Delta_alpha_had' ],
        'nuhm1':['m0','m12','tanb','A0','mh2','mtop','mz','Delta_alpha_had' ],
        'nuhm2':['m0','m12','tanb','A0','mhd2','mhu2','mtop','mz','Delta_alpha_had' ],
#        'pmssm10':['msq12','msq3','msl','A','M1','M2','M3','in_ma','in_mu','tanb','mtop','mz','Delta_alpha_had']
        'pmssm10':['msq12','msq3','msl','M1','M2','M3','A','in_ma','tanb','in_mu','mtop','mz','Delta_alpha_had'],
        }
