package main

import "fmt"

func passSlice(arg []int) {
	fmt.Printf("%p\n", arg)
	arg[1] = 1
}

func passArray(arg [2]int) {
	fmt.Printf("%p\n", &arg)
	arg[1] = 1
}

func passMap(arg map[int]int) {
	fmt.Printf("%p\n", arg)
	arg[2] = 1
}

func main() {
	argSlice := []int{1, 2}
	argArray := [2]int{1, 2}
	argMap := map[int]int{1: 2}

	fmt.Printf("slice address: %p\n", argSlice)
	fmt.Printf("array address: %p\n", &argArray)
	fmt.Printf("map address: %p\n", argMap)

	passSlice(argSlice)
	passArray(argArray)
	passMap(argMap)

	fmt.Println(argSlice)
	fmt.Println(argArray)
	fmt.Println(argMap)
}
