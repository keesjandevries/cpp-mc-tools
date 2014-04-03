def get(name):
    return observables.get(name)

observables={
        'usual':['mneu1','MA','MHp','mstau1','mstop1','mchar1','mu','msqr','ssikocm2','Dssikocm2','mh','Dmh','mg','bsmm','chi2-chi2'],
        'mc9-table2': [ 'chi2-{}'.format(constraint) for constraint in [ 
 'mc9_R_B->Xsg',
 'mc9_R_B->taunu',
 'mc9_epsilon_K',
 'gminus2mu',
 'MW',
 'mc9_Mh',
 'Rl',
 'Afb(b)',
 'Al(SLD)',
 'sigma_had^0',
 'lux131030_unc',
 'atlas20_m0_m12',
 'RmmNov13_mc9',
            ]],
        'EWPO':[
 'MW',
 'Gamma_Z',
 'sigma_had^0',
 'Rl',
 'Afb_l',
 'Al',
 'sintheta_eff',
 'Ac',
 'Ab',
 'Afb(c)',
 'Afb(b)',
 'Rc',
 'Rb',
 'DAlpha_had',
            ],
        'EWPO_TLEP':[
 'mz',
 'Gamma_Z',
 'Rl',
 'Rb',
 'Al',
 'MW',
 'mtop',
 'sintheta_eff'
            ],
        }
