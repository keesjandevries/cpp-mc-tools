#ifndef  INC_CONTOURCONSTRAINT_H
#define INC_CONTOURCONSTRAINT_H
#include <iostream>
#include <vector>
#include "BaseGetValueFunction.h"
#include "Contour.h"

// typedef for member gaussian X^2 function
typedef double(*ContourFunc)(double *, std::vector<int> & , Contour *); 

class ContourConstraint: public BaseGetValueFunction{
    public:
        ContourConstraint(std::vector<int> /*oids*/ ,Contour *, ContourFunc );
        virtual ~ContourConstraint(){};
        virtual double operator()(double *);
        double GetChi2(double *);
    private:
        // observable ids (Oid) for acces to argument of GetChi2(), in this case double *
        std::vector<int> _array_ids;
        Contour *_contour;
        ContourFunc _contour_chi2_function ;
};
#endif
