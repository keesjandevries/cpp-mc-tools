#include "VarsFunction.h"

VarsFunction::VarsFunction(std::vector<int> array_ids, GetVarsFunction get_vars_value ): 
    BaseGetValueFunction(), _array_ids(array_ids), _get_vars_value(get_vars_value)
{
    /* intentionally empty */
}


double VarsFunction::operator()(double * vars){
    return _get_vars_value(vars,_array_ids);
}
