package main

import (
	"fmt"
	"reflect"
)

type Car interface {
	Run() error
}

func main() {
	var nilCar Car
	fmt.Println(reflect.TypeOf(nilCar)) // <nil>
}
