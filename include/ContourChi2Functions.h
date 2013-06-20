#ifndef INC_CONTOURCHI2FUNCTIONS_H
#define INC_CONTOURCHI2FUNCTIONS_H
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include "ContourConstraint.h"

std::map< std::string, ContourFunc>  get_ContourFunc_map();

double ma_tanb_mc8(double * , std::vector<int> & array_ids, std::vector<Contour*> &);
double xenon100_mc8(double * , std::vector<int> & array_ids, std::vector<Contour*> &);
double universal_limits(double * , std::vector<int> & array_ids, std::vector<Contour*> &);
double m3g_universal_limits(double * , std::vector<int> & array_ids, std::vector<Contour*> &);
double mg_universal_limits(double * , std::vector<int> & array_ids, std::vector<Contour*> &);
#endif
