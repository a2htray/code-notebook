package main

import (
	"log"
	"net/http"
	"os"
)

func main() {
	logFile, err := os.OpenFile("/var/log/app.log", os.O_CREATE|os.O_APPEND|os.O_RDWR, 0777)
	if err != nil {
		log.Fatal(err)
	}
	defer logFile.Close()

	http.HandleFunc("/hello-world", func(w http.ResponseWriter, r *http.Request) {
		logFile.WriteString("request arrived\n")
		w.Write([]byte("hello world"))
	})

	log.Fatal(http.ListenAndServe(":8000", nil))
}
