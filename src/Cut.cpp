#include "Cut.h"

Cut::Cut(std::vector<int> array_ids, CutFunction cut_function):
_array_ids(array_ids), _cut_function(cut_function)
{
    //intentionally empty    
}

bool Cut::operator()(double * vars){
    return _cut_function(vars, _array_ids);
}
