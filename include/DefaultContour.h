#ifndef INC_DEFAULTCONTOUR_H
#define INC_DEFAULTCONTOUR_H
#include "Contour.h"


class DefaultContour: public Contour{
    public:
        // Directly accesible
        DefaultContour(){};
        DefaultContour(std::vector<double_pair>/*coords*/);   
        virtual ~DefaultContour(){};
    private:
        // virtual member functions
        virtual double get_point_parameter(double_pair&);    //e.g. get_theta(...), get_x(...)
        virtual double get_point_value(double_pair&);        //e.g. get_radius(...), get_y(...)
        virtual std::pair<double_pair,double_pair> get_segment(double /*parameter*/);
        virtual double interpolate(double /*parameter*/,std::pair<double_pair,double_pair> /*segment*/);
        virtual double low_extrapolate(double /*parameter*/);
        virtual double high_extrapolate(double /*parameter*/);
};
#endif
