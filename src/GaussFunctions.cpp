#include "GaussFunctions.h"
std::map<std::string, GaussFunc > get_GaussFunc_map(){
    std::map<std::string, GaussFunc > gaussfunc_map;
    gaussfunc_map["gauss"]=gauss;
    return gaussfunc_map;
}

double gauss(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c =VARS[array_ids[0]];
    return (data.mu-c)*(data.mu-c)/data.sigma_square;
} 
