#include "ContourConstraint.h"

ContourConstraint::ContourConstraint(std::vector<int> int_obs_ids, Contour * contour, ContourFunc chi2function):
    _array_ids(int_obs_ids),
    _contour_chi2_function(chi2function)
{
    _contours.push_back(contour);
}

ContourConstraint::ContourConstraint(std::vector<int> int_obs_ids, std::vector<Contour*> contours, ContourFunc chi2function):
    _array_ids(int_obs_ids),
    _contour_chi2_function(chi2function),
    _contours(contours)
{
    //intentionally emtpy
}

double ContourConstraint::operator()(double* vars){
    return _contour_chi2_function(vars,_array_ids ,_contours);
}
