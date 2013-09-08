#include <vector>
#include <utility> //std::pair, std::make_pair
#include <iostream>
#include "Contour.h"
#include "DefaultContour.h"
#include "LogXLogYContour.h"
#include "UniversalLimitsContour.h"
#include "ContourChi2Functions.h"

int main(){
    // mneu_mg_contour
    std::vector<double_pair> mneu_mg_coords;
    mneu_mg_coords.push_back(std::make_pair(0,900));
    mneu_mg_coords.push_back(std::make_pair(400,700));
    mneu_mg_coords.push_back(std::make_pair(450,500));
    UniversalLimitsContour mneu_mg_cont(mneu_mg_coords);
    // mneu_m3g_contour
    std::vector<double_pair> mneu_m3g_coords;
    mneu_m3g_coords.push_back(std::make_pair(0,500));
    mneu_m3g_coords.push_back(std::make_pair(300,400));
    UniversalLimitsContour mneu_m3g_cont(mneu_m3g_coords);
    // make contour vector
    Contour * mneu_mg_cont_ptr=&mneu_mg_cont;
    Contour * mneu_m3g_cont_ptr=&mneu_m3g_cont;
    std::vector<Contour*> contours;
    contours.push_back(mneu_mg_cont_ptr);
    contours.push_back(mneu_m3g_cont_ptr);
    // array_ids
    std::vector<int> array_ids;
    for (int i=0; i<6; i++) array_ids.push_back(i);
    // make constraint
    ContourConstraint constraint(array_ids,contours,get_ContourFunc_map()["universal_limits"]);
    //double 
    double vars[]={0,900,500,500,500,500};
    double vars2[]={0,1800,5000,5000,5000,5000};
    double vars3[]={500,500,500,500,500,500};
    std::cout << "constraints should give 7.82:  " << constraint(vars) << std::endl;
    std::cout << "constraints should give 0.345: " << constraint(vars2) << std::endl;
    std::cout << "constraints should give << 1 : " << constraint(vars3) << std::endl;
    return 0;
}
