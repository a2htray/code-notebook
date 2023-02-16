package main

import "fmt"

// 函数柯里化
// 把多个参数的函数变换成接受单一参数的函数，并返回接受余下的参数和返回结果的新函数的技术

func add(a, b int) int {
	return a + b
}

func partialAdd(a int) func(int) int {
	return func(b int) int {
		return add(a, b)
	}
}

func main() {
	partialAdd5 := partialAdd(5)
	fmt.Println(partialAdd5(6))

	partialAdd11 := partialAdd(11)
	fmt.Println(partialAdd11(22))
}
