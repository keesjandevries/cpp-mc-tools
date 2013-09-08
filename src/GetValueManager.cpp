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


void GetValueManager::AddGaussConstraint(const char * name, int* array_ids_p, int n_array_ids, double mu, 
        double* sigmas_p ,int n_sigmas, const char * function_name){
    std::vector<int> array_ids(array_ids_p,array_ids_p+n_array_ids);    
    std::vector<double> sigmas(sigmas_p,sigmas_p+n_sigmas);
    AddGaussConstraint(name,array_ids,mu,sigmas,function_name);
}

//FIXME: since this is almost a repetition of the above, maybe render more abstract
void GetValueManager::AddGaussConstraint(const char * name, std::vector<int> array_ids, 
        double mu, std::vector<double> sigmas, const char * function_name){
    if (_gauss_func_map.size()==0){
        _gauss_func_map=get_GaussFunc_map();
    }
    if (_function_map.find(name)==_function_map.end()){
        std::map<std::string,GaussFunc>::iterator it=_gauss_func_map.find(function_name);
        if (it!=_gauss_func_map.end()){
            GaussConstraint * new_gauss_constraint=new GaussConstraint(array_ids,mu,sigmas,it->second);
            _function_map[name]=new_gauss_constraint;
        }
        else{
            std::cout << "function name: \"" << function_name << "\" not found" << std::endl;
        }
    }
    else{
        std::cout << "Function \"" << name << "\" already defined" << std::endl;  
    }
}
void GetValueManager::AddContourConstraint(const char *name ,int* array_ids_p, int n_array_ids,
        const char ** contour_names_p, int n_contour_names ,const char *function_name){
    std::vector<int> array_ids(array_ids_p,array_ids_p+n_array_ids);    
    std::vector<std::string> contour_names(contour_names_p,contour_names_p+n_contour_names);    
    AddContourConstraint(name,array_ids,contour_names,function_name);
}

void GetValueManager::AddContourConstraint(const char * name, std::vector<int> array_ids,
        std::vector<std::string> contour_names, const char * function_name){
    if (_contour_chi2_function_map.size()==0){
        _contour_chi2_function_map=get_ContourFunc_map();
    }
    if (_function_map.find(name)==_function_map.end()){
        std::map<std::string,ContourFunc>::iterator contour_func_it=_contour_chi2_function_map.find(function_name);
        if (contour_func_it!=_contour_chi2_function_map.end()){
            std::vector<Contour*> contours;
            std::vector<std::string>::iterator contour_names_it;
            ContourManager * contour_manager=ContourManager::GetInstance();
            for (contour_names_it=contour_names.begin(); contour_names_it!=contour_names.end();contour_names_it++){
                Contour * contour=contour_manager->Get((*contour_names_it).c_str());    
                if (contour!=NULL){
                    contours.push_back(contour);
                }
                else{
                    std::cout << "Contour \"" << *contour_names_it << "\" could not be found" << std::endl;
                    std::cout << "Skipping contour" << std::endl;
                    return;
                }
                ContourConstraint * new_contour_constraint=new ContourConstraint(array_ids,contours,contour_func_it->second);
                _function_map[name]=new_contour_constraint;
            }
        }
        else{
            std::cout << "function name: \"" << function_name << "\" not found" << std::endl;
        }
    }
    else{
        std::cout << "Function \"" << name << "\" already defined" << std::endl;  
    }
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
    else {
        std::cout << "ERROR: could not find calculator \'" <<  calculator_name << "\'" << std::endl;
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
