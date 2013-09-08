#include "Chi2Calculator.h"

double Chi2Calculator::operator()(double* VARS){
    std::vector<BaseGetValueFunction*>::iterator it;
    double chi2=0;
    for (it=_constraints.begin();it!=_constraints.end();it++){
        chi2+=(*(*it))(VARS);
    }
    return chi2;
}

void Chi2Calculator::AddConstraint(BaseGetValueFunction* constraint){
    _constraints.push_back(constraint);
}
