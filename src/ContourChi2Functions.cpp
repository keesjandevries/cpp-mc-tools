#include "ContourChi2Functions.h"

std::map< std::string, ContourFunc>  get_ContourFunc_map(){
    std::map< std::string, ContourFunc> ContourFunc_map;
    ContourFunc_map["mc8_ma_tanb"]=mc8_ma_tanb;
    ContourFunc_map["xenon100_jul_2012"]=xenon100_jul_2012;
    ContourFunc_map["xenon100_jul_2012_Sigma_pi_N_unc"]=xenon100_jul_2012_Sigma_pi_N_unc;
    ContourFunc_map["xenon100_Jul12_90CL_ssi_unc"]=xenon100_Jul12_90CL_ssi_unc;
    ContourFunc_map["lux131030_90CL"]=lux131030_90CL;
    ContourFunc_map["lux131030_90CL_ssi_unc"]=lux131030_90CL_ssi_unc;
    ContourFunc_map["m0_m12_power_4"]=m0_m12_power_4;
    ContourFunc_map["one_dim_chi2_lookup"]=one_dim_chi2_lookup;
//    ContourFunc_map["universal_limits"]=universal_limits;
//    ContourFunc_map["m3g_universal_limits"]=m3g_universal_limits;
//    ContourFunc_map["mg_universal_limits"]=mg_universal_limits;
    return ContourFunc_map;
}

double mc8_ma_tanb(double * vars, std::vector<int> & array_ids, std::vector<Contour*> & contours){
    Contour *  ma_tanb_95=contours[0];
    double ma=vars[array_ids[0]];
    double tanb=vars[array_ids[1]];
    double tanb_contour=ma_tanb_95->GetContourValue(ma);
    double largest_ma= ma_tanb_95->GetCoordinatesParameters().back();
    if (ma<largest_ma)  return 5.99146*(tanb/tanb_contour)*(tanb/tanb_contour);
    else return 0;
}

double xenon100_jul_2012(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    //NOTE: this is the old implementation that should be multiplied by 4.61/2.71
    //it is only kept for compatibility purposes 
    Contour * xenon100_contour=contours[0];
    double mneu=vars[array_ids[0]];
    double sigma_p_si=vars[array_ids[1]];
    double sigma_p_si_contour=xenon100_contour->GetContourValue(mneu);
    //number of events
    double N=(sigma_p_si/sigma_p_si_contour)*5.1;
    double mu=1., sigma=2.7;
    return (mu-N)*(mu-N)/(sigma*sigma);
}

double xenon100_jul_2012_Sigma_pi_N_unc(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    //NOTE: this is the old implementation that should be multiplied by 4.61/2.71
    //it is only kept for compatibility purposes 
    Contour * xenon100_contour=contours[0];
    double mneu=vars[array_ids[0]];
    double sigma_p_si=vars[array_ids[1]];
    double D_sigma_p_si=vars[array_ids[2]];
    double sigma_p_si_contour=xenon100_contour->GetContourValue(mneu);
    //number of events
    double N=(sigma_p_si/sigma_p_si_contour)*5.1;
    double D_N=(D_sigma_p_si/sigma_p_si_contour)*5.1;
    double mu=1., sigma=2.7;
    return (mu-N)*(mu-N)/(sigma*sigma+D_N*D_N);
}

double xenon100_Jul12_90CL_ssi_unc(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    //NOTE: this is the old implementation that should be multiplied by 4.61/2.71
    //it is only kept for compatibility purposes 
    Contour * xenon100_contour=contours[0];
    double mneu=vars[array_ids[0]];
    double sigma_p_si=vars[array_ids[1]];
    double D_sigma_p_si=vars[array_ids[2]];
    double sigma_p_si_contour=xenon100_contour->GetContourValue(mneu);
    //number of events
    double N=(sigma_p_si/sigma_p_si_contour)*5.1;
    double D_N=(D_sigma_p_si/sigma_p_si_contour)*5.1;
    double mu=1., sigma=2.7;
    return (4.61/2.71)*(mu-N)*(mu-N)/(sigma*sigma+D_N*D_N);
}

double lux131030_90CL(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    Contour * lux_contour=contours[0];
    double mneu=vars[array_ids[0]];
    double sigma_p_si=vars[array_ids[1]];
    double sigma_p_si_contour=lux_contour->GetContourValue(mneu);
    //number of events
    double N=(sigma_p_si/sigma_p_si_contour)*4.6;
    double mu=0.5, sigma=2.5;
    //multiply by correction factor that transforms 1-d 90CL to 2-d 90CL
    //(numbers are taken from table 36.2 in pdg.lbl.gov/2013/reviews/rpp2012-rev-statistics.pdf)
    return (4.61/2.71)*(mu-N)*(mu-N)/(sigma*sigma);
}

double lux131030_90CL_ssi_unc(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
    Contour * lux_contour=contours[0];
    double mneu=vars[array_ids[0]];
    double sigma_p_si=vars[array_ids[1]];
    double D_sigma_p_si=vars[array_ids[2]];
    double sigma_p_si_contour=(lux_contour->GetContourValue(mneu));
    //number of events
    double N=(sigma_p_si/sigma_p_si_contour)*4.6;
    double D_N=(D_sigma_p_si/sigma_p_si_contour)*4.6;
    double mu=0.5, sigma=2.5;
    //multiply by correction factor that transforms 1-d 90CL to 2-d 90CL
    //(numbers are taken from table 36.2 in pdg.lbl.gov/2013/reviews/rpp2012-rev-statistics.pdf)
    return (4.61/2.71)*(mu-N)*(mu-N)/(sigma*sigma+D_N*D_N);
}

double m0_m12_power_4(double * vars, std::vector<int> & array_ids, std::vector<Contour*> & contours){
    Contour * m0_m12_contour=contours[0];
    double m0=vars[array_ids[0]];
    double m12=vars[array_ids[1]];
    double_pair point(m0,m12);
    double theta=m0_m12_contour->GetPointParameter(point);
    double r=m0_m12_contour->GetPointValue(point);
    double r_contour=m0_m12_contour->GetContourValue(theta);
    return 5.99146*pow(r_contour/r,4);
}

double one_dim_chi2_lookup(double * vars, std::vector<int> & array_ids, std::vector<Contour*> & contours){
    Contour * contour=contours[0];
    return contour->GetContourValue(vars[array_ids[0]]);
}
//double universal_limits(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
//    Contour * neutralino_gluino=contours[0];
//    Contour * neutralino_3g_squark=contours[1];
//    // neutralino mass: take absolute value (needs to be tested!!!)
//    double mneu=std::abs(vars[array_ids[0]]);
//    // gluino mass
//    double mg=vars[array_ids[1]];
//    // 3rd generation squark masses
//    double msb1=vars[array_ids[2]];
//    double msb2=vars[array_ids[3]];
//    double mst1=vars[array_ids[4]];
//    double mst2=vars[array_ids[5]];
//    // average 3rd generation squark mass
//    double m3g= (msb1+msb2+mst1+mst2)/4;
//    // contour values
//    double mg_contour=neutralino_gluino->GetContourValue(mneu);
//    double m3g_contour=neutralino_3g_squark->GetContourValue(mneu);
//    return 7.82/sqrt(2)*sqrt(pow((m3g_contour/m3g),8)+pow((mg_contour/mg),8));
//}
//
//double m3g_universal_limits(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
//    Contour * neutralino_3g_squark=contours[0];
//    // neutralino mass: take absolute value (needs to be tested!!!)
//    double mneu=std::abs(vars[array_ids[0]]);
//    // 3rd generation squark masses
//    double msb1=vars[array_ids[1]];
//    double msb2=vars[array_ids[2]];
//    double mst1=vars[array_ids[3]];
//    double mst2=vars[array_ids[4]];
//    // average 3rd generation squark mass
//    double m3g= (msb1+msb2+mst1+mst2)/4;
//    // contour values
//    double m3g_contour=neutralino_3g_squark->GetContourValue(mneu);
//    return 7.82/sqrt(2)*pow((m3g_contour/m3g),4);
//}
//
//double mg_universal_limits(double * vars, std::vector<int> & array_ids,std::vector<Contour *> & contours) {
//    Contour * neutralino_gluino=contours[0];
//    // neutralino mass: take absolute value (needs to be tested!!!)
//    double mneu=std::abs(vars[array_ids[0]]);
//    // gluino mass
//    double mg=vars[array_ids[1]];
//    // contour values
//    double mg_contour=neutralino_gluino->GetContourValue(mneu);
//    return 7.82/sqrt(2)*pow((mg_contour/mg),4);
//}
