#ifndef INCLUDE_CONTOURMANAGER_H
#define INCLUDE_CONTOURMANAGER_H
// standard library
#include <iostream>
#include <map>
#include <string>
// my own
#include "Contour.h"
#include "DefaultContour.h"
#include "LogXLogYContour.h"
#include "UniversalLimitsContour.h"
#include "RadialContour.h"

class ContourManager {
    public:
        static ContourManager * GetInstance();
        ~ContourManager();
        void AddContour(const char *,std::vector<double_pair>,const char *);
        void AddContour(const char *,double*,double*,int,const char *);
        Contour * Get(const char *);
    private:
        //private so it cannot be called
        ContourManager(){};//constructor
        ContourManager(ContourManager const &); // copy
        ContourManager& operator=(ContourManager const &); //assignment
        static ContourManager* _instance; 
        std::map<std::string,Contour*> _contour_map;
};

#endif // INCLUDE_CONTOURMANAGER_H
