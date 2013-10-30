#ifndef  INCLUDE_SQLITEINSERTER_H_
#define  INCLUDE_SQLITEINSERTER_H_
#include <string>
#include <sstream>
#include <iostream>
#include "sqlite3.h"
#include "TFile.h"
#include "TTree.h"
#include "TLeaf.h"

void InsertRootIntoSqlite(const char *, const char *, int);

#endif
