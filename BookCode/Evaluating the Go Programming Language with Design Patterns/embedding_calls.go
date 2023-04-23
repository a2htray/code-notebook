package main

import "fmt"

type T struct{}

func (t T) Foo() {
	fmt.Println("T")
}

func (t T) Baz() {
	t.Foo()
}

type S struct {
	T
}

func (s S) Foo() {
	fmt.Println("S")
}

func main() {
	s := new(S)
	s.Baz()
}
