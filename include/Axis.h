#ifndef  INCLUDE_AXIS_H_
#define INCLUDE_AXIS_H_
#include<iostream>
#include<string>
#include<vector>
#include<cmath>

#include "BaseGetValueFunction.h"
#include "GaussConstraint.h"

/// for linear and log binning, all that defines the axes are the lower and higher value and the number of bins
struct BinningInputs{std::string binning_type; double low , high; int nbins;};

/// FIXME: this commenting needs updating
/// Axis class has get_value(double * VARS) as key function
/// get_value(double * VARS) uses the function pointer _get_value of the type GetValueFunction. 
/// a GetValueFunction acceses elements of VARS according to the std::vector<int> pointer to _array_ids  
/// the default GetValueFunction is default_get_value(...)
///
/// Binning can also be specified. bin edges are used to initialise TH1D * or TH2D * in the Plot class
/// binning types can be "linear" of "log". The other parameters needed are low, high and nbins
class Axis{
    public:
        ///constructors and destructors
        ///no binning e.g. for Z-axis
        Axis(std::string name); 
        Axis(std::string name, BaseGetValueFunction *); 
        ///with binning for ranges of projections
        Axis(std::string name, BaseGetValueFunction *, BinningInputs); 
        ~Axis(){};
        //member functions
        std::vector<double> get_bin_edges(){return _bin_edges;};
        std::string get_name(){return _name;};
        /// most important function
        double get_value(double* /*VARS*/);
        void print_bin_edges();
    private:
        void init_binning(BinningInputs);
        std::string         _name;
        std::vector<double> _bin_edges;
        BaseGetValueFunction * _get_value;
};

#endif  // INCLUDE_AXIS_H_
