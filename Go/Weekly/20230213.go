package main

import "fmt"

func main() {
	a := ['9']int{
		'0': 1,
		'1': 2,
	}
	// 字符 9 对应的 ascii 码为 57
	// 答案是 57
	fmt.Println(len(a))
	fmt.Println(int('9'))
}
