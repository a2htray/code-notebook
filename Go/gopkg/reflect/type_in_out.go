package main

import (
	"fmt"
	"reflect"
)

func main() {
	type Func func(string) string

	var hello Func = func(s string) string {
		return "hello " + s
	}

	t := reflect.TypeOf(hello)

	fmt.Println(t.Kind())                        // func
	fmt.Println(t.NumIn(), t.NumOut())           // 1 1
	fmt.Println(t.In(0).Kind(), t.Out(0).Kind()) // string string
}
