package main

import (
	"fmt"
	"reflect"
)

func main() {
	var y = 5.2
	const z = 2
	fmt.Println(y / z) // 2.6

	const a = 7.0
	fmt.Println(reflect.TypeOf(a)) // float64
	var b = 2
	fmt.Println(a / b) // 3

	c := 40
	f := float64(c / 100.0)
	fmt.Println(f) // 0

	r := float64(c / 100.0)
	fmt.Println(r, reflect.TypeOf(r))
}
