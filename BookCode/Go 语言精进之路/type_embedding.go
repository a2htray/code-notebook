package main

import (
	"fmt"
	"reflect"
)

// 结构可以只实现接口定义的部分方法

type AA interface {
	Func0()
	Func1()
}

type BB struct {
	AA
}

func (b *BB) Func0() {
	fmt.Println("Func0")
}

type A0 struct{}

func (a A0) Func0() {
	fmt.Println("A0.Func0")
}

func (a *A0) Func1() {
	fmt.Println("A0.Func1")
}

// 类型嵌入方式定义的结构，无法通过反射捕获到其嵌入结构的方法

type A1 struct{}

func (a A1) Func0() {
	fmt.Println("A1.Func0")
}

func (a *A1) Func1() {
	fmt.Println("A1.Func1")
}

type A3 struct {
	A0
	*A1
}

func (a A3) Func2() {
	fmt.Println("A3.Func2")
}

func Methods2(i interface{}) {
	t := reflect.TypeOf(i)

	n := t.NumMethod()
	for i := 0; i < n; i++ {
		fmt.Println("=>", t.Method(i).Name)
	}
}

func main() {
	b := BB{}
	b.Func0()

	var a AA = &BB{}
	a.Func0()

	fmt.Println("======")

	a3 := A3{}
	pa3 := &A3{}

	Methods2(a3)
	Methods2(pa3)
}
