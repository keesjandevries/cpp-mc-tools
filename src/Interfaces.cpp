#include "Interfaces.h"

GetValueManager * my_manager=GetValueManager::GetInstance();

void my_test(const char * name){
    double a[10];
    a[5]=1;
    std::cout << "Hope this gives 1: " << (*(my_manager->Get(name))).get_value(a) << std::endl;

}
    
extern "C"{
void add_vars_lookup(const char * name, int array_id){
    my_manager->AddVarsLookup(name,array_id);
}
void test(const char * name){
    my_test(name);
}
}

