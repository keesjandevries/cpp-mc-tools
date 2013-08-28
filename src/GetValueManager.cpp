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

void GetValueManager::AddChi2Calculator(const char * name){
    if (_chi2_calculator_map.find(name)==_chi2_calculator_map.end()){
        Chi2Calculator * new_chi2_calculator=new Chi2Calculator();
        _chi2_calculator_map[name]=new_chi2_calculator;
    }
}

void GetValueManager::AddConstraintToChi2Calculator(const char * constraint_name, const char * calculator_name){
    std::map<std::string,BaseGetValueFunction*>::iterator it_con;
    std::map<std::string,Chi2Calculator*>::iterator it_cal;
    it_cal=_chi2_calculator_map.find(calculator_name);
    if (it_cal!=_chi2_calculator_map.end()){
        it_con=_function_map.find(constraint_name);
        if (it_con!=_function_map.end()){
            (it_cal->second)->AddConstraint(it_con->second);
        }
        else{
            std::cout << "ERROR: constraint \"" << constraint_name << "\" not found \nThis if very severe" << std::endl;
        }
    }
}

BaseGetValueFunction * GetValueManager::Get(const char * name){
    std::map<std::string,BaseGetValueFunction*>::iterator it;
    std::map<std::string,Chi2Calculator*>::iterator it_cal;
    it=_function_map.find(name);
    it_cal=_chi2_calculator_map.find(name);

    if (it!=_function_map.end()){
        return it->second;
    }
    else if (it_cal!=_chi2_calculator_map.end()){
        return it_cal->second;
    }
    else{
        std::cout << "Function \"" << name << "\" not found" << std::endl;
        return NULL;
    }
}
