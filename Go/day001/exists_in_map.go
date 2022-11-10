package main

import "fmt"

func main() {
	m := map[string]int{
		"v1": 1,
		"v2": 2,
	}

	v1, ok := m["v1"]
	fmt.Println(v1, ok)

	v3, ok := m["v3"]
	fmt.Println(v3, ok)
}
