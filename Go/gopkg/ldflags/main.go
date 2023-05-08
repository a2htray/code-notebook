package main

import "fmt"

// Version go run -ldflags "-X main.Version=v1.10.0" main.go
var Version = "unset"

func main() {
	fmt.Println(Version)
}
