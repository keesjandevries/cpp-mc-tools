#include "GetVarsFunctions.h"
std::map<std::string, GetVarsFunction > get_GetVarsFunction_map(){
    std::map<std::string, GetVarsFunction > function_map;
    function_map["pb_to_cm2"]=pb_to_cm2;
    function_map["bsmm_ratio"]=bsmm_ratio;
    function_map["difference"]=difference;
    function_map["x_minus_2y"]=x_minus_2y;
    function_map["average"]=average;
    function_map["var1_over_var2_square"]=var1_over_var2_square;
    function_map["var1_over_var2"]=var1_over_var2;
    function_map["sqrt_var1_over_var2"]=sqrt_var1_over_var2;
    function_map["C9_straub"]=C9_straub;
    return function_map;
}

double bsmm_ratio(double *VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]]/(3.46e-9);
}

double pb_to_cm2(double *VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]]*(1e-36);
}

double difference(double *VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]]-VARS[array_ids[1]];
}

double x_minus_2y(double *VARS, std::vector<int>& array_ids){
    // useful for e.g. m_H/A-2*m_neu1
    return VARS[array_ids[0]]-2*VARS[array_ids[1]];
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

// Equation 30 arXiv:1308.1501
double f9Hpm(double x){
    return -2*(38 -79*x+47*x*x)/(9*pow((1-x),3)) -4*(4-6*x+3*x*x*x)*log(x)/(3*(pow((1-x),4)));
}

// Equation 15 arXiv:1308.1501
double C9_straub(double * VARS, std::vector<int> & array_ids){
    double mt=VARS[array_ids[0]];
    double mHpm=VARS[array_ids[1]];
    double tanb=VARS[array_ids[2]];
    double cotb=1/tanb;
    double x=mt*mt/(mHpm*mHpm);
    return -x*cotb*cotb*f9Hpm(x);
}


