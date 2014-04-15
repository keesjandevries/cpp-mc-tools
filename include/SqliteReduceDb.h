#ifndef  INCLUDE_SQLITEREDUCEDB_H_
#define  INCLUDE_SQLITEREDUCEDB_H_
#include <string>
#include <sstream>
#include <iostream>
#include "sqlite3.h"
#include "BaseGetValueFunction.h"
void SqliteReduceDB(const char * input_name, const char * output_name, const char * select_query, 
        int select_query_length, BaseGetValueFunction* chi2_function, double max_chi2 );
#endif
