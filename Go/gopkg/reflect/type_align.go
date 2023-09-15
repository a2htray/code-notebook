package main

import (
	"fmt"
	"reflect"
)

func main() {
	t := reflect.TypeOf(1)
	fmt.Println(t.Align())

	fmt.Println(t.FieldAlign())
}
