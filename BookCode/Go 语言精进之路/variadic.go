package main

import "fmt"

func main() {
	b := []byte{}
	// 在调用 append 方法时，字符串可以会转换成 []byte
	b = append(b, "hello"...)

	fmt.Println(b)
	fmt.Println(fmt.Sprintf("%s", b))
}
