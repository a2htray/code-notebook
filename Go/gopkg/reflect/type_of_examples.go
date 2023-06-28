package main

import (
	"fmt"
	"reflect"
)

type Bird struct {
}

func main() {
	i := 1
	pi := &i
	fmt.Println(reflect.TypeOf(i))  // int
	fmt.Println(reflect.TypeOf(pi)) // *int

	b := Bird{}
	pb := &b
	fmt.Println(reflect.TypeOf(b))  // main.Bird
	fmt.Println(reflect.TypeOf(pb)) // *main.Bird
}
