#ifndef  INC_SPACE_H
#define INC_SPACE_H
#include "Plot.h"
#include "Axis.h"
#include "BaseGetValueFunction.h"
///FIXME: for compatibility we hard code the chi2 lookup using a vars lookup
///FIXME: this should ultimately be deprecated
#include "VarsLookup.h"

class Space{
    public:
        ///first set of axes contains the binned axes for the projection
        ///second set of axes contains the onces that are to be plotted
        Space(std::vector<Axis*>);
        Space(std::vector<Axis*>,BaseGetValueFunction*);
        Space(std::vector<Axis*>,std::vector<Axis*>);
        Space(std::vector<Axis*>,std::vector<Axis*>,BaseGetValueFunction*);
        //FIXME: destructor should delete some things!!!
        ~Space(){};
        //public member functions
        /// THE CRUCIAL FUNCTION
        void update(double*,int);    
        void update(double*,int,double);    
        void print_axes_names();
        void write_plots();
    private:
        //private member functions
        void init_reference_plot(std::vector<Axis*>);
        void init_reference_plot(std::vector<Axis*>,BaseGetValueFunction*);
        void init_entry_plot(std::vector<Axis*>);
        void init_other_plots(std::vector<Axis*>,std::vector<Axis*>);
        //private member objects
        //plots
        Plot* _reference_plot;
        Plot* _entry_plot;
        std::vector<Plot*> _other_plots;
        Axis* _reference_zaxis;
};
#endif
