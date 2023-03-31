package main

import (
	"crypto/sha1"
	"fmt"
)

func generateSHA1(value string) string {
	return fmt.Sprintf("%x", sha1.Sum([]byte(value)))
}

func main() {
	fmt.Println(generateSHA1("a"))
	fmt.Println(generateSHA1("ab"))
}
