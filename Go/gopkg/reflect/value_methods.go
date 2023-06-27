package main

import (
	"fmt"
	"reflect"
)

func main() {
	i := 1
	v := reflect.ValueOf(&i)
	if v.Elem().Kind() == reflect.Int {
		v.Elem().SetInt(2)
	}

	fmt.Println(i) // 2

	var s interface{}
	v = reflect.ValueOf(s)
	fmt.Println(v.IsValid()) // false
	fmt.Println(v.Kind())    // invalid
	fmt.Println(v.String())  // <invalid Value>

	i2 := 2
	i3 := 2

	vi2 := reflect.ValueOf(i2)
	vi3 := reflect.ValueOf(i3)
	fmt.Println(vi2.Interface() == vi3.Interface()) // true
}
