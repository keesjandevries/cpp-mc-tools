#ifndef  INC_ROOTMAKEPLOTS_H
#define INC_ROOTMAKEPLOTS_H
//standard library
#include <vector>
//root includes
#include "TFile.h"
#include "TTree.h"
#include "TLeaf.h"
//custom includes
#include "Space.h"
class RootMakePlots{
    public:
        RootMakePlots(const char *, std::vector<Space*>);
        RootMakePlots(const char *, std::vector<Space*>, const char *);
        virtual ~RootMakePlots();    
        void Run();
        void Run(int);
    private:
        void init_root_file(const char *);
        TFile * _file;
        TTree * _tree;
        int _nvars;
        int _nentries;
        double * _vars;
        std::vector<Space*> _spaces; 
};
#endif
