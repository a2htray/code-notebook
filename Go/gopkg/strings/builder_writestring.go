package main

import (
	"fmt"
	"strings"
)

func main() {
	sb := strings.Builder{}
	sb.WriteString("hello world")
	fmt.Println(sb.String()) // hello world
}
