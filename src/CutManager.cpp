#include "CutManager.h"

CutManager * CutManager::_instance=NULL;

CutManager * CutManager::GetInstance(){
    if (!_instance){
        _instance=new CutManager;
    }
    return _instance; 
}

void CutManager::AddCut(const char * name, std::vector<int> array_ids , const char * function_name){
    if (_cut_functions_map.size()==0){
        _cut_functions_map=get_CutFunction_map();
    }
    if (_cut_map.find(name)==_cut_map.end()){
        std::map<std::string,CutFunction>::iterator it=_cut_functions_map.find(function_name);
        if (it!=_cut_functions_map.end()){
            Cut * new_cut=new Cut(array_ids,it->second);
            _cut_map[name]=new_cut;
        }
        else{
            std::cout << "function name: \"" << function_name << "\" not found" << std::endl;
        }
    }
    else{
        std::cout << "Function \"" << name << "\" already defined" << std::endl;  
    }
}
