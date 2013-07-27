#include "RootMakePlots.h"

RootMakePlots::RootMakePlots(const char * filename, std::vector<Space*> spaces):
    _spaces(spaces)
{
    _file=new TFile(filename,"UPDATE");
    _tree=(TTree*)_file->Get("tree");// FIXME: hardcoded
    _nvars=_tree->GetLeaf("vars")->GetLen();
    _vars=new double[_nvars];
    _tree->SetBranchAddress("vars",_vars);
    _nentries = _tree->GetEntries();
}

RootMakePlots::~RootMakePlots(){
    delete _vars;
    delete _file;
}

void RootMakePlots::Run(){
    int nentries=_nentries;
    Run(nentries);
}

void RootMakePlots::Run(int nentries){
    std::cout << "Plotting " << nentries << "points" << std::endl; 
    for(int i=0; i<nentries; i++){
        //FIXME: make progress bar
        if (i%100000==0) std::cout << "Processed: " << i << "entries" << std::endl;
        // get entry
        _tree->GetEntry(i);
        ///Update all _spaces: check whether X^2 is lower than existing X^2
        for( std::vector<Space*>::iterator it=_spaces.begin(); it!=_spaces.end() ; it++){
            (*it)->update(_vars,i);
        }
    }
    //Write all plots (X^2,entries, *zaxes) to root file
    for( std::vector<Space*>::iterator it=_spaces.begin(); it!=_spaces.end() ; it++){
        (*it)->write_plots();
    }
}
