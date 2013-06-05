#ifndef GETVALUEFUNCTIONS_H
#define GETVALUEFUNCTIONS_H
#include <map>
#include <string>
#include <vector>
#include "Axis.h" // for GetValueFunction type def

///Key function that returns a map of function pointers
std::map<std::string, GetValueFunction > get_GetValueFunction_map();

///Individual declarations
double bsmm_ratio(double *VARS, std::vector<int>& array_ids);
double difference(double *VARS, std::vector<int>& array_ids);
double var1_over_var2_square(double *VARS, std::vector<int>& array_ids);
#endif
