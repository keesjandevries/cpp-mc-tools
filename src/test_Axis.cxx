#include<iostream>

#include "Axis.h"


double my_get_value(double * VARS, std::vector<int>* array_ids){
    return VARS[(*array_ids)[0]]/VARS[(*array_ids)[1]];
}

int main(){
    std::cout <<  "Testing the damn axis:D " << std::endl;
    //name of axis
    std::string name("harry");
    //bining in puts
    BinningInputs my_binning;
    my_binning.binning_type="log";
    my_binning.low=1.;
    my_binning.high=1000.;
    my_binning.nbins=3;
    //array int
    int my_array_int=3;
    //initiatlise
    Axis my_axis(name, my_binning,my_array_int);
    //print stuff
    my_axis.print_bin_edges();
    // make up some funny vars array
    double  my_vars[]={1.2, 2.3, 3.4 , 4.5 };
    // test the lookup
    std::cout << "In the array {1.2, 2.3, 3.4 , 4.5 }, I find: " << my_axis.get_value(my_vars) << std::endl;

    //For the second test need int vector
    std::vector<int> my_array_ids;
    my_array_ids.push_back(1);
    my_array_ids.push_back(2);
    Axis my_second_axis(name,my_binning,my_get_value,my_array_ids);
    std::cout << "In the array {1.2, 2.3, 3.4 , 4.5 }, I find: " << my_second_axis.get_value(my_vars) << std::endl;

    //Make a new Axis with no binning
    double  my_second_vars[]={0.1, 1.2, 2.3, 3.4 , 4.5 };
    Axis my_third_axis(name,my_get_value,my_array_ids);
    std::cout << "In the array {0.1, 1.2, 2.3, 3.4 , 4.5 }, I find: " << my_third_axis.get_value(my_second_vars) << std::endl;
    return 0;
}
