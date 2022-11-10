package main

import "fmt"

func main() {
	srcSlice := []int{1, 2, 3, 4}
	dstSlice := make([]int, 2)

	copy(dstSlice, srcSlice)
	fmt.Println(dstSlice[0], dstSlice[1])

	dstSlice2 := make([]int, 2, 3) // 以目标 slice 的长度为准
	copy(dstSlice2, srcSlice)
	fmt.Println(dstSlice2)
}
