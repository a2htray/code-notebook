package main

import (
	"fmt"
	"reflect"
)

func main() {
	a := "你的名字"
	fmt.Println(len(a))

	for _, c := range a {
		fmt.Println(c, reflect.TypeOf(c))
		fmt.Printf("%x, %q, %U\n", c, c, c)
	}
	fmt.Println()
	for i := 0; i < len(a); i++ {
		fmt.Printf("%x\n", a[i])
	}
}
