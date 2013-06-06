#include "Axis.h"


double my_gauss(double * VARS, std::vector<int> * array_ids , GaussData * data){
    double c =VARS[(*array_ids)[0]];
    return (data->mu-c)*(data->mu-c)/data->sigma_square;
} 

int main(){
    std::vector<int> array_ids;
    array_ids.push_back(0);
    double mu=0.;
    std::vector<double> sigmas;
    sigmas.push_back(1.);
    GaussConstraint gauss_constraint(array_ids,  mu,  sigmas , my_gauss);
    double VARS1[]={1.};
    std::cout << "X^2 for 1: "<<gauss_constraint.GetChi2(VARS1) << std::endl;
    double VARS2[]={2.};
    std::cout << "X^2 for 2: "<<gauss_constraint.GetChi2(VARS2) << std::endl;
    Axis axis("constraint",&gauss_constraint);
    std::cout<< "Axis returns for 1: " <<axis.get_value(VARS1)<<std::endl;;
    std::cout<< "Axis returns for 2: " <<axis.get_value(VARS2)<<std::endl;;
    return 0;
}
