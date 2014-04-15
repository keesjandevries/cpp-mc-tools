#include "SqliteReduceDb.h"

std::string get_create_table_statement(int ncols){
    //return string  "create table if not exists points(collections_rowid integer, f1 real, ..., f'ncols' real );"
    std::stringstream sql_ss;
    sql_ss << "create table if not exists points(points_rowid integer" ;
    for (int i =0;i<ncols;i++){
        sql_ss << ", f" << i+1 << " real";
    }
    sql_ss << ");" ;
    return sql_ss.str();
}

std::string get_insert_statement(int ncols){
    //return string "INSERT INTO points VALUES (?,?, ...);" with ncols+1 question marks
    std::stringstream insert_sql_ss;
    insert_sql_ss << "insert into points values (?";
    for (int i=0;i<ncols;i++) insert_sql_ss << ",?" ;
    insert_sql_ss  <<  ")";
    return insert_sql_ss.str();
}

void SqliteReduceDB(const char * input_name, const char * output_name, const char * select_query, 
        int select_query_length, BaseGetValueFunction* chi2_function, double max_chi2 ){
    sqlite3 * conn_in;
    sqlite3 * conn_out;
    int error=0;
    //make connections
    if (sqlite3_open(input_name,&conn_in)!=0){ 
        std::cout << "ERROR opening file\nAborting routine" << std::endl;
        sqlite3_close(conn_in);
        return ;
    }
    if (sqlite3_open(output_name,&conn_out)!=0){ 
        std::cout << "ERROR opening file\nAborting routine" << std::endl;
        sqlite3_close(conn_out);
        return ;
    }
    // prepare statement to get the rows from the input file
    const char * tail_in;
    sqlite3_stmt * stmt_in;
    error = sqlite3_prepare(conn_in,select_query,select_query_length,&stmt_in,&tail_in);
    if (error != SQLITE_OK){
        std::cout << "ERROR: prepare stament failed" << std::endl;
        return;
    }
    // variables for retrieving values from the table
    int points_rowid;
    int ncols=sqlite3_column_count(stmt_in);
    double *vars = new double[ncols-2];
    double chi2;
    // counters
    int nrows_in=0;
    int nrows_out=0;
    //create table in output file
    char* errorMessage;
    //sql query for creating table
    const std::string sql_s(get_create_table_statement(ncols));
    const char * sql_c=sql_s.c_str();
    // execute creation of table
    error=sqlite3_exec(conn_out,sql_c, NULL, NULL, &errorMessage);
    if (error!=SQLITE_OK){
        std::cout << "SQL error: " << errorMessage << std::endl;
        std::cout << "returning" << std::endl;
        sqlite3_free(errorMessage);
        sqlite3_close(conn_out);
        return;
    }
    // start transaction
    sqlite3_exec(conn_out, "BEGIN TRANSACTION", NULL, NULL, &errorMessage);
    //sql query for inserting values
    const std::string insert_sql_s(get_insert_statement(ncols));
    const char * insert_sql_c(insert_sql_s.c_str());
    //prepare statement
    sqlite3_stmt* stmt_out;
    sqlite3_prepare(conn_out, insert_sql_c, insert_sql_s.length(), &stmt_out, NULL);
    /// loop over selected rows
    while (sqlite3_step(stmt_in)==SQLITE_ROW){
        if (nrows_in%100000==0) std::cout << "Currently at " << nrows_in << " rows\r" << std::flush;
        ///Get all variables
        points_rowid=sqlite3_column_int(stmt_in,0);
        for (int i=2;i<ncols;i++){ 
            vars[i]=sqlite3_column_double(stmt_in,i);
        }
        ///Calculate chi2 (usually the chi2)
        chi2=(*chi2_function)(vars);
        if (chi2<max_chi2){
            sqlite3_bind_int(stmt_out, 1, points_rowid);
            for (int j=2 ; j<ncols; j++) sqlite3_bind_double(stmt_out, j, vars[j-2]);
         
            int retVal = sqlite3_step(stmt_out);
            if (retVal != SQLITE_DONE)            {
                std::cout << "Commit failed!! : "<< retVal << std::endl;
            }
            sqlite3_reset(stmt_out);
            nrows_out++;
        }
        nrows_in++;
    }
    error=sqlite3_exec(conn_out, "COMMIT TRANSACTION", NULL, NULL, &errorMessage);
    if (error!=SQLITE_OK){
        std::cout << "ERROR: " << errorMessage << std::endl;
    }
    //Finalising statement
    sqlite3_finalize(stmt_in);
    sqlite3_finalize(stmt_out);
    sqlite3_close(conn_in);
    sqlite3_close(conn_out);
    std::cout << "Number of rows processed:            " << nrows_in << std::endl;
    std::cout << "Number of rows passing selection:    " << nrows_out << std::endl;
    delete vars;
}
