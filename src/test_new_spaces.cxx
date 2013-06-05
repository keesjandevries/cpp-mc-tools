#include <TFile.h>
#include <TTree.h>
#include <TLeaf.h>
#include <TString.h>
#include <TH2D.h>

#include "Space.h"
#include "VarsFunction.h"

double get_bsmm_ratio(double *VARS, std::vector<int>& array_ids){
    int bsmm_id=array_ids[0];
    return VARS[bsmm_id]/(3.46e-9);
}

double my_get_value(double * VARS, std::vector<int>& array_ids){
    return VARS[array_ids[0]];
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
    //mh binning
    BinningInputs my_binning;
    my_binning.binning_type="linear";
    my_binning.low=105.;
    my_binning.high=130.;
    my_binning.nbins=100;
    //setup get_mh
    std::vector<int> array_ids;
    array_ids.push_back(33);
    VarsFunction get_mh(array_ids,my_get_value);
    //make pointers to Axes
    Axis * mh_axis=new Axis("mh",my_binning, &get_mh );
    //initialise plot
    //create axes vector
    std::vector<Axis*> mh;
    mh.push_back(mh_axis);
    //create space
    Space * mh_space=new Space(mh);
    //the for loop
//    nentries=1000;//FIXME: just temporary
    for(int i=0; i<nentries; i++){
        if (i%100000==0) std::cout << "Processed: " << i << "entries" << std::endl;
        t->GetEntry(i);
        mh_space->update(invars,i);
    }
    f->cd();
    mh_space->write_plots();
    delete [] invars;
    f->Close();
}



int main(){
//    TString file="/vols/cms04/kjd110/nuhm2_old/nuhm2_all_old_combined.root";
//    TString file="/vols/cms04/kjd110/nuhm1_mc8_boxes/bak_nuhm1-boxesmc8.root";
    TString file="/vols/cms04/kjd110/pmssm10_bf_of_pmssm8/pMSSM10-mndrop-atlas.root";
    make_histograms(file);
    return 0;
}
