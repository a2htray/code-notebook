package main

import (
	"fmt"
	"sync"
)

// sync.RWMutex 相较于 sync.Mutex，让开发者能够对内存有更多的控制。
// 只要没有其它 goroutine 对某一资源拥有写锁的情况下，任意数量的 goroutine
// 可以对该资源拥有读锁。

func main() {
	var resource int
	var lock sync.RWMutex
	var wg sync.WaitGroup

	setter := func(wg *sync.WaitGroup) {
		defer wg.Done()
		for i := 0; i < 5; i++ {
			lock.Lock()
			resource = i
			lock.Unlock()
		}
	}

	getter := func(wg *sync.WaitGroup) {
		defer wg.Done()
		fmt.Println(resource)
	}

	wg.Add(1)
	go setter(&wg)

	for i := 0; i < 5; i++ {
		wg.Add(1)
		go getter(&wg)
	}

	wg.Wait()
}
