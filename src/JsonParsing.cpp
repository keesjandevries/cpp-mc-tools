#include "JsonParsing.h"

//FIXME: may want to cast this in template
std::vector<int> json_to_int_vector(json_t * object_t){
    std::vector<int> int_vector;
    // if object is array, then loop over it and fill vector
    if (json_is_array(object_t)){
        size_t  size_object_t=json_array_size(object_t);
        for (size_t i=0;i<size_object_t;i++){
            int integer_c;
            json_unpack(json_array_get(object_t,i),"i", &integer_c );
            int_vector.push_back(integer_c);
        }
    }
    // if object if string, then append it to the string vector
    else if json_is_integer(object_t){
        int integer_c;
        json_unpack(object_t,"i",&integer_c);
        int_vector.push_back(integer_c);
    }
    else {
        std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
        std::cout << "      json object was neither an array, nor an integer"<< std::endl;
    }
    return int_vector;
}

std::vector<std::string> json_to_string_vector(json_t * object_t){
    std::vector<std::string> string_vector;
    // if object is array, then loop over it and fill vector
    if (json_is_array(object_t)){
        size_t  size_object_t=json_array_size(object_t);
        for (size_t i=0;i<size_object_t;i++){
            const char * string_c;
            json_unpack(json_array_get(object_t,i),"s", &string_c );
            string_vector.push_back(string_c);
        }
    }
    // if object if string, then append it to the string vector
    else if json_is_string(object_t){
        const char * string_c;
        json_unpack(object_t,"s",&string_c);
        string_vector.push_back(string_c);
    }
    else {
        std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
        std::cout << "      json object was neither an array, nor a string"<< std::endl;
    }
    return string_vector;
}

BinningInputs json_to_binning_inputs(json_t * object_t){
    BinningInputs binning_input;
    if json_is_object(object_t){
        json_unpack(json_object_get(object_t,"low"),"f",   &(binning_input.low) );
        json_unpack(json_object_get(object_t,"high"),"f",  &(binning_input.high) );
        json_unpack(json_object_get(object_t,"nbins"),"i", &(binning_input.nbins) );
        const char * tmp_binning_type;
        json_unpack(json_object_get(object_t,"type"),"s",  &(tmp_binning_type) );
        binning_input.binning_type=tmp_binning_type;
    }
    else {
        std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
        std::cout << "       not a json object"   << std::endl;
    }
    return binning_input;
}

std::vector<AxesZaxesNames> parse_axes_names_list_from_json_file(std::string filename){
    std::vector<AxesZaxesNames> axes_names; 
    json_error_t error;
    json_t * list_t=json_load_file(filename.c_str(),0, &error);
    size_t list_size_t = json_array_size(list_t); 
    for (size_t index_t= 0; index_t<list_size_t;index_t++){
        AxesZaxesNames axes_zaxes_names;
        json_t * axes_zaxes_t = json_array_get(list_t,index_t);        
        if json_is_object(axes_zaxes_t){
            json_t * axes_t = json_object_get(axes_zaxes_t,"axes");
            json_t * zaxes_t= json_object_get(axes_zaxes_t,"zaxes");
            //check whether axes_t is actually filled
            if (axes_t){ 
                //set axes
                axes_zaxes_names.axes=json_to_string_vector(axes_t);
                //print out spaces that entered this 
                std::cout << "  Added axes names: [" ;
                for (std::vector<std::string>::iterator it =axes_zaxes_names.axes.begin();
                        it!=axes_zaxes_names.axes.end(); it++ ){
                    std::cout << *it << "," ; 
                }
                std::cout << "]" <<std::endl;
                //set zaxes if available
                if (zaxes_t) axes_zaxes_names.zaxes =json_to_string_vector(zaxes_t);
                //push_back into the vector
                axes_names.push_back(axes_zaxes_names);
            }
        }
    }
    return axes_names;
}

std::map<std::string, Axis*> parse_axes_from_json_file(std::string filename, 
        std::map<std::string, GetValueFunction> function_map){
    std::map<std::string, Axis*> axes_map;
    /// Following www.digip.org/jansson/doc/2.4/apiref.html, searching from "json_load_file"
    json_t * axes_t;    
    json_error_t error;
    // load file
    axes_t = json_load_file(filename.c_str(),0, &error);
    if(!axes_t){
        std::cout << "ERROR: in " << __FUNCTION__ << "\n Json error message: " << error.text << std::endl;
    }
    // Now loop over the json object
    json_t * axis_t;
    const char * axis_name_c; 
    // Some standard out
    std::cout << "Initialising axes..." << std::endl;
    // reading in the various axes
    json_object_foreach(axes_t,axis_name_c,axis_t){
        std::cout << "   " << axis_name_c << std::endl;
        // Get the json objects
        json_t * binning_t          = json_object_get(axis_t,"binning");
        json_t * observable_ids_t   = json_object_get(axis_t,"observable_ids");
        json_t * function_name_t    = json_object_get(axis_t,"function_name");
        // fill binning inputs
        BinningInputs binning_input=json_to_binning_inputs(binning_t);
        // get array indices
        std::vector<int> array_ids=json_to_int_vector(json_object_get(observable_ids_t,"array_ids"));
        // get function name if specified
        Axis *axis;
        if (json_is_string(function_name_t)){
            const char * function_name_c;
            json_unpack(function_name_t,"s",&function_name_c);
            std::string function_name(function_name_c);
            /// initialise Axis with get_value function from map if it exists
            if (function_map.find(function_name)!=function_map.end()){            
                axis=new Axis(axis_name_c,binning_input,function_map[function_name],array_ids);
            }
            else{
                std::cout << "WARNING: in function \"" << __FUNCTION__ << "\", line \"" << __LINE__ << "\", file \""<< __FILE__ << "\""<< std::endl;
                std::cout << "         could not find function name \"" << function_name << "\" in axes map." << std::endl; 
                std::cout << "          functions in the function map are: " ;
                for(std::map<std::string, GetValueFunction>::iterator it=function_map.begin();it!=function_map.end(); it++){
                    std::cout << " \"" <<it->first << "\", "  ;
                }
                std::cout << std::endl;
            }
        }
        else{
            /// initialise Axis without get_value function
            axis=new Axis(axis_name_c,binning_input,array_ids);
        }
        // append Axis
        axes_map[axis_name_c]=axis;
    }
    return axes_map; 
}
