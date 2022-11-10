package main

import (
	"fmt"
	"time"
)

func runLoopSend(n int, ch chan int) {
	for i := 0; i < n; i++ {
		ch <- i
	}
	close(ch)
}

func runLoopReceive(ch chan int) {
	for {
		i, ok := <-ch
		if !ok {
			break
		}
		fmt.Println(i)
	}
}

func main() {
	ch := make(chan int)
	go runLoopSend(10, ch)
	go runLoopReceive(ch)

	time.Sleep(2 * time.Second)
}
