#include "ContourManager.h"

ContourManager * ContourManager::_instance=NULL;

ContourManager * ContourManager::GetInstance(){
    if (!_instance){
        _instance=new ContourManager;
    }
    return _instance; 
}

