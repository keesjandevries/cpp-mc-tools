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
