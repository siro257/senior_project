package main

import (
    "fmt"
    "log"
    "net/http"
    "strconv"
    "database/sql"
    "../src"
    "encoding/json"
    "github.com/gomodule/redigo/redis"
)
var mysql = src.SQLConnection()
var rediscon = src.RedisConnection()

func handler(w http.ResponseWriter, r *http.Request) {
    var user_id int
    var username string
    var gender string
    var email string
    type User struct {
    	Username string
    	Gender string
    	Email string
    }
    
    userids, ok := r.URL.Query()["gouserid"]
    if !ok || len(userids[0]) < 1 {
        fmt.Println("No input")
        return
    }
    var userid string
    userid = userids[0]
    input, err := strconv.Atoi(userid)
    if err != nil {
        panic(err)
    }
    
    id := mysql.QueryRow("SELECT * FROM user WHERE user_id=?", input)
    switch err := id.Scan(&user_id, &username, &gender, &email); err {
	case sql.ErrNoRows:
  	    fmt.Println("No rows were returned!")
	case nil:
	    if_exist, err := redis.Int(rediscon.Do("EXISTS", userid))
	    fmt.Println(if_exist)
	    if err != nil {fmt.Println("redis error")}
	    if if_exist == 1{
	        fmt.Println("Found the key in redis.")
	    	output, err := rediscon.Do("GET", userid)
	    	if err != nil {log.Fatal(err)}
	    	var o User
	    	bytes, _ := output.([]byte)
	    	erro := json.Unmarshal(bytes, &o)
	    	if erro != nil {
		    panic(err)
	        }
	    	fmt.Println("Username: " + o.Username + ", Gender: " + o.Gender + ", Email: " + o.Email)
	    } else {
	        fmt.Println("Didn't find the key in redis. Will insert key.")
	        output := User {
	        	Username: username,
	        	Gender: gender,
	        	Email: email,
	        }
	        o, err:= json.Marshal(output)
	        if err != nil {
		    fmt.Println("error:", err)
	        }
	        fmt.Println("Username: " + username + ", Gender: " + gender + ", Email: " + email)
  	        rediscon.Do("SET", userid, o)
  	    }
	default:
  	    panic(err)
    }
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}

