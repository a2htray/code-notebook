package main

import (
	"fmt"
	"reflect"
)

func main() {
	m := map[reflect.Type]bool{}

	data := []interface{}{
		1,
		1.0,
		"1",
		'1',
	}

	for _, v := range data {
		m[reflect.TypeOf(v)] = true
	}

	for k, v := range m {
		fmt.Println(k, v)
	}

	fmt.Println(reflect.TypeOf(1) == reflect.TypeOf(2))
}
