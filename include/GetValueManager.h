#ifndef INC_GETVALUEMANAGER_H
#define INC_GETVALUEMANAGER_H
// standard library
#include <map>
#include <string>
// my own
#include "BaseGetValueFunction.h"
#include "VarsLookup.h"
class GetValueManager {
    public:
        static GetValueManager * GetInstance();
        ~GetValueManager();
        void AddVarsLookup(const char *, int);
    private:
        //private so it cannot be called
        GetValueManager(){};//constructor
        GetValueManager(GetValueManager const &); // copy
        GetValueManager& operator=(GetValueManager const &); //assignment
        static GetValueManager* _instance; 
        std::map<std::string,BaseGetValueFunction*> _function_map;
};

#endif
