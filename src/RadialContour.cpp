#include "RadialContour.h"


RadialContour::RadialContour(std::vector<double_pair> coordinates):
    Contour(coordinates)
{
    if (get_point_parameter(_coordinates.front())>get_point_parameter(_coordinates.back())){
        std::reverse(_coordinates.begin(),_coordinates.end());
    }
    _coordinates_parameters=GetCoordinatesParameters();     // e.g. 'x' or 'theta'
}

//theta
double RadialContour::get_point_parameter(double_pair& point){
    return atan2(point.second,point.first); 
}
//radius
double RadialContour::get_point_value(double_pair& point){
    return sqrt(point.first*point.first+point.second*point.second); // the y coordinate
}
std::pair<double_pair,double_pair>RadialContour::get_segment(double parameter){
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
double RadialContour::low_extrapolate(double parameter){
    return get_point_value(_coordinates.front()); // radius
}
double RadialContour::high_extrapolate(double parameter){
    return get_point_value(_coordinates.back()); // radius
}
double RadialContour::interpolate(double theta, std::pair<double_pair,double_pair> segment){
    //get coordinates
    double x1,x2,y1,y2;
    x1=segment.first.first;
    y1=segment.first.second;    
    x2=segment.second.first;
    y2=segment.second.second;
    //make into complex numbers
    std::complex<double>z1(x1,y1);
    std::complex<double>z2(x2,y2);
    // r1, alpha_1, alpha_p
    double r1=std::abs(z1);
    double alpha_p=std::abs(theta-std::arg(z1));
    double alpha_1=std::abs(std::arg(z1/(z1-z2)));
    // finally
    return r1*sin(alpha_1)/sin(alpha_1+alpha_p);
}
