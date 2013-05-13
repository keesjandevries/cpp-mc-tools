#ifndef  INC_PLOT_H
#define INC_PLOT_H
// c++ includes
#include <utility>
// root includes
#include "TH2D.h"
// custom includes
#include "Axis.h"

///Plot is the main class
class Plot{
    public:
        Plot(std::vector<Axis*>,Axis*);
        ~Plot(){};
        //public member functions
        void    fill_default(double);
        int     find_bin(double*);
        void    print_values(double*);
        double  get_bin_content(int);
        void    set_bin_content(int,double*);
        void    set_bin_content(int,double);
        void    print_axes_names();
        void    write();
    private:
        //private member functions
        void init_root_histogram_1d(std::vector<Axis*>,Axis* );
        void init_root_histogram_2d(std::vector<Axis*>,Axis* );
        //private member variables
        int                 _ndim;
        ///case switches determine which one is used
        ///seems a bit retarded, but it is fast enough
        std::pair<TH1D*, TH2D*> _plot;
        std::vector<Axis*>  _axes;
        Axis*               _zaxis;
};
#endif
