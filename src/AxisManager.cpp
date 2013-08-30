#include "AxisManager.h"

AxisManager * AxisManager::_instance=NULL;

AxisManager * AxisManager::GetInstance(){
    if (!_instance){
        _instance=new AxisManager;
    }
    return _instance; 
}

AxisManager::~AxisManager(){
    // emtpy for now
    std::map<std::string,Axis*>::iterator it;
    for (it=_axis_map.begin(); it!=_axis_map.begin(); it++){
        delete it->second;    
    }
    _axis_map.clear();
}

