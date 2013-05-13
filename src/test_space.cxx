#include <iostream>
#include <sstream>
#include <cmath>

#include <TFile.h>
#include <TTree.h>
#include <TLeaf.h>
#include <TString.h>
#include <TH2D.h>

#include "Space.h"
double get_bsmm_ratio(double *VARS, std::vector<int>* array_ids){
    int bsmm_id=(*array_ids)[0];
    return VARS[bsmm_id]/(3.46e-9);
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
// INISTIALISE SPACE
    std::string m0_name("m0");
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
    // make a prediction plot
    std::vector<Axis*> bsmm_pred; bsmm_pred.push_back(bsmm_ratio_axis);
    //initialise plot
    //m0-m12
    std::vector<Axis*> m0m12;
    m0m12.push_back(m0_axis);
    m0m12.push_back(m12_axis);
    Space * my_m0m12=new Space(m0m12,bsmm_pred);
    //mg 
    std::vector<Axis*> mg;
    mg.push_back(mg_axis);
    Space * my_mg=new Space(mg);
    //bsmm
    std::vector<Axis*> bsmm_ratio;
    bsmm_ratio.push_back(bsmm_ratio_axis);
    Space * my_bsmm_ratio=new Space(bsmm_ratio);
    //the for loop
//    nentries=1000;//FIXME: just temporary
    for(int i=0; i<nentries; i++){
        if (i%100000==0) std::cout << "Processed: " << i << "entries" << std::endl;
        t->GetEntry(i);
        my_m0m12->update(invars,i);
        my_mg->update(invars,i);
        my_bsmm_ratio->update(invars,i);
    }
    f->cd();
    my_m0m12->write_plots();
    my_mg->write_plots();
    my_bsmm_ratio->write_plots();
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
