#include "Run.h"

//FIXME: THIS MODULE COULD DO WITH MORE CLEANUP, BUT IT SEEMS TO WORK

/// this function turns something a c++ version of [ {'axes':['m0','m12'], 'zaxes':['bsmm_ratio', ... ]}, ...   ]
/// into a vector of spaces. Here 'm0', 'm12' are keys to Axes in the axes_map
std::vector<Space*> my_get_spaces(std::map<std::string,Axis*> axes_map, std::vector< AxesZaxesNames>  axes_list ){
    std::vector<Space*> spaces;
    for (std::vector<AxesZaxesNames>::iterator axes_names_it=axes_list.begin(); axes_names_it!=axes_list.end() ; axes_names_it++){
        std::vector<Axis*> axes, zaxes;
        //get axes
        for (std::vector<std::string>::iterator axis_name_it=(*axes_names_it).axes.begin();
                axis_name_it!=(*axes_names_it).axes.end();axis_name_it++){
            if (axes_map.find(*axis_name_it) != axes_map.end() ){
                axes.push_back(axes_map[*axis_name_it]);
            }
            else {
                std::cout << "ERROR: \"" << *axis_name_it << "\" not in axis map." << std::endl;
            }
        }
        //get zaxes
        for (std::vector<std::string>::iterator axis_name_it=(*axes_names_it).zaxes.begin();
                axis_name_it!=(*axes_names_it).zaxes.end();axis_name_it++){
            if (axes_map.find(*axis_name_it) != axes_map.end() ){
                zaxes.push_back(axes_map[*axis_name_it]);
            }
            else {
                std::cout << "ERROR: \"" << *axis_name_it << "\" not in axis map." << std::endl;
            }
        }
        //make a space and push back
        Space * space = new Space(axes,zaxes) ;
        spaces.push_back(space);
    }
    return spaces;
}

//FIXME: THIS MODULE COULD DO WITH MORE CLEANUP, BUT IT SEEMS TO WORK
//
void make_histograms(const char * file, const char * json_axes_file, const char * json_spaces_file){
    TString infile(file);
    std::cout << "Making plots for \"" << infile << "\"." << std::endl; 
// INISTIALISE FILE
// FIXME: eventually turn this into a function
    // File
    TFile* f = new TFile(infile,"UPDATE");  
    // Tree
    TTree* t = (TTree*)f->Get("tree");
    // number of entries
    int nentries = t->GetEntries();
    // branch to loop over
    Int_t nTotVars = t->GetLeaf("vars")->GetLen();
    double* invars = new double[nTotVars];
    t->SetBranchAddress("vars",invars);

//FIXME: THIS MODULE COULD DO WITH MORE CLEANUP, BUT IT SEEMS TO WORK
// INITIALISE spaces
    // make axes list
    std::vector< AxesZaxesNames> axes_list=parse_axes_names_list_from_json_file(json_spaces_file);
    // get value functions map
    std::map<std::string,GetValueFunction> function_map=get_GetValueFunction_map();
    // get axes map
    std::map<std::string,Axis*> axes_map=parse_axes_from_json_file(json_axes_file,function_map);
    // get spaces from axes specified in axes_list
    std::vector<Space*> spaces= my_get_spaces(axes_map,axes_list);

    //This if the foreloop that makes the plots
    nentries = 100;
    for(int i=0; i<nentries; i++){
        //FIXME: make progress bar
        if (i%100000==0) std::cout << "Processed: " << i << "entries" << std::endl;
        // get entry
        t->GetEntry(i);
        ///Update all spaces: check whether X^2 is lower than existing X^2
        for( std::vector<Space*>::iterator it=spaces.begin(); it!=spaces.end() ; it++){
            (*it)->update(invars,i);
        }
    }
    //Write all plots (X^2,entries, *zaxes) to root file
    for( std::vector<Space*>::iterator it=spaces.begin(); it!=spaces.end() ; it++){
        (*it)->write_plots();
    }
    delete [] invars;
    f->Close();
}

//FIXME: THIS MODULE COULD DO WITH MORE CLEANUP, BUT IT SEEMS TO WORK

extern "C" {
    void run(const char * root_file,const char * json_axes_files, const char * json_spaces_file){
        make_histograms(root_file,json_axes_files,json_spaces_file);
    }
}
