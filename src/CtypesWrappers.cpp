#include "CtypesWrappers.h"

GetValueManager * my_manager=GetValueManager::GetInstance();

void my_test(){
    double a[10];
    a[5]=1;
    a[0]=0;
    a[1]=1;
    std::cout << "Hope this gives 1: " << (*(my_manager->Get("name1"))).get_value(a) << std::endl;
    std::cout << "Hope this gives 0.5: " << (*(my_manager->Get("name2"))).get_value(a) << std::endl;
    std::cout << "Hope this gives 1.5: " << (*(my_manager->Get("chi2"))).get_value(a) << std::endl;
}
    
extern "C"{
void add_vars_lookup(const char * name, int array_id){
    my_manager->AddVarsLookup(name,array_id);
}
void add_vars_function(const char * name, int * array_ids, int n_array_ids,const char *function_name){
    my_manager->AddVarsFunction(name,array_ids,n_array_ids,function_name);
}
void add_chi2_calculator(const char * name){
    my_manager->AddChi2Calculator(name);
}
void add_constraint_to_chi2_calculator(const char * constraint_name, const char* calculator_name){
    my_manager->AddConstraintToChi2Calculator(constraint_name,calculator_name);
}
void test(){
    my_test();
}
}

