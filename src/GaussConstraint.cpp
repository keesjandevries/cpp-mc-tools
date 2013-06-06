#include "GaussConstraint.h"
//NOTE: members of classes are indicated with "_" in front of the variable

GaussConstraint::GaussConstraint(std::vector<int> int_obs_ids, double mu, std::vector<double> sigmas , GaussFunc chi2function):
    _array_ids(int_obs_ids),
    _gauss_chi2_function(chi2function)
{
    _data.mu=mu;
    _data.sigma_square  = get_sigma_square(sigmas);
}

double GaussConstraint::GetChi2(double* VARS){
    return _gauss_chi2_function(VARS,_array_ids ,_data);
}

double GaussConstraint::operator()(double* VARS){
    return _gauss_chi2_function(VARS,_array_ids ,_data);
}

double GaussConstraint::get_sigma_square(std::vector<double> sigmas){
    double sigma_square=0.;
    //FIXME: use proper iterator, to lazy atm
    for(unsigned int i=0;i<sigmas.size();i++){
        sigma_square+= sigmas[i]*sigmas[i] ;
    }
    return sigma_square;
}

