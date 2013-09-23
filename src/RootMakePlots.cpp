#include "RootMakePlots.h"

RootMakePlots::RootMakePlots(const char * filename, std::vector<Space*> spaces):
    _spaces(spaces)
{
    _outfile=new TFile(filename,"UPDATE");
    _outdir="";
    init_root_file(filename);
}

RootMakePlots::RootMakePlots(const char * filename, std::vector<Space*> spaces, const char * directory):
    _spaces(spaces)
{
    _outfile=new TFile(filename,"UPDATE");
    _outdir=directory;
    init_root_file(filename);
}

RootMakePlots::RootMakePlots(std::vector<const char *> filenames, const char * outfile, 
        std::vector<Space*> spaces, const char * directory):
    _spaces(spaces)
{
    _outfile=new TFile(outfile,"UPDATE");
    _outdir=directory;
    init_root_files(filenames);
}

RootMakePlots::~RootMakePlots(){
    delete _vars;
    delete _outfile;
    delete _chain;
}

void RootMakePlots::Run(){
    int nentries=_nentries;
    Run(nentries);
}

void RootMakePlots::init_root_file(const char * filename){
    std::vector<const char *> filenames;
    filenames.push_back(filename);
    init_root_files(filenames);
}

void RootMakePlots::init_root_files(std::vector<const char *> filenames){
    _chain=new TChain("tree");// FIXME: hardcoded
    std::vector<const char *>::iterator filenames_it;
    for(filenames_it=filenames.begin();filenames_it!=filenames.end();filenames_it++){
        _chain->Add(*filenames_it);
    }
    _nvars=_chain->GetLeaf("vars")->GetLen();
    _vars=new double[_nvars];
    _chain->SetBranchAddress("vars",_vars);
    _nentries = _chain->GetEntries();
}

void RootMakePlots::Run(int nentries){
    std::cout << "Plotting " << nentries << "points" << std::endl; 
    for(int i=0; i<nentries; i++){
        //FIXME: make progress bar
        if (i%100000==0) std::cout << "Processed: " << i << "entries" << std::endl;
        // get entry
        _chain->GetEntry(i);
        ///Update all _spaces: check whether X^2 is lower than existing X^2
        for( std::vector<Space*>::iterator it=_spaces.begin(); it!=_spaces.end() ; it++){
            (*it)->update(_vars,i);
        }
    }
    //Write all plots (X^2,entries, *zaxes) to root file
    if (_outfile->cd(_outdir)!=kTRUE){
        _outfile->mkdir(_outdir);
        _outfile->cd(_outdir);
    }
    for( std::vector<Space*>::iterator it=_spaces.begin(); it!=_spaces.end() ; it++){
        (*it)->write_plots();
    }
}
