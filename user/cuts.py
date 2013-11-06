def get():
    return cuts

cuts={
        'feynhiggs_error':{
            'observable_ids':{
                'mcpp':('FeynHiggs','error'),
                },
            'function':'predictor_error',
            },
        'micromegas_error':{
            'observable_ids':{
                'mcpp':('Micromegas','error'),
                },
            'function':'predictor_error',
            },
        'chi2-check':{
            'observable_ids':{
                'mcpp':('tot_X2','all'),
                },
            'function':'chi2_error',
            }
        }
