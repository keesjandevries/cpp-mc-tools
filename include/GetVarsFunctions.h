#ifndef GETVALUEFUNCTIONS_H
#define GETVALUEFUNCTIONS_H
#include <cmath>
#include <map>
#include <string>
#include <vector>
#include "VarsFunction.h" // for GetVarsFunction type def

///Key function that returns a map of function pointers
std::map<std::string, GetVarsFunction > get_GetVarsFunction_map();

///Individual declarations
double abs(double *VARS, std::vector<int>& array_ids);
double pb_to_cm2(double *VARS, std::vector<int>& array_ids);
double bsmm_ratio(double *VARS, std::vector<int>& array_ids);
double difference(double *VARS, std::vector<int>& array_ids);
double x_minus_2y(double *VARS, std::vector<int>& array_ids);
double average(double *VARS, std::vector<int>& array_ids);
double m3g(double *VARS, std::vector<int>& array_ids);
double power_4_weighted_average(double *VARS, std::vector<int>& array_ids);
double standard_deviation(double *VARS, std::vector<int>& array_ids);
double var1_over_var2_square(double *VARS, std::vector<int>& array_ids);
double var1_over_var2(double *VARS, std::vector<int>& array_ids);
double sqrt_var1_over_var2(double *VARS, std::vector<int>& array_ids);
double C9_straub(double * , std::vector<int> & );
double f9Hpm(double );
#endif
