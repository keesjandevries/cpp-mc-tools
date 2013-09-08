#include "CtypesWrappers.h"

GetValueManager * get_value_manager=GetValueManager::GetInstance();
AxisManager * axis_manager=AxisManager::GetInstance();
SpaceManager * space_manager=SpaceManager::GetInstance();
ContourManager * contour_manager=ContourManager::GetInstance();
//FIXME: remove this test function
    
extern "C"{
void add_vars_lookup(const char * name, int array_id){
    get_value_manager->AddVarsLookup(name,array_id);
}
void add_vars_function(const char * name, int * array_ids, int n_array_ids,const char *function_name){
    get_value_manager->AddVarsFunction(name,array_ids,n_array_ids,function_name);
}
void add_gauss_constraint(const char * name, int* array_ids_p, int n_array_ids, double mu, 
        double* sigmas_p ,int n_sigmas, const char * function_name){
    get_value_manager->AddGaussConstraint(name, array_ids_p,n_array_ids,mu,sigmas_p,n_sigmas,function_name);
}
void add_contour_constraint(const char *name ,int* array_ids_p, int n_array_ids,
        const char ** contour_names_p, int n_contour_names ,const char *function_name){
    get_value_manager->AddContourConstraint(name, array_ids_p,n_array_ids,contour_names_p,n_contour_names, function_name);
}
void add_chi2_calculator(const char * name){
    get_value_manager->AddChi2Calculator(name);
}
void add_constraint_to_chi2_calculator(const char * constraint_name, const char* calculator_name){
    get_value_manager->AddConstraintToChi2Calculator(constraint_name,calculator_name);
}
void test(){
    double x[]={1,100};
    double y[]={0.01,1};
    contour_manager->AddContour("harry",x,y,2,"log_x_log_y");
    std::cout << "THIS SHOULD GIVE 0.1: " << contour_manager->Get("harry")->GetContourValue(10) << std::endl;
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
    for (int i=0;i<n_zaxes_names;i++){
        zaxes_names.push_back(c_zaxes_names[i]);
    }
    space_manager->AddSpace(axes_names,zaxes_names,reference_function_name);
}
void add_contour(const char * name, double * xs, double * ys, int n_coords, const char * type){
    contour_manager->AddContour(name,xs,ys,n_coords,type);
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
