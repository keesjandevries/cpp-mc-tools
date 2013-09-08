#include <iostream>
#include "GetValueFunctions.h"

int main(){
    std::map<std::string,GetValueFunction> function_map=get_GetValueFunction_map();
    double VARS[4]={0.1,1.2,2.3,3.4};
    std::vector<int> array_ids;
    array_ids.push_back(1);
    std::cout << "WE GET" << function_map["bsmm_ratio"](VARS,array_ids) <<  std::endl;
    std::cout << "calculating the same thing? " << 1.2/3.46e-9 << std::endl;
    return 0;
}
