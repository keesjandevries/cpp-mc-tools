#include "CtypesWrappers.h"

GetValueManager * get_value_manager=GetValueManager::GetInstance();
AxisManager * axis_manager=AxisManager::GetInstance();
SpaceManager * space_manager=SpaceManager::GetInstance();
ContourManager * contour_manager=ContourManager::GetInstance();
CutManager * cut_manager=CutManager::GetInstance();
    
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
double get_value(const char * name,double * vars){
    return (*(get_value_manager->Get(name)))(vars);
}
void test(){
    double vars[300];
    vars[71]=83.2504;
    vars[184]=2.14692e-09;
    std::cout << "THIS SHOULD GIVE 2.14692e-09: " << contour_manager->Get("xenon100_july_2012")->GetContourValue(83.2504) << std::endl;
    std::cout << "THIS SHOULD GIVE 2.3: " << (*(get_value_manager->Get("xenon100_july_2012")))(vars) << std::endl;
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
void add_cut(const char * name, int * array_ids, int n_array_ids,const char *function_name){
    cut_manager->AddCut(name,array_ids,n_array_ids,function_name);
}
void make_plots(const char ** root_file_names,int n_root_file_names,
        const char * outfile, int nentries, const char * directoryname, const char ** cut_names, int n_cut_names){
    std::vector<const char *> filenames(root_file_names,root_file_names+n_root_file_names);
    std::vector<const char *> cut_names_v(cut_names,cut_names+n_cut_names);
    std::vector<Space*> spaces=space_manager->Get();
    std::vector<Cut*> cuts;
    std::vector<const char*>::iterator cut_names_it;
    for (cut_names_it=cut_names_v.begin();cut_names_it!=cut_names_v.end();cut_names_it++){
        Cut * cut=cut_manager->Get(*cut_names_it);
        if (cut!=NULL){
            cuts.push_back(cut);
        }
    }
//    std::vector<Cut*> cuts=cut_manager->Get();
    RootMakePlots root_make_plots(filenames,outfile,spaces,directoryname);
    if (nentries==-1){
        root_make_plots.Run(cuts);
    }
    else{
        root_make_plots.Run(nentries,cuts);
    }
}
void sqlite_make_plots(const char * sqlite_db_file, const char * query, const char * outfile_name){
    std::vector<Space*> spaces=space_manager->Get();
    SqliteMakePlots plotter(sqlite_db_file);
    plotter.Run(query,spaces);
    TFile outfile(outfile_name,"UPDATE");
    for( std::vector<Space*>::iterator it=spaces.begin(); it!=spaces.end() ; it++){
        (*it)->write_plots();
    }
    outfile.Close();
}
void insert_root_into_sqlite(const char * root_file_name, const char * sqlite_db, int collection_rowid){
    InsertRootIntoSqlite(root_file_name, sqlite_db, collection_rowid);
}
}
