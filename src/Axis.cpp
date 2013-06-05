#include "Axis.h"


void Axis::init_binning(BinningInputs bin_inp ){
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
}


Axis::Axis(std::string name):
_name(name)
{
    //intentionally empty
}

Axis::Axis(std::string name,BaseGetValueFunction * func):
_name(name), _get_value(func)
{
    //intentionally empty
}

Axis::Axis(std::string name,BaseGetValueFunction * func, BinningInputs binning ):
_name(name), _get_value(func)
{
    init_binning(binning);
}


double Axis::get_value(double * VARS){
    return (*_get_value)(VARS);
}

void Axis::print_bin_edges(){
    std::cout << "Bin Edges are: [";
    for (std::vector<double>::iterator it=_bin_edges.begin(); it!=_bin_edges.end(); ++it){
        std::cout << *it << "," ;
    }
    std::cout << "]" << std::endl;
}

