#include "GetValueManager.h"

GetValueManager * GetValueManager::_instance=NULL;

GetValueManager * GetValueManager::GetInstance(){
    if (!_instance){
        _instance=new GetValueManager;
    }
    return _instance; 
}

GetValueManager::~GetValueManager(){
    // emtpy for now
    std::map<std::string,BaseGetValueFunction*>::iterator it;
    for (it=_function_map.begin(); it!=_function_map.begin(); it++){
        delete it->second;    
    }
}

void GetValueManager::AddVarsLookup(const char * name, int array_id){
    if (_function_map.find(name)==_function_map.end()){
        VarsLookup * new_vars_lookup=new VarsLookup(array_id);
        _function_map[name]=new_vars_lookup;
    }
}

void GetValueManager::AddVarsFunction(const char * name, std::vector<int> array_ids , const char * function_name){
    if (_get_vars_function_map.size()==0){
        _get_vars_function_map=get_GetVarsFunction_map();
    }
    if (_function_map.find(name)==_function_map.end()){
        std::map<std::string,GetVarsFunction>::iterator it=_get_vars_function_map.find(function_name);
        if (it!=_get_vars_function_map.end()){
            VarsFunction * new_vars_lookup=new VarsFunction(array_ids,it->second);
            _function_map[name]=new_vars_lookup;
        }
        else{
            std::cout << "function name: \"" << function_name << "\" not found" << std::endl;
        }
    }
    else{
        std::cout << "Function \"" << name << "\" already defined" << std::endl;  
    }
}

void GetValueManager::AddVarsFunction(const char * name, int* array_ids_p, int n_array_ids , const char * function_name){
    std::vector<int> array_ids(array_ids_p,array_ids_p+n_array_ids);    
    AddVarsFunction(name,array_ids,function_name);
}

BaseGetValueFunction * GetValueManager::Get(const char * name){
    std::map<std::string,BaseGetValueFunction*>::iterator it;
    it=_function_map.find(name); 
    if (it!=_function_map.end()){
        return it->second;
    }
    else{
        std::cout << "Function \"" << name << "\" not found" << std::endl;
        return NULL;
    }
}
