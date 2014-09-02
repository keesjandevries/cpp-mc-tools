#include "GetVarsFunctions.h"
std::map<std::string, GetVarsFunction > get_GetVarsFunction_map(){
    std::map<std::string, GetVarsFunction > function_map;
    function_map["abs"]=abs;
    function_map["negative"]=negative;
    function_map["pb_to_cm2"]=pb_to_cm2;
    function_map["bsmm_ratio"]=bsmm_ratio;
    function_map["difference"]=difference;
    function_map["x_minus_2y"]=x_minus_2y;
    function_map["average"]=average;
    function_map["m3g"]=m3g;
    function_map["power_4_weighted_average"]=power_4_weighted_average;
    function_map["standard_deviation"]=standard_deviation;
    function_map["var1_over_var2_square"]=var1_over_var2_square;
    function_map["var1_over_var2"]=var1_over_var2;
    function_map["abs_var1_over_var2"]=abs_var1_over_var2;
    function_map["sqrt_var1_over_var2"]=sqrt_var1_over_var2;
    function_map["var1_minus_var2_over_var3"]=var1_minus_var2_over_var3;
    function_map["coannihilation_measure"]=coannihilation_measure;
    function_map["focus_point_measure"]=focus_point_measure;
    function_map["funnel_measure"]=funnel_measure;
    function_map["C9_straub"]=C9_straub;
    return function_map;
}

double bsmm_ratio(double *VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]]/(3.46e-9);
}

double abs(double *VARS, std::vector<int>& array_ids){
    return std::abs(VARS[array_ids[0]]);
}

double negative(double *VARS, std::vector<int>& array_ids){
    return -VARS[array_ids[0]];
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

double abs_var1_over_var2(double *VARS, std::vector<int>& array_ids){
    double var1=VARS[array_ids[0]], var2=VARS[array_ids[1]];
    return std::abs(var1/var2);
}

double sqrt_var1_over_var2(double *VARS, std::vector<int>& array_ids){
    double var1=VARS[array_ids[0]], var2=VARS[array_ids[1]];
    double sign_var1=(var1>0)-(var1<0);
    return sign_var1*sqrt(var1)/var2;
}

double var1_minus_var2_over_var3(double *VARS, std::vector<int>& array_ids){
    double var1=VARS[array_ids[0]], var2=VARS[array_ids[1]], 
           var3=VARS[array_ids[2]];
    return var1-var2/var3;
}

double coannihilation_measure(double *VARS, std::vector<int>& array_ids){
    double m1=VARS[array_ids[0]], m2=VARS[array_ids[1]];
    return std::abs(std::abs(m1/m2) - 1);
}

double focus_point_measure(double *VARS, std::vector<int>& array_ids){
    double mu=std::abs(VARS[array_ids[0]]);
    double mneu1=std::abs(VARS[array_ids[1]]); 
    double ma=std::abs(VARS[array_ids[2]]);
    bool is_a_funnel = std::abs(std::abs(ma/(2*mneu1)) - 1) < 0.2;
    return std::abs(std::abs(mu/mneu1) - 1) + 1e9*is_a_funnel;
}

double funnel_measure(double *VARS, std::vector<int>& array_ids){
    double m1=VARS[array_ids[0]], m2=VARS[array_ids[1]];
    return std::abs(std::abs(m1/m2) - 2);
}

double average(double * VARS, std::vector<int> & array_ids){
    double average=0;
    for (std::vector<int>::iterator it=array_ids.begin(); it!=array_ids.end();it++){
        average += VARS[*it];
    }
    average/=array_ids.size();
    return average;
}

double m3g(double * VARS, std::vector<int> & array_ids){
    // m3g calculated as "m3g=(4/sum(M**a))**1/a"
    // this is based on the assumption that the xsection scales as 1/M**a
    // hence sum(1/M**a)=4/m3g**a
    double sum_1_over_M_to_a=0;
    double a=8;
    for (int i=0; i<4; i++){
        sum_1_over_M_to_a+=pow(VARS[array_ids[i]],-a);
    }
    return pow(4/sum_1_over_M_to_a,1/a);
}

double power_4_weighted_average(double * VARS, std::vector<int> & array_ids){
    double summed_weighted_avarage=0;
    double summed_weights=0;
    for (std::vector<int>::iterator it=array_ids.begin(); it!=array_ids.end();it++){
        double mass=VARS[*it];
        summed_weighted_avarage += mass/pow(mass,4);
        summed_weights+=1/pow(mass,4);
    }
    return summed_weighted_avarage/summed_weights;;
}

double standard_deviation(double * VARS, std::vector<int> & array_ids){
    double average=0;
    int N=array_ids.size();
    for (std::vector<int>::iterator it=array_ids.begin(); it!=array_ids.end();it++){
        average += VARS[*it];
    }
    average/=N;
    double sum_squared_differences=0;
    for (std::vector<int>::iterator it=array_ids.begin(); it!=array_ids.end();it++){
        sum_squared_differences += (VARS[*it]-average)*(VARS[*it]-average);
    }
    return sqrt(sum_squared_differences/N);
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
