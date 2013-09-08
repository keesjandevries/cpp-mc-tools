#include "GaussFunctions.h"
std::map<std::string, GaussFunc > get_GaussFunc_map(){
    std::map<std::string, GaussFunc > gaussfunc_map;
    gaussfunc_map["gauss"]=gauss;
    return gaussfunc_map;
}

double sum_squares(std::vector<double> sigmas){
    double sum=0;
    std::vector<double>::iterator it;
    for (it=sigmas.begin();it!=sigmas.end();it++){
        sum+=(*it)*(*it);
    }
    return sum;
}

double gauss(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=VARS[array_ids[0]];
    double sigma_squared=sum_squares(data.sigmas);
    return (data.mu-c)*(data.mu-c)/sigma_squared;
} 
