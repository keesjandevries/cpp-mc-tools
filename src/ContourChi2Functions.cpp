#include "ContourChi2Functions.h"

std::map< std::string, ContourFunc>  get_ContourFunc_map(){
    std::map< std::string, ContourFunc> ContourFunc_map;
    ContourFunc_map["ma_tanb_mc8"]=ma_tanb_mc8;
    ContourFunc_map["xenon100_mc8"]=xenon100_mc8;
    return ContourFunc_map;
}

double ma_tanb_mc8(double * vars, std::vector<int> & array_ids, Contour * ma_tanb_95){
    double_pair point(vars[array_ids[0]],vars[array_ids[1]]);
    double ma_point     =ma_tanb_95->GetPointParameter(point);
    double tanb_point   =ma_tanb_95->GetPointValue(point);
    double tanb_contour =ma_tanb_95->GetContourValue(ma_point);
    return 4*(tanb_point/tanb_contour)*(tanb_point/tanb_contour);
}


double xenon100_mc8(double * vars, std::vector<int> & array_ids, Contour * xenon100_contour){
    // standard: create point
    double_pair point(vars[array_ids[0]],vars[array_ids[1]]);
    double mneu_point = xenon100_contour->GetPointParameter(point);
    double sigma_p_si_point = xenon100_contour->GetPointValue(point);
    double sigma_p_si_contour = xenon100_contour->GetContourValue(mneu_point);
    //number of events
    double N=(sigma_p_si_point/sigma_p_si_contour)*5.1;
    //
    double mu=1., sigma=2.7;
    return (mu-N)*(mu-N)/(sigma*sigma);
}
