#include "GetValueFunctions.h"
std::map<std::string, GetValueFunction > get_GetValueFunction_map(){
    std::map<std::string, GetValueFunction > function_map;
    function_map["bsmm_ratio"]=bsmm_ratio;
    return function_map;
}

double bsmm_ratio(double *VARS, std::vector<int>* array_ids){
    int bsmm_id=(*array_ids)[0];
    return VARS[bsmm_id]/(3.46e-9);
}
