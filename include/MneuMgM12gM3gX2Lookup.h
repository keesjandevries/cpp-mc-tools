#ifndef INC_MNEUMGM12GM3GX2LOOKUP_H
#define INC_MNEUMGM12GM3GX2LOOKUP_H
#include "BaseGetValueFunction.h"

class MgM12gM3gX2Lookup{
    public:
        MgM12gM3gX2Lookup(){};
        MgM12gM3gX2Lookup(double * /*masses_3d*/, int nmg, int nm12g, int nm3g);
        virtual ~MgM12gM3gX2Lookup(){};
        double get_X2(double,double,double);
    private:
        int _nmg, _nm12g, _nm3g;
        std::vector<double> _mg_m12g_m3g_ranges;
};

class MneuMgM12gM3gX2Lookup: public BaseGetValueFunction{
    public:
        //constructors & destructors
        MneuMgM12gM3gX2Lookup(){};
        MneuMgM12gM3gX2Lookup(int);
        virtual ~MneuMgM12gM3gX2Lookup(){};
        //the get value functions
        virtual double operator()(double *);
    private:
        std::vector<MgM12gM3gX2Lookup*> _mg_m12g_m3g_X2_lookups;
};

double c1(std::vector<double>::iterator , double );
double c2(std::vector<double>::iterator , double );
#endif
