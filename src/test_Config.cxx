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
double get_bsmm_ratio(double *VARS, std::vector<int>* array_ids){
    int bsmm_id=(*array_ids)[0];
    return VARS[bsmm_id]/(3.46e-9);
}


//FIXME: For now this is hard coded should come from config file
std::map<std::string,Axis*> get_axes_map(){
    std::map<std::string,Axis*> axes_map;
// INISTIALISE SPACE
    std::string m0_name("m0-test");
    std::string m12_name("m12");
    std::string mg_name("mg");
    std::string bsmm_ratio_name("bsmm_ratio");
    //bining in puts
    //for m0 and m12
    BinningInputs my_binning;
    my_binning.binning_type="linear";
    my_binning.low=0.;
    my_binning.high=4000.;
    my_binning.nbins=100;
    //for m_gluino
    BinningInputs mg_binning;
    mg_binning.binning_type="linear";
    mg_binning.low=0.;
    mg_binning.high=6000.;
    mg_binning.nbins=100;
    //for bsmm ratio
    BinningInputs bsmm_ratio_binning;
    bsmm_ratio_binning.binning_type="linear";
    bsmm_ratio_binning.low=0.;
    bsmm_ratio_binning.high=3.;
    bsmm_ratio_binning.nbins=100;
    //array int
    int m0_id=1;
    int m12_id=2;
    int mg_id=95;
    int bsmm_ratio_id=12;
    //vec
    std::vector<int> bsmm_ratio_id_vec;
    bsmm_ratio_id_vec.push_back(bsmm_ratio_id);
    //make pointers to Axes
    Axis * m0_axis=new Axis(m0_name,my_binning,m0_id );
    Axis * m12_axis=new Axis(m12_name,my_binning,m12_id );
    Axis * mg_axis=new Axis(mg_name,mg_binning,mg_id);
    Axis * bsmm_ratio_axis=new Axis(bsmm_ratio_name,bsmm_ratio_binning,get_bsmm_ratio,bsmm_ratio_id_vec);
    //fill map
    axes_map[m0_axis->get_name()]=m0_axis;
    axes_map[m12_axis->get_name()]=m12_axis;
    return axes_map;
}

// FIXME: for now hard coded, later from config file
std::vector< AxesZaxesNames> get_axes_names_list(){
    std::vector< AxesZaxesNames> axes_names_list;
    AxesZaxesNames m0m12_names;
    m0m12_names.axes.push_back("m0");
    m0m12_names.axes.push_back("m12");
    axes_names_list.push_back(m0m12_names);
    return axes_names_list;
}

std::vector<Space*> get_spaces(std::map<std::string,Axis*> axes_map, std::vector< AxesZaxesNames>  axes_list ){
    std::vector<Space*> spaces;
    // this function turn something like this : [ {'axes':['m0','m12'  ], 'zaxes':['bsmm_ratio', ... ]}, ...   ]
    // into a vector of spaces. 'm0'. 'm12' are keys to Axes in the axes_map
    for (std::vector<AxesZaxesNames>::iterator axes_names_it=axes_list.begin(); axes_names_it!=axes_list.end() ; axes_names_it++){
        std::vector<Axis*> axes, zaxes;
        //get axes
        for (std::vector<std::string>::iterator axis_name_it=(*axes_names_it).axes.begin();
                axis_name_it!=(*axes_names_it).axes.end();axis_name_it++){
            axes.push_back(axes_map[*axis_name_it]);
        }
        //get zaxes
        for (std::vector<std::string>::iterator axis_name_it=(*axes_names_it).zaxes.begin();
                axis_name_it!=(*axes_names_it).zaxes.end();axis_name_it++){
            zaxes.push_back(axes_map[*axis_name_it]);
        }
        //make a space and push back
        Space * space = new Space(axes,zaxes) ;
        spaces.push_back(space);
    }
    return spaces;
}

void make_histograms(TString infile){
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
    std::vector< AxesZaxesNames> axes_list=get_axes_names_list();
    // get axes map
    std::map<std::string,Axis*> axes_map=get_axes_map();
    // get spaces from axes specified in axes_list
    std::vector<Space*> spaces= get_spaces(axes_map,axes_list);

    //This if the foreloop that makes the plots
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
//    TString file="/vols/cms04/kjd110/nuhm1_mc8_boxes/bak_nuhm1-boxesmc8.root";
    TString file="/vols/cms04/kjd110/nuhm1_mc8_boxes_mh2/nuhm1-boxesmc8.root";
    make_histograms(file);
    return 0;
}
