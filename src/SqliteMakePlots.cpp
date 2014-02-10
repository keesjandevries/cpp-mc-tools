#include <SqliteMakePlots.h>

SqliteMakePlots::SqliteMakePlots(const char * filename){
    int error;
    error = sqlite3_open(filename,&_connection);
    if (error){
        std::cout << "ERROR: opening file" << std::endl;
    }
}

void SqliteMakePlots::Run(const char * query,int query_length, std::vector<Space*> spaces, 
        BaseGetValueFunction * reference_function){
    ///FIXME: atm the 'collection_rowid' columns has to be selected. This should be only optional
    /// Prepare sql statement
    int error;
    const char * tail;
    sqlite3_stmt * stmt;
    error = sqlite3_prepare(_connection,query,query_length,&stmt,&tail);
    if (error != SQLITE_OK){
        std::cout << "ERROR: prepare stament failed" << std::endl;
        return;
    }
    /// for retrieving tha vars
    int rowid;
    int ncols=sqlite3_column_count(stmt);
    double *vars = new double[ncols-2];
    /// Space iterator
    std::vector<Space*>::iterator space_it;
    /// some definitions
    int nrows=0, n_chi2_lt_45=0;
    double reference;
    /// loop over selected rows
    while (sqlite3_step(stmt)==SQLITE_ROW){
        if (nrows%100000==0) std::cout << "Currently at " << nrows << " rows\r" << std::flush;
        ///Get all variables
        rowid=sqlite3_column_int(stmt,0);
        for (int i=0;i<ncols-2;i++){ 
            vars[i]=sqlite3_column_double(stmt,i+2);
        }
        ///Calculate reference (usually the chi2)
        reference=(*reference_function)(vars);
        if (reference<45) n_chi2_lt_45++;
        ///Update all _spaces: check whether X^2 is lower than existing X^2
        for( space_it=spaces.begin(); space_it!=spaces.end() ; space_it++){
            (*space_it)->update(vars,rowid,reference);
        }
        nrows++;
    }
    sqlite3_finalize(stmt);
    sqlite3_close(_connection);
    std::cout << "Number of rows processed:       " << nrows << std::endl;
    std::cout << "Number of points with chi2<45 : " << n_chi2_lt_45 << std::endl;
    delete vars;
}
