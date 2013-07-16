def get_file_properties():
    return {
            'mc-old-cmssm':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':10, 'spectrum_index':74  }}, 
                },
            'mc-old-nuhm1':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':12, 'spectrum_index':76  }}, 
                },
            'mc-old-pmssm8':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':13, 'spectrum_index':77  }}, 
                },
            'mc-old-pmssm10':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':15, 'spectrum_index':79  }}, 
                'mc_point_inputs':['msq12','msq3','msl', 'M1','M2','M3', 'A', 'MA','tanb','mu','mtop','MZ','DAlpha_had']
                },
            }
