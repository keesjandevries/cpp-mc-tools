#ifndef  INC_AXIS_H
#define INC_AXIS_H
#include<iostream>
#include<string>
#include<vector>
#include<cmath>

#include "BaseGetValueFunction.h"
#include "GaussConstraint.h"

/// for linear and log binning, all that defines the axes are the lower and higher value and the number of bins
struct BinningInputs{std::string binning_type; double low , high; int nbins;};
///Make function pointer into a type def 
typedef  double (*GetValueFunction)(double *, std::vector<int>&);

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
        Axis(std::string name, int /*array id*/); 
        Axis(std::string name, BaseGetValueFunction *); 
        Axis(std::string name, GetValueFunction,std::vector<int> /*array ids*/ );
        ///with binning for ranges of projections
        Axis(std::string name, BinningInputs, int /*array id*/);
        Axis(std::string name, BaseGetValueFunction *, BinningInputs); 
        Axis(std::string name, BinningInputs, std::vector<int> /*array ids*/);
        Axis(std::string name, BinningInputs, GetValueFunction ,std::vector<int> /*array ids*/ );
        ///constraint
        Axis(std::string name, GaussConstraint*);
        ~Axis(){};
        //member functions
        std::vector<double> get_bin_edges(){return _bin_edges;};
        std::string get_name(){return _name;};
        /// most important function
        double get_value(double* /*VARS*/);
        double new_get_value(double* /*VARS*/);
        void print_bin_edges();
        void print_array_indices();
    private:
        bool _is_new;
        void init(std::string name,  BinningInputs, GetValueFunction ,std::vector<int>/*aids*/ );
        void init_binning(BinningInputs);
        std::vector<double> _bin_edges;
        std::vector<int>    _array_ids;
        std::string         _name;
        GaussConstraint *   _gauss_constraint;
        GetValueFunction    _get_value;
        BaseGetValueFunction * _new_get_value;
};

/// Default function for getting value, when Constructor is called without function name,
double default_get_value(double * VARS, std::vector<int>& array_ids);
#endif
