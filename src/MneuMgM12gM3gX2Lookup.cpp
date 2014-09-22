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
        if(m_it==m_begin){
            m[i]=*m_begin;
            m_it++;
        } 
        else if (m_it==m_end){
            m[i]=*(--m_end);
            m_it--;
        }
        c[i][0]=c1(m_it,m[i]);
        c[i][1]=c2(m_it,m[i]);
        lower_index[i]=(m_it-m_begin-1);
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
    _default_X2(default_X2),
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
    // mneu & mg: fermion masses can be negative
    double mneu=abs(vars[_array_ids[0]]);
    double mg=abs(vars[_array_ids[1]]);
    double m12g=0, m3g;
    // m12g is the avarage over first 2 generation squark masses
    for (int i=2; i<10; i++){
        m12g+=vars[_array_ids[i]]/8;
    }
    // m3g calculated as "m3g=(4/sum(M**a))**1/a"
    // this is based on the assumption that the xsection scales as 1/M**a
    // hence sum(1/M**a)=4/m3g**a
    double sum_1_over_M_to_a=0;
    double a=8;
    // if stop1 is in the compressed region, apply limit as if the mass was very
    // high
    double  msq3[4];
    for (int i=0; i<4; i++){
        msq3[i] = vars[_array_ids[i+10]];
    }
    if (msq3[0] - mneu < 175)
        msq3[0] = 5000.0;
    for (int i=0; i<4; i++){
        sum_1_over_M_to_a+=pow(msq3[i], -a);
    }
    m3g=pow(4/sum_1_over_M_to_a,1/a);
    //calculate X2
    std::vector<double>::iterator m_begin=_mneu.begin();
    std::vector<double>::iterator m_end=_mneu.end();
    std::vector<double>::iterator m_it=std::upper_bound(m_begin,m_end,mneu);
    bool outside=(m_it==m_begin) || (m_it==m_end);
    double X2;
    if (!outside){
        double c1_mneu=c1(m_it,mneu);
        double c2_mneu=c2(m_it,mneu);
        int i_mneu=(m_it-_mneu.begin()-1);
        double X2_1=_mg_m12g_m3g_X2_lookups[i_mneu]->get_X2(mg,m12g,m3g);
        double X2_2=_mg_m12g_m3g_X2_lookups[i_mneu+1]->get_X2(mg,m12g,m3g);
        X2=c1_mneu*X2_1+c2_mneu*X2_2;
    }
    else{
        X2=_default_X2;
    }
    // add correction
//    std::vector<double> chi2(5), dchi2(5);
//    chi2[0]=0; chi2[1]=1; chi2[2]=4 ; chi2[3]=6; chi2[4]=1000;
//    dchi2[0]=0; dchi2[1]=0.47; dchi2[2]=1.72 ; dchi2[3]=2.41; dchi2[4]=2.41;
//    std::vector<double>::iterator X2_begin=chi2.begin();
//    std::vector<double>::iterator X2_end=chi2.end();
//    std::vector<double>::iterator X2_it=std::upper_bound(X2_begin,X2_end,X2);
//    double c1_X2=c1(X2_it,X2);
//    double c2_X2=c2(X2_it,X2);
//    int index=X2_it-X2_begin-1;
//    double correction=c1_X2*dchi2[index]+c2_X2*dchi2[index+1];
//    return X2-correction;
    return X2;
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
