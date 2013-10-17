def get_spaces(choice=None):
    if choice is not None:
        try:
            return spaces[choice]
        except KeyError:
            print('spaces option \"{}\" not in user/spaces.py'.format(choice))
    else:
    #    return spaces['cmssm']
    #    return spaces['nuhm1']
        return spaces['pmssm']

spaces={
    'pmssm-chi2-slices': [
        {'axes':'pmssm-mc9-chi2','zaxes':['msq3','msq12','msl','M1','M2','M3','A','in_ma','tanb','in_mu','mt','mz','Delta_alpha_had']},
        ],
    'cmssm-chi2-slices': [
        {'axes':'cmssm-mc9-chi2','zaxes':['m0','m12','A0','tanb','mt','mz','Delta_alpha_had']},
        ],
    'cmssm-params-and-breakdowns':[
        {'axes':['m0','m12'],'zaxes':['m0','m12','A0','tanb', 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs/DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ]},
        {'axes':['MA','tanb'],'zaxes':['m0','m12','A0','tanb', 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs/DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ]}
        ],
    'pmssm-params-and-breakdowns':[
        {'axes':['m3g','mneu1'],'zaxes':['msq3','msq12','msl','M1','M2','M3','A','in_ma','tanb','in_mu', 
            'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs/DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ]},
        {'axes':['mstop1'],'zaxes':['msq3','msq12','msl','M1','M2','M3','A','in_ma','tanb','in_mu', 
            'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs/DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ]},
        ],
    'nuhm1-chi2-breakdowns':[
        {'axes':['m0','mh2'],'zaxes':['m12','tanb','A0', 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs/DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ]}
        ],
    'fh-unc':[
        {'axes':['fh-ss','Dmh']}
        ],
    'cmssm': [
            {'axes':'mtop'},
#            {   'axes':['m0','m12'] , 'zaxes':['mh','chi2_mh','mstop1','A0','BsmmRatio','ssmh'] },
#            { 'axes': 'mh'},
#            { 'axes': 'ssmh'},
#            {   'axes':['m0','mh2_m0^2_Ratio']  },
            #standard spaces
            {   'axes':['m0','m12'] },
            {   'axes':['MA','tanb']},
            {   'axes':['m0','tanb']},
            {   'axes':['A0','tanb']},
            {   'axes':['tanb','m12']},
            {   'axes':['logmneu1','logssikocm2']},
            {   'axes':['logmneu1','logssicm2']},
            {   'axes':'BsmmRatio'}, 
            {   'axes':'mg'},
            {   'axes':'mstop1' },
            {   'axes':'mh' }, 
            {   'axes':'MA' }, 
            {   'axes':'mstau1' }, 
            {   'axes':'msqr' }, 
#            {   'axes':'mh' }, 
#            {   'axes':'m3g' },
#            {   'axes':'m12g' },
#            {   'axes':'C9' }, 
#            {   'axes':'m0'},
#            {   'axes':'chi2'},
#            {   'axes':['mneu1','mg']},
        ],
    'nuhm1': [
        {   'axes':['m0','m12']},
        {   'axes':['m0','mh2']},
        {   'axes':['MA','tanb']},
        {   'axes':['m0','tanb']},
        {   'axes':['A0','tanb']},
        {   'axes':['tanb','m12']},
        {   'axes':['logmneu1','logssikocm2']},
        {   'axes':['logmneu1','logssicm2']},
        {   'axes':'BsmmRatio'}, 
        {   'axes':'mg'},
        {   'axes':'mstop1' },
        {   'axes':'mh' }, 
        {   'axes':'mstau1' }, 
        {   'axes':'msqr' }, 
#        {   'axes':['m0','mh_over_m0']},
#        {   'axes':['m0','mh2_m0^2_Ratio']},
      ],
   'pmssm':[
            {'axes':'mstop1'},
            {'axes':'msbot1'},
            {'axes':'mneu1'},
            {'axes':'mstau1'},
            {'axes':'mchar1'},
            {'axes':'mg'},
#            {'axes':['mg','mneu1'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['M3','M1']},
#            {'axes':['M2','M1'],'zaxes':'mneu1'},
#            {'axes':['M1','mneu1']},
#            {'axes':['M2','mneu1']},
#            #
            #mneu vs all physical masses
            {'axes':['mg','mneu1']},
            {'axes':['m3g','mneu1']},
            {'axes':['m12g','mneu1']},
            {'axes':['mstau1','mneu1']},
            {'axes':['mchar1','mneu1']},
            {'axes':['MA','mneu1']},
            {'axes':['tanb','mneu1']},
            {'axes':['A','mneu1']},
            #oh2 vs all physical masses
            {'axes':['mg','oh2']},
            {'axes':['m3g','oh2']},
            {'axes':['m12g','oh2']},
            {'axes':['mstau1','oh2']},
            {'axes':['mchar1','oh2']},
            {'axes':['MA','oh2']},
            {'axes':['tanb','oh2']},
            {'axes':['A','oh2']},
            #mh vs all physical masses
            {'axes':['mg','mh']},
            {'axes':['m3g','mh']},
            {'axes':['m12g','mh']},
            {'axes':['mstau1','mh']},
            {'axes':['mchar1','mh']},
            {'axes':['MA','mh']},
            {'axes':['tanb','mh']},
            {'axes':['A','mh']},
            {'axes':['mstop1','mh']},
            {'axes':['mstop2','mh']},
            {'axes':['msbot1','mh']},
            {'axes':['msbot2','mh']},
            {'axes':['A','mstop2-mstop1']},
            #check whether input parameters correspond to actual masses
#            {'axes':['mneu1','M1']},
#            {'axes':['mg','M3']},
#            {'axes':['m3g','msq3']},
#            {'axes':['m12g','msq12']},
#            {'axes':['mstau1','msl']},
#            {'axes':['in_ma','MA']},
#            {'axes':['in_mu','mu']},
#            #other parameters
#            {'axes':['MA','tanb']},
#            {'axes':['A','mu']},
#            {'axes':['M1','mg']},
#            {'axes':['m3g','mneu1'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['jadmg','jadmgmneu1'],'zaxes':['chi2_jad','chi2_m3g_only']},
#            {'axes':['m3g','jadmsq3mneu1'],'zaxes':['chi2_jad','chi2_m3g_only']},
#            {'axes':['m3g','jadmg'],'zaxes':['chi2_jad','chi2_m3g_only']},
#            {'axes':['jadmg','jadmgmneu1'],'zaxes':['chi2_jad','chi2_mg_only']},
#            {'axes':['m3g','jadmsq3mneu1'],'zaxes':['chi2_jad','chi2_mg_only']},
#            {'axes':['m3g','jadmg'],'zaxes':['chi2_jad','chi2_mg_only']},
#           {'axes':['mneu1','mg']},
#            {'axes':['M1','mg']},
#            {'axes':['M2','mg']},
#            {'axes':['M3','mg']},
#            {'axes':['msq12','tanb']},
#            {'axes':['msq3','tanb']},
#           {'axes':['msq3','msq12']},
#            {'axes':['msl' ,'tanb']},
#            {'axes':['msl' ,'msq12']},
#            {'axes':['msl' ,'msq3']},
#            {'axes':['A'   ,'tanb']},
#            {'axes':['A'   ,'msq12']},
#            {'axes':['A'   ,'msq3']},
#            {'axes':['A'   ,'msl']},
#            {'axes':['M1'  ,'tanb']},
#            {'axes':['M1'  ,'msq12']},
#            {'axes':['M1'  ,'msq3']},
#            {'axes':['M1'  ,'msl']},
#            {'axes':['M1'  ,'A']},
#            {'axes':['in_mu','tanb'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_mu','msq12'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_mu','msq3'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_mu','msl'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_mu','A'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_mu','M1'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_mu','M2'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_mu','M3'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['in_ma','tanb']},
#            {'axes':['in_ma','msq12']},
#            {'axes':['in_ma','msq3']},
#            {'axes':['in_ma','msl']},
#            {'axes':['in_ma','A']},
#            {'axes':['in_ma','M1']},
#            {'axes':['in_ma','in_mu'],'zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':['mneu1','mstop1']},
#            {'axes':'mg'},
#            {'axes':['mh','msq3']},
#            {'axes':'chi2','zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':'mh'},
#            {'axes':'tanb'},
#            {'axes':'msq12'},
#            {'axes':'msq3'},
#            {'axes':'msl' },
#            {'axes':'A'   },
#            {'axes':'M1'  },
#            {'axes':'mg'  },
#            {'axes':'mneu1'  },
#            {'axes':'in_mu','zaxes':['chi2_mh','chi2_oh2','chi2_g-2']},
#            {'axes':'in_ma','zaxes':'mh'},
#            {'axes':'mh','zaxes':'chi2_mh'},
#            {'axes':'mh'},
#            {   'axes':'BsmmRatio', 'zaxes':['BsmmRatio','chi2_mh'] }, 
                   ],
    }
