package main

import "fmt"

func main() {

	defer func() {
		if recover() == nil {
			// 1.20 及之前版本
			fmt.Println("recover() is equal to nil")
		} else {
			// 1.21 及更高版本
			fmt.Println("recover() is not equal to nil")
		}
	}()

	panic(nil)
}
