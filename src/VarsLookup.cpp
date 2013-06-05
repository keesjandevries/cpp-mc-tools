#include "VarsLookup.h"

VarsLookup::VarsLookup(int array_id): 
    _array_id(array_id)
{
    /* intentionally empty */
}

double VarsLookup::operator()(double * vars){
    return vars[_array_id];
}
