#ifndef  INC_SPACE_H
#define INC_SPACE_H
#include "Plot.h"
#include "Axis.h"

class Space{
    public:
        ///first set of axes contains the binned axes for the projection
        ///second set of axes contains the onces that are to be plotted
        Space(std::vector<Axis*> axes);
        Space(std::vector<Axis*> axes, std::vector<Axis*>);
        ~Space(){};
        //public member functions
        /// THE CRUCIAL FUNCTION
        void update(double*,int);    
        void print_axes_names();
        void write_plots();
    private:
        //private member functions
        void init_base_chi2_plot(std::vector<Axis*>);
        void init_entry_plot(std::vector<Axis*>);
        void init_other_plots(std::vector<Axis*>,std::vector<Axis*>);
        //private member objects
        Plot*               _base_chi2_plot;
        Plot*               _entry_plot;
        std::vector<Plot*>  _other_plots;
        int _chi2_index;  
        double _chi2_init_default;
        double _entry_init_default;
};
#endif
