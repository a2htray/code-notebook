package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	c := sync.NewCond(&sync.Mutex{})
	queue := make([]int, 0, 10)

	removeFromQueue := func(delay time.Duration) {
		time.Sleep(delay) // 这里延时是为了让 goroutine 在 main goroutine 释放了锁之后才执行
		c.L.Lock()
		queue = queue[1:]
		fmt.Println("remove from queue")
		c.L.Unlock()
		c.Signal()
	}

	for i := 0; i < 10; i++ {
		c.L.Lock()
		for len(queue) == 2 {
			c.Wait() // 程序会阻塞，直到收到 c.Signal() 的信号
		}

		fmt.Println("adding to queue")
		queue = append(queue, i)

		go removeFromQueue(1 * time.Second)
		fmt.Println(queue)
		c.L.Unlock()
	}

}
