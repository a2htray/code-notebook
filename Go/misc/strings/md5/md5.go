package main

import (
	"crypto/md5"
	"fmt"
)

func generateMD5(value string) string {
	return fmt.Sprintf("%x", md5.Sum([]byte(value)))
}

func main() {
	fmt.Println(generateMD5("a"))
	fmt.Println(generateMD5("ab"))
}
