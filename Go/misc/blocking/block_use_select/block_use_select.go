package main

import (
	"fmt"
	"time"
)

func blockForever() {
	select {}
}

func main() {
	go func() {
		for {
			time.Sleep(time.Second * 2)
			fmt.Println("hello world")
		}
	}()
	blockForever()
}
