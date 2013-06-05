#ifndef  INC_GETVALUEFUNCTION_H
#define INC_GETVALUEFUNCTION_H

class GetValueFunction{
    public:
    GetValueFunction();
    virtual ~GetValueFunction();
    virtual double operator()(double * /*VARS*/);
};

#endif
