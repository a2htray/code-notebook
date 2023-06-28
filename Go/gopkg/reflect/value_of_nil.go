package main

import (
	"fmt"
	"reflect"
)

type Book interface{}

func main() {
	var b Book

	fmt.Println(reflect.ValueOf(b)) // <invalid reflect.Value>
}
