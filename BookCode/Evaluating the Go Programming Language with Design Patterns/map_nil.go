package main

import "fmt"

func main() {
	m := map[string]interface{}{
		"id1": "123",
		"id2": nil,
	}

	id1, ok := m["id1"]
	fmt.Println(id1, ok)

	id2, ok := m["id2"]
	fmt.Println(id2, ok)
}
