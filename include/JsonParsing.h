#ifndef JSONPARSING_H
#define JSONPARSING_H
#include <map>
#include "Axis.h"
#include "GaussConstraint.h"
#include "BaseGetValueFunction.h"
#include "VarsFunction.h"
#include "VarsLookup.h"
//FIXME: JSONPARSING_H is also used in recalculate/ maybe will crash at some point

#include "jansson.h"

// to facilitate initiation of spaces
struct AxesZaxesNames {
    std::vector<std::string> axes;
    std::vector<std::string> zaxes;
};
/// This function deals with a json file containing something like:
///{
///   "mh2_m0^2_Ratio": {
///      "vars_function": {
///         "observable_ids": {
///            "array_ids": [
///               6, 
///               1
///            ]
///         }, 
///         "name": "var1_over_var2_square"
///      }, 
///      "binning": {
///         "low": -3.0, 
///         "type": "linear", 
///         "high": 3.0, 
///         "nbins": 100
///      }
///   }, 
///
///   "mstop1": {
///      "vars_lookup": {
///         "array_id": 96
///      }, 
///      "binning": {
///         "low": 0.0, 
///         "type": "linear", 
///         "high": 3000.0, 
///         "nbins": 100
///      }
///   }, 
///   "chi2_mh": {
///      "gauss_constraint": "Mh125"
///   }
///}
///And returns a map with pointers to Axis objects
std::map<std::string, Axis*> parse_axes_from_json_file(std::string /*json file*/ ,
        std::map<std::string, GetVarsFunction> /*function map*/ ,
        std::map<std::string, GaussConstraint*> /*constraint map*/);

/// This function deals with a file containing a json array of objects like: of [[axes,zaxes] , axes, ...  ], e.g. 
///[{  'axes':['m0','m12'],'zaxes':['mh'] },
/// {  'axes':'mh' } ]
/// Returned is a vector of AxesZaxesNames
std::vector<AxesZaxesNames> parse_axes_names_list_from_json_file(std::string );
/// This function deals with file containing json object like
///
///    'Mh125':{
///        'observable_ids':{
///            'array_ids': 28,
///            },
///        'gaussian':{
///            'mu':125.,
///            'sigmas':[1.0,2.5],
///            'function':'gaussian',
///        },
///    }
std::map<std::string, GaussConstraint*> parse_gauss_constraint_from_json_file(std::string filename,
        std::map<std::string, GaussFunc> gauss_func_map);

/// Usefull parsing functions other functions
std::vector<std::string> json_to_string_vector(json_t * object_t);
std::vector<double> json_to_double_vector(json_t * object_t);
std::vector<int> json_to_int_vector(json_t * object_t);

#endif
