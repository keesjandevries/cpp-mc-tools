#include "MneuMgM12gM3gX2Lookup.h"


MgM12gM3gX2Lookup::MgM12gM3gX2Lookup(double * X2, double default_X2, std::vector<double> grid_mg,
    std::vector<double> grid_m12g, std::vector<double> grid_m3g):
    _default_X2(default_X2)
{
    _nmg=grid_mg.size();
    _nm12g=grid_m12g.size();
    _nm3g=grid_m3g.size();
    _mg_m12g_m3g_ranges.push_back(grid_mg);
    _mg_m12g_m3g_ranges.push_back(grid_m12g);
    _mg_m12g_m3g_ranges.push_back(grid_m3g);
    _X2=new double[_nmg*_nm12g*_nm3g];
    for (int i=0; i<_nmg*_nm12g*_nm3g; i++){
        _X2[i]=X2[i];
    }
}

MgM12gM3gX2Lookup::~MgM12gM3gX2Lookup(){
    delete  _X2;
}

double MgM12gM3gX2Lookup::get_X2(double mg, double m12g, double m3g){
    // helper variables
    double m[3];
    m[0]=mg; m[1]=m12g; m[2]=m3g;
    int lower_index[3];
    double c[3][2];
    bool outside;
    int i_mg,i_m12g,i_m3g; 
    std::vector<double>::iterator m_it;
    std::vector<double>::iterator m_begin;
    std::vector<double>::iterator m_end;
    //result
    double X2_interp=0;
    for (int i=0;i<3;i++){
        m_begin=_mg_m12g_m3g_ranges[i].begin();
        m_end=_mg_m12g_m3g_ranges[i].end();
        m_it=std::upper_bound(m_begin,m_end,m[i]);
        outside=(m_it==_mg_m12g_m3g_ranges[i].begin()) || (m_it==_mg_m12g_m3g_ranges[i].end());
        if (!outside){
            c[i][0]=c1(m_it,m[i]);
            c[i][1]=c2(m_it,m[i]);
            lower_index[i]=(m_it-m_begin-1);
        }
        else{
            break;
        }
    }
    if (outside){
        return _default_X2;
    }
    for (int a_mg=0; a_mg<2; a_mg++){
        for (int a_m12g=0; a_m12g<2; a_m12g++){
            for (int a_m3g=0; a_m3g<2; a_m3g++){
                i_mg=lower_index[0]+a_mg; i_m12g=lower_index[1]+a_m12g; i_m3g=lower_index[2]+a_m3g;
                X2_interp+=c[0][a_mg]*c[1][a_m12g]*c[2][a_m3g]*_X2[i_mg*_nm12g*_nm3g+i_m12g*_nm3g+i_m3g];
            }
        }
    }
    return X2_interp;  
}

MneuMgM12gM3gX2Lookup::MneuMgM12gM3gX2Lookup(std::vector<int> array_ids, 
                std::vector<double *> X2_s,double default_X2,std::vector<double> mneu,
                std::vector< std::vector<double> > grid_mgs,std::vector< std::vector<double> > grid_m12gs,
                std::vector< std::vector<double> > grid_m3gs):
    _array_ids(array_ids),
    _mneu(mneu)
{
    int nmneu=(int)mneu.size();
    _mg_m12g_m3g_X2_lookups.reserve(nmneu);
    for (int i=0; i<nmneu; i++){
        _mg_m12g_m3g_X2_lookups[i]=new MgM12gM3gX2Lookup(X2_s[i],default_X2,grid_mgs[i],grid_m12gs[i],grid_m3gs[i]); 
    }
}

MneuMgM12gM3gX2Lookup::~MneuMgM12gM3gX2Lookup(){
    std::vector<MgM12gM3gX2Lookup*>::iterator lookup_it; 
    for (lookup_it=_mg_m12g_m3g_X2_lookups.begin();lookup_it!=_mg_m12g_m3g_X2_lookups.end();lookup_it++){
        delete *lookup_it;
    }
}

double MneuMgM12gM3gX2Lookup::operator()(double * vars){
    double mneu=vars[_array_ids[0]];
    double mg=vars[_array_ids[1]];
    double m12g=vars[_array_ids[2]];
    double m3g=vars[_array_ids[3]];
    //calculate X2
    std::vector<double>::iterator m_it=std::upper_bound(_mneu.begin(),_mneu.end(),mneu);
    double c1_mneu=c1(m_it,mneu);
    double c2_mneu=c2(m_it,mneu);
    int i_mneu=(m_it-_mneu.begin()-1);
    double X2_1=_mg_m12g_m3g_X2_lookups[i_mneu]->get_X2(mg,m12g,m3g);
    double X2_2=_mg_m12g_m3g_X2_lookups[i_mneu+1]->get_X2(mg,m12g,m3g);
    return c1_mneu*X2_1+c2_mneu*X2_2;
}

double c1(std::vector<double>::iterator m_it , double m){
    double m2=*m_it;
    double m1=*(--m_it);
    return 1-(m-m1)/(m2-m1);
}

double c2(std::vector<double>::iterator m_it , double m){
    double m2=*m_it;
    double m1=*(--m_it);
    return (m-m1)/(m2-m1);
}
