#include "ContourManager.h"

ContourManager * ContourManager::_instance=NULL;

ContourManager * ContourManager::GetInstance(){
    if (!_instance){
        _instance=new ContourManager;
    }
    return _instance; 
}

void ContourManager::AddContour(const char * name, std::vector<double_pair> coords, const char * type){
    if (_contour_map.find(name)==_contour_map.end()){
        std::string contour_type(type);
        Contour * new_contour=NULL;
        if (contour_type=="default") 
            new_contour=new DefaultContour(coords);
        else if (contour_type=="log_x_log_y") 
            new_contour=new LogXLogYContour(coords);
        else if (contour_type=="universal_limits") 
            new_contour=new UniversalLimitsContour(coords);
        else{
            std::cout << "WARNING: for contour \"" << name << "\" no valid type was specified." << std::endl
                      << "Skipping contour." << std::endl;
            return;
        }
        _contour_map[name]=new_contour;
    }
}

void ContourManager::AddContour(const char * name, double * xs, double * ys, int n_coords, const char * type){
    std::vector<double_pair> coords;
    for (int i=0; i<n_coords; i++){
        coords.push_back(std::make_pair(xs[i],ys[i]));
    }
    AddContour(name,coords,type);
}

Contour * ContourManager::Get(const char * name){
    std::map<std::string,Contour*>::iterator it;
    it=_contour_map.find(name);
    if (it!=_contour_map.end()){
        return it->second;
    }
    else return NULL;
}
