#include <SqliteMakePlots.h>
#include <ctime>

SqliteMakePlots::SqliteMakePlots(const char * filename){
    int error;
    error = sqlite3_open(filename,&_connection);
    if (error){
        std::cout << "ERROR: opening file" << std::endl;
    }
}

void SqliteMakePlots::Run(const char * query, std::vector<Space*> spaces){
    //FIXME: remove, this is only for testing
    clock_t t1,t2,t3;
    /// Prepare sql statement
    int error;
    const char * tail;
    sqlite3_stmt * stmt;
    t1=clock();
    error = sqlite3_prepare(_connection,"select * from points;",1000,&stmt,&tail);
    t2=clock();
    std::cout << "SQL preparation took: " << ((float)(t2-t1))/CLOCKS_PER_SEC << " seconds" << std::endl;

    if (error != SQLITE_OK){
        std::cout << "ERROR: prepare stament failed" << std::endl;
        return;
    }
    /// for retrieving tha vars
    //FIXME: get proper number of columns
    int ncols=2;
    double vars[1000];
    //FIXME: get proper row number
    int row_nr=0;
    /// Space iterator
    std::vector<Space*>::iterator space_it;
    while (sqlite3_step(stmt)==SQLITE_ROW){
        ///Get all variables
        for (int i=0;i<ncols;i++){ 
            vars[i]=sqlite3_column_double(stmt,i);
        }
        ///Update all _spaces: check whether X^2 is lower than existing X^2
        for( space_it=spaces.begin(); space_it!=spaces.end() ; space_it++){
            (*space_it)->update(vars,row_nr);
        }
        row_nr++;
    }
    t3=clock();
    std::cout << "Looping over results took : " << ((float)(t3-t2))/CLOCKS_PER_SEC << " seconds" << std::endl;
    sqlite3_finalize(stmt);
    sqlite3_close(_connection);
    //FIXME: for now use row nr for row counting
    std::cout << "Number of rows processed: " << row_nr << std::endl;
}
