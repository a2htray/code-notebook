package main

import (
	"fmt"
	"math/rand"
	"time"
)

/*
 * 随机排列 slice 中的元素
 */

func Shuffle[V any](values []V) {
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(values), func(i, j int) {
		values[i], values[j] = values[j], values[i]
	})
}

func main() {
	values1 := []string{"1", "2", "3", "4"}
	Shuffle(values1)
	fmt.Println(values1)

	value2 := []int{1, 2, 3, 4}
	Shuffle(value2)
	fmt.Println(value2)
}
