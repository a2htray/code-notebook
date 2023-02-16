package main

import "fmt"

// deferOrder deferred 函数后进先出
func deferOrder() {
	defer func() {
		fmt.Println("input order 1")
	}()

	defer func() {
		fmt.Println("input order 2")
	}()

	defer func() {
		fmt.Println("input order 3")
	}()
}

func main() {
	deferOrder()
}
