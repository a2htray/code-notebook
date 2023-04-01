package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	wg := sync.WaitGroup{}
	wg.Add(1)
	go func() {
		for {
			time.Sleep(time.Second * 2)
			fmt.Println("hello world")
		}
	}()
	wg.Wait()
}
