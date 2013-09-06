#include "CtypesWrappers.h"

GetValueManager * get_value_manager=GetValueManager::GetInstance();
AxisManager * axis_manager=AxisManager::GetInstance();
SpaceManager * space_manager=SpaceManager::GetInstance();

void my_test(){
    double a[10];
    a[5]=1;
    a[0]=0;
    a[1]=1;
    std::cout << "Hope this gives 1: " << (*(get_value_manager->Get("name1"))).get_value(a) << std::endl;
    std::cout << "Hope this gives 0.5: " << (*(get_value_manager->Get("name2"))).get_value(a) << std::endl;
    std::cout << "Hope this gives 1.5: " << (*(get_value_manager->Get("chi2"))).get_value(a) << std::endl;
    std::cout << "Now test axis" << std::endl;
    std::cout << "Hope this gives \"axis1\": " << (*(axis_manager->Get("axis1"))).get_name() << std::endl;
    std::cout << "Hope this gives 1: " << (*(axis_manager->Get("axis1"))).get_value(a) << std::endl;
    std::cout << "Bin edges:" << std::endl;
    axis_manager->Get("axis2")->print_bin_edges();
}
    
extern "C"{
void add_vars_lookup(const char * name, int array_id){
    get_value_manager->AddVarsLookup(name,array_id);
}
void add_vars_function(const char * name, int * array_ids, int n_array_ids,const char *function_name){
    get_value_manager->AddVarsFunction(name,array_ids,n_array_ids,function_name);
}
void add_chi2_calculator(const char * name){
    get_value_manager->AddChi2Calculator(name);
}
void add_constraint_to_chi2_calculator(const char * constraint_name, const char* calculator_name){
    get_value_manager->AddConstraintToChi2Calculator(constraint_name,calculator_name);
}
void test(){
    my_test();
}
void add_axis(const char * axis_name, const char * value_function_name){
    axis_manager->AddAxis(axis_name,value_function_name);
}
void add_axis_with_binning(const char * axis_name, const char * value_function_name,
        const char * binning_type, double low, double high, int nbins){
    axis_manager->AddAxis(axis_name,value_function_name,binning_type,low,high,nbins);
}
void add_space(const char * c_axes_names[], int n_axes_names,const char * c_zaxes_names[], 
        int n_zaxes_names,const char * reference_function_name){
    std::vector<std::string> axes_names;
    std::vector<std::string> zaxes_names;
    for (int i=0;i<n_axes_names;i++){
        axes_names.push_back(c_axes_names[i]);
    }
    std::cout << "n axes: " << axes_names.size() << std::endl;
    for (int i=0;i<n_zaxes_names;i++){
        zaxes_names.push_back(c_zaxes_names[i]);
    }
    std::cout << "n zaxes: " << zaxes_names.size() << std::endl;
    space_manager->AddSpace(axes_names,zaxes_names,reference_function_name);
}

void make_plots_in_directory(const char * root_file_name,int nentries, const char * directoryname){
    std::vector<Space*> spaces=space_manager->Get();
    RootMakePlots root_make_plots(root_file_name,spaces,directoryname);
//    int nentries=100;
    if (nentries==-1){
        root_make_plots.Run();
    }
    else{
        root_make_plots.Run(nentries);
    }
}
void make_plots(const char * root_file_name,int nentries){
    make_plots_in_directory(root_file_name,nentries,""); 
}
}
