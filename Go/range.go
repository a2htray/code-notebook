package main

import (
	"fmt"
	"reflect"
	"strings"
)

func main() {
	var s []string

	for i := range s {
		fmt.Println(i)
	}

	for i, ch := range "中国话" {
		fmt.Printf("type of ch: %s\n", reflect.TypeOf(ch).Name())
		fmt.Printf("%d %#U\n", i, ch)
	}

	var m map[int]string

	for i, v := range m {
		fmt.Printf("%i %s\n", i, v)
	}

	ch := make(chan int)
	go func() {
		ch <- 1
		ch <- 2
		ch <- 3
		close(ch)
	}()
	for v := range ch {
		fmt.Println(v)
	}

	strings.EqualFold()
}
