#include "BaseGetValueFunction.h"

BaseGetValueFunction::BaseGetValueFunction(){
    //empty
}
BaseGetValueFunction::~BaseGetValueFunction(){
    //emtpy
}

double BaseGetValueFunction::operator()(double * /*VARS*/){
    //emtpy
}

double BaseGetValueFunction::get_value(double * vars){
    return (*this)(vars);
}
