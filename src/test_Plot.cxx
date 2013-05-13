#include<iostream>

#include "Plot.h"
#include "Axis.h"

int main(){
    //make m0, m12 Axis
    std::string m0_name("m0");
    std::string m12_name("m12");
    std::string chi2_name("chi2");
    //bining in puts
    BinningInputs my_binning;
    my_binning.binning_type="linear";
    my_binning.low=0.;
    my_binning.high=4000.;
    my_binning.nbins=100;
    //array int
    int m0_id=1;
    int m12_id=2;
    int chi2_id=0;
    //make pointers to Axex
    Axis * m0_axis=new Axis(m0_name,my_binning,m0_id );
    Axis * m12_axis=new Axis(m12_name,my_binning,m12_id );
    Axis * chi2_axis=new Axis(chi2_name,chi2_id );
    //initialise plot
    std::vector<Axis*> m0m12;
    m0m12.push_back(m0_axis);
    m0m12.push_back(m12_axis);
    Plot * my_plot=new Plot(m0m12,chi2_axis);
    return 0;
}
