package main

import "fmt"

func f() {
	defer func() {
		defer func() { recover() }()
		defer recover()
		panic(2)
	}()
	panic(1)
}

func main() {
	defer func() {
		fmt.Println(recover()) // 1
	}()
	f()
}
