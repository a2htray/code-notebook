package main

import (
	"fmt"
	"time"
)

func main() {
	go func() {
		sum := 0
		for i := 0; i < 1000000; i++ {
			sum += i
		}
		fmt.Println(sum)
	}()

	time.Sleep(5 * time.Second)
}
