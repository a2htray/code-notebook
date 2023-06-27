package main

import "fmt"

func main() {
	myArr := [3]int{1, 2, 3}
	myArr2 := [...]int{1, 2, 3}
	fmt.Println(myArr, myArr2)
}
