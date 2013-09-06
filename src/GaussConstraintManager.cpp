#include "GaussConstraintManager.h"

GaussConstraintManager * GaussConstraintManager::_instance=NULL;

GaussConstraintManager * GaussConstraintManager::GetInstance(){
    if (!_instance){
        _instance=new GaussConstraintManager;
    }
    return _instance; 
}
