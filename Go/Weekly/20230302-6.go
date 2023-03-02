package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var m sync.Mutex
	fmt.Println(111)
	m.Lock()

	go func() {
		time.Sleep(2 * time.Microsecond)
		m.Unlock()
	}()

	m.Lock()
	fmt.Println(222)
}
