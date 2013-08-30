#ifndef INCLUDE_SPACEMANAGER_H_
#define INCLUDE_SPACEMANAGER_H_
// standard library
#include <iostream>
#include <map>
#include <string>
// my own

#include "Space.h"
#include "AxisManager.h"
class SpaceManager {
    public:
        static SpaceManager * GetInstance();
        ~SpaceManager();
        void AddSpace(std::vector<std::string>, std::vector<std::string>, std::string);
        std::vector<Space*> Get();
    private:
        //private so it cannot be called
        SpaceManager(){};//constructor
        SpaceManager(SpaceManager const &); // copy
        SpaceManager& operator=(SpaceManager const &); //assignment
        static SpaceManager* _instance; 
        std::vector<Space*> _space_vector;
};

#endif // INCLUDE_SPACEMANAGER_H_
