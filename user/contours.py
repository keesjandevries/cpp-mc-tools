def get():
    return {
            'xenon100_july_2012':{
                    'type':'log_x_log_y',
                    'file':'user/data_files/xenon100_july_1012.dat',
                    'info':'''obtained form Xenon Jul 2012 paper: 1207.2988v2 Fig 3 bleu curve. 
                    Extended using lus paper: Fig. 5 1310.8214v1 red curve and factor to allign two curves'''
                },
            'lux131030':{
                    'type':'log_x_log_y',
                    'file':'user/data_files/lux131030.dat',
                    'info':'''obtained from blue curve, Fig. 5 1310.8214v1 using digitizer. 
                    subsequently divided ssi by 10e-36: cm2 to picobarn.''',
                },
            'mc8_ma_tanb':{
                    'type':'default',
                    'file':'user/data_files/mc8_ma_tanb.dat',
                },
            'atlas_5fb_m0_m12':{
                    'type':'radial',
                    'file':'user/data_files/atlas_5fb_m0_m12.dat'
                },
            'atlas_20fb_m0_m12':{
                    'type':'radial',
                    'file':'user/data_files/atlas_20fb_m0_m12.dat'
                },
            'atlas_ichep2014_m0_m12':{
                    'type':'radial',
                    'file':'user/data_files/140806_atlas_ichep2014.dat',
                    'info':'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/'
                    'CombinedSummaryPlots/SUSY/ATLAS_SUSY_MSUGRA/ATLAS_SUSY_MSUGRA.png',
                },
            'atlas_susy2014_ma_tanb':{
                    'type': 'default',
                    'file': 'user/data_files/140806_atlas_susy2014_ma_tanb.dat',
                    'info': "Sekula's talk at SUSY 2014, p. 31 (ATLAS-CONF-2014-049 Fig. 6(a))"
                },
            'atlas_3000fb_14TeV_m0_m12':{
                    'type':'radial',
                    'file':'user/data_files/projected_m0_m12_14_TeV_3000_fb-1.dat'
                },
            'atlas_putative_3000fb_msqr_mg':{
                    'type':'radial',
                    'file':'user/data_files/atlas_putative_3000fb_msqr_mg.dat'
                },
            'mc8_bsmm':{
                    'type':'default',
                    'file':'user/data_files/mc8_bsmm.dat',
                }
            }
