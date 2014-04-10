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

void GetValueManager::AddMneuMgM12gM3gX2Lookup(const char * name, std::vector<int> array_ids, 
                std::vector<double *> X2_s,double default_X2,std::vector<double> mneus,
                std::vector< std::vector<double> > mneu_mgs,std::vector< std::vector<double> > mneu_m12gs,
                std::vector< std::vector<double> > mneu_m3gs){
    if (_function_map.find(name)==_function_map.end()){
        MneuMgM12gM3gX2Lookup * new_mneu_mg_m12g_m3g_X2_lookup=new MneuMgM12gM3gX2Lookup(array_ids,
                X2_s,default_X2,mneus,mneu_mgs,mneu_m12gs,mneu_m3gs);
        _function_map[name]=new_mneu_mg_m12g_m3g_X2_lookup;
    }
}

void GetValueManager::AddMneuMgM12gM3gX2Lookup(const char * name, int * array_ids_p, int n_array_ids, 
        double default_X2, double * mneu_mg_m12g_m3g_X2_table, int n_elements){
    //assume that the table mneu_mg_m12g_m3g_X2_table is lexicographicly ordered in the first 4 columns
    //vectors to be populated
    std::vector<double*> X2_s;
    std::vector<double> mneus;
    std::vector< std::vector<double> > mneu_mgs;
    std::vector< std::vector<double> > mneu_m12gs;
    std::vector< std::vector<double> > mneu_m3gs;
    //intermediate steps variables
    int n_rows=n_elements/5;
    std::vector<int> mneu_row_numbers;
    //populate X2 
    double * X2 = new double[n_rows]; 
    for (int i=0;i<n_rows;i++){
        X2[i]=mneu_mg_m12g_m3g_X2_table[i*5+4];
    }
    //populate unique mneus
    double current_mneu=-12345;
    double previous_mneu;
    for (int i=0;i<n_rows;i++){
        previous_mneu=current_mneu;
        current_mneu=mneu_mg_m12g_m3g_X2_table[i*5+0];
        if ((int)current_mneu!=(int)previous_mneu){
            mneus.push_back(current_mneu);
            mneu_row_numbers.push_back(i);
            X2_s.push_back(X2+i);
        }
    }
    mneu_row_numbers.push_back(n_rows);
    //populate unique m3gs
    int nmneu=mneus.size();
    std::vector<double>::iterator m_it;
    //hopefully this brute force method works
    for (int imneu=0; imneu<nmneu; imneu++){
        std::vector<double> mgs;
        std::vector<double> m12gs;
        std::vector<double> m3gs;
        mgs.clear();
        m12gs.clear();
        m3gs.clear();
        for (int i=mneu_row_numbers[imneu]; i<mneu_row_numbers[imneu+1];i++){
            double mg=mneu_mg_m12g_m3g_X2_table[i*5+1]; 
            double m12g=mneu_mg_m12g_m3g_X2_table[i*5+2]; 
            double m3g=mneu_mg_m12g_m3g_X2_table[i*5+3]; 
            //mg
            bool mgfound=false;
            for (m_it=mgs.begin();m_it!=mgs.end();m_it++){
                if ((int)(*m_it)==(int)mg){
                    mgfound=true;
                    break;
                }
            }
            if (!mgfound){
                mgs.push_back(mg);
            }
            //m12g
            bool m12gfound=false;
            for (m_it=m12gs.begin();m_it!=m12gs.end();m_it++){
                if ((int)(*m_it)==(int)m12g){
                    m12gfound=true;
                    break;
                }
            }
            if (!m12gfound){
                m12gs.push_back(m12g);
            }
            //m3g
            bool m3gfound=false;
            for (m_it=m3gs.begin();m_it!=m3gs.end();m_it++){
                if ((int)(*m_it)==(int)m3g){
                    m3gfound=true;
                    break;
                }
            }
            if (!m3gfound){
                m3gs.push_back(m3g);
            }
        }
        mneu_mgs.push_back(mgs);
        mneu_m12gs.push_back(m12gs);
        mneu_m3gs.push_back(m3gs);
    }
    std::vector<int> array_ids(array_ids_p,array_ids_p+n_array_ids);    
    AddMneuMgM12gM3gX2Lookup(name,array_ids,X2_s,default_X2,mneus,mneu_mgs,mneu_m12gs,mneu_m3gs);
    delete X2;
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
