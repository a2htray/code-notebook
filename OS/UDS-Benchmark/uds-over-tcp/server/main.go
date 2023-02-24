package main

import (
	"log"
	"net"
	"os"
)

var unixSocket = "/tmp/uds-over-tcp.sock"

func main() {
	f, _ := os.Create(unixSocket)

	f.Close()

	listener, err := net.Listen("unix", unixSocket)
	if err != nil {
		log.Fatal(err)
	}
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal(err)
		}

		go func(conn net.Conn) {
			defer conn.Close()

			log.Printf("client address: %s\n", conn.RemoteAddr().String())
			buf := make([]byte, 1024)
			conn.Read(buf)
			conn.Write([]byte("pong"))
		}(conn)

	}
}
