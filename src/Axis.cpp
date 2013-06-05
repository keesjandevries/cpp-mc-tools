#include "Axis.h"

/// If you want to overload constructors, then you need to do it this way 
///(http://stackoverflow.com/questions/7330296/constructor-overloading-in-c)
void Axis::init(std::string name,  BinningInputs bin_inp , GetValueFunction get_value ,std::vector<int> array_ids){
    //////////////////////
    //initialise bin edges
    //////////////////////
    double low=bin_inp.low , high=bin_inp.high ;
    int nbins=bin_inp.nbins;
    //Check whether binning type is linear or log, warn otherwise
    if ((bin_inp.binning_type!="linear")&&(bin_inp.binning_type!="log")){
        std::cout << "ERROR in initialising Axis: binning_type not defined" << std::endl;
    }
    //Log binning is handled here
    if (bin_inp.binning_type=="log"){
        low=log10(low); high=log10(high);
    }
    //Fill bin edges
    double step_size=(high-low)/double(nbins);
    for (int i=0;i<(nbins+1);i++){
        double edge=low+i*step_size;
        if (bin_inp.binning_type=="log") edge=pow(10.,edge);
        _bin_edges.push_back(edge);
    }
    //array ids tell the get_value function where to look in the array
    _array_ids=array_ids;
    //when no function is given, the default get_value is used
    _get_value=get_value;
    //set name of axis
    _name=name;
}

Axis::Axis(std::string name, BinningInputs bin_inp , GetValueFunction get_value, std::vector<int> array_ids){
    init( name, bin_inp ,get_value, array_ids);
}

Axis::Axis(std::string name, BinningInputs bin_inp ,std::vector<int> array_ids){
    //call constructor with default_get_value, and the temporary array_ids
    init(name, bin_inp, default_get_value, array_ids);
    //set name of axis
    _name=name;
}

Axis::Axis(std::string name, BinningInputs bin_inp ,int array_id){
    //make temporary array_ids
    std::vector<int> tmp_array_ids;
    tmp_array_ids.push_back(array_id);
    //call constructor with default_get_value, and the temporary array_ids
    init(name, bin_inp, default_get_value, tmp_array_ids);
    //set name of axis
    _name=name;
}

Axis::Axis(std::string name,int array_id){
    //array ids tell the get_value function where to look in the array
    _array_ids.push_back(array_id);
    //when no function is given, the default get_value is used
    _get_value=default_get_value;
    //set name of axis
    _name=name;
}

//FIXME: this is a coding style that should be adopted everywhere
//only non-trivial actions should be in the body of the function
Axis::Axis(std::string name, GaussConstraint * gauss_constraint): 
    _name(name),    
    _gauss_constraint(gauss_constraint), 
    _get_value(NULL) {
    // intentionally empty
}

Axis::Axis(std::string name,GetValueFunction get_value, std::vector<int> array_ids){
    //array ids tell the get_value function where to look in the array
    _array_ids=array_ids;
    //when no function is given, the default get_value is used
    _get_value=get_value;
    //set name of axis
    _name=name;
}

double Axis::get_value(double * VARS){
    //FIXME: this is ugly and result oriented USE ENUM
    if (_get_value==NULL){
        return _gauss_constraint->GetChi2(VARS);
    }
    return _get_value(VARS,_array_ids);
}

void Axis::print_array_indices(){
    std::cout << "Array indices of Axis \""<< _name << "\" are: [";
    for (std::vector<int>::iterator it=_array_ids.begin(); it!=_array_ids.end(); ++it){
        std::cout << *it << "," ;
    }
    std::cout << "]" << std::endl;
}

void Axis::print_bin_edges(){
    std::cout << "Bin Edges are: [";
    for (std::vector<double>::iterator it=_bin_edges.begin(); it!=_bin_edges.end(); ++it){
        std::cout << *it << "," ;
    }
    std::cout << "]" << std::endl;
}

double default_get_value(double * VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]];
}

