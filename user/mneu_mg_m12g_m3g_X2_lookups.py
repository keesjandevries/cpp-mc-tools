def get():
    constraints=constraints_dict
    #rename to chi2-<constraint name>
    constraints={'chi2-{}'.format(name):details for name, details in constraints.items()}
    return constraints

constraints_dict={
'universal_limits_7TeV' :{
    'observable_ids':{
        'mcpp':[
            #mneu
            ('MASS', 'MNeu(1)'),
            #mg
            ('MASS', 'MGl'),
            #m12g
            ('MASS', 'MSf(1,3,1)'),('MASS', 'MSf(1,3,2)'),('MASS', 'MSf(1,4,1)'),('MASS', 'MSf(1,4,2)'),
            ('MASS', 'MSf(2,3,1)'),('MASS', 'MSf(2,3,2)'),('MASS', 'MSf(2,4,1)'),('MASS', 'MSf(2,4,2)'),
            #m3g
            ('MASS', 'MSf(1,3,3)'),('MASS', 'MSf(2,3,3)'),('MASS', 'MSf(1,4,3)'),('MASS', 'MSf(2,4,3)'),
            ]
        },
    'file':'user/data_files/140410_7TeV_mneu_mg_m12g_m3g_X2_lookup.dat',
    'info':'this data is already sorted',
    'default_X2':0,
    },
}
