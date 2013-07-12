#ifndef  INC_GETENTRY_H
#define INC_GETENTRY_H
#include <TFile.h>
#include <TTree.h>
#include <TLeaf.h>

class GetEntry{
    public:
        GetEntry(){};
        GetEntry(const char *);
        virtual ~GetEntry(); 
        double * GetVars(int);
    private:
        TFile * _file;
        TTree * _tree;
        int _nvars;
        double * _vars;
};
#endif
