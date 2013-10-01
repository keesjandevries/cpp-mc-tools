#ifndef CUTFUNCTIONS_H
#define CUTFUNCTIONS_H
#include <iostream> //for debugging
#include <cmath>
#include <map>
#include <string>
#include <vector>
#include "Cut.h" 

///Key function that returns a map of function pointers
std::map<std::string, CutFunction > get_CutFunction_map();
bool predictor_error(double *, std::vector<int> &);
bool chi2_error(double *, std::vector<int> &);

#endif // CUTFUNCTIONS_H

