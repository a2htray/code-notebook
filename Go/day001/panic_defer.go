package main

import "fmt"

func main() {
	defer func() {
		fmt.Println("defer")
		r := recover()
		fmt.Println(r)
	}()
	panic("panic")
}
