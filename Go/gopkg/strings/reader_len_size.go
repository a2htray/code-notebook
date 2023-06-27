package main

import (
	"fmt"
	"strings"
)

func main() {
	r := strings.NewReader("hello world")
	fmt.Printf("Len: %d, Size: %d\n", r.Len(), r.Size())
	buf := make([]byte, 1)
	r.Read(buf)
	fmt.Printf("Len: %d, Size: %d\n", r.Len(), r.Size())
}
