#include "ContourChi2Functions.h"

std::map< std::string, ContourFunc>  get_ContourFunc_map(){
    std::map< std::string, ContourFunc> ContourFunc_map;
    ContourFunc_map["ma_tanb_mc8"]=ma_tanb_mc8;
    ContourFunc_map["xenon100_mc8"]=xenon100_mc8;
    ContourFunc_map["universal_limits"]=universal_limits;
    ContourFunc_map["m3g_universal_limits"]=m3g_universal_limits;
    ContourFunc_map["mg_universal_limits"]=mg_universal_limits;
    return ContourFunc_map;
}

double ma_tanb_mc8(double * vars, std::vector<int> & array_ids, std::vector<Contour*> & contours){
    Contour *  ma_tanb_95=contours[0];
    double ma_point=vars[array_ids[0]];
    double tanb_point=vars[array_ids[1]];
    double tanb_contour=ma_tanb_95->GetContourValue(ma_point);
    return 4*(tanb_point/tanb_contour)*(tanb_point/tanb_contour);
}

double xenon100_mc8(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    Contour * xenon100_contour=contours[0];
    double mneu_point=vars[array_ids[0]];
    double sigma_p_si_point=vars[array_ids[1]];
    double sigma_p_si_contour=xenon100_contour->GetContourValue(mneu_point);
    //number of events
    double N=(sigma_p_si_point/sigma_p_si_contour)*5.1;
    double mu=1., sigma=2.7;
    return (mu-N)*(mu-N)/(sigma*sigma);
}

double universal_limits(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    Contour * neutralino_gluino=contours[0];
    Contour * neutralino_3g_squark=contours[1];
    // neutralino mass: take absolute value (needs to be tested!!!)
    double mneu=std::abs(vars[array_ids[0]]);
    // gluino mass
    double mg=vars[array_ids[1]];
    // 3rd generation squark masses
    double msb1=vars[array_ids[2]];
    double msb2=vars[array_ids[3]];
    double mst1=vars[array_ids[4]];
    double mst2=vars[array_ids[5]];
    // average 3rd generation squark mass
    double m3g= (msb1+msb2+mst1+mst2)/4;
    // contour values
    double mg_contour=neutralino_gluino->GetContourValue(mneu);
    double m3g_contour=neutralino_3g_squark->GetContourValue(mneu);
    return 7.82/sqrt(2)*sqrt(pow((m3g_contour/m3g),8)+pow((mg_contour/mg),8));
}

double m3g_universal_limits(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    Contour * neutralino_3g_squark=contours[0];
    // neutralino mass: take absolute value (needs to be tested!!!)
    double mneu=std::abs(vars[array_ids[0]]);
    // 3rd generation squark masses
    double msb1=vars[array_ids[1]];
    double msb2=vars[array_ids[2]];
    double mst1=vars[array_ids[3]];
    double mst2=vars[array_ids[4]];
    // average 3rd generation squark mass
    double m3g= (msb1+msb2+mst1+mst2)/4;
    // contour values
    double m3g_contour=neutralino_3g_squark->GetContourValue(mneu);
    return 7.82/sqrt(2)*pow((m3g_contour/m3g),4);
}

double mg_universal_limits(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    Contour * neutralino_gluino=contours[0];
    // neutralino mass: take absolute value (needs to be tested!!!)
    double mneu=std::abs(vars[array_ids[0]]);
    // gluino mass
    double mg=vars[array_ids[1]];
    // contour values
    double mg_contour=neutralino_gluino->GetContourValue(mneu);
    return 7.82/sqrt(2)*pow((mg_contour/mg),4);
}
