#ifndef GAUSSFUNCTIONS_H
#define GAUSSFUNCTIONS_H
#include <map>
#include <string>
#include <vector>
#include "GaussConstraint.h" // for GetValueFunction type def

//typedef double(*GaussFunc)(double *, std::vector<int> * , GaussData *); 
//
///Key function that returns a map of function pointers
std::map<std::string, GaussFunc > get_GaussFunc_map();
///Auxiliry funcitons
double sum_squares(std::vector<double>);
///Individual declarations
double gauss(double * VARS, std::vector<int> & array_ids , GaussData & data);
#endif
