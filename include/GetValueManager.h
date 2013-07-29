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
class GetValueManager {
    public:
        static GetValueManager * GetInstance();
        ~GetValueManager();
        void AddVarsLookup(const char *, int);
        void AddVarsFunction(const char *, std::vector<int>, const char *);
        void AddVarsFunction(const char *, int*, int, const char *);
        BaseGetValueFunction * Get(const char *);
    private:
        //private so it cannot be called
        GetValueManager(){};//constructor
        GetValueManager(GetValueManager const &); // copy
        GetValueManager& operator=(GetValueManager const &); //assignment
        static GetValueManager* _instance; 
        std::map<std::string,BaseGetValueFunction*> _function_map;
        std::map<std::string,GetVarsFunction> _get_vars_function_map;
};

#endif
