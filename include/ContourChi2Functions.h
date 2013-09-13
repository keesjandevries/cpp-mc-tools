#ifndef INC_CONTOURCHI2FUNCTIONS_H
#define INC_CONTOURCHI2FUNCTIONS_H
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include "Contour.h"
#include "ContourConstraint.h"

std::map< std::string, ContourFunc>  get_ContourFunc_map();

double mc8_ma_tanb(double * , std::vector<int> & , std::vector<Contour*> &);
double xenon100_jul_2012(double * , std::vector<int> & , std::vector<Contour*> &);
double xenon100_jul_2012_Sigma_pi_N_unc(double * , std::vector<int> & , std::vector<Contour*> &);
double m0_m12_power_4(double *, std::vector<int>&, std::vector<Contour*> &);
double one_dim_chi2_lookup(double *, std::vector<int>&, std::vector<Contour*> &);
//double universal_limits(double * , std::vector<int> & , std::vector<Contour*> &);
//double m3g_universal_limits(double * , std::vector<int> & , std::vector<Contour*> &);
//double mg_universal_limits(double * , std::vector<int> & , std::vector<Contour*> &);
#endif
