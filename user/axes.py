from math import sqrt
def get():
    axes.update(chi2_axes)
    return axes
axes={
            'pmssm-mc9-chi2':{
                'binning':{
                    'low':24,
                    'high':35,
                    'nbins':10000,
                    'type':'linear',
                    },
                'value':'mc9_no_lhc',
                },
            'cmssm-mc9-chi2':{
                'binning':{
                    'low':30,
                    'high':45,
                    'nbins':2000,
                    'type':'linear',
                    },
                'value':'mc9',
                },
            'mtop': {
                'binning': {
                    'high': 175.2,
                    'low': 171.2,
                    'nbins': 100,
                    'type': 'linear'
                    },
                'value': 'mtop'},
            'A': {
                'binning': {
                    'high': 5000.0,
                    'low': -5000.0,
                    'nbins': 100,
                    'type': 'linear'
                    },
                'value': 'A'},
            'A0': {
                'binning': {
                    'high': 5000.0,
                    'low': -5000.0,
                    'nbins': 100,
                    'type': 'linear'
                    },
                'value': 'A0'
                },
            'A0_nuhm2': {
                'binning': {
                    'high': 8000.0,
                    'low': -8000.0,
                    'nbins': 100,
                    'type': 'linear'
                    },
                'value': 'A0',
                'xticks': 4000,
                'texname':r'$A_0$',
                },
            'A0_over_m0': {
                'binning': {
                    'high': 5.0,
                    'low': -5.0,
                    'nbins': 100,
                    'type': 'linear'
                    },
                'value': 'A0_over_m0'
                },
            'BsmmRatio': {
                'binning': {
                    'high': 3.0,
                    'low': 0.0,
                    'nbins': 100,
                    'type': 'linear'
                    },
                'value': 'BsmmRatio',
                'texname':r'$R_{\mu\mu}$',
                },
            'C9': {'binning': {'high': 0.05,
                               'low': -0.05,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'C9'},
            'M1': {'binning': {'high': 2500.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'M1'},
            'M2': {'binning': {'high': 2500.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'M2'},
            'M3': {'binning': {'high': 2500.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'M3'},
            'MA': {'binning': {'high': 4000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'MA',
                   'xticks': 1000,
                   'texname':r'$M_A$[GeV]'},
            'MA_6K': {'binning': {'high': 6000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'MA',
                   'xticks': 1000,
                   'texname':r'$M_A$[GeV]'},
            'MA_2500': {'binning': {'high': 2500.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'MA',
                   'texname':r'$M_A$[GeV]'},
            'chi2': {'binning': {'high': 300.0,
                                 'low': 30.0,
                                 'nbins': 500,
                                 'type': 'linear'},
                     'value': 'chi2'},
            'chi2_g-2': {'value': 'g-2'},
            'chi2_jad': {'value': 'universal_limits'},
            'chi2_m3g_only': {'value': 'm3g_universal_limits'},
            'chi2_mg_only': {'value': 'mg_universal_limits'},
            'chi2_mh': {'value': 'Mh125'},
            'chi2Oh2': {
                    'value': 'chi2Oh2',
                    },
            'in_ma': {
                    'binning': {
                        'high': 4000.0,
                        'low': 0.0,
                        'nbins': 100,
                        'type': 'linear'
                        },
                    'value': 'in_ma'},
            'in_mu': {'binning': {'high': 5000.0,
                                  'low': -5000.0,
                                  'nbins': 100,
                                  'type': 'linear'},
                      'value': 'in_mu'},
            'logmneu1': {'binning': {'high': 4000.0,
                                     'low': 10.0,
                                     'nbins': 100,
                                     'type': 'log'},
                         'value': 'mneu1',
                         'texname': r'$m_{\tilde{\chi}^0_1}$[GeV]',
                         },
            'logssicm2': {'binning': {'high': 1e-40,
                                      'low': 1e-48,
                                      'nbins': 100,
                                      'type': 'log'},
                          'value': 'ssicm2',
                          'texname': r'$\sigma^{SI}_p$[cm$^2$]',
                          },
            'logssikocm2': {'binning': {'high': 1e-40,
                                        'low': 1e-48,
                                        'nbins': 100,
                                        'type': 'log'},
                            'value': 'ssikocm2',
                            'texname': r'$\sigma^{SI}_p$[cm$^2$]',
                            },
            'logssikocm2_50': {'binning': {'high': 1e-40,
                                        'low': 1e-50,
                                        'nbins': 100,
                                        'type': 'log'},
                            'value': 'ssikocm2',
                            'texname': r'$\sigma^{SI}_p$[cm$^2$]',
                            },
            'Dssicm2': {
                    'value': 'Dssikocm2'
                    },
            'Dssi': {
                    'value': 'Dssi'
                    },
            'm0': {'binning': {'high': 4000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'm0',
                   'xticks': 1000,
                   'texname':r'$m_0$[GeV]'},
            'm0_nuhm2': {'binning': {'high': 4000.0,
                               'low': -1000.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'm0',
                   'xticks': 1000,
                   'texname':r'$m_0$[GeV]'},
            'mstau1-mneu1': {'binning': {'high': 30.0,
                               'low': -5.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mstau1-mneu1'},
            'mchar1-mneu1': {'binning': {'high': 30.0,
                               'low': -5.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mchar1-mneu1'},
            'MA-2mneu1': {'binning': {'high': 30.0,
                               'low': -5.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'MA-2mneu1'},
            'nuhm1m0': {'binning': {'high': 4500.0,
                               'low': -500.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'm0'},
            'm0_6K': {'binning': {'high': 6000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'm0',
                   'texname':r'$m_0$[GeV]'},
            'm0_7K': {'binning': {'high': 7000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'm0',
                   },
            'm12': {'binning': {'high': 4000.0,
                                'low': 0.0,
                                'nbins': 100,
                                'type': 'linear'},
                    'value': 'm12',
                    'texname':r'$m_{1/2}$[GeV]'},
            'm12g': {'binning': {'high': 4000.0,
                                 'low': 0.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'm12g'},
            'm12g_2K': {'binning': {'high': 2000.0,
                                 'low': 0.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'm12g'},
            'm3g': {'binning': {'high': 4000.0,
                                'low': 0.0,
                                'nbins': 100,
                                'type': 'linear'},
                    'value': 'm3g'},
            'mchar1': {'binning': {'high':4000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mchar1'},
            'mchar1_2_5K': {'binning': {'high':2500.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'texname':r'$m_{\tilde{\chi}^{\pm}_1}$[GeV]',
                       'value': 'mchar1'},
            'mchar1_4K': {'binning': {'high':4000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'texname':r'$m_{\tilde{\chi}^{\pm}_1}$[GeV]',
                       'value': 'mchar1'},
            'mchar1_5K': {'binning': {'high':5000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'texname':r'$m_{\tilde{\chi}^{\pm}_1}$[GeV]',
                       'value': 'mchar1'},
            'mchar1_6K': {'binning': {'high':6000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'texname':r'$m_{\tilde{\chi}^{\pm}_1}$[GeV]',
                       'value': 'mchar1'},
            'mg': {'binning': {'high': 4000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mg',
                   'xticks': 1000,
                   'texname':r'$m_{\tilde{g}}$[GeV]'},
            'mg_140131': {
                    'binning': {'high': 4100.0,
                               'low': 1500.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mg',
                   'xticks': 1000,
                   'texname':r'$m_{\tilde{g}}$[GeV]'},
            'mg_6K': {'binning': {'high': 6000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mg',
                   'texname':r'$m_{\tilde{g}}$[GeV]'
                   },
            'mg_5K': {'binning': {'high': 5000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mg',
                   'texname':r'$m_{\tilde{g}}$[GeV]'
                   },
            'mg_2K': {'binning': {'high': 2000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mg',
                   'texname':r'$m_{\tilde{g}}$[GeV]'
                   },
            'mh': {'binning': {'high': 130.0,
                               'low': 105.0,
                               'nbins': 100,    
                               'type': 'linear'},
                   'value': 'mh',
                   'texname':'$M_h$[GeV]'},
            'Dmh': {'binning': {'high': 40.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'Dmh'},
            'Dmh_20': {'binning': {'high': 20.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'Dmh'},
            'Dmh_10': {'binning': {'high': 10.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'Dmh'},
            'Dmh_5': {'binning': {'high': 5.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'Dmh'},
            'fh-ss': {'binning': {'high': 40,
                               'low': -40,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'fh-ss'},
            'fh-ss_20': {'binning': {'high': 20,
                               'low': -20,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'fh-ss'},
            'fh-ss_10': {'binning': {'high': 10,
                               'low': -10,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'fh-ss'},
            'fh-ss_5': {'binning': {'high': 5,
                               'low': -5,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'fh-ss'},
            'mh2': {'binning': {'high': 46000000.0,
                                'low': -46000000.0,
                                'nbins': 100,
                                'type': 'linear'},
                    'value': 'mh2'},
            'mhu2': {'binning': {'high': 50000000.0,
                                'low': -50000000.0,
                                'nbins': 100,
                                'type': 'linear'},
                    'value': 'mhu2',
                    'texname':r'$M_{H_u}^2$',
                    },
            'mhd2': {'binning': {'high': 50000000.0,
                                'low': -50000000.0,
                                'nbins': 100,
                                'type': 'linear'},
                    'value': 'mhd2',
                    'texname':r'$M_{H_d}^2$',
                    },
            'mh2_m0^2_Ratio': {'binning': {'high': 10.0,
                                           'low': -10.0,
                                           'nbins': 100,
                                           'type': 'linear'},
                               'value': 'mh2_m0^2_Ratio'},
            'mh_over_m0': {'binning': {'high': 10.0,
                                       'low': -10.0,
                                       'nbins': 100,
                                       'type': 'linear'},
                           'value': 'mh_over_m0'},
            'mneu1': {'binning': {'high':4000.0,
                                  'low': 0.0,
                                  'nbins': 100,
                                  'type': 'linear'},
                      'value': 'mneu1',
                      'texname': r'$m_{\tilde{\chi}^0_1}$[GeV]',
                      },
            'mneu1_50gev': {'binning': {'high':50.0,
                                  'low': 0.0,
                                  'nbins': 100,
                                  'type': 'linear'},
                      'value': 'mneu1',
                      'texname': r'$m_{\tilde{\chi}^0_1}$[GeV]',
                      },
            'mneu1_900': {'binning': {'high': 900.0,
                                      'low': 0.0,
                                      'nbins': 100,
                                      'type': 'linear'},
                          'value': 'mneu1_900'},
            'msbot1': {'binning': {'high': 4000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'msbot1'},
            'msbot2': {'binning': {'high': 4000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'msbot2'},
            'msl': {'binning': {'high': 4000.0,
                                'low': 0.0,
                                'nbins': 100,
                                'type': 'linear'},
                    'value': 'msl'},
            'msq12': {'binning': {'high': 4000.0,
                                  'low': 0.0,
                                  'nbins': 100,
                                  'type': 'linear'},
                      'value': 'msq12'},
            'msq3': {'binning': {'high': 4000.0,
                                 'low': 0.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'msq3'},
            'msqr': {'binning': {'high': 6000.0,
                                 'low': 0.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'msqr',
                     'texname': r'$m_{\tilde{q}_R}$[GeV]'
                     },
            'msqr_140131': {
                    'binning': {'high': 4100.0,
                                 'low': 1900.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'msqr',
                     'texname': r'$m_{\tilde{q}_R}$[GeV]'
                     },
            'msqr_8K': {'binning': {'high': 8000.0,
                                 'low': 0.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'msqr',
                     'texname': r'$m_{\tilde{q}_R}$[GeV]'
                     },
            'mstau1': {'binning': {'high':4000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstau1',
                       'vmin':0,
                       'vmax':2000,
                       'xticks': 1000,
                       'texname':r'$m_{\tilde{\tau}_1}$[GeV]',
                       },
            'mstau1_6K': {'binning': {'high': 6000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstau1',
                       'texname':r'$m_{\tilde{\tau}_1}$[GeV]',
                       },
            'mstau1_5K': {'binning': {'high': 5000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstau1',
                       'texname':r'$m_{\tilde{\tau}_1}$[GeV]',
                       },
            'mstop1': {'binning': {'high': 4000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstop1',
                       'xticks': 1000,
                       'texname':r'$m_{\tilde{t}_1}$[GeV]'
                       },
            'mstop1_2K': {'binning': {'high': 2000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstop1',
                       'texname':r'$m_{\tilde{t}_1}$[GeV]'
                       },
            'mstop1_5K': {'binning': {'high': 5000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstop1',
                       'texname':r'$m_{\tilde{t}_1}$[GeV]'
                       },
            'mstop1_6K': {'binning': {'high': 6000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstop1',
                       'texname':r'$m_{\tilde{t}_1}$[GeV]'
                       },
            'mstop2': {'binning': {'high': 4000.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'xticks': 1000,
                       'value': 'mstop2'},
            'mstop2-mstop1': {'binning': {'high': 1000.0,
                                          'low': 0.0,
                                          'nbins': 100,
                                          'type': 'linear'},
                              'value': 'mstop2-mstop1'},
            'mstop1_750': {'binning': {'high': 750.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstop1',
                       },
            'mselL_750': {'binning': {'high': 750.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mselL',
                       },
            'msmuL_750': {'binning': {'high': 750.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'msmuL',
                       },
            'mstau1_750': {'binning': {'high': 750.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mstau1',
                       },
            'mneu1_750': {'binning': {'high': 750.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mneu1',
                       },
            'mneu2_750': {'binning': {'high': 750.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mneu2',
                       },
            'mchar1_750': {'binning': {'high': 750.0,
                                   'low': 0.0,
                                   'nbins': 100,
                                   'type': 'linear'},
                       'value': 'mchar1',
                       },
            'mu': {'binning': {'high': 3000.0,
                               'low': 0.0,
                               'nbins': 100,
                               'type': 'linear'},
                   'value': 'mu',
                   'texname':r'$\mu$'},
            'oh2': {
                    'binning': {
                        'low': 0.0, 
                        'high': 0.3, 
                        'nbins': 100, 
                        'type': 'linear',
                        },
                    'value': 'oh2'
                    },
            'ssmh': {'binning': {'high': 130.0,
                                 'low': 105.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'ssmh'},
            'tanb': {'binning': {'high': 60.0,
                                 'low': 0.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'tanb',
                     'texname': r'$\tan\beta$'},
            'tanb40': {'binning': {'high': 40.0,
                                 'low': 0.0,
                                 'nbins': 100,
                                 'type': 'linear'},
                     'value': 'tanb',
                     'texname':r'$\tan\beta$',
                     },
            'Delta_alpha_had':{
                    'value':'Delta_alpha_had',
                   },
            'mz':{
                    'value':'mz',
                    },
            'mt':{
                    'value':'mtop',
                    },
            'TLEP_mz':{
                    'value':'mz',
#                    'texname':r'$\frac{M_Z(cMSSM)-M_Z(meas.)}{\sigma_{M_Z}(TLEP)}$',
#                    'vmin':91.18719946048513,
#                    'vmax':91.18780053951487,
#                    'colorbar_ticks': [91.187199, 91.187300, 91.187400, 91.187500, 91.187600, 91.187700, 91.187801],
 #                   'texname':r'$\frac{M_Z(cMSSM)-M_Z(cMSSM\/best\/fit\/low\/mass)}{\sigma_{M_Z}(TLEP)}$',
 #                   'vmin':91.18723246048513,
 #                   'vmax':91.18783353951487,
 #                   'colorbar_ticks': [91.187232, 91.187333, 91.187433, 91.187533, 91.187633, 91.187733, 91.187834],
                    'texname':r'$\frac{M_Z(cMSSM)-M_Z(cMSSM\/best\/fit\/high\/mass)}{\sigma_{M_Z}(TLEP)}$',
                    'vmin':91.18718646048514,
                    'vmax':91.18778753951487,
                    'colorbar_ticks': [91.187186, 91.187287, 91.187387, 91.187487, 91.187587, 91.187687, 91.187788],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'TLEP_mt':{
                    'value':'mtop',
 #                   'texname':r'$\frac{m_{top}(cMSSM)-m_{top}(meas.)}{\sigma_{m_{top}}(TLEP)}$',
 #                   'vmin':173.15313850194457,
 #                   'vmax':173.24686149805547,
 #                   'colorbar_ticks': [173.153139, 173.168759, 173.184380, 173.200000, 173.215620, 173.231241, 173.246861],
 #                   'texname':r'$\frac{m_{top}(cMSSM)-m_{top}(cMSSM\/best\/fit\/low\/mass)}{\sigma_{m_{top}}(TLEP)}$',
 #                   'vmin':173.10933950194456,
 #                   'vmax':173.20306249805546,
 #                   'colorbar_ticks': [173.109340, 173.124960, 173.140581, 173.156201, 173.171821, 173.187442, 173.203062],
                    'texname':r'$\frac{m_{top}(cMSSM)-m_{top}(cMSSM\/best\/fit\/high\/mass)}{\sigma_{m_{top}}(TLEP)}$',
                    'vmin':173.25737950194454,
                    'vmax':173.35110249805544,
                    'colorbar_ticks': [173.257380, 173.273000, 173.288621, 173.304241, 173.319861, 173.335482, 173.351102],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'TLEP_Gamma_Z':{
                    'value':'Gamma_Z',
                    'binning':{
                        'low':2495.2-3*sqrt( 2.3**2+ 1.0**2),
                        'high':2495.2+3*sqrt( 2.3**2+ 1.0**2),
                        'nbins':100,
                        'type':'linear' },
 #                   'texname':r'$\frac{\Gamma_Z(cMSSM)-\Gamma_Z(meas.)}{\sigma_{\Gamma_Z}(TLEP)}$',
 #                   'vmin':2494.898503731367,
 #                   'vmax':2495.5014962686337,
 #                   'colorbar_ticks': [2494.898504, 2494.999002, 2495.099501, 2495.200000, 2495.300499, 2495.400998, 2495.501496],
 #                   'texname':r'$\frac{\Gamma_Z(cMSSM)-\Gamma_Z(cMSSM\/best\/fit\/low\/mass)}{\sigma_{\Gamma_Z}(TLEP)}$',
 #                   'vmin':2494.9548327313664,
 #                   'vmax':2495.557825268633,
 #                   'colorbar_ticks': [2494.954833, 2495.055331, 2495.155830, 2495.256329, 2495.356828, 2495.457327, 2495.557825],
                    'texname':r'$\frac{\Gamma_Z(cMSSM)-\Gamma_Z(cMSSM\/best\/fit\/high\/mass)}{\sigma_{\Gamma_Z}(TLEP)}$',
                    'vmin':2494.1572037313667,
                    'vmax':2494.7601962686335,
                    'colorbar_ticks': [2494.157204, 2494.257702, 2494.358201, 2494.458700, 2494.559199, 2494.659698, 2494.760196],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'TLEP_Rl'     :{
                    'value':'Rl'     ,
                    'binning':{
                        'low':20.767-3*0.025,
                        'high':20.767+3*0.025,
                        'nbins':100,
                        'type':'linear' },
 #                   'texname':r'$\frac{R_l(cMSSM)-R_l(meas.)}{\sigma_{R_l}(TLEP)}$',
 #                   'vmin':20.766531385019444,
 #                   'vmax':20.767468614980555,
 #                   'colorbar_ticks': [20.766531, 20.766688, 20.766844, 20.767000, 20.767156, 20.767312, 20.767469],
 #                   'texname':r'$\frac{R_l(cMSSM)-R_l(cMSSM\/best\/fit\/low\/mass)}{\sigma_{R_l}(TLEP)}$',
 #                   'vmin':20.741050385019445,
 #                   'vmax':20.741987614980555,
 #                   'colorbar_ticks': [20.741050, 20.741207, 20.741363, 20.741519, 20.741675, 20.741831, 20.741988],
                    'texname':r'$\frac{R_l(cMSSM)-R_l(cMSSM\/best\/fit\/high\/mass)}{\sigma_{R_l}(TLEP)}$',
                    'vmin':20.740262385019445,
                    'vmax':20.741199614980555,
                    'colorbar_ticks': [20.740262, 20.740419, 20.740575, 20.740731, 20.740887, 20.741043, 20.741200],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'TLEP_Rb'     :{
                    'value':'Rb'     ,
                    'binning':{
                        'low':0.21629-3*0.00066,
                        'high':0.21629+3*0.00066,
                        'nbins':100,
                        'type':'linear' },
 #                   'texname':r'$\frac{R_b(cMSSM)-R_b(meas.)}{\sigma_{R_b}(TLEP)}$',
 #                   'vmin':0.21610960044345953,
 #                   'vmax':0.2164703995565405,
 #                   'colorbar_ticks': [0.216110, 0.216170, 0.216230, 0.216290, 0.216350, 0.216410, 0.216470],
 #                   'texname':r'$\frac{R_b(cMSSM)-R_b(cMSSM\/best\/fit\/low\/mass)}{\sigma_{R_b}(TLEP)}$',
 #                   'vmin':0.21577660044345953,
 #                   'vmax':0.2161373995565405,
 #                   'colorbar_ticks': [0.215777, 0.215837, 0.215897, 0.215957, 0.216017, 0.216077, 0.216137],
                    'texname':r'$\frac{R_b(cMSSM)-R_b(cMSSM\/best\/fit\/low\/mass)}{\sigma_{R_b}(TLEP)}$',
                    'vmin':0.21575960044345951,
                    'vmax':0.21612039955654047,
                    'colorbar_ticks': [0.215760, 0.215820, 0.215880, 0.215940, 0.216000, 0.216060, 0.216120],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'TLEP_MW'     :{
                    'value':'MW'     ,
                    'binning':{
                        'low':80.385-3*sqrt(0.015**2+0.01**2),
                        'high':80.385+3*sqrt(0.015**2+0.01**2),
                        'nbins':100,
                        'type':'linear' },
 #                   'texname':r'$\frac{M_W(cMSSM)-M_W(meas.)}{\sigma_{M_W}(TLEP)}$',
 #                   'vmin':80.38307906272877,
 #                   'vmax':80.38692093727124,
 #                   'colorbar_ticks': [80.383079, 80.383719, 80.384360, 80.385000, 80.385640, 80.386281, 80.386921],
 #                   'texname':r'$\frac{M_W(cMSSM)-M_W(cMSSM\/best\/fit\/low\/mass)}{\sigma_{M_W}(TLEP)}$',
 #                   'vmin':80.37457906272876,
 #                   'vmax':80.37842093727123,
 #                   'colorbar_ticks': [80.374579, 80.375219, 80.375860, 80.376500, 80.377140, 80.377781, 80.378421],
                    'texname':r'$\frac{M_W(cMSSM)-M_W(cMSSM\/best\/fit\/high\/mass)}{\sigma_{M_W}(TLEP)}$',
                    'vmin':80.36213206272876,
                    'vmax':80.36597393727124,
                    'colorbar_ticks': [80.362132, 80.362772, 80.363413, 80.364053, 80.364693, 80.365334, 80.365974],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'current_mz':{
                    'value':'mz',
                    'texname':r'$\frac{M_Z(cMSSM)-M_Z(meas.)}{\sigma_{M_Z}(current)}$',
                    'vmin':91.1812,
                    'vmax':91.1938,
                    'colorbar_ticks': [91.181200, 91.183300, 91.185400, 91.187500, 91.189600, 91.191700, 91.193800],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'current_mt':{
                    'value':'mtop',
                    'texname':r'$\frac{m_{top}(cMSSM)-m_{top}(meas.)}{\sigma_{m_{top}}(current)}$',
                    'vmin':170.50000000000003,
                    'vmax':175.9,
                    'colorbar_ticks': [170.500000, 171.400000, 172.300000, 173.200000, 174.100000, 175.000000, 175.900000],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            #FIXME: need more elegant way of including this.
            'current_Gamma_Z':{
                    'value':'Gamma_Z',
                    'binning':{
                        'low':2495.2-3*sqrt( 2.3**2+ 1.0**2),
                        'high':2495.2+3*sqrt( 2.3**2+ 1.0**2),
                        'nbins':100,
                        'type':'linear' },
                    'texname':r'$\frac{\Gamma_Z(cMSSM)-\Gamma_Z(meas.)}{\sigma_{\Gamma_Z}(current)}$',
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    'vmin':2488.3,
                    'vmax':2502.1000000000004,
                    'colorbar_ticks': [2488.300000, 2490.600000, 2492.900000, 2495.200000, 2497.500000, 2499.800000, 2502.100000],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'current_Rl'     :{
                    'value':'Rl'     ,
                    'binning':{
                        'low':20.767-3*0.025,
                        'high':20.767+3*0.025,
                        'nbins':100,
                        'type':'linear' },
                    'texname':r'$\frac{R_l(cMSSM)-R_l(meas.)}{\sigma_{R_l}(current)}$',
                    'vmin':20.692,
                    'vmax':20.842,
                    'colorbar_ticks': [20.692000, 20.717000, 20.742000, 20.767000, 20.792000, 20.817000, 20.842000],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'current_Rb'     :{
                    'value':'Rb'     ,
                    'binning':{
                        'low':0.21629-3*0.00066,
                        'high':0.21629+3*0.00066,
                        'nbins':100,
                        'type':'linear' },
                    'texname':r'$\frac{R_b(cMSSM)-R_b(meas.)}{\sigma_{R_b}(current)}$',
                    'vmin':0.21431,
                    'vmax':0.21827000000000002,
                    'colorbar_ticks': [0.214310, 0.214970, 0.215630, 0.216290, 0.216950, 0.217610, 0.218270],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            'current_MW'     :{
                    'value':'MW'     ,
                    'binning':{
                        'low':80.385-3*sqrt(0.015**2+0.01**2),
                        'high':80.385+3*sqrt(0.015**2+0.01**2),
                        'nbins':100,
                        'type':'linear' },
                    'texname':r'$\frac{M_W(cMSSM)-M_W(meas.)}{\sigma_{M_W}(current)}$',
                    'vmin':80.34,
                    'vmax':80.43,
                    'colorbar_ticks': [80.340000, 80.355000, 80.370000, 80.385000, 80.400000, 80.415000, 80.430000],
                    'colorbar_ticklabels':[-3,-2,-1,0,1,2,3] ,
                    },
            }
            
chi2_axes={name:{'value':'chi2-{}'.format(name)} for name in   [ 'Al(SLD)', 'Ab', 'Ac', 'mc9_Oh2', 'mc9_Mh',   
            'Gamma_Z', 'GZ_in', 'R(B->Xsll)', 'Al(P_tau)', 'MZ', 'mc9_R_DMBs', 'MW', 'Afb_l', 
            'lux131030_unc', 'mc9_DAlpha_had', 'mc9_epsilon_K',  'sigma_had^0', 'Afb(c)', 
            'atlas20_m0_m12', 'Afb(b)',  'mc9_R_B->Xsg', 'mc9_R_DMBs_DMBd', 'mc9_R_B->taunu', 
            'Rc', 'Rb',  'Rl', 'RmmNov13_mc9', 'sintheta_eff', 'mc9_Mt', 'R(K->lnu)', 'R(Kp->pinn)', 'gminus2mu', 'MATANB' ,
            'LEP-chargino', 'LEP-neutralino', 'LEP-slepton', 'LEP-sneutrino', 'LEP-squark','neutralino-lsp'
            ]}
        
