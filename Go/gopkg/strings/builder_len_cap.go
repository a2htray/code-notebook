package main

import (
	"fmt"
	"strings"
)

func main() {
	sb := strings.Builder{}
	sb.WriteString("hello world")

	fmt.Printf("Len: %d, Cap: %d\n", sb.Len(), sb.Cap())

	sb.Grow(3) // 不进行扩容
	fmt.Printf("Len: %d, Cap: %d\n", sb.Len(), sb.Cap())

	sb.Grow(6)
	fmt.Printf("Len: %d, Cap: %d\n", sb.Len(), sb.Cap())
}
