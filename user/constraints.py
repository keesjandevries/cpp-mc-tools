def get_constraints():
    return {
        'Mh125':{
            'observable_ids' :{
                'mc_old':'mh',
            },
            'gaussian':{
                'mu':125.,
                'sigmas':[1.0,2.5],
                'function_name':'gauss',
            },
        }
    }
