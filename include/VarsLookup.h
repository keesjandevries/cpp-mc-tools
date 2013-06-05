#ifndef  INC_VARSLOOKUP_H
#define INC_VARSLOOKUP_H
#include "BaseGetValueFunction.h"

///This is the simplest version of the BaseGetValueFunction
class VarsLookup: public BaseGetValueFunction{
    public:
        //constructors & destructors
        VarsLookup(){};
        VarsLookup(int);
        virtual ~VarsLookup(){};
        //the get value functions
        virtual double operator()(double *);
    private:
        int _array_id;
};
#endif
