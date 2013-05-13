#ifndef JSONPARSING_H
#define JSONPARSING_H
#include <map>
#include "Axis.h"
//FIXME: JSONPARSING_H is also used in recalculate/ maybe will crash at some point

#include "jansson.h"

// to facilitate initiation of spaces
struct AxesZaxesNames {
    std::vector<std::string> axes;
    std::vector<std::string> zaxes;
};
/// This function deals with a json file containing something like:
///{
///   "m12": {
///      "observable_ids": {
///         "array_id": 2
///      }, 
///      "binning": {
///         "high": 4000.0, 
///         "nbins": 100, 
///         "type": "linear", 
///         "low": 0.0
///      }
///   }, 
///   "m0": {
///      "observable_ids": {
///         "array_id": 1
///      }, 
///      "binning": {
///         "high": 4000.0, 
///         "nbins": 100, 
///         "type": "linear", 
///         "low": 0.0
///      }
///   }
///}
///And returns a map with pointers to Axis objects
std::map<std::string, Axis*> parse_axes_from_json_file(std::string /*json file*/ ,std::map<std::string, GetValueFunction> /*function map*/ );
/// This function deals with a file containing a json array of objects like: of [[axes,zaxes] , axes, ...  ], e.g. 
///[{  'axes':['m0','m12'],'zaxes':['mh'] },
/// {  'axes':'mh' } ]
/// Returned is a vector of AxesZaxesNames
std::vector<AxesZaxesNames> parse_axes_names_list_from_json_file(std::string );
/// This function turns a json object like ["m0","m12"] or "mh" into std::vector<std::string> 
std::vector<std::string> json_to_string_vector(json_t * object_t);

#endif
