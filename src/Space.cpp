#include "Space.h"
Space::Space(std::vector<Axis*> axes){
    init_reference_plot(axes);
    init_entry_plot(axes);
}

Space::Space(std::vector<Axis*> axes,BaseGetValueFunction * reference_function){
    init_reference_plot(axes,reference_function); 
    init_entry_plot(axes);
}

Space::Space(std::vector<Axis*> axes,std::vector<Axis*> zaxes){
    init_reference_plot(axes);
    init_entry_plot(axes);
    init_other_plots(axes,zaxes);
}

Space::Space(std::vector<Axis*> axes,std::vector<Axis*> zaxes,BaseGetValueFunction * reference_function){
    init_reference_plot(axes,reference_function); 
    init_entry_plot(axes);
    init_other_plots(axes,zaxes);
}

void Space::init_reference_plot(std::vector<Axis *> axes){
    /// For compatibility the default reference function is 
    /// the vars lookup at index 0.
    /// Traditionally we minimise chi2 which is stored at index 0.
    VarsLookup * default_reference_function=new VarsLookup(0);
    init_reference_plot(axes,default_reference_function); 
}

void Space::init_reference_plot(std::vector<Axis *> axes, BaseGetValueFunction * reference_function){
    _reference_zaxis = new Axis("chi2",reference_function);
    _reference_plot = new Plot(axes,_reference_zaxis);
    _reference_plot->fill_default(1e9);
}

void Space::init_entry_plot(std::vector<Axis *> axes){
    Axis * entry_zaxis = new Axis("entries" );
    _entry_plot = new Plot(axes,entry_zaxis);
    _entry_plot->fill_default(-1);
}

void Space::init_other_plots(std::vector<Axis *> axes, std::vector<Axis *> zaxes){
    for (std::vector<Axis*>::iterator zaxis_it=zaxes.begin(); zaxis_it!=zaxes.end(); zaxis_it++){
        Plot * plot=new Plot(axes,*zaxis_it);
        _other_plots.push_back(plot);
    }
}

void Space::update(double * VARS, int entry_nr){
    int ibin=_reference_plot->find_bin(VARS);
    double reference=_reference_zaxis->get_value(VARS);
    if(reference<_reference_plot->get_bin_content(ibin)){
        _reference_plot->set_bin_content(ibin,reference);
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
