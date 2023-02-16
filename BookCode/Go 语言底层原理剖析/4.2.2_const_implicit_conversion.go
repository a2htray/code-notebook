package main

import "fmt"

type Month int

const (
	Jan Month = 1
	Feb       = 2
	Mar       = 3
)

func main() {
	Aug := Feb * 4
	fmt.Println(Aug)
}
