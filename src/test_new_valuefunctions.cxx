#include <iostream>
#include "VarsFunction.h"


double my_get_value(double * VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]];
}

int main(){
    std::vector<int> array_ids;
    array_ids.push_back(0);

    VarsFunction my_vars_function(array_ids,my_get_value);
    double vars[]={1.};

    std::cout << "return:" << my_vars_function(vars) << std::endl;;
    return 0;
}    
