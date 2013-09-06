#ifndef INCLUDE_CONTOURMANAGER_H
#define INCLUDE_CONTOURMANAGER_H
// standard library
#include <iostream>
#include <map>
#include <string>
// my own
#include "Contour.h"

class ContourManager {
    public:
        static ContourManager * GetInstance();
        ~ContourManager();
    private:
        //private so it cannot be called
        ContourManager(){};//constructor
        ContourManager(ContourManager const &); // copy
        ContourManager& operator=(ContourManager const &); //assignment
        static ContourManager* _instance; 
};

#endif // INCLUDE_CONTOURMANAGER_H
