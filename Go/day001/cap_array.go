package main

import "fmt"

func main() {
	arr := [3]int{1, 2, 3}
	fmt.Println(cap(arr), len(arr))
}
