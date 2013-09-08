def get():
    return {
            'xenon100_july_2012':{
                'observable_ids':{
                    'mcpp':[('MASS', 'MNeu(1)'),('Micromegas','sigma_p_si')],
                    },
                'contours':['xenon100_july_2012'],
                'function':'xenon100_mc8',
                },
            }
    #FIXME: tidy up
#    return {'m3g_universal_limits': {'contours': [{'coordinates': [[0.0, 500.0],
#                                                        [300.0, 400.0]],
#                                        'type': 'UniversalLimits'}],
#                          'function_name': 'm3g_universal_limits',
#                          'observable_ids': {'mc_old': ['neu1',
#                                                        'sbottom1',
#                                                        'sbottom2',
#                                                        'stop1',
#                                                        'stop2']}},
# 'mg_universal_limits': {'contours': [{'coordinates': [[0.0, 900.0],
#                                                       [400.0, 700.0],
#                                                       [450.0, 500.0]],
#                                       'type': 'UniversalLimits'}],
#                         'function_name': 'mg_universal_limits',
#                         'observable_ids': {'mc_old': ['neu1', 'gluino']}},
# 'universal_limits': {'contours': [{'coordinates': [[0.0, 900.0],
#                                                    [400.0, 700.0],
#                                                    [450.0, 500.0]],
#                                    'type': 'UniversalLimits'},
#                                   {'coordinates': [[0.0, 500.0],
#                                                    [300.0, 400.0]],
#                                    'type': 'UniversalLimits'}],
#                      'function_name': 'universal_limits',
#                      'observable_ids': {'mc_old': ['neu1',
#                                                    'gluino',
#                                                    'sbottom1',
#                                                    'sbottom2',
#                                                    'stop1',
#                                                    'stop2']}}}
#
