#ifndef  INC_GETVALUEFUNCTION_H
#define INC_GETVALUEFUNCTION_H

class BaseGetValueFunction{
    public:
    BaseGetValueFunction();
    virtual ~BaseGetValueFunction();
    virtual double operator()(double * /*VARS*/);
};

#endif
