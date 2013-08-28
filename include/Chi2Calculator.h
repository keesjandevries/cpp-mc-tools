#ifndef  INCLUDE_CHI2CALCULATOR_H_
#define INCLUDE_CHI2CALCULATOR_H_
#include <vector>
#include "BaseGetValueFunction.h"

class Chi2Calculator: public BaseGetValueFunction{
    public:
        Chi2Calculator(){};
        ~Chi2Calculator(){};
        virtual double operator()(double *);
        void AddConstraint(BaseGetValueFunction*);
    private:
        std::vector<BaseGetValueFunction*> _constraints;
};

#endif  // INCLUDE_CHI2CALCULATOR_H_
