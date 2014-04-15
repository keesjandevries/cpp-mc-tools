#include "SqliteInserter.h"

namespace SqliteInserter{
    std::string get_create_table_statement(int nvars){
        //return string  "create table if not exists points(collections_rowid integer, f1 real, ..., f'nvars' real );"
        std::stringstream sql_ss;
        sql_ss << "create table if not exists points(collections_rowid integer" ;
        for (int i =0;i<nvars;i++){
            sql_ss << ", f" << i+1 << " real";
        }
        sql_ss << ");" ;
        return sql_ss.str();
    }
    std::string get_insert_statement(int nvars){
        //return string "INSERT INTO points VALUES (?,?, ...);" with nvars+1 question marks
        std::stringstream insert_sql_ss;
        insert_sql_ss << "insert into points values (?";
        for (int i=0;i<nvars;i++) insert_sql_ss << ",?" ;
        insert_sql_ss  <<  ")";
        return insert_sql_ss.str();
    }
}

void InsertRootIntoSqlite(const char * root_file_name, const char * sqlite_db, int collection_rowid){
    // define and open connection
    sqlite3 * conn;
    int error=0;
    if (sqlite3_open(sqlite_db,&conn)!=0){ 
        std::cout << "ERROR opening file\nAborting routine" << std::endl;
        sqlite3_close(conn);
        return ;
    }
       
    //root stuff: opening a 
    TFile root_file(root_file_name);
    TTree * tree;
    if(root_file.Get("tree")){
        tree=(TTree*)(root_file.Get("tree"));
    }
    else {
        std::cout << "tree not found in \"" << root_file_name << "\""<< std::endl;
        root_file.Close();
        sqlite3_close(conn);
        return;
    }
    int nvars;
    if (tree->GetLeaf("vars")){
        nvars=tree->GetLeaf("vars")->GetLen();
    }
    else{
        std::cout << "vars not found in \"" << root_file_name << "\"" << std::endl;
        root_file.Close();
        sqlite3_close(conn);
        return;
    }
    double * vars=new double[nvars];
    tree->SetBranchAddress("vars",vars);
    int nentries = tree->GetEntries();

    //prepare sqlite stuff
    char* errorMessage;
    //sql query for creating table
    const std::string sql_s(SqliteInserter::get_create_table_statement(nvars));
    const char * sql_c=sql_s.c_str();
    // execute creation of table
    error=sqlite3_exec(conn,sql_c, NULL, NULL, &errorMessage);
    if (error!=SQLITE_OK){
        std::cout << "SQL error: " << errorMessage << std::endl;
        std::cout << "returning" << std::endl;
        sqlite3_free(errorMessage);
        root_file.Close();
        sqlite3_close(conn);
        return;
    }

    // start transaction
    sqlite3_exec(conn, "BEGIN TRANSACTION", NULL, NULL, &errorMessage);
    //sql query for inserting values
    const std::string insert_sql_s(SqliteInserter::get_insert_statement(nvars));
    const char * insert_sql_c(insert_sql_s.c_str());
    //prepare statement
    sqlite3_stmt* stmt;
    sqlite3_prepare(conn, insert_sql_c, insert_sql_s.length(), &stmt, NULL);
    //loop over enties of the root file
    std::cout << "Inserting " << nentries << " entries from \"" << root_file_name << "\" into \""
        << sqlite_db << "\""<<  std::endl; 
    for (int i = 0; i < nentries; i++)
    {
        if (nentries>100000 && i%100000 == 0) std::cout << "    inserted " << i << " rows " << std::endl;
        tree->GetEntry(i);
        sqlite3_bind_int(stmt, 1, collection_rowid);
        for (int j=0 ; j<nvars; j++) sqlite3_bind_double(stmt, j+2, vars[j]);
     
        int retVal = sqlite3_step(stmt);
        if (retVal != SQLITE_DONE)
        {
            std::cout << "Commit failed!! : "<< retVal << std::endl;
        }
        sqlite3_reset(stmt);
    }
     
    error=sqlite3_exec(conn, "COMMIT TRANSACTION", NULL, NULL, &errorMessage);
    if (error!=SQLITE_OK){
        std::cout << "ERROR: " << errorMessage << std::endl;
    }
    //Finalising statement
    sqlite3_finalize(stmt);

    //Close connection and root file
    root_file.Close();
    sqlite3_close(conn);
}
