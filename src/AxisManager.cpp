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

void AxisManager::AddAxis(const char * axis_name, const char * value_function_name){
    if (_axis_map.find(axis_name)==_axis_map.end()){
        GetValueManager * get_value_manager=GetValueManager::GetInstance();
        BaseGetValueFunction * get_value_function=get_value_manager->Get(value_function_name);
        if (get_value_function!=NULL){
            _axis_map[axis_name]=new Axis(axis_name,get_value_function);
        }
        else{
            std::cout << "ERROR: function \"" << value_function_name  << "\" not defined in GetValueManager" << std::endl;
        }
    }
}

void AxisManager::AddAxis(const char * axis_name, const char * value_function_name,
        const char * binning_type, double low, double high, int nbins){
    BinningInputs binning_inputs;
    binning_inputs.binning_type=binning_type;
    binning_inputs.low=low;
    binning_inputs.high=high;
    binning_inputs.low=low;
    if (_axis_map.find(axis_name)==_axis_map.end()){
        GetValueManager * get_value_manager=GetValueManager::GetInstance();
        BaseGetValueFunction * get_value_function=get_value_manager->Get(value_function_name);
        if (get_value_function!=NULL){
            _axis_map[axis_name]=new Axis(axis_name,get_value_function,binning_inputs);
        }
        else{
            std::cout << "ERROR: function \"" << value_function_name << "\" not defined in GetValueManager" << std::endl;
        }
    }
}

