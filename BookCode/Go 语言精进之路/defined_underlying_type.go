package main

// @link https://stackoverflow.com/questions/61247864/what-is-the-difference-between-type-alias-and-type-definition-in-go
import (
	"fmt"
	"os"
	"reflect"
)

// DefinedInt 是 defined 类型
// int 是 underlying 类型
type DefinedInt int

// MyReader
// defined 类型无法直接使用 underlying 的方法
type MyReader os.File // 类型定义

// MyNewReader 类型别名与原类型拥有完全相同的方法集合
type MyNewReader = os.File // 类型别名

func main() {
	reader := MyReader{}

	t := reflect.TypeOf(reader)
	for i := 0; i < t.NumMethod(); i++ {
		fmt.Println(t.Method(i).Name)
	}

	reader2 := MyNewReader{}
	t = reflect.TypeOf(reader2)
	fmt.Println(t.NumMethod())
	for i := 0; i < t.NumMethod(); i++ {
		fmt.Println(t.Method(i).Name)
	}
}
