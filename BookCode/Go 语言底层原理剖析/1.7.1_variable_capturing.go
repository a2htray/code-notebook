package main

import "fmt"

func main() {
	a := 1
	b := 2

	f := func() {
		fmt.Println(a, b)
	}
	f()
	b = 3
}
