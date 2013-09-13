#ifndef INC_RADIALCONTOUR_H
#define INC_RADIALCONTOUR_H
#include <cmath>
#include <complex>
#include <algorithm>
#include "Contour.h"

class RadialContour: public Contour{
    public:
/// Reverse order of coordinates if they start with largest theta
        RadialContour(){};
        RadialContour(std::vector<double_pair>/*coords*/);   
        virtual ~RadialContour(){};
    private:
/// theta
        virtual double get_point_parameter(double_pair&);    
/// radius
        virtual double get_point_value(double_pair&);        //radius
        virtual std::pair<double_pair,double_pair> get_segment(double /*parameter*/);
/// Derivation for interpolation:
///
/// We are given theta, corresponding to a point p=(p1,p2)
/// and a line segment between z1=(x1,y1), z2=(x2,y2).
/// We denote their sperical coordinates theta_{n} and r{n} where n=p,1,2
///
/// Note that z1, z2 and the origin make up a triangle.
/// Let us denote alpa_{i} i=0,1,2 the corresponding angles
///
/// We want to find the disance rp corresponding to the point where
/// a line through the origin to p intersects the line segment.
///
/// Let aplha_p be the angle beween the arcs correspondoing to r1 and rp.
///
/// Note that rp/sin(alpha_1)=r1/sin(pi-alpha_p-alpha_1)
/// Hence rp=r1*sin(alpha_1)/sin(aplha_p+alpha_1)
///
/// using complex numbers:
/// alhpa_1=|arg(z1/(z1-z2))|, r1=abs(z1), alpha_p=|theta-arg(z1)|
///
        virtual double interpolate(double /*parameter*/,std::pair<double_pair,double_pair> /*segment*/);
/// extrapolation: get the radius of the first or last coordinate 
        virtual double low_extrapolate(double /*parameter*/);
        virtual double high_extrapolate(double /*parameter*/);
};
#endif
