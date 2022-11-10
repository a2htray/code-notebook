package main

import "fmt"

func main() {
	arr := [5]int{1, 2, 3, 4, 5}
	subArr := arr[2:4]

	subArr[0] = 10

	fmt.Println(arr[2])
}
