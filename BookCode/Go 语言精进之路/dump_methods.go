package main

import (
	"fmt"
	"reflect"
)

// 通过对接口类型进行反射，可以枚举出包含 receiver 为结构的方法
// 通过对结构类型进行反射，只能枚举出 receiver 为结构的方法

type A interface {
	Func()
	Func2()
}

type B struct{}

func (b B) Func() {
	fmt.Println("Struct B . Func")
}

func (b *B) Func2() {
	fmt.Println("Pointer B . Func2")
}

func Methods(i interface{}) {
	t := reflect.TypeOf(i)

	n := t.NumMethod()
	for i := 0; i < n; i++ {
		fmt.Println("=>", t.Method(i).Name)
	}
}

func main() {
	a := &B{}
	b := B{}

	Methods(a)
	fmt.Println("=======")
	Methods(b)
}

// => Func
// => Func2
// =======
// => Func
