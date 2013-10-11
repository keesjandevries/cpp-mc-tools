#include "RootMerge.h"

//FIXME: WARNING THIS IS RESULT ORIENTED AND SHOULD BE KEPT SEPARATE FROM THE REST OF THE MODULES 
//UNTIL IT IS BETTER
struct RootSpace {
    TH2D * reference_hist;
    std::vector<TH2D *> other_hists;
    TFile * file_handle;
};

RootSpace get_space_from_file(const char * file_name, const char * reference_name, std::vector<const char *> other_names){
    RootSpace root_space;
    TFile * file=new TFile(file_name);
    if (file->IsOpen()){
        root_space.file_handle=file;
        if(file->Get(reference_name)){
            root_space.reference_hist=(TH2D*)file->Get(reference_name)->Clone();
        }
        std::vector<const char* >::iterator other_names_it;
        for (other_names_it=other_names.begin();other_names_it!=other_names.end();other_names_it++){
            if(file->Get(*other_names_it)){
                root_space.other_hists.push_back((TH2D*)file->Get(*other_names_it)->Clone());
            }
        }
    }
    else {
        std::cout << "ERROR: could not open \"" << file_name <<"\"" << std::endl;
    }
    return root_space;
}

//FIXME: WARNING THIS IS RESULT ORIENTED AND SHOULD BE KEPT SEPARATE FROM THE REST OF THE MODULES 
//UNTIL IT IS BETTER
RootSpace RootMerge2D(std::vector<const char *> filenames, const char * reference_path,
        std::vector<const char *> other_hist_paths){
    std::vector<const char *>::iterator filenames_it=filenames.begin();
    //the first file serves as the merged starting point
    RootSpace merged_root_space=get_space_from_file(*filenames_it,reference_path,other_hist_paths);
    //define nbins and number of other plots
    int nbins=merged_root_space.reference_hist->GetSize();
    int n_other_hists=merged_root_space.other_hists.size();
    //useful definitions outside loop
    double merged_reference_value;
    double new_reference_value;
    //loop over other files
    for (;filenames_it!=filenames.end();filenames_it++){
        RootSpace new_root_space=get_space_from_file(*filenames_it,reference_path,other_hist_paths);
        //loop over bins
        for (int i=0;i<nbins;i++){
            merged_reference_value=merged_root_space.reference_hist->GetAt(i);
            new_reference_value=new_root_space.reference_hist->GetAt(i);
            //if new refernce value is smaller, then update all values
            if (new_reference_value<merged_reference_value){
                merged_root_space.reference_hist->SetAt(new_reference_value,i);
                for (int k=0; k<n_other_hists; k++){
                    double new_other_hist_value=new_root_space.other_hists[k]->GetAt(i);
                    merged_root_space.other_hists[k]->SetAt(new_other_hist_value,i);
                }
            }
        }
        new_root_space.file_handle->Close();
    }
    return merged_root_space;
}



extern "C"{

void root_merge_spaces_2d(const char ** c_filenames, int n_filenames, const char * outfilename,
           const char * reference_path, const char ** c_other_hist_paths,int n_other_hist_paths){
    std::vector<const char *> filenames(c_filenames,c_filenames+n_filenames);
    std::vector<const char *> other_hist_paths(c_other_hist_paths,c_other_hist_paths+n_other_hist_paths);
    RootSpace result=RootMerge2D(filenames,reference_path,other_hist_paths); 
    if (result.reference_hist!=NULL){
        TFile outfile(outfilename,"UPDATE");
        result.reference_hist->Write();
        std::vector<TH2D*>::iterator other_hists_it=result.other_hists.begin();
        std::vector<TH2D*>::iterator other_hists_it_end=result.other_hists.end();
        for (;other_hists_it!=other_hists_it_end;other_hists_it++){
            (*other_hists_it)->Write();
        }
//        outfile->Close();
    }
}
}
