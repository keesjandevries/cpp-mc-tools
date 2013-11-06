#ifndef INCLUDE_CUTMANAGER_H
#define INCLUDE_CUTMANAGER_H
// standard library
#include <iostream>
#include <map>
#include <string>
// my own
#include "Cut.h"
#include "CutFunctions.h"

class CutManager {
    public:
        static CutManager * GetInstance();
        ~CutManager();
        void AddCut(const char *,std::vector<int>,const char *);
        void AddCut(const char *,int*,int,const char *);
        Cut * Get(const char *);
    private:
        //private so it cannot be called
        CutManager(){};//constructor
        CutManager(CutManager const &); // copy
        CutManager& operator=(CutManager const &); //assignment
        static CutManager* _instance; 
        std::map<std::string,Cut*> _cut_map;
        std::map<std::string,CutFunction> _cut_functions_map;
};

#endif // INCLUDE_CUTMANAGER_H
