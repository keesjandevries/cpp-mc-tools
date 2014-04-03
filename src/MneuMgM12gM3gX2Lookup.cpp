#include "MneuMgM12gM3gX2Lookup.h"


MgM12gM3gX2Lookup::MgM12gM3gX2Lookup(double * 3d_masses, int nmg, int nm12g, int nm3g):
    _nmg(nmg), _nm12g(nm12g), _nm3g(nm3g)
{
    std::vector<double> grid_mg(nmg);
    std::vector<double> grid_m12g(nm12g);
    std::vector<double> grid_m3g(nm3g);
    for (int i=0; i<nmg; i++){  
        grid_mg[i]=masses[i*nm12g*nm3g*3+1];
    }
    for (int i=0; i<nm12g; i++){
        grid_m12g[i]=masses[i*nm3g*3+2];
    }
    for (int i=0; i<nm3g; i++){
        grid_m3g[i]=masses[i*3+3];
    }
    _mg_m12g_m3g_ranges.push_back(grid_mg);
    _mg_m12g_m3g_ranges.push_back(grid_m12g);
    _mg_m12g_m3g_ranges.push_back(grid_m3g);
}

MgM12gM3gX2Lookup::get_X2(double mg, double m12g, double m3g){

    // helper variables
    double m[3];
    m[0]=mg; m[1]=m12g; m[2]=m3g;
    int lower_index[3];
    double c[4][2];
    bool outside;
    int i_mg,i_m12g,i_m3g; 
    std::vector<double>::iterator m_it;
    //result
    double X2_interp=0;
    for (int i=0;i<3;i++){
        m_it=std::upper_bound(_mg_m12g_m3g_ranges[i]);
        outside=(m_it==_mg_m12g_m3g_ranges[i].begin()) || (m_it==_mg_m12g_m3g_ranges[i].end());
        if (!outside){
            c[i][0]=c1(m_it,m[i]);
            c[i][1]=c2(m_it,m[i]);
            lower_index[i]=(m_it-_mg_m12g_m3g_ranges[i].begin());
        }
        else{
            //FIXME: remove print statement 
            std::cerr << "m[" << i << "] = " << m[i] << " out of range" << std::endl;
            break;
        }
        //FIXME: remove print statement
        std::cout << "lower_index[" << i << "]: " << lower_index[i] << std::endl; 
    }
    if (outside){
        std::cerr << "one of the masses was outside the ranges\nExiting" <<   std::endl;
        return _default;
    }
    for (int a_mg=0; a_mg<2; a_mg++){
        for (int a_m12g=0; a_m12g<2; a_m12g++){
            for (int a_m3g=0; a_m3g<2; a_m3g++){
                i_mg=lower_index[0]+a_mg; i_m12g=lower_index[0]+a_m12g; i_m3g=lower_index[0]+a_m3g;
                X2_interp+=c[0][a_mg]*c[1][a_m12g]*c[2][a_m3g]*X2[i_mg*nm12g*nm3g+i_m12g*nm3g+i_m3g];
            }
        }
    }
    return X2_interp;  
}

MneuMgM12gM3gX2Lookup::MneuMgM12gM3gX2Lookup(int array_id): 
    _array_id(array_id)
{
    /* intentionally empty */
}

double MneuMgM12gM3gX2Lookup::operator()(double * vars){
    return vars[_array_id];
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
