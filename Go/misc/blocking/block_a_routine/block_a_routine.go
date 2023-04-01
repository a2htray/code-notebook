package main

import (
	"fmt"
	"time"
)

func main() {
	stopChan := make(chan struct{})
	go func() {
		for {
			time.Sleep(time.Second * 2)
			fmt.Println("hello world")
		}
	}()
	<-stopChan
}
