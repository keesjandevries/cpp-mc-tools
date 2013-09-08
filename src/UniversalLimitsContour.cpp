#include "UniversalLimitsContour.h"

UniversalLimitsContour::UniversalLimitsContour(std::vector<double_pair> coordinates):
    Contour(coordinates)
{
    _coordinates_parameters=GetCoordinatesParameters();     // e.g. 'x' or 'theta'
}
double UniversalLimitsContour::get_point_parameter(double_pair& point){
    // the x coordinate
    return point.first; 
}
double UniversalLimitsContour::get_point_value(double_pair& point){
    // the y coordinate
    return point.second; 
}
std::pair<double_pair,double_pair>UniversalLimitsContour::get_segment(double parameter){
    //loop over coordinates paramters and compare with parameter
    std::pair<double_pair,double_pair> segment;
    int i=0;
    for (std::vector<double>::iterator it= _coordinates_parameters.begin()
            ;it !=_coordinates_parameters.end();it++){
        if (parameter < *it ){
            segment=std::make_pair(_coordinates[i-1],_coordinates[i]);
            break;
        }
        i++;
    }
    return segment;
}
double UniversalLimitsContour::low_extrapolate(double parameter){
    // want to keep constant after smallest neutralino mass. 
    return _coordinates.front().second; 
}
double UniversalLimitsContour::high_extrapolate(double parameter){
    // for neutralino masses beyond contours apply 0 chi2, otherwise it counts as degree of freedom
    return 0.; 
}
double UniversalLimitsContour::interpolate(double parameter, std::pair<double_pair,double_pair> segment){
    double x1,x2,y1,y2;
    x1=segment.first.first;
    y1=segment.first.second;    
    x2=segment.second.first;
    y2=segment.second.second;
    double gradient=(y2-y1)/(x2-x1);
    return y1+(parameter-x1)*gradient;
}
