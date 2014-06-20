def get():
    return {
            'get_chi2_eq_4_limit':{
                'chi2_eq_4_limit':True,
                },
            'preliminary':{
                'text_box':{
                    'args':[0.05,0.95,'Not even preliminary!!'],
                    },
                },
            'preliminary_1d':{
                'text_box':{
                    'args':[0.95,0.97,'Not even preliminary!!'],
                    'kwargs':{'horizontalalignment':'right'}
                    },
                },
            'mc9lux_legend':{
                'solid_dashed_contours_legend':['ATLAS8','ATLAS7']
                },
            'pmssm_workshop_legend':{
                'solid_dashed_contours_legend':['w LHC@7TeV','w/o LHC@7TeV']
                },
            'Mitesh_legend':{
                'solid_dashed_contours_legend':[r'w $B_s\to\mu\mu$',r'w/o $B_s\to\mu\mu$'],
                'title':'cMSSM July 2012',
                },
            }
