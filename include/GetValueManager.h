#ifndef INC_GETVALUEMANAGER_H
#define INC_GETVALUEMANAGER_H
// standard library
#include <map>
#include <string>
// my own
#include "BaseGetValueFunction.h"
class GetValueManager {
    public:
        GetValueManager(){};
        virtual ~GetValueManager(){};
        void Add(const char *, BaseGetValueFunction*){};
    private:
        std::map<std::string,BaseGetValueFunction*> _function_map;
};

#endif
