#ifndef  INC_VARSFUNCTION_H
#define INC_VARSFUNCTION_H
#include <vector>
#include "BaseGetValueFunction.h"

typedef  double (*GetVarsFunction)(double *, std::vector<int>&);

class VarsFunction: public BaseGetValueFunction{
    public:
        //constructors & destructors
        VarsFunction(){};
        VarsFunction(std::vector<int>, GetVarsFunction );
        virtual ~VarsFunction(){};
        //the get value functions
        virtual double operator()(double *);
    private:
        std::vector<int> _array_ids;
        GetVarsFunction _get_vars_value;
};


#endif
