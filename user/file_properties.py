def get_files():
    return {
            'mc-old-nuhm1':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':12, 'spectrum_index':76  }}, 
                },
            'mc-old-pmssm8':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':13, 'spectrum_index':77  }}, 
                },
            'mc-old-pmssm10':{
                'observable_ids':{ 'mc_old' :{ 'prediction_index':15, 'spectrum_index':79  }}, 
                'mc_point_inputs':['msq12','msq3','msl', 'M1','M2','M3', 'A', 'MA','tanb','mu','mt','mz','Delta_alpha_had']
                },
            }
