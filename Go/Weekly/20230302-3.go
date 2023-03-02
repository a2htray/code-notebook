package main

import "fmt"

func main() {
	defer func() {
		fmt.Println(1, recover())
	}()
	defer func() {
		fmt.Println(2, recover())
	}()

	panic(1)
}
