#include "Plot.h"

///FIXME: doing everything with case switched seems a bit dump, but this way we keep the funcitonality within the Plot class
Plot::Plot(std::vector<Axis*> axes,Axis* zaxis){
    //FIXME: for the moment only 2d
    _ndim=axes.size();
    _axes=axes;
    _zaxis=zaxis;
    switch (_ndim){
        case 1:
            init_root_histogram_1d(axes,zaxis);
            break;
        case 2:
            init_root_histogram_2d(axes,zaxis);
            break;
        default:
            std::cout << "ERROR: "<< _ndim << "axes have been provided instead of 1 or 2" << std::endl;
            return;
    }
}

void Plot::init_root_histogram_1d(std::vector<Axis*> axes,Axis* zaxis){
    // Tried to concatenate and turn into c_str() in one go, but didn't work
    if (axes[0]){
        // Prepare name of histogram
        std::string name=axes[0]->get_name()+"_" +zaxis->get_name();
        const char * c_name=name.c_str();
        // Prepare title of histogram
        const char * title= zaxis->get_name().c_str();  //FIXME: not sure yet if this title makes sense
        // Prepare the bin edges
        std::vector<double> x_bin_edges=axes[0]->get_bin_edges();
        int nxbins=x_bin_edges.size()-1;
        double * xbins=new double[nxbins+1];
        for(int i=0; i<nxbins+1;i++)xbins[i]=x_bin_edges[i];
        // Initialise TH1D with these settings
        _plot.first=new TH1D(c_name,title,nxbins,xbins);
        // Set axis title
        const char * axis_name_c=axes[0]->get_name().c_str();
        _plot.first->SetXTitle(axis_name_c);
        delete [] xbins;
    }
    else{
        std::cout << "WARNING: in " << __FUNCTION__ << " line " << __LINE__ << std::endl;
        std::cout << "         axis pointer was empty" << std::endl;
    }
}

void Plot::init_root_histogram_2d(std::vector<Axis*> axes,Axis* zaxis){
    // Tried to concatenate and turn into c_str() in one go, but didn't work
    // Prepare name of histogram
    std::string name=axes[0]->get_name()+"_" +axes[1]->get_name()+"_" +zaxis->get_name();
    const char * c_name=name.c_str();
    // Prepare title of histogram
    const char * title= zaxis->get_name().c_str();  //FIXME: not sure yet if this title makes sense
    // Prepare the bin edges
    std::vector<double> x_bin_edges=axes[0]->get_bin_edges();
    std::vector<double> y_bin_edges=axes[1]->get_bin_edges();
    int nxbins=x_bin_edges.size()-1;
    int nybins=y_bin_edges.size()-1;
    double * xbins=new double[nxbins+1];
    double * ybins=new double[nybins+1];
    for(int i=0; i<nxbins+1;i++)xbins[i]=x_bin_edges[i];
    for(int i=0; i<nybins+1;i++)ybins[i]=y_bin_edges[i];
    // Initialise TH1D with these settings
    _plot.second=new TH2D(c_name,title,nxbins,xbins,nybins,ybins);
    // Set axes titles
    const char * x_axis_name_c=axes[0]->get_name().c_str();
    const char * y_axis_name_c=axes[1]->get_name().c_str();
    _plot.second->SetXTitle(x_axis_name_c);
    _plot.second->SetYTitle(y_axis_name_c);
    delete [] xbins;
    delete [] ybins;
}

void Plot::fill_default(double default_content){
    switch (_ndim){
        case 1:
            for (int i=0;i<_plot.first->fN;i++){
                _plot.first->fArray[i]=default_content;
            }
            return;
        case 2:
            for (int i=0;i<_plot.second->fN;i++){
                _plot.second->fArray[i]=default_content;
            }
            return;
    }
} 

int Plot::find_bin(double * VARS){
    double var1, var2;
    switch (_ndim){
        case 1:
            var1=_axes[0]->get_value(VARS);
            return (_plot.first)->FindBin(var1);
        case 2:
            var1=_axes[0]->get_value(VARS);
            var2=_axes[1]->get_value(VARS);
            return (_plot.second)->FindBin(var1,var2);
    }
}

void Plot::print_axes_names(){
    std::cout << "Axes: " ;
    for (std::vector<Axis*>::iterator it=_axes.begin(); it!=_axes.end() ; it++){
        std::cout << (*it)->get_name() << ", ";
    }
    std::cout << "Axis: " << _zaxis->get_name() << std::endl;
}

void Plot::print_values(double * VARS){
    switch (_ndim){
        case 1:
            std::cout << "X-axis: " << _axes[0]->get_value(VARS) << std::endl;
            return;
        case 2:
            std::cout << "X-axis: " << _axes[0]->get_value(VARS) << "   "
                      << "Y-axis: " << _axes[1]->get_value(VARS) << std::endl;
            return;
    }
}

double Plot::get_bin_content(int ibin){
    switch (_ndim){
        case 1:
            return _plot.first->GetBinContent(ibin);
        case 2:
            return _plot.second->GetBinContent(ibin);
    }
}

void Plot::set_bin_content(int ibin, double * VARS){
    double content=_zaxis->get_value(VARS);
    switch (_ndim){
        case 1:
            _plot.first->SetBinContent(ibin,content);
            return;
        case 2:
            _plot.second->SetBinContent(ibin,content);
            return;
    }
}
void Plot::set_bin_content(int ibin, double  content){
    switch (_ndim){
        case 1:
            _plot.first->SetBinContent(ibin,content);
            return;
        case 2:
            _plot.second->SetBinContent(ibin,content);
            return;
    }
}

void Plot::write(){
    switch (_ndim){
        case 1:
            _plot.first->Write(_plot.first->GetName() ,TObject::kOverwrite);
            return;
        case 2:
            _plot.second->Write(_plot.second->GetName() ,TObject::kOverwrite);
            return;
    }
}
