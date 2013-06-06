#include "ContourChi2Functions.h"

std::map< std::string, ContourFunc>  get_ContourFunc_map(){
    std::map< std::string, ContourFunc> ContourFunc_map;
    ContourFunc_map["ma_tanb_mc8"]=ma_tanb_mc8;
    return ContourFunc_map;
}

double ma_tanb_mc8(double * vars, std::vector<int> & array_ids, Contour * ma_tanb_95){
    std::vector<double> obs;
    obs.push_back(vars[array_ids[0]]);
    obs.push_back(vars[array_ids[1]]);
    double ma_point     =ma_tanb_95->GetPointParameter(obs);
    double tanb_point   =ma_tanb_95->GetPointValue(obs);
    double tanb_contour =ma_tanb_95->GetContourValue(ma_point);
    return 4*(tanb_point/tanb_contour)*(tanb_point/tanb_contour);
}
