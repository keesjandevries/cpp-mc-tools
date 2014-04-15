#ifndef  INCLUDE_SQLITEREDUCEDB_H_
#define  INCLUDE_SQLITEREDUCEDB_H_
#include <string>
#include <sstream>
#include <iostream>
#include "sqlite3.h"
#include "BaseGetValueFunction.h"
void SqliteReduceDB(const char * input_name, const char * output_name,BaseGetValueFunction* chi2_function );
#endif
