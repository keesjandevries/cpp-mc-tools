def get(name):
    return constraints.get(name)

constraints={
        'oh2-only':['chi2Oh2'],
        'chi2+nuisance':['chi2','chi2-Mt','chi2-Dalpha-had','chi2-MZ'],
        }
            
