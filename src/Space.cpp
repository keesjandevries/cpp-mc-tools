#include "Space.h"
Space::Space(std::vector<Axis*> axes){
    init_base_chi2_plot(axes);
    init_entry_plot(axes);
}

Space::Space(std::vector<Axis*> axes,std::vector<Axis*> zaxes){
    init_base_chi2_plot(axes);
    init_entry_plot(axes);
    init_other_plots(axes,zaxes);
}

void Space::init_base_chi2_plot(std::vector<Axis *> axes){
    _chi2_init_default=1e9; //FIXME: global variable here?
    _chi2_index=0;
    std::string chi2_name="chi2";
    Axis * base_chi2_zaxis = new Axis(chi2_name, _chi2_index );
    _base_chi2_plot = new Plot(axes,base_chi2_zaxis);
    _base_chi2_plot->fill_default(_chi2_init_default);
}

void Space::init_entry_plot(std::vector<Axis *> axes){
    double _entry_init_default=-1.;// makes sense to have -1 as  marker for invalid entry number
    int entry_index=-1; //NOTE: Dummy, because entries has no lookup 
    std::string entry_name="entries";
    Axis * entry_zaxis = new Axis(entry_name, entry_index );
    _entry_plot = new Plot(axes,entry_zaxis);
    _entry_plot->fill_default(_entry_init_default);
}

void Space::init_other_plots(std::vector<Axis *> axes, std::vector<Axis *> zaxes){
    for (std::vector<Axis*>::iterator zaxis_it=zaxes.begin(); zaxis_it!=zaxes.end(); zaxis_it++){
        Plot * plot=new Plot(axes,*zaxis_it);
        _other_plots.push_back(plot);
    }
}

void Space::update(double * VARS, int entry_nr){
    int ibin=_base_chi2_plot->find_bin(VARS);
    double chi2=VARS[_chi2_index];
    if(chi2<_base_chi2_plot->get_bin_content(ibin)){
        _base_chi2_plot->set_bin_content(ibin,chi2);
        _entry_plot->set_bin_content(ibin,(double)entry_nr);
        for (std::vector<Plot*>::iterator it=_other_plots.begin(); it!=_other_plots.end(); it++){
            (*it)->set_bin_content(ibin,VARS);
        }
    }
}

void Space::write_plots(){
    _base_chi2_plot->write();
    _entry_plot->write();
    for (std::vector<Plot*>::iterator it=_other_plots.begin(); it!=_other_plots.end(); it++){
        (*it)->write();
    }
}

void Space::print_axes_names(){
    _base_chi2_plot->print_axes_names();
}
