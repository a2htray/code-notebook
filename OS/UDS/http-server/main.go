package main

import (
	"net"
	"net/http"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	socket, err := net.Listen("unix", "/tmp/http-server.sock")
	if err != nil {
		panic(err)
	}

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		os.Remove("/tmp/http-server.sock")
		os.Exit(-1)
	}()

	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("http server via unix domain socket\n"))
	})

	server := http.Server{
		Addr:    ":8000",
		Handler: mux,
	}
	if err := server.Serve(socket); err != nil {
		panic(err)
	}
}
