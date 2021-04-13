package src

import (
    "database/sql"
    _ "github.com/go-sql-driver/mysql"

)

func SQLConnection() (*sql.DB) {
    con, err := sql.Open("mysql", "chen:12345678@/web")
    if err != nil {panic(err)}
    return con
}
