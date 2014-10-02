def get(name):
    return parameters.get(name)

parameters={
        'sigma-m3g':['sigma_m3g'],
        'mg-m12g-m3g':['mg','m12g','m3g'],
        'mg-m12g-m3g_new':['mg','m12g','m3g_new'],
        'mneu1-mg-m12g-m3g':['mneu1','mg','m12g','m3g'],
        'mneu1-mg-m12g-m3g_new':['mneu1','mg','m12g','m3g_new'],
        'pmssm10':['msq12','msq3','msl','M1','M2','M3','A','in_ma','tanb','in_mu','mtop','mz','Delta_alpha_had'],
        'cmssm':['m0','m12','tanb','A0','mtop','mz','Delta_alpha_had' ],
        'mneu1-mg-m12gs-m3gs':['mneu1','mg','msuL','mscL','msdL','mssL','msuR','mscR','msdR','mssR','msbot1','msbot2','mstop1','mstop2'],
        'lhc8':['mneu1','mg','m12g','m3g','chi2-universal_limits_8TeV'],
        }

