#include <vector>
#include <utility> //std::pair, std::make_pair
#include <iostream>
#include "Contour.h"
#include "DefaultContour.h"
#include "LogXLogYContour.h"
#include "ContourChi2Functions.h"

int main(){
    double_pair x0(-1.0, 10.0);
    double_pair x1(0.0, 0.0);
    double_pair x2(1.0, 1.0);
    std::vector<double_pair> coords;
    coords.push_back(x0);
    coords.push_back(x1);
    coords.push_back(x2);
    DefaultContour contour(coords);
    std::vector<double> point;
    point.push_back(0.5);
    point.push_back(2.0);
    std::cout << "parameter for x3: " << contour.GetPointParameter(point) << std::endl; 
    std::cout << "value for x3: " << contour.GetPointValue(point) << std::endl; 
    std::cout << "contour at -10 "<< contour.GetContourValue(-10) << std::endl;
    std::cout << "contour at 0.5 "<< contour.GetContourValue(0.5) << std::endl;

    std::vector<int> array_ids;
    array_ids.push_back(0);
    array_ids.push_back(1);
    Contour * contour_ptr=&contour;

    ContourConstraint constraint(array_ids,contour_ptr,get_ContourFunc_map()["ma_tanb_mc8"]);
    double vars[]={12., 50.};
    std::cout << "test constraint " << constraint(vars) << std::endl; 

    // try out log contour
    // make a coordinates
    double_pair l0(1.0, 1.0);
    double_pair l1(10.0, 100.0);
    double_pair l2(100.0, 10000.0);
    std::vector<double_pair> lcoords;
    lcoords.push_back(l0);
    lcoords.push_back(l1);
    lcoords.push_back(l2);
    // make contour
    LogXLogYContour lcontour(lcoords);
    // make a point
    std::vector<double> point1;
    point1.push_back(2.0);
    point1.push_back(2.0);
    // output
    std::cout << "Parameters should return the square value" << std::endl;
    std::cout << "For 2.0 get contour value" << lcontour.GetContourValue(2.0) << std::endl;
   
    return 0;
}
