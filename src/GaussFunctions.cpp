#include "GaussFunctions.h"
std::map<std::string, GaussFunc > get_GaussFunc_map(){
    std::map<std::string, GaussFunc > gaussfunc_map;
    gaussfunc_map["gauss"]=gauss;
    gaussfunc_map["asymmetric_gauss"]=asymmetric_gauss;
    gaussfunc_map["ratio_gauss"]=ratio_gauss;
    gaussfunc_map["R_bsmm_chi2"]=R_bsmm_chi2;
    gaussfunc_map["bsmm_ratio_gauss"]=bsmm_ratio_gauss;
    gaussfunc_map["higgs_gauss"]=higgs_gauss;
    gaussfunc_map["lowerlimit"]=lowerlimit;
    gaussfunc_map["abs_lowerlimit"]=abs_lowerlimit;
    gaussfunc_map["upperlimit"]=upperlimit;
    gaussfunc_map["multi_lowerlimit"]=multi_lowerlimit;
    gaussfunc_map["multi_abs_lowerlimit"]=multi_abs_lowerlimit;
    gaussfunc_map["neutralino_lsp"]=neutralino_lsp;
    return gaussfunc_map;
}

double sum_squares(std::vector<double> sigmas){
    double sum=0;
    std::vector<double>::iterator it;
    for (it=sigmas.begin();it!=sigmas.end();it++){
        sum+=(*it)*(*it);
    }
    return sum;
}

double gauss(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=VARS[array_ids[0]];
    double sigma_squared=sum_squares(data.sigmas);
    return (data.mu-c)*(data.mu-c)/sigma_squared;
} 

double asymmetric_gauss(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=VARS[array_ids[0]];
    double sigma_plus=data.sigmas[0];
    double sigma_min=data.sigmas[1];
    if (c<data.mu)  return (data.mu-c)*(data.mu-c)/(sigma_min*sigma_min);
    if (c>=data.mu)  return (data.mu-c)*(data.mu-c)/(sigma_plus*sigma_plus);
} 

double ratio_gauss(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=VARS[array_ids[0]]/VARS[array_ids[1]];
    double sigma_squared=sum_squares(data.sigmas);
    return (data.mu-c)*(data.mu-c)/sigma_squared;
} 

double bsmm_ratio_gauss(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=VARS[array_ids[0]]/3.46e-9;
    double sigma_squared=sum_squares(data.sigmas);
    return (data.mu-c)*(data.mu-c)/sigma_squared;
} 

double R_bsmm_chi2(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double br=VARS[array_ids[0]]/3.46e-9;
    double mu=data.mu;
    double sigma_plus=std::abs(data.sigmas[0]);
    double sigma_min=std::abs(data.sigmas[1]);
    return 2*pow((mu*sqrt(-(-br/mu+1)*(8*sigma_plus/mu -8*sigma_min/mu)+ 
                    pow((-sigma_plus/mu -sigma_min/mu),2))-sigma_plus-sigma_min),2)/(8*pow((sigma_plus-sigma_min),2));
}

double higgs_gauss(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double mh=VARS[array_ids[0]];
    std::vector<double> sigmas=data.sigmas;
    sigmas.push_back(VARS[array_ids[1]]);
    double sigma_squared=sum_squares(sigmas);
    return (data.mu-mh)*(data.mu-mh)/sigma_squared;
} 

double lowerlimit(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=VARS[array_ids[0]];
    double sigma_squared=sum_squares(data.sigmas);
    if (c<data.mu) return (data.mu-c)*(data.mu-c)/sigma_squared;
    else return 0;
} 

double abs_lowerlimit(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=std::abs(VARS[array_ids[0]]);
    double sigma_squared=sum_squares(data.sigmas);
    if (c<data.mu) return (data.mu-c)*(data.mu-c)/sigma_squared;
    else return 0;
} 

double upperlimit(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double c=VARS[array_ids[0]];
    double sigma_squared=sum_squares(data.sigmas);
    if (c>data.mu) return (data.mu-c)*(data.mu-c)/sigma_squared;
    else return 0;
} 

double multi_lowerlimit(double * vars, std::vector<int> & array_ids , GaussData & data){
    std::vector<int>::iterator it=array_ids.begin();
    //find minimum  
    double min=vars[*it];
    for (;it!=array_ids.end();it++){
        if (vars[*it]<min) min=vars[*it];
    }
    if (min>data.mu) return 0;
    else{ 
        double sigma_squared=sum_squares(data.sigmas);
        return (data.mu-min)*(data.mu-min)/sigma_squared;
    }
}

double multi_abs_lowerlimit(double * vars, std::vector<int> & array_ids , GaussData & data){
    std::vector<int>::iterator it=array_ids.begin();
    //find minimum  
    double min=std::abs(vars[*it]);
    it++;
    for (;it!=array_ids.end();it++){
        if (vars[*it]<min) min=std::abs(vars[*it]);
    }
    if (min>data.mu) return 0;
    else{ 
        double sigma_squared=sum_squares(data.sigmas);
        return (data.mu-min)*(data.mu-min)/sigma_squared;
    }
}

double neutralino_lsp(double * VARS, std::vector<int> & array_ids , GaussData & data){
    double chi2=0;
    std::vector<int>::iterator it=array_ids.begin();
    double mneu=std::abs(VARS[*it]);
    double mass;
    it++;
    for (;it!=array_ids.end();it++){
        mass=std::abs(VARS[*it]);
        if (mass<mneu) chi2+=(mass-mneu)*(mass-mneu);
    }
    return chi2;
}
