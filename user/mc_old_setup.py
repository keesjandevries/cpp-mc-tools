def get(choice=None):
    if choice is not None:
        try:
            return mc_old_setups[choice]
        except KeyError:
            print('ERROR: \'{}\'not in defined user/mc_old_setup.py '.format(choice))
    else:
        return None

mc_old_setups= {
            'mc-old-cmssm-mc8-ko':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':10, 'spectrum_index':124  }}, 
                },
            'mc-old-cmssm-mc8':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':10, 'spectrum_index':117  }}, 
                },
            'mc-old-cmssm':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':10, 'spectrum_index':74  }}, 
                'mc_point_inputs':['m0','m12','tanb','A0','mtop','MZ','DAlpha_had'],
                'mc_point_flag':'--mc-cmssm',
                },
            'mc-old-nuhm1':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':12, 'spectrum_index':76  }}, 
                },
            'mc-old-pmssm8':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':13, 'spectrum_index':77  }}, 
                },
            'mc-old-pmssm10':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':15, 'spectrum_index':79  }}, 
                'mc_point_inputs':['msq12','msq3','msl', 'M1','M2','M3', 'A', 'MA','tanb','mu','mtop','MZ','DAlpha_had'],
                'mc_point_flag':'--mc-pmssm10',
                },
            }
