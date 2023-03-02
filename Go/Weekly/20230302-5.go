package main

import (
	"fmt"
	"sync"
)

func main() {
	var m sync.Mutex
	fmt.Println(111)
	m.Lock()
	m.Lock()
	m.Unlock()
	fmt.Println(222)
}
