#ifndef INC_RADIALCONTOUR_H
#define INC_RADIALCONTOUR_H
#include <cmath>
#include <complex>
#include <algorithm>
#include "Contour.h"

class RadialContour: public Contour{
    public:
        // Directly accesible
        RadialContour(){};
        RadialContour(std::vector<double_pair>/*coords*/);   
        virtual ~RadialContour(){};
    private:
        bool parameter_comparison(double_pair&,double_pair&);
        // virtual member functions
        virtual double get_point_parameter(double_pair&);    //theta
        virtual double get_point_value(double_pair&);        //radius
        virtual std::pair<double_pair,double_pair> get_segment(double /*parameter*/);
        virtual double interpolate(double /*parameter*/,std::pair<double_pair,double_pair> /*segment*/);
        virtual double low_extrapolate(double /*parameter*/);
        virtual double high_extrapolate(double /*parameter*/);
};
#endif
