#ifndef  INC_CONSTRAINT_H
#define INC_CONSTRAINT_H
#include <iostream>
#include <vector>
#include "BaseGetValueFunction.h"

// data structure is always central value mu, st
struct GaussData{
    double mu, sigma_square;
}; 
// typedef for member gaussian X^2 function
typedef double(*GaussFunc)(double *, std::vector<int> & , GaussData &); 

class GaussConstraint: public BaseGetValueFunction{
    public:
        GaussConstraint(std::vector<int> /*oids*/ ,double /*mu*/, std::vector<double>  /*sigmas*/,GaussFunc);
        virtual ~GaussConstraint(){};
        virtual double operator()(double *);
        double GetChi2(double *);
        //Note: no copy or assignment operators are defined
        //following the google c++ style guide, this can be 
        //simply handled by using pointers in the STL containers.
    private:
        // observable ids (Oid) for acces to argument of GetChi2(), in this case double *
        std::vector<int> _array_ids;
        GaussData        _data; 
        GaussFunc        _gauss_chi2_function;
        // FIXME: not sure if this function should be private, in is not used anywhere else
        double get_sigma_square(std::vector<double>);
};
#endif
