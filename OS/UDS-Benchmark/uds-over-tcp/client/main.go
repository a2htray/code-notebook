package main

import (
	"flag"
	"fmt"
	"log"
	"net"
	"time"
)

func parseArgs() (int, int) {
	numCoroutine := flag.Int("coroutine", 1, "number of coroutine")
	pingPerCoroutine := flag.Int("ping-n", 10, "number of each coroutine ping")
	flag.Parse()
	return *numCoroutine, *pingPerCoroutine
}

var unixSocket = "/tmp/uds-over-tcp.sock"

func main() {
	numCoroutine, pingPerCoroutine := parseArgs()
	costChan := make(chan time.Duration, numCoroutine)

	for i := 0; i < numCoroutine; i++ {
		go func(c chan time.Duration) {
			startTime := time.Now()
			conn, err := net.Dial("unix", unixSocket)
			if err != nil {
				log.Fatal(err)
			}
			defer conn.Close()

			buf := make([]byte, 1024)
			for j := 0; j < pingPerCoroutine; j++ {
				conn.Write([]byte("ping"))
				_, _ = conn.Read(buf)
			}
			c <- time.Now().Sub(startTime)
		}(costChan)
	}

	for i := 0; i < numCoroutine; i++ {
		costTime := <-costChan
		fmt.Printf("coroutine %02d cost: %d\nus", i, costTime.Microseconds())
	}
}
