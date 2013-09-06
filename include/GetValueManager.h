#ifndef INC_GETVALUEMANAGER_H
#define INC_GETVALUEMANAGER_H
// standard library
#include <iostream>
#include <map>
#include <string>
// my own
#include "BaseGetValueFunction.h"
#include "VarsLookup.h"
#include "VarsFunction.h"
#include "GetVarsFunctions.h"
#include "GaussConstraint.h"
#include "GaussFunctions.h"
#include "Chi2Calculator.h"

class GetValueManager {
    public:
        static GetValueManager * GetInstance();
        ~GetValueManager();
        void AddVarsLookup(const char *, int);
        void AddVarsFunction(const char *, std::vector<int>, const char *);
        void AddVarsFunction(const char *, int*, int, const char *);
        void AddGaussConstraint(const char *, std::vector<int>, double, std::vector<double>, const char *);
        // FIXME: perhaps separating out the Chi2Calculator
        void AddChi2Calculator(const char *);
        void AddConstraintToChi2Calculator(const char *,const char *);
        BaseGetValueFunction * Get(const char *);
    private:
        //private so it cannot be called
        GetValueManager(){};//constructor
        GetValueManager(GetValueManager const &); // copy
        GetValueManager& operator=(GetValueManager const &); //assignment
        static GetValueManager* _instance; 
        std::map<std::string,BaseGetValueFunction*> _function_map;
        std::map<std::string,Chi2Calculator*> _chi2_calculator_map;
        std::map<std::string,GetVarsFunction> _get_vars_function_map;
        std::map<std::string,GaussFunc> _gauss_func_map;
};

#endif
