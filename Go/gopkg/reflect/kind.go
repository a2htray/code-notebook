package main

import (
	"fmt"
	"reflect"
)

func main() {
	i := 1
	t := reflect.TypeOf(i)
	fmt.Println(uint(t.Kind()), t.Kind()) // 2 int

	m := map[int]interface{}{}
	t = reflect.TypeOf(m)
	fmt.Println(uint(t.Kind()), t.Kind()) // 21 map
}
