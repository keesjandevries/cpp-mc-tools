#include "GetVarsFunctions.h"
std::map<std::string, GetVarsFunction > get_GetVarsFunction_map(){
    std::map<std::string, GetVarsFunction > function_map;
    function_map["bsmm_ratio"]=bsmm_ratio;
    function_map["difference"]=difference;
    function_map["average"]=average;
    function_map["var1_over_var2_square"]=var1_over_var2_square;
    function_map["var1_over_var2"]=var1_over_var2;
    function_map["sqrt_var1_over_var2"]=sqrt_var1_over_var2;
    return function_map;
}

double bsmm_ratio(double *VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]]/(3.46e-9);
}

//FIXME: use pass by reference e.g. std::vector<int>& array
double difference(double *VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]]-VARS[array_ids[1]];
}

double var1_over_var2_square(double *VARS, std::vector<int>& array_ids){
    // useful for e.g. mh2/(m0*m0) 
    double var1=VARS[array_ids[0]], var2=VARS[array_ids[1]];
    return var1/(var2*var2);
}

double var1_over_var2(double *VARS, std::vector<int>& array_ids){
    double var1=VARS[array_ids[0]], var2=VARS[array_ids[1]];
    return var1/var2;
}

double sqrt_var1_over_var2(double *VARS, std::vector<int>& array_ids){
    double var1=VARS[array_ids[0]], var2=VARS[array_ids[1]];
    double sign_var1=(var1>0)-(var1<0);
    return sign_var1*sqrt(var1)/var2;
}

double average(double * VARS, std::vector<int> & array_ids){
    double average;
    for (std::vector<int>::iterator it=array_ids.begin(); it!=array_ids.end();it++){
        average += VARS[*it];
    }
    average/=array_ids.size();
    return average;
}
