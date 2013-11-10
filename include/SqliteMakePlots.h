#include <iostream>
#include <sqlite3.h>
#include "Space.h"

class SqliteMakePlots {
    public:
        SqliteMakePlots(){};
        SqliteMakePlots(const char * filename);
        ~SqliteMakePlots(){};
        void Run(const char *,int, std::vector<Space*> );
    private:
        sqlite3 * _connection;
};
