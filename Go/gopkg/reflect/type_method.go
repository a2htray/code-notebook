package main

import (
	"fmt"
	"reflect"
)

type Foo1 struct {
}

func (f *Foo1) A() {

}

func (f *Foo1) a() {

}

func (f Foo1) B() {

}

func (f Foo1) b() {

}

func main() {
	t := reflect.TypeOf(1)
	fmt.Println(t.NumMethod())

	t = reflect.TypeOf(&Foo1{})
	fmt.Println(t.NumMethod())

	t = reflect.TypeOf(Foo1{})
	fmt.Println(t.NumMethod())

	pt := reflect.TypeOf(&Foo1{})
	st := reflect.TypeOf(Foo1{})

	ma, ok := pt.MethodByName("A")
	if ok {
		fmt.Println(ma.Name, ma.Type)
	}

	for i := 0; i < pt.NumMethod(); i++ {
		m := pt.Method(i)
		fmt.Println(i, m.Name, m.Type)
	}

	for i := 0; i < st.NumMethod(); i++ {
		m := st.Method(i)
		fmt.Println(i, m.Name, m.Type)
	}
}
