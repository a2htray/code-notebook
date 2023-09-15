package main

import (
	"fmt"
	"sync"
	"time"
)

// WaitGroup 用于等待一组 goroutine 的完成，可视为并发安全的 goroutine 计数器
// 适用于主程序不需要老虎 goroutine 结果的场景

func main() {
	var wg sync.WaitGroup

	wg.Add(1)
	go func() {
		defer wg.Done()
		time.Sleep(1)
		fmt.Println("goroutine 1 completed")
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		time.Sleep(1)
		fmt.Println("goroutine 2 completed")
	}()

	// wg.Wait() 会阻塞 main goroutine，直到所有的 goroutine 完成
	wg.Wait()

	fmt.Println("main goroutine completed")
}
