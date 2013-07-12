#include "GetEntry.h"
GetEntry::GetEntry(const char * filename){
    _file=new TFile(filename);
    _tree=(TTree*)_file->Get("tree");// FIXME: hardcoded
    _nvars=_tree->GetLeaf("vars")->GetLen();
    _vars=new double[_nvars];
    _tree->SetBranchAddress("vars",_vars);
}

GetEntry::~GetEntry(){
    delete _vars;
    delete _file;
}

double * GetEntry::GetVars(int entry){
    _tree->GetEntry(entry);
    return _vars;
}
