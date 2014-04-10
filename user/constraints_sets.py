def get(name):
    return ['chi2-{}'.format(name) for name in constraints.get(name,[])]

#FIXME: there should be a unified way
#this list is copied from mcpp and modified
constraints={
'chi2+nuisance':['chi2','mc9_Mt','mc9_DAlpha_had','MZ'],
'micromegas-only': ['mc9_Oh2'],
'mc9': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_HLLHC': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas_putative_3000_msqr_mg', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_3000ob': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas_3000fb_14TeV_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_HLLHC_TLEP_low': [
    'TLEP_low_bf_MZ' ,
    'TLEP_low_bf_Gamma_Z' ,
    'TLEP_low_bf_Rl' ,
    'TLEP_low_bf_Rb' ,
    'TLEP_low_bf_Al',
    'TLEP_low_bf_MW',
    'TLEP_low_bf_Mt',
    'TLEP_low_bf_sintheta_eff',
    'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas_putative_3000_msqr_mg', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_TLEP_low': [ 
    #add the TLEP low best fit 'measurements on top'
    'TLEP_low_bf_MZ' ,
    'TLEP_low_bf_Gamma_Z' ,
    'TLEP_low_bf_Rl' ,
    'TLEP_low_bf_Rb' ,
    'TLEP_low_bf_Al',
    'TLEP_low_bf_MW',
    'TLEP_low_bf_Mt',
    'TLEP_low_bf_sintheta_eff',
    'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_TLEP_high': [ 
    #add the TLEP high best fit 'measurements on top'
    'TLEP_high_bf_MZ' ,
    'TLEP_high_bf_Gamma_Z' ,
    'TLEP_high_bf_Rl' ,
    'TLEP_high_bf_Rb' ,
    'TLEP_high_bf_Al',
    'TLEP_high_bf_MW',
    'TLEP_high_bf_Mt',
    'TLEP_high_bf_sintheta_eff',
    'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_drop_mh': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2',    
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_no_unc': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_universal_7TeV': ['universal_limits_7TeV' ,'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_no_lhc': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_pmssm': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino',  'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_pmssm_upper': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh2_upper_limit', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino',  'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_no_lhc_asym': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh2_asymmetric', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9lux_no_lhc_Oh2_upper': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh2_upper_limit', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9_no_lhc': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9_no_lhc_upper_oh2': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh2_upper_limit', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9_no_nuisance': [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)',  'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc',  'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff',  'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9_no_nuisance_Oh2_upper': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh2_upper_limit', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)',  'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc',  'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff',  'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc9_no_nuisance_Oh2_asymmetric': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh2_asymmetric', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)',  'mc9_R_DMBs', 'MW', 'Afb_l', 
            'xenon100_SpiN_unc',  'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'R_Bsmm_mc9', 'sintheta_eff',  'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc8': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'atlas5_m0_m12', 'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc8_no_bsmm': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'atlas5_m0_m12', 'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc8new': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100_90CL_ssi_unc', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'atlas5_m0_m12', 'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'mc8-no-higgs': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8',  'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'atlas5_m0_m12', 'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'pre-lhc': [ 'Al(SLD)', 'Ab', 'Ac', 'Oh^2_mc8', 'HiggsLEP', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW-mc-old', 'Afb_l', 
             'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'generic': [ 'Al(SLD)', 'Ab', 'Ac',  'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)',  'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'Oh^2_mc8','LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'generic2': ['Al(SLD)','Ab','Ac','Gamma_Z','GZ_in','Al(P_tau)','MW','Afb_l','DAlpha_had',
            'sigma_had^0','Afb(c)','Afb(b)','Rc','Rb','Rl','sintheta_eff',
            'BR(Bd->ll)','R(B->Xsll)','R(D_ms)','R(Delta_mk)','R(b->sg)','R(Dms)/R(Dmd)','R(B->taunu)','mc8_bsmm','R(K->lnu)','R(Kp->pinn)',
            'Higgs125','gminus2mu',
            'Oh^2_mc8',
            'xenon100',
            'Mt',
            'MATANB',
            'LEP-chargino','LEP-neutralino-abs','LEP-slepton','LEP-sneutrino','LEP-squark','neutralino-lsp',
            ],
'pmssm': [ 'Al(SLD)', 'Ab', 'Ac',  'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'pmssm_with_Oh2': ['Oh^2_mc8', 'Al(SLD)', 'Ab', 'Ac',  'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],
'pmssm_upper_Oh2': ['Oh2_upper_limit', 'Al(SLD)', 'Ab', 'Ac',  'Higgs125', 'BR(Bd->ll)',  
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'R(D_ms)', 'MW', 'Afb_l', 
            'xenon100', 'DAlpha_had', 'R(Delta_mk)',  'sigma_had^0', 'Afb(c)', 
            'Afb(b)',  'R(b->sg)', 'R(Dms)/R(Dmd)', 'R(B->taunu)', 
            'Rc', 'Rb',  'Rl', 'mc8_bsmm', 'sintheta_eff', 'Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ],

        }
            
