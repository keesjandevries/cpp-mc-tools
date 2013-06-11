#include "LogXLogYContour.h"

LogXLogYContour::LogXLogYContour(std::vector<double_pair> coordinates):
    Contour(coordinates)
{
    _coordinates_parameters=GetCoordinatesParameters();     // e.g. 'x' or 'theta'
}
double LogXLogYContour::get_point_parameter(double_pair& point){
    return point.first; // the x coordinate
}
double LogXLogYContour::get_point_value(double_pair& point){
    return point.second; // the y coordinate
}
std::pair<double_pair,double_pair>LogXLogYContour::get_segment(double parameter){
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
double LogXLogYContour::low_extrapolate(double parameter){
    return _coordinates.front().second; // the y-coordinate of the first element
}
double LogXLogYContour::high_extrapolate(double parameter){
    return _coordinates.back().second; // the y-coordinate of the last element
}
double LogXLogYContour::interpolate(double parameter, std::pair<double_pair,double_pair> segment){
    double log_x1=log10(segment.first.first);
    double log_y1=log10(segment.first.second);    
    double log_x2=log10(segment.second.first);
    double log_y2=log10(segment.second.second);
    double gradient=(log_y2-log_y1)/(log_x2-log_x1);
    return pow(10,(log_y1+(log10(parameter)-log_x1)*gradient));
}
