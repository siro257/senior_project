package src

import (
    "log"
    "github.com/gomodule/redigo/redis"
)

func RedisConnection() (redis.Conn) {
    con, err := redis.Dial("tcp", "localhost:6379")
    if err != nil {log.Fatal(err)}
    return con
}
