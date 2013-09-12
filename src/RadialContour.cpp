#include "RadialContour.h"

//FIXME: maybe want to sort all contours, not only the Radial
struct sort_pred{
    bool operator()(const double_pair& p1, const double_pair& p2){
        return (atan2(p1.second,p1.first)<atan2(p2.second,p2.first));
    }
};

RadialContour::RadialContour(std::vector<double_pair> coordinates):
    Contour(coordinates)
{
    //sort coordinates according to theta
    std::sort(_coordinates.begin(),_coordinates.end(),sort_pred());
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
    return _coordinates.front().second; // the y-coordinate of the first element
}
double RadialContour::high_extrapolate(double parameter){
    return _coordinates.back().second; // the y-coordinate of the last element
}
double RadialContour::interpolate(double theta, std::pair<double_pair,double_pair> segment){
    // Derivation:
    //
    // We are given theta, corresponding to a point p=(p1,p2)
    // and a line segment between z1=(x1,y1), z2=(x2,y2).
    // We denote their sperical coordinates theta_{n} and r{n} where n=p,1,2
    //
    // Note that z1, z2 and the origin make up a triangle.
    // Let us denote alpa_{i} i=0,1,2 the corresponding angles
    //
    // We want to find the disance rp corresponding to the point where
    // a line through the origin to p intersects the line segment.
    //
    // Let aplha_p be the angle beween the arcs correspondoing to r1 and rp.
    //
    // Note that rp/sin(alpha_1)=r1/sin(pi-alpha_p-alpha_1)
    // Hence rp=r1*sin(alpha_1)/sin(aplha_p+alpha_1)
    //
    // using complex numbers:
    // alhpa_1=|arg(z1/(z1-z2))|, r1=norm(z1), alpha_p=|theta-arg(z1)|
    //
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
    double r1=std::norm(z1);
    double alpha_p=std::abs(theta-std::arg(z1));
    double alpha_1=std::abs(std::arg(z1/(z1-z2)));
    // finally
    std::cout << "Theta: "  << theta << std::endl;
    return r1*sin(alpha_1)/sin(alpha_1+alpha_p);
}
