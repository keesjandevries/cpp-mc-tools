#ifndef  INC_GETVALUEFUNCTION_H
#define INC_GETVALUEFUNCTION_H
/// The BaseGetValueFunction class is an abstract class that lies at the heart of these analysis tools. 
/// The implementations of BaseGetValueFunction return a double as a function of double array.
class BaseGetValueFunction{
    public:
    BaseGetValueFunction();
    virtual ~BaseGetValueFunction();
    virtual double operator()(double * /*VARS*/);
    double get_value(double *);
};

#endif
