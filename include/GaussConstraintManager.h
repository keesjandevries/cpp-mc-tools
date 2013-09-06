#ifndef INCLUDE_GAUSSCONSTRAINTMANAGER_H
#define INCLUDE_GAUSSCONSTRAINTMANAGER_H
// standard library
#include <iostream>
#include <map>
#include <string>
// my own
#include "GaussConstraint.h"

class GaussConstraintManager {
    public:
        static GaussConstraintManager * GetInstance();
        ~GaussConstraintManager();
    private:
        //private so it cannot be called
        GaussConstraintManager(){};//constructor
        GaussConstraintManager(GaussConstraintManager const &); // copy
        GaussConstraintManager& operator=(GaussConstraintManager const &); //assignment
        static GaussConstraintManager* _instance; 
};

#endif // INCLUDE_GAUSSCONSTRAINTMANAGER_H
