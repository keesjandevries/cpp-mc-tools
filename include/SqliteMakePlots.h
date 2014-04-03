#ifndef INC_SQLITEMAKEPLOTS_H
#define INC_SQLITEMAKEPLOTS_H
#include <iostream>
#include <sqlite3.h>
#include "BaseGetValueFunction.h"
#include "Space.h"

class SqliteMakePlots {
    public:
        SqliteMakePlots(){};
        SqliteMakePlots(const char * filename);
        ~SqliteMakePlots(){};
        void Run(const char *,int, std::vector<Space*>, BaseGetValueFunction * );
    private:
        sqlite3 * _connection;
};
#endif // INC_SQLITEMAKEPLOTS_H
