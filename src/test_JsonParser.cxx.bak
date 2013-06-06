#include <iostream>
#include "Space.h"
#include "JsonParsing.h"
#include "GetValueFunctions.h"

std::map<std::string,Axis*> get_axes_map(std::string axes_file_name,  std::map<std::string, GetValueFunction> function_map ){
    std::map<std::string, GaussConstraint*> dummy;
    return parse_axes_from_json_file(axes_file_name,function_map, dummy);
}
std::vector< AxesZaxesNames> get_axes_names_list(std::string filename){
    return parse_axes_names_list_from_json_file(filename);
}
/// this function turns something a c++ version of [ {'axes':['m0','m12'], 'zaxes':['bsmm_ratio', ... ]}, ...   ]
/// into a vector of spaces. Here 'm0', 'm12' are keys to Axes in the axes_map
std::vector<Space*> get_spaces(std::map<std::string,Axis*> axes_map, std::vector< AxesZaxesNames>  axes_list ){
    std::vector<Space*> spaces;
    for (std::vector<AxesZaxesNames>::iterator axes_names_it=axes_list.begin(); axes_names_it!=axes_list.end() ; axes_names_it++){
        std::vector<Axis*> axes, zaxes;
        //get axes
        std::cout << "Initialising ases: AXES" << std::endl;
        for (std::vector<std::string>::iterator axis_name_it=(*axes_names_it).axes.begin();
                axis_name_it!=(*axes_names_it).axes.end();axis_name_it++){
            axes.push_back(axes_map[*axis_name_it]);
            std::cout << *axis_name_it << std::endl;
        }
        //get zaxes
        std::cout << "Initialising ases: ZAXES" << std::endl;
        for (std::vector<std::string>::iterator axis_name_it=(*axes_names_it).zaxes.begin();
                axis_name_it!=(*axes_names_it).zaxes.end();axis_name_it++){
            zaxes.push_back(axes_map[*axis_name_it]);
            std::cout << *axis_name_it << std::endl;
        }
        //make a space and push back
        Space * space = new Space(axes,zaxes) ;
        spaces.push_back(space);
    }
    return spaces;
}

int main(){
    std::vector< AxesZaxesNames> axes_list=get_axes_names_list("user/example_spaces.json");
    // get value functions map
    std::map<std::string,GetValueFunction> function_map=get_GetValueFunction_map();
    // get axes map
    std::map<std::string,Axis*> axes_map=get_axes_map("user/example_axes.json",function_map);
    // get spaces from axes specified in axes_list
    std::vector<Space*> spaces= get_spaces(axes_map,axes_list);
    Axis * bsmm_axis=axes_map["BsmmRatio"];
    double bla[]={1.,1.,1., 1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,10.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.};
    std::cout << "I get flippin: " << bsmm_axis->get_value(bla) << " compare with  "<< 1/3.46e-9<< std::endl;
    spaces[2]->print_axes_names();
//    if (it!=axes_map.end()) it->second->print_bin_edges();
    return 0;
}
