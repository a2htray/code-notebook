package main

import (
	_ "embed"
	"fmt"
)

var (
	//go:embed version.txt
	version string
)

func main() {
	fmt.Println(version)
}
