#include "CutFunctions.h"
std::map<std::string, CutFunction > get_CutFunction_map(){
    std::map<std::string, CutFunction > function_map;
    function_map["predictor_error"]=predictor_error;
    function_map["chi2_error"]=chi2_error;
    return function_map;
}

bool predictor_error(double * vars,std::vector<int> & array_ids){
    return (vars[array_ids[0]]!=0);
}

bool chi2_error(double * vars,std::vector<int> & array_ids){
    return (vars[array_ids[0]]>1e9);
}
