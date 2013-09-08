#include "Contour.h"
Contour::Contour(std::vector<double_pair> coordinates):
    _coordinates(coordinates)
{
    // intentionally empty
    // cannot invoke GetCoordinatesParameters, since in depends on get_point_parameters
}

double Contour::GetContourValue(double parameter){
    if (parameter < _coordinates_parameters.front()){ 
        return low_extrapolate(parameter);
    }
    else if (parameter <=_coordinates_parameters.back()){ 
        std::pair< double_pair,double_pair > segment=get_segment(parameter);
        return interpolate(parameter,segment);
    }
    else { 
        return high_extrapolate(parameter);
    }
}
double Contour::GetPointParameter(std::vector<double> point_coordinates_vec){
    if (point_coordinates_vec.size() ==2){
        double_pair point_coordinates(point_coordinates_vec[0],point_coordinates_vec[1]);
        return get_point_parameter(point_coordinates);    
    }
    else{
        //FIXME: maybe have to throw something.. this may be better error handling
        std::cout << "ERROR: GetPointParameter takes two doubles in a vector or pair" << std::endl;
        std::cout << "       " << point_coordinates_vec.size() << " were given" << std::endl;
    }
}
double Contour::GetPointParameter(double_pair & point){
    return get_point_parameter(point);    
}
double Contour::GetPointValue(std::vector<double> point_coordinates_vec){
    if (point_coordinates_vec.size() ==2){
        double_pair point_coordinates(point_coordinates_vec[0],point_coordinates_vec[1]);
        return get_point_value(point_coordinates);    
    }
    else{
        //FIXME: maybe have to throw something.. this may be better error handling
        std::cout << "ERROR: GetPointValue takes two doubles in a vector " << std::endl;
        std::cout << "       " << point_coordinates_vec.size() << " were given" << std::endl;
    }
}
double Contour::GetPointValue(double_pair& point){
    return get_point_value(point);    
}
std::vector<double> Contour::GetCoordinatesParameters(){
    std::vector<double> coordinates_parameters;
    for (std::vector<double_pair>::iterator it=_coordinates.begin();it!=_coordinates.end();it++){
        coordinates_parameters.push_back(get_point_parameter(*it));
    }
    return coordinates_parameters;
}

