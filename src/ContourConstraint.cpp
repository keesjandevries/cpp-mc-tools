#include "ContourConstraint.h"
//NOTE: members of classes are indicated with "_" in front of the variable

ContourConstraint::ContourConstraint(std::vector<int> int_obs_ids, Contour * contour, ContourFunc chi2function):
    _array_ids(int_obs_ids),
    _contour_chi2_function(chi2function),
    _contour(contour)
{
    // intentionally empty
}

double ContourConstraint::GetChi2(double* vars){
    return _contour_chi2_function(vars,_array_ids ,_contour);
}

double ContourConstraint::operator()(double* vars){
    return _contour_chi2_function(vars,_array_ids ,_contour);
}
