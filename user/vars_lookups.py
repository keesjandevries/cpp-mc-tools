def get():
    return {
        'chi2': {'array_ids': 0},
        #cmssm/nuhm1 inputs
        'm0': {'mc_old': 'm0', 'mcpp': ('MINPAR', 'in_M0')},
        'm12': {'mc_old': 'm12', 'mcpp': ('MINPAR', 'in_M12')},
        'A0': {'mc_old': 'A0', 'mcpp': ('MINPAR', 'in_A')},
        'tanb': {'mc_old': 'tanb', 'mcpp': ('MINPAR', 'TB')},
        'mh2': {'mc_old': 'mh2', 'mcpp': ('EXTPAR', 'in_MH2')},
        #pmssm inputs
        'msq12': {'mc_old': 'msq12', 'mcpp': ('MC_EXTPAR', 'in_MC_Msq12')},
        'msq3': {'mc_old': 'msq3', 'mcpp': ('MC_EXTPAR', 'in_MC_Msq3')},
        'msl': {'mc_old': 'msl', 'mcpp': ('MC_EXTPAR', 'in_MC_Msl')},
        'A': {'mc_old': 'A', 'mcpp': ('MC_EXTPAR', 'in_MC_A')},
        'M1': {'mc_old': 'M1', 'mcpp': ('EXTPAR', 'in_M1')},
        'M2': {'mc_old': 'M2'},
        'M3': {'mc_old': 'M3', 'mcpp': ('EXTPAR', 'in_M3')},
        'in_ma': {'mc_old': 'in_ma', 'mcpp': ('EXTPAR', 'in_MA0')},
        'in_mu': {'mc_old': 'in_mu', 'mcpp': ('EXTPAR', 'in_MUE')},
        #observables
        'MA': {'mc_old': 'MA', 'mcpp': ('MASS', 'MA0')},
        'mg': {'mc_old': 'gluino', 'mcpp': ('MASS', 'MGl')},
        'mh': {'mc_old': 'mh', 'mcpp': ('MASS', 'Mh0')},
        'mneu1': {'mc_old': 'neu1', 'mcpp': ('MASS', 'MNeu(1)')},
        'mchar1': {'mc_old': 'chi1', 'mcpp': ('MASS', 'MCha(1)')},
        'msbot1': {'mc_old': 'sbottom1', 'mcpp': ('MASS', 'MSf(1,4,3)')},
        'msbot2': {'mc_old': 'sbottom2', 'mcpp': ('MASS', 'MSf(2,4,3)')},
        'mstau1': {'mc_old': 'stau1', 'mcpp': ('MASS', 'MSf(1,2,3)')},
        'mstop1': {'mc_old': 'stop1', 'mcpp': ('MASS', 'MSf(1,3,3)')},
        'mstop2': {'mc_old': 'stop2', 'mcpp': ('MASS', 'MSf(2,3,3)')},
        'mu': {'mc_old': 'mu', 'mcpp': ('HMIX', 'MUE')},
        'oh2': {'mcpp': ('Micromegas', 'Omega')},
        'ssmh': {'mc_old': 'ssmh'},
        }