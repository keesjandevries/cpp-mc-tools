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
            ],
        'mc_old':[
            'neu1',
            'gluino',
            'squark_l','squark_l','squark_l','squark_l','squark_r','squark_r','squark_r','squark_r',
            'sbottom1','sbottom2','stop1','stop2',
            ],
        },
    'file':'user/data_files/140416_7TeV_mneu_mg_m12g_m3g_X2_lookup.dat',
    'info':'grid with mneu=10,100,200,300,400,500; mg=m12g=(mneu+100)-1700,2500,5000; m3g=(mneu+200)-1300,2500,5000',
    'default_X2':0,
    },
'universal_limits_8TeV' :{
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
            ],
        'mc_old':[
            'neu1',
            'gluino',
            'squark_l','squark_l','squark_l','squark_l','squark_r','squark_r','squark_r','squark_r',
            'sbottom1','sbottom2','stop1','stop2',
            ],
        },
    'file':'user/data_files/140923_lhc8_grid_mneu_mg_m12g_m3g_X2.txt',
    'info':'grid with mneu=10, 110, 210, 310, 410, 510, 600; '
            'mg=m12g=(mneu+40)-1740, 2500, 5000; m3g=(mneu+180)-1290,2500,5000',
    'default_X2':0,
    },
}
