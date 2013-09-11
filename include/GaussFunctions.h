#ifndef GAUSSFUNCTIONS_H
#define GAUSSFUNCTIONS_H
#include <cmath>
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
double gauss(double * , std::vector<int> &  , GaussData & );
double asymmetric_gauss(double * , std::vector<int> &  , GaussData & );
double ratio_gauss(double * , std::vector<int> &  , GaussData & );
double bsmm_ratio_gauss(double * , std::vector<int> &  , GaussData & );
double R_bsmm_chi2(double * , std::vector<int> &  , GaussData & );
double higgs_gauss(double * , std::vector<int> &  , GaussData & );
double lowerlimit(double * , std::vector<int> &  , GaussData & );
double abs_lowerlimit(double * , std::vector<int> &  , GaussData & );
double upperlimit(double * , std::vector<int> &  , GaussData & );
double multi_lowerlimit(double * , std::vector<int> &  , GaussData & );
double multi_abs_lowerlimit(double * , std::vector<int> &  , GaussData & );
double neutralino_lsp(double * , std::vector<int> &  , GaussData & );
#endif
