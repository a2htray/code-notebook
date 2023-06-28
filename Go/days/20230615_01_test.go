package main

import "testing"

type Duck interface {
	Quack()
}

type Cat struct {
	Name string
}

func (c *Cat) Quack() {
	println(c.Name + " meow")
}

func BenchmarkStructDirectCall(b *testing.B) {
	cat := Cat{Name: "a2htray"}
	for i := 0; i < b.N; i++ {
		cat.Quack()
	}
}

func BenchmarkInterfaceDirectCall(b *testing.B) {
	cat := &Cat{Name: "a2htray"}
	for i := 0; i < b.N; i++ {
		cat.Quack()
	}
}
