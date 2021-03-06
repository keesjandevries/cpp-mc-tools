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
void add_mneu_mg_m12g_m3g_X2_lookup(const char * name, int * array_ids_p, int n_array_ids, 
        double default_X2, double * mneu_mg_m12g_m3g_X2_table, int n_rows){
    get_value_manager->AddMneuMgM12gM3gX2Lookup(name, array_ids_p,  n_array_ids, 
         default_X2,  mneu_mg_m12g_m3g_X2_table,  n_rows);
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
double get_contour_value(const char * name,double parameter_value){
    return contour_manager->Get(name)->GetContourValue(parameter_value);
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
void sqlite_make_plots(const char * sqlite_db_file, const char * query,int query_length, 
        const char * outfile_name, const char * reference_name){
    std::vector<Space*> spaces=space_manager->Get();
    BaseGetValueFunction * reference_function=get_value_manager->Get(reference_name);
    SqliteMakePlots plotter(sqlite_db_file);
    std::pair<int, double> result=plotter.Run(query,query_length,spaces,reference_function);
    TFile outfile(outfile_name,"UPDATE");
    for( std::vector<Space*>::iterator it=spaces.begin(); it!=spaces.end() ; it++){
        (*it)->write_plots();
    }
    TTree *tree = new TTree("min_reference_tree","Tree with minimum reference value/rowid");
    Int_t min_reference_rowid = result.first;
    Double_t min_reference = result.second;
    tree->Branch("min_reference_rowid", &min_reference_rowid,
            "min_reference_rowid/I");
    tree->Branch("min_reference", &min_reference, "min_reference/D");
    tree->Fill();
    tree->Write();
    outfile.Close();
}
void sqlite_reduce_db(const char * input_name, const char * output_name, const char * select_query, 
    int select_query_length, const char * chi2_function_name, double max_chi2 ){
    BaseGetValueFunction * chi2_function=get_value_manager->Get(chi2_function_name);
    SqliteReduceDB(input_name, output_name,  select_query, select_query_length, chi2_function, max_chi2);
}
void insert_root_into_sqlite(const char * root_file_name, const char * sqlite_db, int collection_rowid){
    InsertRootIntoSqlite(root_file_name, sqlite_db, collection_rowid);
}
void get_2d_hist_content(const char* root_file_name, const char * th2d_name, int n, double * content){
    TFile file(root_file_name);
    if (file.IsOpen()){
        if(file.Get(th2d_name)){
            TH2D* hist=(TH2D*)file.Get(th2d_name)->Clone();
            if (n==hist->fN){
                for (int i=0;i<n;i++){
                    content[i]=hist->GetAt(i);
                }
            
            }
            else{
                std::cout << "Number provided doesn't equal the number of elements in the 2d hist"<< std::endl;
            }
        }
        else{
            std::cout<< "Couldn't find hist name \"" << th2d_name <<"\"" << std::endl; 
        }
    }
    else{
        std::cout << "Couldn't open rootfile: \"" << root_file_name <<"\"" << std::endl;
    }
    file.Close();
}
double get_min_reference(const char * root_file_name){
    TFile file(root_file_name);
    TTree * tree = (TTree*) file.Get("min_reference_tree");
    double min_reference = 1e9;
    if (tree!=0){
        tree->SetBranchAddress("min_reference",&min_reference);
        tree->GetEntry(0);
    }
    return min_reference;
}
int get_min_reference_rowid(const char * root_file_name){
    TFile file(root_file_name);
    TTree * tree = (TTree*) file.Get("min_reference_tree");
    int min_reference_rowid = -1;
    if (tree!=0){
        tree->SetBranchAddress("min_reference_rowid",&min_reference_rowid);
        tree->GetEntry(0);
    }
    return min_reference_rowid;
}
void get_1d_hist_content(const char* root_file_name, const char * th1d_name, int n, double * content){
    TFile file(root_file_name);
    if (file.IsOpen()){
        if(file.Get(th1d_name)){
            TH1D* hist=(TH1D*)file.Get(th1d_name)->Clone();
            if (n==hist->fN){
                for (int i=0;i<n;i++){
                    content[i]=hist->GetAt(i);
                }
            
            }
            else{
                std::cout << "Number provided doesn't equal the number of elements in the 1d hist"<< std::endl;
            }
        }
        else{
            std::cout<< "Couldn't find hist name \"" << th1d_name <<"\"" << std::endl; 
        }
    }
    else{
        std::cout << "Couldn't open rootfile: \"" << root_file_name <<"\"" << std::endl;
    }
    file.Close();
}
double chi2_ndof_to_cl(double chi2, int ndof){
    return TMath::Prob(chi2,ndof);
}
}
