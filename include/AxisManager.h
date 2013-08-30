#ifndef INCLUDE_AXISMANAGER_H_
#define INCLUDE_AXISMANAGER_H_
// standard library
#include <iostream>
#include <map>
#include <string>
// my own
#include "Axis.h"

class AxisManager {
    public:
        static AxisManager * GetInstance();
        ~AxisManager();
    private:
        //private so it cannot be called
        AxisManager(){};//constructor
        AxisManager(AxisManager const &); // copy
        AxisManager& operator=(AxisManager const &); //assignment
        static AxisManager* _instance; 
        std::map<std::string,Axis*> _axis_map;
};

#endif // INCLUDE_AXESMANAGER_H_
