package main

import (
	"fmt"
	"net"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	socket, err := net.Listen("unix", "/tmp/echo.sock")
	if err != nil {
		panic(err)
	}

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		os.Remove("/tmp/echo.sock")
		os.Exit(-1)
	}()

	for {
		conn, err := socket.Accept()
		if err != nil {
			panic(err)
		}
		fmt.Println(conn.RemoteAddr(), "connected")

		go func(conn net.Conn) {
			defer func() {
				conn.Close()
				fmt.Println(conn.RemoteAddr(), "closed")
			}()

			buf := make([]byte, 1024)
			n, err := conn.Read(buf)
			if err != nil {
				panic(err)
			}
			_, err = conn.Write(buf[:n])
			if err != nil {
				panic(err)
			}
		}(conn)
	}
}
