#ifndef INC_MNEUMGM12GM3GX2LOOKUP_H
#define INC_MNEUMGM12GM3GX2LOOKUP_H
#include <iostream>
#include <vector>
#include <algorithm>
#include "BaseGetValueFunction.h"

class MgM12gM3gX2Lookup{
    public:
        MgM12gM3gX2Lookup(){};
//        MgM12gM3gX2Lookup(double * /*masses_3d*/, int nmg, int nm12g, int nm3g);
        MgM12gM3gX2Lookup(double * /*X2*/, double /*default_X2*/, std::vector<double> /*grid_mg*/,
            std::vector<double> /*grid_m12g*/, std::vector<double> /*grid_m3g*/);
        virtual ~MgM12gM3gX2Lookup();
        double get_X2(double,double,double);
    private:
        int _nmg, _nm12g, _nm3g;
        double* _X2;
        double _default_X2;
        std::vector<std::vector<double> > _mg_m12g_m3g_ranges;
};

class MneuMgM12gM3gX2Lookup: public BaseGetValueFunction{
    public:
        //constructors & destructors
        MneuMgM12gM3gX2Lookup(){};
        MneuMgM12gM3gX2Lookup(std::vector<int> /*array_ids*/, 
                std::vector<double *> /*X2_s*/,double /*default_X2*/,std::vector<double> /*mneus*/,
                std::vector< std::vector<double> > /*grid_mgs*/,std::vector< std::vector<double> > /*grid_m12gs*/,
                std::vector< std::vector<double> > /*grid_m3gs*/);
        virtual ~MneuMgM12gM3gX2Lookup();
        //the get value functions
        virtual double operator()(double *);
    private:
        std::vector<int> _array_ids;
        std::vector<double> _mneu;
        std::vector<MgM12gM3gX2Lookup*> _mg_m12g_m3g_X2_lookups;
};

double c1(std::vector<double>::iterator , double );
double c2(std::vector<double>::iterator , double );
#endif
