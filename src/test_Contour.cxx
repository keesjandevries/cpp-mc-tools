#include <vector>
#include <utility> //std::pair, std::make_pair
#include <iostream>
#include "Contour.h"

int main(){
    double_pair x0(-1.0, 10.0);
    double_pair x1(0.0, 0.0);
    double_pair x2(1.0, 1.0);
    std::vector<double_pair> coords;
    coords.push_back(x0);
    coords.push_back(x1);
    coords.push_back(x2);
    Contour contour(coords);
    double_pair x3(2.0, 1.0);

    std::cout << "parameter for x3: " << contour.GetPointParameter(x3) << std::endl; 
    std::cout << "value for x3: " << contour.GetPointValue(x3) << std::endl; 
    std::cout << "contour at -10 "<< contour.GetContourValue(-10) << std::endl;
    return 0;
}
