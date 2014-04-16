#ifndef INC_GETVALUEMANAGER_H
#define INC_GETVALUEMANAGER_H
// standard library
#include <iostream>
#include <map>
#include <string>
// my own
#include "BaseGetValueFunction.h"
// implementations of "BaseGetValueFunction"s
#include "VarsLookup.h"
#include "VarsFunction.h"
#include "GaussConstraint.h"
#include "ContourConstraint.h"
#include "MneuMgM12gM3gX2Lookup.h"
#include "Chi2Calculator.h"
// modules that contain std::map<string, FUNCTIONPTR >
#include "GetVarsFunctions.h"
#include "GaussFunctions.h"
#include "ContourChi2Functions.h"
// contour manager
#include "ContourManager.h"

class GetValueManager {
    public:
        static GetValueManager * GetInstance();
        ~GetValueManager();
        void AddVarsLookup(const char *, int);
        void AddVarsFunction(const char *, std::vector<int>, const char *);
        void AddVarsFunction(const char *, int*, int, const char *);
        void AddGaussConstraint(const char *, std::vector<int>, double, std::vector<double>, const char *);
        void AddGaussConstraint(const char *, int*, int, double, double*,int, const char *);
        void AddContourConstraint(const char *,std::vector<int>,std::vector<std::string>,const char *);
        void AddContourConstraint(const char *,int*, int,const char **, int ,const char *);
        void AddMneuMgM12gM3gX2Lookup(const char *, std::vector<int> /*array_ids*/, 
                std::vector<double *> /*X2_s*/,double /*default_X2*/,std::vector<double> /*mneus*/,
                std::vector< std::vector<double> > /*grid_mgs*/,std::vector< std::vector<double> > /*grid_m12gs*/,
                std::vector< std::vector<double> > /*grid_m3gs*/);
        void AddMneuMgM12gM3gX2Lookup(const char * name, int * array_ids_p, int n_array_ids, 
            double default_X2, double * mneu_mg_m12g_m3g_X2_table, int n_rows);
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
        std::map<std::string,ContourFunc> _contour_chi2_function_map;
};

#endif
