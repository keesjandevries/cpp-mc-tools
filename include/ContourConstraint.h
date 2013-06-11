#ifndef  INC_CONTOURCONSTRAINT_H
#define INC_CONTOURCONSTRAINT_H
#include <iostream>
#include <vector>
#include "BaseGetValueFunction.h"
#include "Contour.h"

// typedef for member gaussian X^2 function
typedef double(*ContourFunc)(double *, std::vector<int> & , std::vector<Contour*> &); 

class ContourConstraint: public BaseGetValueFunction{
    public:
        //FIXME: may want to remove this constructor if no longer in use
        ContourConstraint(std::vector<int> /*oids*/ ,Contour*, ContourFunc );
        ContourConstraint(std::vector<int> /*oids*/ ,std::vector<Contour*>, ContourFunc );
        virtual ~ContourConstraint(){};
        virtual double operator()(double *);
    private:
        std::vector<int> _array_ids;
        std::vector<Contour*> _contours;
        ContourFunc _contour_chi2_function ;
};
#endif
