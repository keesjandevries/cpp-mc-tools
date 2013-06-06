#include "DefaultContour.h"

DefaultContour::DefaultContour(std::vector<double_pair> coordinates):
    Contour(coordinates)
{
    _coordinates_parameters=GetCoordinatesParameters();     // e.g. 'x' or 'theta'
}
double DefaultContour::get_point_parameter(double_pair point){
    return point.first; // the x coordinate
}
double DefaultContour::get_point_value(double_pair point){
    return point.second; // the y coordinate
}
std::pair<double_pair,double_pair>DefaultContour::get_segment(double parameter){
    //loop over coordinates paramters and compare with parameter
    std::pair<double_pair,double_pair> segment;
    int i=0;
    for (std::vector<double>::iterator it= _coordinates_parameters.begin()
            ;it !=_coordinates_parameters.end();it++){
        //FIXME: this comparison depends on the coordinates being 
        //       sorted according to the magnitude of their parameter
        if (parameter < *it ){
            segment=std::make_pair(_coordinates[i],_coordinates[i+1]);
            break;
        }
        i++;
    }
    return segment;
}
double DefaultContour::low_extrapolate(double parameter){
    return _coordinates.front().second; // the y-coordinate of the first element
}
double DefaultContour::high_extrapolate(double parameter){
    return _coordinates.back().second; // the y-coordinate of the last element
}
double DefaultContour::interpolate(double parameter, std::pair<double_pair,double_pair> segment){
    double x1,x2,y1,y2;
    x1=segment.first.first;
    y1=segment.first.second;    
    x2=segment.second.first;
    y2=segment.second.second;
    double gradient=(y2-y1)/(x2-x1);
    return y1+(parameter-x1)*gradient;
}
