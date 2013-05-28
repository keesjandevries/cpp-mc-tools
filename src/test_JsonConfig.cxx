#include <iostream>
#include <sstream>
#include <cmath>

#include <TFile.h>
#include <TTree.h>
#include <TLeaf.h>
#include <TString.h>
#include <TH2D.h>

#include "Space.h"
#include "JsonParsing.h"
#include "GetValueFunctions.h"

std::map<std::string,Axis*> get_axes_map(std::string axes_file_name,  std::map<std::string, GetValueFunction> function_map ){
    return parse_axes_from_json_file(axes_file_name,function_map);
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

void make_histograms(TString infile){
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

// INITIALISE spaces
    // make axes list
    std::vector< AxesZaxesNames> axes_list=get_axes_names_list("user/example_spaces.json");
    // get value functions map
    std::map<std::string,GetValueFunction> function_map=get_GetValueFunction_map();
    // get axes map
    std::map<std::string,Axis*> axes_map=get_axes_map("user/example_axes.json",function_map);
    // get spaces from axes specified in axes_list
    std::vector<Space*> spaces= get_spaces(axes_map,axes_list);

    //This if the foreloop that makes the plots
//    nentries = 100;
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
    //FIXME: not sure if this is needed
    f->cd();
    //Write all plots (X^2,entries, *zaxes) to root file
    for( std::vector<Space*>::iterator it=spaces.begin(); it!=spaces.end() ; it++){
        (*it)->write_plots();
    }
    delete [] invars;
    f->Close();
}



int main(){
//    TString file="/vols/cms04/kjd110/nuhm2_old/nuhm2_all_old_combined.root";
//    TString file="/vols/cms04/kjd110/nuhm1_mc8_boxes_mh2/nuhm1-boxesmc8.root";
//    TString file="/vols/cms04/kjd110/nuhm1_mc8_boxes_mh2/bak2_nuhm1-boxesmc8.root";
//    TString file="/vols/cms04/kjd110/nuhm1_mc8_boxes_mh2/bak_nuhm1-boxesmc8.root";
//    TString file= "/vols/cms04/kjd110/nuhm1_mc8_boxes_mh2_fix//nuhm1-boxesmc8.root";
    TString file= "/vols/cms04/kjd110/mo_fix_cmssm_mc8//cmssm-boxes-combined-mc8.root";
    make_histograms(file);
    return 0;
}
