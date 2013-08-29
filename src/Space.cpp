#include "Space.h"
Space::Space(std::vector<Axis*> axes){
    init_reference_plot(axes);
    init_entry_plot(axes);
}

Space::Space(std::vector<Axis*> axes,std::vector<Axis*> zaxes){
    init_reference_plot(axes);
    init_entry_plot(axes);
    init_other_plots(axes,zaxes);
}

void Space::init_reference_plot(std::vector<Axis *> axes){
    _reference_init_default=1e9; //FIXME: global variable here?
    _chi2_index=0;
    Axis * base_chi2_zaxis = new Axis("chi2");
    _reference_plot = new Plot(axes,base_chi2_zaxis);
    _reference_plot->fill_default(_reference_init_default);
}

void Space::init_entry_plot(std::vector<Axis *> axes){
    double _entry_init_default=-1.;// makes sense to have -1 as  marker for invalid entry number
    Axis * entry_zaxis = new Axis("entries" );
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
    int ibin=_reference_plot->find_bin(VARS);
    double chi2=VARS[_chi2_index];
    if(chi2<_reference_plot->get_bin_content(ibin)){
        _reference_plot->set_bin_content(ibin,chi2);
        _entry_plot->set_bin_content(ibin,(double)entry_nr);
        for (std::vector<Plot*>::iterator it=_other_plots.begin(); it!=_other_plots.end(); it++){
            (*it)->set_bin_content(ibin,VARS);
        }
    }
}

void Space::write_plots(){
    _reference_plot->write();
    _entry_plot->write();
    for (std::vector<Plot*>::iterator it=_other_plots.begin(); it!=_other_plots.end(); it++){
        (*it)->write();
    }
}

void Space::print_axes_names(){
    _reference_plot->print_axes_names();
}
