#include "SpaceManager.h"

SpaceManager * SpaceManager::_instance=NULL;

SpaceManager * SpaceManager::GetInstance(){
    if (!_instance){
        _instance=new SpaceManager;
    }
    return _instance; 
}

SpaceManager::~SpaceManager(){
    std::vector<Space*>::iterator it;
    for (it=_space_vector.begin(); it!=_space_vector.begin(); it++){
        delete (*it);    
    }
    _space_vector.clear();
}

void SpaceManager::AddSpace(std::vector<std::string> axes_names , std::vector<std::string> zaxes_names, std::string reference_function_name){
    std::vector<Axis*> axes;
    std::vector<Axis*> zaxes;
    std::vector<std::string>::iterator axis_names_it;
    AxisManager * axis_manager=AxisManager::GetInstance();
    GetValueManager * get_value_manager=GetValueManager::GetInstance();
    //fill axes
    for(axis_names_it=axes_names.begin();axis_names_it!=axes_names.end();axis_names_it++){
        Axis * axis=axis_manager->Get((*axis_names_it).c_str());
        if (axis!=NULL){
            axes.push_back(axis);
        }
        else{
            std::cout << "ERROR: Axis \""<< *axis_names_it <<"\" is not defined. Skipping space" << std::endl;
            return;
        }
    }
    //fill z-axes
    for(axis_names_it=zaxes_names.begin();axis_names_it!=zaxes_names.end();axis_names_it++){
        Axis * zaxis=axis_manager->Get((*axis_names_it).c_str());
        if (zaxis!=NULL){
            axes.push_back(zaxis);
        }
        else{
            std::cout << "ERROR: Z-Axis \""<< *axis_names_it <<"\" is not defined. Skipping space" << std::endl;
            return;
        }
    }
    //get reference function
    BaseGetValueFunction * reference_function=get_value_manager->Get(reference_function_name.c_str());
    if (reference_function!=NULL){
        Space * space=new Space(axes,zaxes,reference_function);
        _space_vector.push_back(space);
    }
    else{
        std::cout << "ERROR: reference function \""<< reference_function_name <<"\" is not defined. Skipping space" << std::endl;
        return;
    }

}
