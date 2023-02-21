package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	conn, err := net.Dial("unix", "/tmp/echo.sock")
	if err != nil {
		panic(err)
	}
	defer conn.Close()

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		os.Exit(-1)
	}()

	for {
		fmt.Println("input text:")
		reader := bufio.NewReader(os.Stdin)
		lineText, err := reader.ReadString('\n')
		if err != nil {
			panic(err)
		}
		conn.Write([]byte(lineText))

		buf := make([]byte, 1024)
		conn.Read(buf)
		fmt.Printf("echo: %s\n", string(buf))
	}
}
