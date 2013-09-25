#ifndef CUTFUNCTIONS_H
#define CUTFUNCTIONS_H
#include <cmath>
#include <map>
#include <string>
#include <vector>
#include "Cut.h" 

///Key function that returns a map of function pointers
std::map<std::string, CutFunction > get_CutFunction_map();
#endif // CUTFUNCTIONS_H

