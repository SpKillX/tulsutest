package main

import (
    "fmt"
    "net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Сервер на Go.")
}

func main() {
    http.HandleFunc("/hello", helloHandler)
    fmt.Println("Сервер запущен на :8080...")
    http.ListenAndServe(":8080", nil)
}