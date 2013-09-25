#ifndef  INC_ROOTMAKEPLOTS_H
#define INC_ROOTMAKEPLOTS_H
//standard library
#include <vector>
#include <iomanip>
//root includes
#include "TFile.h"
#include "TLeaf.h"
#include "TChain.h"
//custom includes
#include "Space.h"
class RootMakePlots{
    public:
        RootMakePlots(const char *, std::vector<Space*>);
        RootMakePlots(const char *, std::vector<Space*>, const char *);
        RootMakePlots(std::vector<const char *>, const char *, std::vector<Space*>, const char *);
        virtual ~RootMakePlots();    
        void Run();
        void Run(int);
    private:
        void init_root_file(const char *);
        void init_root_files(std::vector<const char *>);
        TFile * _outfile;
        TString _outdir;
        TChain * _chain;
        int _nvars;
        int _nentries;
        double * _vars;
        std::vector<Space*> _spaces; 
};
#endif
