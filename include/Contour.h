#ifndef INC_CONTOUR_H
#define INC_CONTOUR_H
#include <iostream>
#include <map>
#include <utility>  //std::pair
#include <vector>
#include <string>

// define double_pair to reduce syntacs
typedef std::pair<double,double> double_pair;

class Contour{
    public:
        // Directly accesible
        Contour(){};
        Contour(std::vector<double_pair>/*coords*/);   //FIXME: only coordinates for now
        virtual ~Contour(){};
        // These are functions that should be available
        double GetPointParameter(std::vector<double> /*point_coordinates*/);
        //FIXME: make this into const (cf. http://stackoverflow.com/questions/13555556/cannot-convert-parameter-from-int-to-int)
        double GetPointParameter(double_pair&);
        double GetPointValue(std::vector<double> /*point_coordinates*/);
        double GetPointValue(double_pair &);
        double GetContourValue(double /*parameter*/);
        // FIXME: these should maybe be private memberfunctions
        std::vector<double> GetCoordinatesParameters();
    protected:
        std::vector<double_pair> _coordinates;
        std::vector<double> _coordinates_parameters;     // e.g. 'x' or 'theta'
        // virtual member functions
        virtual double get_point_value(double_pair&)=0;        //e.g. get_radius(...), get_y(...)
        virtual double get_point_parameter(double_pair&)=0;    //e.g. get_theta(...), get_x(...)
        //FIXME: since this is always the same, it's better to make it non-virtual
        virtual std::pair<double_pair,double_pair> get_segment(double /*parameter*/)=0;
        virtual double interpolate(double /*parameter*/,std::pair<double_pair,double_pair> /*segment*/)=0;
        virtual double low_extrapolate(double /*parameter*/)=0;
        virtual double high_extrapolate(double /*parameter*/)=0;
};
#endif
