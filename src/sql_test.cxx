#include <iostream>
#include <stdlib.h>
#include <sqlite3.h>

int main(){
    sqlite3 * conn;
    sqlite3_stmt * res;
    int error = 0;
    int rec_count = 0;
    const char * tail;
    
    error = sqlite3_open("test.db",&conn);
    if (error){
        std::cout << "ERROR: opening file\nExiting" << std::endl;
        exit(1);
    }
    error = sqlite3_prepare(conn,"select * from points ;",1000,&res,&tail);
    if (error != SQLITE_OK){
        std::cout << "ERROR: prepare stament failed\nExiting" << std::endl;
        exit(1);
    }
    while (sqlite3_step(res)==SQLITE_ROW){

    std::cout << "Row: "<< rec_count << " column 0: " <<sqlite3_column_double(res,0) << std::endl;
    rec_count ++;
    }
    return 0;
}

