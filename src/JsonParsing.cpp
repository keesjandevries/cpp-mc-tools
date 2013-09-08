#include "JsonParsing.h"

//FIXME: put nicer error messaging, like in FeynHIggs

//Note: this function is quite compact
std::vector<double> json_to_double_vector(json_t * object_t){
    std::vector<double> double_vector;
    // if object is array, then loop over it and fill vector
    if (json_is_array(object_t)){
        size_t  size_object_t=json_array_size(object_t);
        for (size_t i=0;i<size_object_t;i++){
            double_vector.push_back(json_real_value(json_array_get(object_t,i)));
        }
    }
    else {
        std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
        std::cout << "      json object was not an array"<< std::endl;
    }
    return double_vector;
}

//FIXME: may want to cast this in template
//FIXME: Make less flexible. Python should handle the input!!
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

std::vector<double_pair> json_to_coordinates_vector(json_t * array_t){
    std::vector<double_pair> double_pair_vector;
    // if object is array, then loop over it and fill vector
    if (json_is_array(array_t)){
        size_t  size_array_t=json_array_size(array_t);
        for (size_t i=0;i<size_array_t;i++){
            json_t * point_t=json_array_get(array_t,i);
            if (json_array_size(point_t)==2){
                double x=json_real_value(json_array_get(point_t,0));
                double y=json_real_value(json_array_get(point_t,1));
                double_pair_vector.push_back(std::make_pair(x,y));
            }
            else{
                std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
                std::cout << "coordinates don't consist of two entries, return empty vector"<< std::endl;
                double_pair_vector.clear();
                return double_pair_vector;
            }
        }
    }
    else {
        std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
        std::cout << "json object was not an array, returning empty vector"<< std::endl;
    }
    return double_pair_vector;
}

Contour * json_to_contour(json_t * contour_t){
    Contour * contour;
    json_t * coordinates_t=json_object_get(contour_t,"coordinates");
    json_t * type_t=json_object_get(contour_t,"type");
    //get coordinates
    std::vector<double_pair> coordinates=json_to_coordinates_vector(coordinates_t);
    //fill type
    const char * type_c = json_string_value(type_t);
    if (type_c){
        std::string type(type_c);
        if (type=="UniversalLimits"){
            contour = new UniversalLimitsContour(coordinates);
        } 
        else{
            std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
            std::cout << "Contour type not found"<< std::endl;
        }
    }
    return contour;
}

std::vector<Contour*> json_to_contour_vector(json_t * contours_t){
    std::vector<Contour*> contours;
    if (json_is_array(contours_t)){
        size_t n_contours=json_array_size(contours_t);
        for (size_t i=0;i<n_contours;i++){
            json_t * contour_t = json_array_get(contours_t,i);
            Contour * contour=json_to_contour(contour_t); 
            if(contour){
                contours.push_back(contour); 
            }
            else{
                std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
                std::cout << "contour failed, returning empty vector of contours"<< std::endl;
                contours.clear();
                return contours;
            }
        }
    }
    else{
        std::cout << "ERROR: in " << __FUNCTION__ << std::endl;
        std::cout << "json object was not an array, returning empty vector"<< std::endl;
    }
    return contours;
}

BinningInputs json_to_binning_inputs(json_t * object_t){
    BinningInputs binning_input;
    if json_is_object(object_t){
        //FIXME: don't need unpack
        json_unpack(json_object_get(object_t,"low"),"f",   &(binning_input.low) );
        json_unpack(json_object_get(object_t,"high"),"f",  &(binning_input.high) );
        json_unpack(json_object_get(object_t,"nbins"),"i", &(binning_input.nbins) );
        const char * tmp_binning_type;
        json_unpack(json_object_get(object_t,"type"),"s",  &(tmp_binning_type) );
        binning_input.binning_type=tmp_binning_type;
    }
    else {
        std::cout << "WARNING: in " << __FUNCTION__ << std::endl;
        std::cout << "not a json object. Was binning defined?"   << std::endl;
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
                //set zaxes if available
                if (zaxes_t) axes_zaxes_names.zaxes =json_to_string_vector(zaxes_t);
                //push_back into the vector
                axes_names.push_back(axes_zaxes_names);
            }
        }
    }
    return axes_names;
}

//FIXME: cleanup this function and the error messages
GaussConstraint * parse_gauss_constraint(json_t* constraint_t, std::map<std::string, GaussFunc> gauss_func_map){
    GaussConstraint *constraint=NULL;
    //get array ids
    json_t * observable_ids_t   = json_object_get(constraint_t,"observable_ids");
    //get array ids
    std::vector<int> array_ids;
    if (observable_ids_t){
        array_ids=json_to_int_vector(json_object_get(observable_ids_t,"array_ids"));
    }
    else return constraint;
    //get gaussian settings
    json_t * mu_t=json_object_get(constraint_t,"mu");
    json_t * sigmas_t=json_object_get(constraint_t,"sigmas");
    json_t * function_name_t=json_object_get(constraint_t,"function_name");
    //get mu 
    double mu;
    if (json_is_real(mu_t))  mu=json_real_value(mu_t); 
    else {
        std::cout << "ERROR: in " << __FUNCTION__<< ", LINE:" <<__FUNCTION__<< "\nmu is not real or not given" << std::endl;
        return constraint;
    }
    //get sigmas
    std::vector<double> sigmas=json_to_double_vector(sigmas_t);  
    if (sigmas.size()==0){ 
        std::cout << "ERROR: in " << __FUNCTION__<< ", LINE:" <<__FUNCTION__<< "\nsigmas has length 0" << std::endl;
        return constraint;
    }
    //get gauss_fucntion
    GaussFunc gauss_func;
    const char * function_name_c = json_string_value(function_name_t);
    if (function_name_c){
        if (gauss_func_map.find(function_name_c)!=gauss_func_map.end()){
            gauss_func=gauss_func_map[function_name_c];
        }
    }
    else {
        std::cout << "ERROR: in " << __FUNCTION__<< ", LINE:" <<__FUNCTION__<< "\nfunction name goes wrong." << std::endl;
        return constraint;
    }
    //allocate new gauss constraint
    constraint= new GaussConstraint(array_ids , mu, sigmas, gauss_func);
    return constraint;
}

ContourConstraint * parse_contour_constraint(json_t* constraint_t, std::map<std::string, ContourFunc> contour_func_map){
    ContourConstraint *constraint=NULL;
    //get contour settings
    json_t * observable_ids_t   = json_object_get(constraint_t,"observable_ids");
    json_t * contours_t=json_object_get(constraint_t,"contours");
    json_t * function_name_t=json_object_get(constraint_t,"function_name");
    //get array ids
    std::vector<int> array_ids;
    if (observable_ids_t){
        array_ids=json_to_int_vector(json_object_get(observable_ids_t,"array_ids"));
    }
    else return constraint;
    //get contours
    std::vector<Contour*> contours= json_to_contour_vector(contours_t);
    if (contours.size()==0) return constraint;
    //get contour_fucntion
    ContourFunc contour_func;
    const char * function_name_c = json_string_value(function_name_t);
    if (function_name_c){
        if (contour_func_map.find(function_name_c)!=contour_func_map.end()){
            contour_func=contour_func_map[function_name_c];
        }
    }
    else {
        std::cout << "ERROR: in " << __FUNCTION__<< ", LINE:" <<__FUNCTION__<< "\nfunction name goes wrong." << std::endl;
        return constraint;
    }
    //allocate new contour constraint
    constraint= new ContourConstraint(array_ids , contours, contour_func);
    return constraint;
}

std::map<std::string, BaseGetValueFunction*> parse_constraints_from_json_file(std::string filename,
        std::map<std::string, GaussFunc> gauss_func_map,
        std::map<std::string, ContourFunc> contour_func_map){
    // define resultent map
    std::map<std::string, BaseGetValueFunction*> constraint_map;
    // load objects from file
    json_t * constraints_t;    
    json_error_t error;
    // load file
    constraints_t = json_load_file(filename.c_str(),0, &error);
    //prepare loop
    json_t * constraint_t;
    const char * constraint_name_c; 
    // loop over objects
    json_object_foreach(constraints_t,constraint_name_c,constraint_t){
        json_t * gauss_constraint_t=json_object_get(constraint_t,"gauss_constraint");
        json_t * contour_constraint_t=json_object_get(constraint_t,"contour_constraint");

        BaseGetValueFunction * constraint = NULL;
        if (gauss_constraint_t){
            constraint=parse_gauss_constraint(gauss_constraint_t,gauss_func_map); 
        }
        else if (contour_constraint_t){
            constraint=parse_contour_constraint(contour_constraint_t,contour_func_map); 
        }
        
        if (constraint){
            constraint_map[constraint_name_c]=constraint;    
        }
    }
    return constraint_map;
}

std::map<std::string, GaussConstraint*> parse_gauss_constraint_from_json_file(std::string filename,
        std::map<std::string, GaussFunc> gauss_func_map){
    // define resultent map
    std::map<std::string, GaussConstraint*> constraint_map;
    // load objects from file
    json_t * constraints_t;    
    json_error_t error;
    // load file
    constraints_t = json_load_file(filename.c_str(),0, &error);
    //prepare loop
    json_t * constraint_t;
    const char * constraint_name_c; 
    // loop over objects
    json_object_foreach(constraints_t,constraint_name_c,constraint_t){
        GaussConstraint * constraint = parse_gauss_constraint(constraint_t,gauss_func_map);
        if (constraint){
            constraint_map[constraint_name_c]=constraint;    
        }
    }
    return constraint_map;
}

VarsLookup * get_VarsLookup(json_t * vars_lookup_t){
    VarsLookup * vars_lookup=NULL;
    int array_id=-1;
    // json_object_get will return NULL in case vars_lookup_t is not object
    json_t * array_id_t = json_object_get(vars_lookup_t,"array_id");
    // json_is_integer will also give false if array_id_t is NULL
    // hence all the checks are done
    if (json_is_integer(array_id_t)){
        array_id=json_integer_value(array_id_t); 
        vars_lookup = new VarsLookup(array_id);
    }
    else{
        std::cout << "ERROR: in " << __FUNCTION__ << ", line: " <<__LINE__ << std::endl;
        std::cout << "array_id is not an integer" << std::endl;
    }
    return vars_lookup;
}

VarsFunction * get_VarsFunction(json_t * vars_function_t , std::map<std::string, GetVarsFunction> function_map){
    VarsFunction * vars_function=NULL;
    json_t * observable_ids_t = json_object_get(vars_function_t, "observable_ids");
    json_t * name_t = json_object_get(vars_function_t, "name");
    // retrieve values:
    // function name
    const char * name_c=json_string_value(name_t);
    // array_ids
    json_t * array_ids_t = json_object_get(observable_ids_t,"array_ids");
    std::vector<int> array_ids=json_to_int_vector(array_ids_t);
    if ((array_ids.size() > 0 ) && (function_map.find(name_c)!=function_map.end())){
        vars_function = new VarsFunction(array_ids,function_map[name_c]); 
    }
    return vars_function;
}
//
//ContourConstraint * get_ContourConstraint(json_t * gauss_constraint_t, std::map<std::string, ContourConstraint*> constraint_map){
//    ContourConstraint * gauss_constraint=NULL;
//    const char * name_c = json_string_value(gauss_constraint_t);
//    if (constraint_map.find(name_c)!=constraint_map.end()){
//        gauss_constraint=constraint_map[name_c];
//    }
//    return gauss_constraint;
//}
//GaussConstraint * get_GaussConstraint(json_t * gauss_constraint_t, std::map<std::string, GaussConstraint*> constraint_map){
//    GaussConstraint * gauss_constraint=NULL;
//    const char * name_c = json_string_value(gauss_constraint_t);
//    if (constraint_map.find(name_c)!=constraint_map.end()){
//        gauss_constraint=constraint_map[name_c];
//    }
//    return gauss_constraint;
//}
BaseGetValueFunction * get_BaseGetValueFunction(json_t * gauss_constraint_t, std::map<std::string, BaseGetValueFunction*> constraint_map){
    BaseGetValueFunction * gauss_constraint=NULL;
    const char * name_c = json_string_value(gauss_constraint_t);
    if (constraint_map.find(name_c)!=constraint_map.end()){
        gauss_constraint=constraint_map[name_c];
    }
    else{
        std::cout << "ERROR: \"" << name_c << "\" not defined" << std::endl;;
    }
    return gauss_constraint;
}


//FIXME: should have overloaded this function to remain backward compatibility
//std::map<std::string, Axis*> parse_axes_from_json_file(std::string filename, 
//        std::map<std::string, GetVarsFunction> function_map, 
//        std::map<std::string, GaussConstraint*> gauss_constraint_map){
//    std::map<std::string, ContourConstraint*> contour_constraint_map;
//    return parse_axes_from_json_file( filename, function_map, gauss_constraint_map, contour_constraint_map);
//}

std::map<std::string, Axis*> parse_axes_from_json_file(std::string filename, 
        std::map<std::string, GetVarsFunction> function_map, 
        std::map<std::string, BaseGetValueFunction*> constraint_map){
    std::map<std::string, Axis*> axes_map;
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
    // reading in the various axes
    json_object_foreach(axes_t,axis_name_c,axis_t){
        // method of getting a value out of the "vars" array
        json_t * vars_lookup_t = json_object_get(axis_t,"vars_lookup");
        json_t * vars_function_t = json_object_get(axis_t,"vars_function");
        json_t * gauss_constraint_t = json_object_get(axis_t,"gauss_constraint");
        json_t * contour_constraint_t = json_object_get(axis_t,"contour_constraint");
        // binning
        json_t * binning_t = json_object_get(axis_t,"binning");
        // fill binning inputs
        BinningInputs binning_input=json_to_binning_inputs(binning_t);
        // fill function that gets values from vars
        BaseGetValueFunction * get_value=NULL;
        Axis * axis=NULL;
        //
        if (vars_lookup_t){
            get_value = get_VarsLookup(vars_lookup_t);
        }
        else if (vars_function_t){
            get_value = get_VarsFunction(vars_function_t,function_map);
        }
        else if (gauss_constraint_t){
            get_value = get_BaseGetValueFunction(gauss_constraint_t,constraint_map);
        }
        else if (contour_constraint_t){
            get_value = get_BaseGetValueFunction(contour_constraint_t,constraint_map);
        }
        if (get_value){
            Axis * axis=new Axis(axis_name_c,get_value,binning_input);
            axes_map[axis_name_c]=axis;
        }
    }
    return axes_map; 
}
