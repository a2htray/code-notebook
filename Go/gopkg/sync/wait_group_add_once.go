package main

import (
	"fmt"
	"sync"
)

// 只调用一次 wg.Add 的使用
func main() {
	var wg sync.WaitGroup
	run := func(wg *sync.WaitGroup, id int) {
		defer wg.Done()
		fmt.Printf("run %d\n", id)
	}
	
	numOfRun := 10
	wg.Add(numOfRun)

	for i := 0; i < numOfRun; i++ {
		go run(&wg, i)
	}

	wg.Wait()
	fmt.Println("main goroutine completed")
}
