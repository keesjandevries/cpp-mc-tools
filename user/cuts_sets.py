def get(name):
    return cuts_sets.get(name,[])

cuts_sets={
        'default':['feynhiggs_error','micromegas_error'],
        'chi2-check':['chi2-check'],
        }
